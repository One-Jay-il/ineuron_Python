a=input('Enter first name:')
b=input('Enter last name:')
c=a+' '+b
d=[]
for i in range (-1,-((len(c)+1)),-1):
   d.append(c[i])
e=''
e=''.join(d)
print('Reversed Name:',e)