
p=int(input("Enter product number\n"))
cost=0.0
c=0

while p!=0 and c<10:
 if p==1:
		cost=cost+2.98
 elif p==2:		 
		cost=cost+4.50
 elif p==3:		 
		cost=cost+9.98
  	
 elif p==4:		 
		cost=cost+4.49	
 elif p==5:		 
		cost=cost+6.87	
 else:
	  print("Try again") 
 p=int(input("Enter product number\n"))
 c=c+1

print("------------------------------------")



print("The cost of the products purchased is %.2f and the number of the items purchased is %d"%(cost,c))
