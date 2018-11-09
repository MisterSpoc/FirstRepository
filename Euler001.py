import time

i=1
sum=0

while i<1000:
	if i%3 or i%5:
		print (i)
		sum += 1
	i+=1
print ("The sum is: ", sum)

input("Press enter to close")
