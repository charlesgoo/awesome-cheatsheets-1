#!/usr/bin/python
##In this file, simple examples will be used to introduce all python functions:

Level=input('input level of the Hanno tower: ')
##Input parameters

def Hanno(n,a,b,c):
	## define functions
	n=int(n)
	if n==1:
		print('disk',n,':',a,'->',c)
	else:
		Hanno(n-1,a,c,b)
		print('disk',n,':',a,'->',c)
		Hanno(n-1,b,a,c)
	return

Hanno(Level,'A','B','C')
## use functions