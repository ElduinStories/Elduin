import math
import sys

Fi = [0,0,0]

def mag(vec):
	return math.sqrt(vec[0]**2+vec[1]**2+vec[2]**2)

def dif(p1, p2):
	dv = [0,0,0]
	for i in xrange(3):
		dv[i] = p2[i]-p1[i]
	return dv

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

def plin(alv):
	return 1

def pprf(p1, p2):
	rf = [0,0,0]
	Rm = 10
	kr = 1
	d = dif(p1, p2)

	d2 = [0,0,0]
	for i in xrange(3):
		d2[i] = d[i]/Rm

	m = mag(d2)

	for i in xrange(3):
		rf[i] = -kr*d[i]/m

	return rf

def drag(vel):
	De = 1
	Fd = [0,0,0]
	for i in xrange(3):
		Fd[i]=-vel[i]*De
	return Fd

def accel(pos,vel,alv):
	FF = [0,0,0]
	Ft = F(pos,alv)
	for i in xrange(3):
		FF[i]+=Ft[i]
	Ft = drag(vel)
	for i in xrange(3):
		FF[i]+=Ft[i]
	ACC = [0,0,0]
	In = plin(alv)
	for i in xrange(3):
		ACC[i] = FF[i]/In
	return ACC

def findequ(pos,alv):
	maxCycles = 100000
	ini = pos
	for i in xrange(maxCycles):
		Force = F(ini,aln)
		mForce = mag(Force)
		for j in xrange(3):
			ini[j] += Force[j]/2

		if (mForce < 0.000001):
			break
	return ini

pos = map(float, sys.argv[1:4])
vel = [0,0,0]
acc = [0,0,0]
Force = [0,0,0]

aln = map(float, sys.argv[4:11])

maxCycles = 100000
tss = 0.0001
path = []
for i in xrange(maxCycles):
	acc = accel(pos,vel,aln)
	for j in xrange(3):
		vel[j]+=acc[j]*tss
		pos[j]+=vel[j]*tss
	path.append(pos)
#	if (mag(vel)<0.001):
#		print "Stopping Early"
#		break

print "Final Position: " + str(pos)
print "Final Velocity: " + str(vel)
print "Final Accelera: " + str(acc)


f1=open("path.mat","w")
line2= "ListPointPlot3D[{"
flag = 0
for r in path:

	if flag==1:
		line2 = line2 + ","
	if flag==0:
		flag = 1

	line = ""
	line2= line2 + "{" + str(math.floor(10000*r[0])/10000) + "," + str(math.floor(10000*r[1])/10000) + "," + str(math.floor(10000*r[2])/10000) + "}"

line2 = line2 +"}]\n"
f1.write(line2)
f1.close()
