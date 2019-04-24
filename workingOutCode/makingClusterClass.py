import numpy as np
import operator

class Cluster:
	cluster = []
	def __init__(self, center):
		self.center = center

		self.methodSum = 0
		self.protocolSum = 0
		self.pragmaSum = 0
		self.cacheSum = 0
		self.connectSum = 0
		self.contentLengthSum = 0
		self.contentTypeSum = 0

		self.acceptEnc = {}
		self.accept = {}
		self.acceptChar = {}
		
		self.numberOfPoints = 0

	def updateCenter(self,newCenter):
		self.center = newCenter

	def updateCenterByMean(self):
		pass

	def getCenter(self):
		return self.center

	def add(self, data):
		self.cluster.append(data)
		self.numberOfPoints = self.numberOfPoints+1
		self.methodSum = self.methodSum + data[1]
		self.protocolSum = self.protocolSum + data[3]
		self.pragmaSum = self.pragmaSum + data[5]
		self.cacheSum = self.cacheSum + data[6]
		self.connectSum = self.connectSum + data[12]
		self.contentLengthSum = self.contentLengthSum + data[13] 
		self.contentTypeSum = self.contentTypeSum + data[14] 

		if(data[7] in self.accept.keys()):
			self.accept[data[7]] =  self.accept[data[7]]+1
		else:
			self.accept[data[7]] = 1

		if(data[8] in self.acceptEnc.keys()):
			self.acceptEnc[data[8]] =  self.acceptEnc[data[8]]+1
		else:	
			self.acceptEnc[data[8]] = 1
		
		if(data[9] in self.acceptChar.keys()):
			self.acceptChar[data[9]] =  self.acceptChar[data[9]]+1
		else:
			self.acceptChar[data[9]] = 1
		
		self.center[1] = round(self.methodSum/self.numberOfPoints)
		self.center[3] = round(self.protocolSum/self.numberOfPoints)
		self.center[5] = round(self.pragmaSum/self.numberOfPoints)
		self.center[6] = round(self.cacheSum/self.numberOfPoints)
		self.center[12] = round(self.connectSum/self.numberOfPoints)
		self.center[13] = round(self.contentLengthSum/self.numberOfPoints)
		self.center[14] = round(self.contentTypeSum/self.numberOfPoints)
		self.center[7] = max(self.	accept.items(), key=operator.itemgetter(1))[0]
		self.center[8] = max(self.	acceptEnc.items(), key=operator.itemgetter(1))[0]
		self.center[9] = max(self.	acceptChar.items(), key=operator.itemgetter(1))[0]



	def getDataPoints(self):
		return self.cluster

	def printMeans(self):
		print("Method", self.methodSum)
		print("protocol", self.protocolSum)
		print("Pragma", self.pragmaSum)
		print("Cache", self.cacheSum)
		print("Connect", self.connectSum)
		print("Content Len", self.contentLengthSum)
		print("Content Type", self.contentTypeSum)
		print("Accept", self.accept)
		print("Accept Enc", self.acceptEnc)
		print("Accept Char", self.acceptChar)

X = np.array([14948, 1,	'http://localhost:8080/tienda1/publico/registro.jsp',	0,	'Mozilla/5.0 (compatible Konqueror/3.5 Linux) KHTML/3.5.8 (like Gecko)',0,	0, 	'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',	'x-gzip, x-deflate, gzip, deflate',	'utf-8, utf-8;q=0.5, *;q=0.5',	'en',	'localhost:8080',	0,	-100,	0,	'JSESSIONID=451E3DA61EFEEE2245FBBF203986A122','dniA=93202432S',0])
d1 = [14949, 1,	'http://localhost:8080/tienda1/publico/registro.jsp',	0,	'Mozilla/5.0 (compatible Konqueror/3.5 Linux) KHTML/3.5.8 (like Gecko)',0,	0, 	'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',	'x-gzip, x-deflate, gzip, deflate',	'utf-8, utf-8;q=0.5, *;q=0.5',	'en',	'localhost:8080',	0,	-100,	0,	'JSESSIONID=451E3DA61EFEEE2245FBBF203986A122','dniA=93202432S',0]
d2 = [1, 1,	'http://localhost:8080/tienda1/publico/registro.jsp',	0,	'Mozilla/5.0 (compatible Konqueror/3.5 Linux) KHTML/3.5.8 (like Gecko)',0,	0, 	'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',	'x-gzip, x-deflate, gzip, deflate',	'utf-8, utf-8;q=0.5, *;q=0.5',	'en',	'localhost:8080',	0,	-100,	0,	'JSESSIONID=451E3DA61EFEEE2245FBBF203986A122','dniA=93202432S',0]
d3 = [2, 1,	'http://localhost:8080/tienda1/publico/registro.jsp',	0,	'Mozilla/5.0 (compatible Konqueror/3.5 Linux) KHTML/3.5.8 (like Gecko)',0,	0, 	'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',	'x-gzip, x-deflate, gzip, deflate',	'utf-8, utf-8;q=0.5, *;q=0.5',	'en',	'localhost:8080',	0,	-100,	0,	'JSESSIONID=451E3DA61EFEEE2245FBBF203986A122','dniA=93202432S',0]
d4 = [3, 1,	'http://localhost:8080/tienda1/publico/registro.jsp',	0,	'Mozilla/5.0 (compatible Konqueror/3.5 Linux) KHTML/3.5.8 (like Gecko)',0,	0, 	'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',	'x-gzip, x-deflate, gzip, deflate',	'utf-8, utf-8;q=0.5, *;q=0.5',	'en',	'localhost:8080',	0,	-100,	0,	'JSESSIONID=451E3DA61EFEEE2245FBBF203986A122','dniA=93202432S',0]
d5 = [3, 1,	'http://localhost:8080/tienda1/publico/registro.jsp',	0,	'Mozilla/5.0 (compatible Konqueror/3.5 Linux) KHTML/3.5.8 (like Gecko)',0,	0, 	'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5,text/out',	'x-gzip, x-deflate, gzip, deflate, compress',	'utf-8, utf-8;q=0.5, *;q=0.5',	'en',	'localhost:8080',	0,	-100,	0,	'JSESSIONID=451E3DA61EFEEE2245FBBF203986A122','dniA=93202432S',0]
clus = Cluster(X)
print(clus.getCenter())
print("\n\n")
clus.add(d1)
clus.add(d2)
clus.add(d3)
clus.add(d4)
clus.add(d5)

#for i in clus.getDataPoints():
#	print(i)

#clus.printMeans()

print(clus.getCenter())
print("\n\n")
