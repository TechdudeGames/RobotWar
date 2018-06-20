from blessings import Terminal
term = Terminal()
import os
import sys
import time
import War
import multiprocessing
os.system("clear")
starttime=time.time()
#Some terminal option configuations
#Todo add some terminal configuring options

avcores = multiprocessing.cpu_count() - 1
number_of_total_games= 33000000 # 33 million
print("Playing %i games." %(number_of_total_games//avcores * avcores))

rtstatlist = []
for loops in range(0, avcores):
    stat = multiprocessing.Array('i', range(4))
    for kount in range(0,4):
        stat[kount] = 0
    rtstatlist.append(stat)


#Playing functions
def warthread(numgames,threadnum,statlist):
    print("Thread %i online" %threadnum)
    for i in range (0,numgames):
        result=War.playwar()
        if result==1:
            statlist[threadnum][0] += 1
        elif result==2:
            statlist[threadnum][1] += 1
        elif result==3:
            statlist[threadnum][2] += 1
        statlist[threadnum][3] += 1

def totalup(statlist,dataindex,numbcores):
    returnresult = 0
    internalcount = numbcores
    for dive in range(0,numbcores):
        returnresult += statlist[dive][dataindex]
    return returnresult


#Creating the thread list and spawning the threads
threads = []
if avcores == 1:
    wthread=multiprocessing.Process(target=warthread, args=(number_of_total_games//avcores,0,rtstatlist))
    threads.append(wthread)
else:
    for count in range(0, avcores):
        wthread=multiprocessing.Process(target=warthread, args=(number_of_total_games//avcores,count,rtstatlist))
        threads.append(wthread)
        threads[count].start()


#Main Event
last_run = False
while totalup(rtstatlist,3,avcores) != number_of_total_games//avcores * avcores:
    if totalup(rtstatlist,3,avcores) != 0:
        with term.location(0,10):
            print("Player One has won %f percent of the time       " %float(totalup(rtstatlist,0,avcores) * 100 / totalup(rtstatlist,3,avcores)))
            print("Player Two has won %f percent of the time       " %float(totalup(rtstatlist,1,avcores) * 100 / totalup(rtstatlist,3,avcores)))
            print("There has been a draw %f percent of the time     \n" %float(totalup(rtstatlist,2,avcores) / totalup(rtstatlist,3,avcores)))
            print("Player One has won %i times" %totalup(rtstatlist,0,avcores))
            print("Player Two has won %i times" %totalup(rtstatlist,1,avcores))
            print("There have been %i draws" %totalup(rtstatlist,2,avcores))
            print("The game has been played %i times" %totalup(rtstatlist,3,avcores))
            elapsted_seconds = time.time()-starttime
            #elapsted_seconds = 602263 #Debug time amount. Should be 6 days, 23 hours, 17 minutes, and 43 seconds
            days = int(elapsted_seconds // 86400)
            hours = int(elapsted_seconds // 3600 - (days * 24))
            minutes = int(elapsted_seconds // 60 - (hours * 60) - (days * 1440))
            seconds = int(elapsted_seconds - (minutes * 60) - (hours * 3600) - (days * 86400))
            print("Time Elapsed: ", days, ":", hours, ":", minutes, ":", seconds)
os.system("clear")
with term.location(0, 10):
    print("Player One has won %f percent of the time       " % float(
        totalup(rtstatlist, 0, avcores) * 100 / totalup(rtstatlist, 3, avcores)))
    print("Player Two has won %f percent of the time       " % float(
        totalup(rtstatlist, 1, avcores) * 100 / totalup(rtstatlist, 3, avcores)))
    print("There has been a draw %f percent of the time     \n" % float(
        totalup(rtstatlist, 2, avcores) / totalup(rtstatlist, 3, avcores)))
    print("Player One has won %i times" % totalup(rtstatlist, 0, avcores))
    print("Player Two has won %i times" % totalup(rtstatlist, 1, avcores))
    print("There have been %i draws" % totalup(rtstatlist, 2, avcores))
    print("The game has been played %i times" % totalup(rtstatlist, 3, avcores))
    elapsted_seconds = time.time() - starttime
    days = int(elapsted_seconds//86400)
    hours = int(elapsted_seconds//3600 - (days * 24))
    minutes = int(elapsted_seconds//60 - (hours * 60) - (days  * 1440))
    seconds = int(elapsted_seconds - (minutes * 60) - (hours * 3600) - (days * 86400) )
    print("Time Elapsed: ", days, " : ", hours, " : ", minutes, " : ", seconds)
