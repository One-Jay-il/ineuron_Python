a=int(input("Enter maximum no of stars to be displayed on a single rows:"))
for i in range(0,a):
   for j in range(0,i+1):
      print('*',end='')
   print('\r')
for i in range(a,0,-1):
   for j in range(0,i-1):
      print('*',end='')
   print('\r')