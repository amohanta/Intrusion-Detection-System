#this file generates the training and testing data
f=open("kddcup.data_10_percent_corrected","r")
str1=''

for i in range(0,80000):
	f.readline()

for i in range(0,5000):
	str1=str1+str(f.readline())

for i in range(0,1000):
	str1=str1+str(f.readline())


f1=open("data.txt","a")
f1.write(str1)

