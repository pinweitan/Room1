#! /usr/bin/python

num = 10
for i in range(0, num+1):
	if i == num:
		print("TRADITION")
	elif i % 15 == 0:
		print("fizz buzz")
	elif i % 5 == 0:
		print("buzz")
	elif i % 3 == 0:
		print("fizz")
	else:
		print(i)
