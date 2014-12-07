import numpy as np
import MySQLdb as mdb
import sys
import time
import datetime

#Define tic-tok function
def tic():
    #Homemade version of matlab tic and toc functions
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    if 'startTime_for_tictoc' in globals():
        return(time.time() - startTime_for_tictoc)
    


#load data file, change path for beaglebone
file = "C:\Users\wes\Documents\BuckeyeCurrent\CANCorder-UI\home\cancorder\NormalData.csv"

#create matrix containing data from file
data = np.loadtxt(file, dtype=float, delimiter=',', skiprows = 1)

#load matrix into variable arrays
#+- statements for more/different data
PhaseAtemp = data[:,2]
BusVoltage = data[:,3]
MotorId = data[:,4]
MotorTemp = data[:,5]
MotorVelocity = data[:,6]
PackTemp = data[:,6]
PackSOC = data[:,7]
PackBalance = data[:,8]
PrechargeCont = data[:,9]
MainCont = data[:,10]
EStop = data[:,11]


#establish connection with database

con = mdb.connect('192.168.7.35','dbUser','buckeyes','westest')


with con:
    #establish pointer? I think that's what this does
    cur = con.cursor()

    #Drop table Names if it exists
    cur.execute("DROP TABLE IF EXISTS Names")

    #creates table of Names
    cur.execute("CREATE TABLE Names(MsgName TEXT, Unit TEXT)")

    #occupies table Names with values
    cur.executemany("""INSERT INTO Names(MsgName, Unit)
                VALUES (%s,%s)""",
                    [
                    ('PhaseAtemp','unit'),
                    ('BusVoltage','unit'),
                    ('MotorId','unit'),
                    ('MotorTemp','unit'),
                    ('MotorVelocity','unit'),
                    ('PackTemp','unit'),
                    ('PackSOC','unit'),
                    ('PackBalance','unit'),
                    ('PrechargeCont','unit'),
                    ('MainCont','unit'),
                    ('EStop','unit')
                    ])

    #Drop table Messages if it exists
    cur.execute("DROP TABLE IF EXISTS Messages")
    
    #creates table to be occupied with date
    cur.execute("CREATE TABLE Messages(time TEXT, MsgName TEXT, Value FLOAT)")

    #insert values into table
    tic()
    for i in range(0,500):
        
        #import pdb; pdb.set_trace()
        time.sleep(.5)
    
        cur.executemany('''INSERT INTO Messages(time, MsgName, Value)
                VALUES(%s,%s,%s)''',
        [
        (str(datetime.datetime.now()),'PhaseAtemp',str(PhaseAtemp[i])),
        (str(datetime.datetime.now()),'BusVoltage',str(BusVoltage[i])),
        (str(datetime.datetime.now()),'MotorId',str(MotorId[i])),
        (str(datetime.datetime.now()),'MotorTemp',str(MotorTemp[i])),
        (str(datetime.datetime.now()),'MotorVelocity',str(MotorVelocity[i])),
        (str(datetime.datetime.now()),'PackTemp',str(PackTemp[i])),
        (str(datetime.datetime.now()),'PackSOC',str(PackSOC[i])),
        (str(datetime.datetime.now()),'PackBalance',str(PackBalance[i])),
        (str(datetime.datetime.now()),'PrechargeCont',str(PrechargeCont[i])),
        (str(datetime.datetime.now()),'MainCont',str(MainCont[i])),
        (str(datetime.datetime.now()),'EStop',str(EStop[i]))
        ])
        
        con.commit()


        #code to force a timeout error
        #if(toc() >= 3):  #force aditional sleep after certain time
        #    time.sleep(.5) #aditional sleep
        #
