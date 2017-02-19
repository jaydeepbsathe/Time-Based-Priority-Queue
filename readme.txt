Problem: A time-based priority queue.

A queue based on time and priority is implemented using binary heap. This program can be used to schedule tasks at a given time.


Running
Pass filename & starttime as parameters to program

	python PriorityQueue input_events.csv  "2017/02/10 4:59"

Input:
Input to the program will be a file containing all the events in CSV format.  
	
event_name, time_to_expire , priority
"Task_#501", "2017/02/10 5:01"
"Task_#500", "2017/02/10 5:00"
"Task_#500", "2017/02/10 5:00" , 1

Note: Priority is an optional field.


Output: 
-- After 1 minute --
Current time [ 2017/02/10 5:00  ] , Event "Task_#500" Processed
Current time [ 2017/02/10 5:00  ] , Event "Task_#500" Processed
-- After another 1 minute --
Current time [ 2017/02/10 5:01  ] , Event "Task_#501" Processed

sampleData.csv is sample input file