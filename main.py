import mysql.connector
from utilis import send_whatsapp_message

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="whatsapp_send")

mycursor = mydb.cursor()

mycursor.execute("select * from people")
result = mycursor.fetchall()
for message in result:
    for m in message:
        send_whatsapp_message(m)
