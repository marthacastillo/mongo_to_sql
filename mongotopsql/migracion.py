import pymongo as mon
import psycopg2 as psql

mongoClient = mon.MongoClient('172.17.0.2',27017)
conn = psql.connect("dbname='grad' user='mar' host='localhost' password='martha'")
print(conn)
# PASO 2: Conexión a la base de datos
db = mongoClient.grad

# PASO 3: Obtenemos una coleccion para trabajar con ella
collection = db.users

#Cursores
curMon = collection.find()
curPSQL = conn.cursor()

print("Migrando de Mongodb ...")
for user in curMon:
	#print (user["_id"])
#	print (user["name"])
#	print(user["age"])
#	print(user["type"])
#	print(user["status"])
#	print(user["finished"])
#	print(user["favorites"])
#	print(user["badges"])
#	print(user["points"])
	curPSQL.execute("""INSERT INTO users VALUES ("""+str(user['_id'])+""",
                                                     '"""+str(user['name'])+"""',
					                                 """+str(user['age'])+""",
                                                     """+str(user['type'])+""",
                                                     '"""+str(user['status'])+"""');""")

	for finish in user["finished"]:
		curPSQL.execute("""INSERT INTO finished VALUES (DEFAULT,"""+str(user['_id'])+""",
					"""+str(finish)+""");""")

	curPSQL.execute("""INSERT INTO favorites VALUES (DEFAULT,"""+str(user['_id'])+""",'"""+str(user['favorites']['artist'])+"""',
							'"""+str(user['favorites']['food'])+"""');""")

	for badge in user["badges"]:
		curPSQL.execute("""INSERT INTO badges VALUES (DEFAULT,'"""+str(badge)+"""',
                                                     """+str(user['_id'])+""");""")

	for point in user["points"]:
		curPSQL.execute("""INSERT INTO points VALUES (DEFAULT,"""+str(user['_id'])+""","""+str(point['points'])+""",
							      """+str(point['bonus'])+""");""")

	
conn.commit()

#curPSQL.execute("""SELECT * FROM users;""")

#rows = curPSQL.fetchall()
#for row in rows:
    #print (row)