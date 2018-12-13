from tkinter import *
from tkinter import messagebox
import distancePlots
import traffic
import threading
import pickle
import datetime
from multiprocessing.pool import ThreadPool
import time
import random

def draw():
	window = Tk()
	
	window.title("Astrid ") 
	window.geometry('600x400')
	lbl = Label(window, text="A specialised trained intrusion detection system")
	lbl.grid(column=0, row=0, padx = (100, 30), pady = (10,50))
	btn = Button(window, text="TRAIN", command = runTests)
	btn.grid(column=0, row=1)
	btn = Button(window, text="VALIDATE", command = runValidationData)
	btn.grid(column=0, row=2)
	btn = Button(window, text="SUMMARY", command = viewSummary)
	btn.grid(column=1, row=1)
	btn = Button(window, text="MONITOR SYSTEM", command = monitor)
	btn.grid(column=1, row=2)
	window.mainloop()
def runTests():
	learning_thread = threading.Thread(target=distancePlots.startTraining)
	learning_thread.start()
	messagebox.showinfo('Notification', 'Training Started. Please Wait...')
	learning_thread.join()
	messagebox.showinfo('Notification', 'Finished.')
	
def runValidationData():
	file2 = open(r'myLearnedData.pkl', 'rb')
	c1 = pickle.load(file2)
	c2 = pickle.load(file2)
	c3 = pickle.load(file2)
	c4 = pickle.load(file2)
	file2.close()
	print(c1, c2, c3, c4)
	messagebox.showinfo('Notification', 'Validating Model. Please Wait...')
	validate_thread = threading.Thread(target=distancePlots.validateModel)
	validate_thread.start()
	validate_thread.join()
	messagebox.showinfo('Notification', 'Finished Validation. View Summary')
	
def viewSummary():
	file2 = open(r'run_Results_Log.pkl', 'rb')
	dateTime = pickle.load(file2)
	correct = pickle.load(file2)
	wrong = pickle.load(file2)
	total = pickle.load(file2)
	tp = pickle.load(file2)
	fp = pickle.load(file2)
	tn = pickle.load(file2)
	fn = pickle.load(file2)
	file2.close()

	print('----------------------------------------------------------')
	print("Summary")
	print('----------------------------------------------------------\n')
	
	print("Validation Test run at", dateTime)
	print("Number of correctly classified instances:", correct)
	print("Number of wrongly classified instances:", wrong)
	print("Number of classified instances:", total)
	print("\n")
	print("Accuracy (tp+tn/total):", correct/total)
	print("Precision (tp/tp+fp):", tp/tp+fp)
	print("Recall (tp/tp+fn):", tp/tp+fn)
	print("Sensitivity (tp/tp+fn):", tn/tn+fp)
	
	
	summary = Tk()
	summary.title('Validation Summary')
	summary.geometry('600x400')
	lbl = Label(summary, text="Results from Validation Data")
	lbl.grid(column=0, row=0, padx=(50, 50),pady=(20, 50))

	lbl = Label(summary, text="Last Done On:")
	lbl.grid(column=5, row=0, padx = (10,10), pady = (20,5))

	lbl = Label(summary, text=str(dateTime))
	lbl.grid(column=5, row=0, pady = (0,20))

	lbl = Label(summary, text="Number of Samples Taken")
	lbl.grid(column=0, row=2, pady = (20,5))

	lbl = Label(summary, text=str(total))
	lbl.grid(column=0, row=3, pady = (0,20))
	
	lbl = Label(summary, text="Correctly classified")
	lbl.grid(column=5, row=2, pady = (20,5))

	lbl = Label(summary, text=str(correct))
	lbl.grid(column=5, row=3, pady = (0,20))

	



	lbl = Label(summary, text="Accuracy")
	lbl.grid(column=0, row=6, pady = (20,5))

	lbl = Label(summary, text=str(correct/total))
	lbl.grid(column=0, row=7, pady = (0,20))
	
	lbl = Label(summary, text="Precision")
	lbl.grid(column=5, row=6, pady = (20,5))

	lbl = Label(summary, text=str(tp/tp+fp))
	lbl.grid(column=5, row=7, pady = (0,20))

	lbl = Label(summary, text="Recall")
	lbl.grid(column=0, row=9, pady = (20,5))

	lbl = Label(summary, text=str(tp/tp+fn))
	lbl.grid(column=0, row=10, pady = (0,20))
	
	lbl = Label(summary, text="Sensitivity")
	lbl.grid(column=5, row=9, pady = (20,5))

	lbl = Label(summary, text=str(tn/tn+fp))
	lbl.grid(column=5, row=10, pady = (0,20))
	summary.mainloop()
	
def printClock(monitor):
	
def monitor():
	monitor = Tk()
	monitor.title('Current Network: 14.8 Hawk')
	monitor.geometry('600x400')
	lbl = Label(monitor, text="Dashboard")
	lbl.grid(column=0, row=0, padx=(200, 50),pady=(20, 10))
	now = datetime.datetime.now()
	lbl = Label(monitor, text="System Time")
	lbl.grid(column=5, row=0, padx=(40, 50),pady=(20, 5))
	lbl = Label(monitor, text=str(now.strftime("%X")))
	lbl.grid(column=5, row=1, padx=(40, 50),pady=(0, 10))

	count = 0
	lbl = Label(monitor, text="Request Received")
	lbl.grid(column=0, row=4)
	lbl = Label(monitor, text="Status")
	lbl.grid(column=9, row=4)
	lbl = Label(monitor, text="At")
	lbl.grid(column=5, row=4)
		
	while(True):
		now = datetime.datetime.now()
		lbl = Label(monitor, text=str(now.strftime("%X")))
		lbl.grid(column=5, row=1, padx=(40, 50),pady=(0, 10))
		pool = ThreadPool(processes=1)
		async_result = pool.apply_async(traffic.sendTraffic, (count,))
		request, classif = async_result.get()
		if classif == -1:
			break
		count = count+1
		
		lbl = Label(monitor, text=str(request[2]))
		lbl.grid(column=0, row=6+count*2)

		now = now = datetime.datetime.now()
		lbl = Label(monitor, text=str(now.strftime("%X")))
		lbl.grid(column=5, row=6+count*2)

		if(classif<3):
			status = "abnormal"
			messagebox.showerror('URGENT', 'ABNORMAL TRAFFIC')
	
		else:
				status = "normal"
		lbl = Label(monitor, text=status)
		lbl.grid(column=9, row=6+count*2)
		monitor.update()
		waitTime = random.randint(0, 10)	
		time.sleep(waitTime)
	monitor.mainloop()
	
	

