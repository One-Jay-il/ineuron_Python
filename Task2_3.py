a=input('Enter a Word:')
d=[]
for i in range (-1,-((len(a)+1)),-1):
   d.append(a[i])
e=''
e=''.join(d)
print('Reversed Name:',e)