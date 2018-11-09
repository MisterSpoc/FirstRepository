import math
import time

def main():

	compare = 0

	for i in range (100, 999):
		for j in range (100, 999):
			product = i*j
			str_product = str(product)
			length = len(str_product)
			if pd(length, str_product, compare) is True:
				if product > compare:
					compare = product
	print ("The largest palindrome product of 3 digit numbers is: ", compare)
	return


def pd(length, str_product, compare):

	test_value = True

	for c in range (1, int(length/2)+1):
		if str_product[c-1] != str_product[length-c]:
			test_value = False

	return test_value


main()
time.sleep(2)
input("Press enter to exit.")
