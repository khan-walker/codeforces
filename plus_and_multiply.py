for s1 in[*open(0)][1:]:n,a,b=map(int,s1.split());print('YNeos'[all(n<a**k or (n-a**k)%b for k in range(32))::2])
 	  		  									   		