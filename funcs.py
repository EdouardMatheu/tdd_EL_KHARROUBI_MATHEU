import math

def max_int(a,b):
	if a < b :
		return b
	else :
		return a

def min_int(a,b):
	if a > b :
		return b
	else :
		return a

def mean_int(l):
	s = 0.0
	for i in range(0, len(l)) :
		s += l[i]
	s /= len(l)
	return s

def median_int(l):
	l.sort()
	if len(l)==0 : 
		return None
	elif len(l)%2==0:
		return l[(len(l)//2)-1]
	else: 	
		return l[len(l)//2]

def std_dev(l):
	mu = mean_int(l)
	s = 0.0
	for e in l :
		s += (e - mu)*(e - mu)
	s /= len(l)
	return math.sqrt(s)

def is_geo_progression(l):
	temp1 = l[1]%l[0]
	for i in range(2,len(l)):
		temp = l[i]%l[i-1]
		if (temp != temp1):
			return False 
		temp1 = temp
	return True

def is_ari_progression(l):
	temp1 = l[1]-l[0]
	for i in range(2,len(l)):
		temp = l[i]-l[i-1]
		if ( temp != temp1):
			return False 
		temp1=temp
	return True

def geo_progression(n,l):
	temp1 = l[1]%l[0]
	for i in range(2,len(l)):
		temp = l[i]%l[i-1]
		if (temp != temp1):
			return False 
		temp1 = temp

	temp1 = l[-1]//l[-2]
	temp = l[-1]*temp1
	l2 = []
	if n != 0 : l2.append(temp)
	for i in range(n-1):
		u = l2[i] * temp1
		l2.append(u)
	return True, l2

def ari_progression(n,l):
	temp1 = l[1]-l[0]
	for i in range(2,len(l)):
		temp = l[i]-l[i-1]
		if (temp != temp1):
			return False 
		temp1 = temp
	temp1 = l[-1]-l[-2]
	temp = l[-1] + temp1
	l2 = []
	if n != 0 : l2.append(temp)
	for i in range(n-1):
		u = l2[i] + temp1
		l2.append(u)
	return True, l2