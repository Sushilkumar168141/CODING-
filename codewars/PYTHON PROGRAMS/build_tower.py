'''
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *
a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
'''



a=[]
n_floors=3
length=n_floors*2-1
for i in range(n_floors):
    line=(((2*i)+1)*"*")
    x=line.center(length," ")
    a.append(x)
print(a)
