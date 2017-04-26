import MySQLdb


def connection():

	conn = MySQLdb.connect(host="localhost", 
							user="root",
							passwd="testing",
							db="netflowdata")
	c = conn.cursor()

	return c, conn
