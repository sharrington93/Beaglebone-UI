import numpy as np
import MySQLdb as mdb
import sys
import time

#Define tic-tok function
def tic():
    #Homemade version of matlab tic and toc functions
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    if 'startTime_for_tictoc' in globals():
        print "Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds."
    else:
        print "Toc: start time not set"



#load data file, change path for beaglebone
file = "C:\Users\wes\Documents\BuckeyeCurrent\HackAThon\data.csv"

#create matrix containing data from file
data = np.loadtxt(file, dtype=float, delimiter=',')

#load matrix into variable arrays
#+- statements for more/different data
voltage = data


#establish connection with database

con = mdb.connect('localhost','root','buckeyes','test_tutorial')

tic()
with con:
    #establish pointer? I think that's what this does
    cur = con.cursor()

    #Drop table Example if it exists
    cur.execute("DROP TABLE IF EXISTS Example")
    
    #creates table, will not need for real script
    cur.execute("CREATE TABLE Example(time datetime(6), voltage float, three float)")
    
    
    for i in range(0,100):
        #insert time variable into table
        cur.execute('INSERT INTO Example(time, voltage, three) VALUES (now(6), 1, 1)')
        #time.sleep(.5)


toc()
