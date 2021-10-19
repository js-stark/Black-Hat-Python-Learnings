n = int(input('Enter the number of rows needed'))
a,b,c=[],[],[]
for i in range(1,n+1):
       a.append('* '*i)
for j in range(n,0,-1):
    b.append(' '*j)
for i,j in zip(a,b):
    c.append(j+i)
for i in c:
    print(i)


#     *
#    * *
#   * * *
#  * * * *
# * * * * *