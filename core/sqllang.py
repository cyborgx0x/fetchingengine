import mysql.connector
config = {
  'user': 'bb7rscqll4s4fucu',
  'password': 'o4q5vdaua9r1k7x3',
  'host': 'un0jueuv2mam78uv.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
  'database': 'wp0cqq4t5leuhx3v',
  'raise_on_warnings': True
}
def printallpost():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT * FROM post ")
    cursor.execute(query)
    for i in cursor:
        print(i)
    cursor.close()
    cnx.close()
 