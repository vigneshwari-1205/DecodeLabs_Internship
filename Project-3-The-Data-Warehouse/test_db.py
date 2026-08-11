import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='admin', password='vignesh12', database='interns_db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Interns1;")
for row in cursor.fetchall():
    print(row)
conn.close()