n = int(input("Enter any number ="))
def even_num():

    for i in range(1,n+1):
      res=i**2
      print(res)
      yield(res)

a=even_num()
print(a)

for x in range(1,n+1):
    next(a)


