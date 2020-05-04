a=input('Enter lower limit:')
a=int(a)
b=input('Enter upper limit:')
b=int(b)
c=a
print('List of Numbers',end=':')
for i in range( 0,((b-a)+1),1):
 if (c%5 != 0)&(c%7 == 0):
      print(c,end=',')
 c=c+1