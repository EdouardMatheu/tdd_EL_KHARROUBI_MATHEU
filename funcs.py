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