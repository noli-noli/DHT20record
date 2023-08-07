import datetime
import os
from time import sleep
import DHT20

log_file="time-recoad_log.txt"

DATA1=[0,0,0,0,0]
DATA2=[0,0,0,0,0]

#DATA1=旧時刻
#DATA2=新時刻

def reload():
    dt_now = datetime.datetime.now()
    DATA2[0]=dt_now.year
    DATA2[1]=dt_now.month
    DATA2[2]=dt_now.day
    DATA2[3]=dt_now.hour
    DATA2[4]=dt_now.minute

def backup():
        f=open(log_file,"r+")
        f.truncate(0)
        for a in range(5):
            f.write(str(DATA2[a]) + "\n")
            DATA1[a] = DATA2[a] 
        f.close()

def recoad():
    tmp,hum = DHT20.DHT20()
    f = open(str(DATA2[0]) + "/" + str(DATA2[1]) + ".txt", 'a')
    f.write(str(DATA2[0]) + "," + str(DATA2[1])+ "," + str(DATA2[2])+ "," + str(DATA2[3])+","+str(tmp)+","+str(hum)+"\n")
    print(str(DATA2)+" tmp:"+str(tmp)+" hum:"+str(hum)+"を記録しました")
    f.close()

if(os.path.exists(log_file)==False):
    reload()
    f=open(log_file,'w')
    for a in range(5):
        f.write(str(DATA2[a]) + "\n")
    f.close()
    print("DATA1初期作成")
else:
    f=open(log_file)
    for a in range(5):
        line = f.readline()
        DATA1[a]=int(line.strip())
    f.close()
    print("DATA1読込完了")

while True:
    reload()
    if(os.path.isdir(str(DATA2[0]))==False):
        os.makedirs(str(DATA2[0]))
        print("フォルダ作成")
    if(os.path.isfile(str(DATA2[0]) + "/" + str(DATA2[1]) + ".txt")==False):
        f = open(str(DATA2[0]) + "/" + str(DATA2[1]) + ".txt", 'w')
        f.close()
    if(DATA1[0]!=DATA2[0]):
        print("year")
        backup()
        recoad()
    elif(DATA1[1]!=DATA2[1]):
        print("month")
        backup()
        recoad()
    elif(DATA1[2]!=DATA2[2]):
        print("day")
        backup()
        recoad()
    elif(DATA1[3]!=DATA2[3]):
        print("hour")
        backup()
        recoad()
    sleep(1)
