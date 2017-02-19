import sys
import csv
from datetime import datetime

class PriorityQueue:   
    def __init__(self):
        self.taskList = [0]
        self.timeList = [0]
        self.priorityList = [0]
        self.qSize = 0

        
    #To adjust heap form lastnode to rootnode
    def up(self,i):
        while i // 2 > 0:
            # if two task have same time then compare their priorities
            if self.timeList[i] == self.timeList[i // 2] :
                
                if self.priorityList[i] > self.priorityList[i // 2] :
                    tmp = self.taskList[i // 2]
                    self.taskList[i // 2] = self.taskList[i]
                    self.taskList[i] = tmp
                    tmp = self.timeList[i // 2]
                    self.timeList[i // 2] = self.timeList[i]
                    self.timeList[i] = tmp
                    tmp = self.priorityList[i // 2]
                    self.priorityList[i // 2] = self.priorityList[i]
                    self.priorityList[i] = tmp
                    
            elif self.timeList[i] < self.timeList[i // 2] :
                tmp = self.taskList[i // 2]
                self.taskList[i // 2] = self.taskList[i]
                self.taskList[i] = tmp
                tmp = self.timeList[i // 2]
                self.timeList[i // 2] = self.timeList[i]
                self.timeList[i] = tmp
                tmp = self.priorityList[i // 2]
                self.priorityList[i // 2] = self.priorityList[i]
                self.priorityList[i] = tmp
             
            i = i // 2


    #To enter new task in queue
    def enqueue(self,task,time,priority):
        #append new task at the end of heap
        self.taskList.append(task)
        self.timeList.append(time)
        self.priorityList.append(priority)

        #increase queue size
        self.qSize = self.qSize + 1

        #adjust heap form lastnode to rootnode
        self.up(self.qSize)


    #method to adjust heap from rootnode to lastnode
    def down(self,i):
        while (i * 2) <= self.qSize:
            mc = self.minChild(i)

            # if two task have same time then compare their priorities
            if self.timeList[i] == self.timeList[mc] :

                if self.priorityList[i] < self.priorityList[mc] :
                    tmp = self.taskList[i]
                    self.taskList[i] = self.taskList[mc]
                    self.taskList[mc] = tmp
                    tmp = self.timeList[i]
                    self.timeList[i] = self.timeList[mc]
                    self.timeList[mc] = tmp
                    tmp = self.priorityList[i]
                    self.priorityList[i] = self.priorityList[mc]
                    self.priorityList[mc] = tmp

            elif self.timeList[i] > self.timeList[mc] :
                tmp = self.taskList[i]
                self.taskList[i] = self.taskList[mc]
                self.taskList[mc] = tmp
                tmp = self.timeList[i]
                self.timeList[i] = self.timeList[mc]
                self.timeList[mc] = tmp
                tmp = self.priorityList[i]
                self.priorityList[i] = self.priorityList[mc]
                self.priorityList[mc] = tmp
            i = mc


    #to find child with minimum value
    def minChild(self,i):
        if i * 2 + 1 > self.qSize:
            return i * 2
        else:
            if self.timeList[i*2] < self.timeList[i*2+1] :
                return i * 2
            else:
                return i * 2 + 1

    def dequeue(self):
        retval=['0','0','0']
      
        #copy first element before deleting
        retval[0] = self.taskList[1]
        retval[1] = self.timeList[1]
        retval[2] = self.priorityList[1]

        #copy last element of list at index 1 of the list
        self.taskList[1] = self.taskList[self.qSize]
        self.timeList[1] = self.timeList[self.qSize]
        self.priorityList[1] = self.priorityList[self.qSize]

        #decerment queue size
        self.qSize = self.qSize - 1

        #delete last elements of list
        self.taskList.pop()
        self.timeList.pop()
        self.priorityList.pop()

        #adjust heap from root
        self.down(1)
        return retval

    def buildPriorityQueue(self,tasklist,timelist,prioritylist):
        i = len(tasklist) // 2
        self.qSize = len(tasklist)
        self.taskList = [0] + tasklist[:]
        self.timeList = [0] + timelist[:]
        self.priorityList = [0] + prioritylist[:]
        while (i > 0):
            self.down(i)
            i = i - 1
      

if __name__ == "__main__":

    if len(sys.argv) != 3 :
        print("you need two arguments(csv file name and time) to run this program)")
        sys.exit(0)

    fileName = sys.argv[1]
    currentTime = datetime.strptime(sys.argv[2], '%Y/%m/%d %H:%M')

    task = []
    time = []
    priority = []

    #read input csv file
    dataFile = open(fileName)
    dataReader = csv.reader(dataFile)
    for row in dataReader :
        task.append(row[0])
        time.append(row[1])
        if row[2] == '' :
            priority.append('0')
        else:
            priority.append(row[2])
    dataFile.close()
    #Total number of task
    dataSize = len(task)

    #priority queue object
    pq = PriorityQueue()

    #build priority queue from input data
    pq.buildPriorityQueue(task,time,priority)

    flag = 0;

    #Process task in the queue
    for i in range(dataSize):
        task = pq.dequeue()
        timeElapsed = datetime.strptime(task[1], '%Y/%m/%d %H:%M')-currentTime
        currentTime = datetime.strptime(task[1], '%Y/%m/%d %H:%M')
        if(str(timeElapsed) != '0:00:00') :
            if flag == 0 :
                print("-- After ", str(timeElapsed).split(':')[1] , "minute")
                flag = 1
            else : 
                print("-- After another", str(timeElapsed).split(':')[1] , "minute")
            print("Current time [" , task[1], "], Event" , repr(task[0]), "Processed")
        else :
            print("Current time [" , task[1], "], Event" , repr(task[0]), "Processed")
        
