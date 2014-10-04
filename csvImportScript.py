import numpy as np
import MySQLdb as mdb
import sys

#load data file, change path for beaglebone
file = "C:\Users\wes\Documents\BuckeyeCurrent\HackAThon\data.csv"

#create matrix containing data from file
data = np.loadtxt(file, dtype=float, delimiter=',')

#load matrix into variable arrays
#+- statements for more/different data
time = data[:,0]
voltage = data[:,1]


#establish connection with database

con = mdb.connect('localhost','root','buckeyes','test_tutorial')


with con:
    #establish pointer? I think that's what this does
    cur = con.cursor()

    #Drop table Example if it exists
    cur.execute("DROP TABLE IF EXISTS Example")
    
    #creates table, will not need for real script
    cur.execute("CREATE TABLE Example(time float)")


    for i in range(0,len(time)):
        #insert time variable into table
        cur.execute('INSERT INTO Example(time) VALUES ('+str(time[i])+')')

    
    


