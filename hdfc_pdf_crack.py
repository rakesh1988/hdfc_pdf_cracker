import PyPDF2 as pypdf
import sys
import subprocess
import threading 
import argparse
from multiprocessing import Process, Pool

parser = argparse.ArgumentParser()  

parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()


filePath = args.file
inputFile = pypdf.PdfFileReader(open(filePath, "rb"))

output = pypdf.PdfFileWriter()

def decryptFile(customerId):
	if(customerId%1000==0):
		print(customerId)
	try:
		inputFile.decrypt(str(customerId)) #if this fails goes to except
		for pageNumber in range (0, inputFile.getNumPages()):
			output.addPage(inputFile.getPage(pageNumber))
			outputStream = open(str(customerId)+"-decrypted.pdf", "wb")
			output.write(outputStream)
			outputStream.close()
			print ("Decoded password is " + str(customerId))
			sys.exit(1)
	except pypdf.utils.PdfReadError:
		pass

def looper(start: int,end: int):
	for currCustId in range(start, end):
		#print(currCustId)
		decryptFile(currCustId)

p1 = Process(target=looper, args=(10000000,20000000))
p2 = Process(target=looper, args=(20000000,30000000))
p3 = Process(target=looper, args=(30000000,40000000))
p4 = Process(target=looper, args=(40000000,50000000))
p5 = Process(target=looper, args=(50000000,60000000))
p6 = Process(target=looper, args=(60000000,70000000))
p7 = Process(target=looper, args=(70000000,80000000))
p8 = Process(target=looper, args=(80000000,90000000))
p9 = Process(target=looper, args=(90000000,100000000))


p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p9.start()


p1.join()
p2.join()
p3.join()
p4.join()
p5.join()
p6.join()
p7.join()
p8.join()
p9.join()


print("done")
