import MySQLdb
from time import sleep
while True:
    sleep(5)
    try:
        db=MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="xmlp")
    except MySQLdb.Error:
        #os.system("systemctl restart mysql")
        print("err")
    else:
        break