import distancePlots
import pandas as pd
import pickle

def sendTraffic(count):
	data = pd.read_csv('flowData.csv')
	if(count==len(data.values)):
		return None, -1
	distancePlots.dataCleanup(data)
	file2 = open(r'myLearnedData.pkl', 'rb')
	c1 = pickle.load(file2)
	c2 = pickle.load(file2)
	c3 = pickle.load(file2)
	c4 = pickle.load(file2)
	file2.close()
	distancePlots.prettyPrintLine("Receiving Data")
	entry = data.values[count]
	distancePlots.prettyPrintLine("Received: " + str(entry[2]))
        #input()
	dist1 = distancePlots.getDissimilarityDist(entry, c1)
	dist2 = distancePlots.getDissimilarityDist(entry, c2)
	dist3 = distancePlots.getDissimilarityDist(entry, c3)
	dist4 = distancePlots.getDissimilarityDist(entry, c4)

	classif = -1
	if dist1<dist2 and dist1<dist3 and dist1<dist4:
		print("Classified into c1 (anomalous)")
		classif = 1
	elif dist2<dist3 and dist2<dist4:
		print("Classified into c2 (anomalous)")
		classif = 2
	elif dist3<dist4:
		print("Classified into c3 (normal)")
		classif = 3
	else:
		print("Classified into c4 (normal)")
		classif = 4
	return entry, classif
