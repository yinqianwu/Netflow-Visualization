from flask import Flask, render_template, jsonify, flash, request, url_for, redirect,session
import os
import numpy as np
import subprocess
import pprint
import json
import datetime

app = Flask(__name__)

def restapi():

	jsondata = []

	# The path to the directory where the nfcapd files are stored - this should be directory that contains
	nfStore="/Users/yinqianwu/Desktop/Flask/app/netflow"

	os.chdir(nfStore)

	# time function


	timewindows =[]
	start_time = datetime.datetime(2016,12,16,12)
	start_timewindow ='{:%Y%m%d%H00}'.format(datetime.datetime(2016,12,16,12))
	end_timewindow ='{:%Y%m%d%H00}'.format(datetime.datetime(2016,12,16,17))


	while (start_timewindow < end_timewindow):

	    timewindows.insert(-1, str(start_timewindow))
	    start_time = start_time + datetime.timedelta(seconds=300)
	    start_timewindow ='{:%Y%m%d%H%M}'.format(start_time + datetime.timedelta(seconds=300))


	for timewindow in timewindows:
		p = subprocess.Popen(['nfdump', '-o', 'fmt:%ra,%in,%out,%ibyt,%obyt', '-r', 'nfcapd.'+timewindow], stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
		output, err = p.communicate()
		outputline = output.split("\n")
		output_Array = ['1','1','1','1','1','1','1','1']
		for eachline in outputline:
			output_Array.insert(-1,eachline)
		summary = output_Array[-6] + output_Array[-5] + output_Array[-4] + output_Array[-3] + output_Array[-2]

		data_line = summary.split(",")
		for line in data_line:
			if 'Summary: total flows:' in line:
				(junk,totalflow)=line.split('Summary: total flows:')
				totalflow = totalflow.strip()
			
			if 'total bytes:' in line:
				(junk,totalbytes)=line.split('total bytes:')
				totalbytes = totalbytes.strip()
		
			if 'total packets:' in line:
				(junk,totalpackets)=line.split('total packets:')
				totalpackets = totalpackets.strip()

			if 'avg bps:' in line:
				(junk,avgbps)=line.split('avg bps:')
				avgbps = avgbps.strip()

			if 'avg pps:' in line:
				(junk,avgpps)=line.split('avg pps:')
				avgpps = avgpps.strip()

			if 'avg bpp:' in line:
				(junk,avgbpp)=line.split('avg bpp:')
				avgbpp = avgbpp.strip()

		data = {'timewindow' : int(timewindow),
				'totalflow'  : int(totalflow),
				'totalbytes' : int(totalbytes),
				'totalpackets' : int(totalpackets),
				'average bps' : int(avgbps),
				'average pps' : int(avgpps),
				# 'average bpp' : str(avgbpp),
				#'flowspersec' : str(flowspersec)
				}
		jsondata.insert(-1,data)

	return jsondata

    # for line in data_line:
    #     if 'flows/second:' in line:
    #         (junk,flowspersec)=line.split('flows/second:')
    #         flowspersec=flowspersec.strip()

#     data[timewindow]= {
#         'timewindow' : str(timewindow),
#         'totalflow'  : str(totalflow),
#         'totalbytes' : str(totalbytes),
#         'totalpackets' :  str(totalpackets),
#         # 'flowspersec' : str(flowspersec)
#         }

# json_data = json.dumps(data)
#     print (json_data)

