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