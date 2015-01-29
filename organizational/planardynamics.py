import math
import sys

Fi = [0,0,0]

def mag(vec):
	return math.sqrt(vec[0]**2+vec[1]**2+vec[2]**2)

def Fc(Al,vec,Ac):
	d = [0,0,0]
	Fc = [0,0,0]

	if (Al=="o" or Al=="O" or Al==0):
		d[0] = -vec[0]
		d[1] = -vec[1]
		d[2] = 2 -vec[2]
	if (Al=="d" or Al=="D" or Al==1):
		d[0] = -vec[0]
		d[1] = -vec[1]
		d[2] = -2 -vec[2]

	if (Al=="t" or Al=="T" or Al==2):
		d[0] = -vec[0]
		d[1] = 1 -vec[1]
		d[2] = -vec[2]
	if (Al=="a" or Al=="A" or Al==3):
		d[0] = -vec[0]
		d[1] = -1 -vec[1]
		d[2] = -vec[2]

	if (Al=="i" or Al=="I" or Al==4):
		d[0] = 1 -vec[0]
		d[1] = -1 * vec[1]
		d[2] = -1 * vec[2]
	if (Al=="q" or Al=="Q" or Al==5):
		d[0] = -1 -vec[0]
		d[1] = -vec[1]
		d[2] = -vec[2]

	m = mag(d)

	Fc[0] = Ac*d[0]/m
	Fc[1] = Ac*d[1]/m
	Fc[2] = Ac*d[2]/m

	return Fc

def F(vec,alv):
	F = [0,0,0]
	for i in xrange(6):
		Ft = Fc(i,vec,alv[i])
		for j in xrange(3):
			F[j] += Ft[j]
	return F

vec = map(float, sys.argv[1:4])
aln = map(float, sys.argv[4:11])

maxCycles = 100000
ini = vec
for i in xrange(maxCycles):
	Force = F(ini,aln)
	mForce = mag(Force)
	for j in xrange(3):
		ini[j] += Force[j]/2

	if (mForce < 0.000001):
		print "Hey!"
		break

print "Final position: " + str(ini)


