def grouping(n):
   odd=[]
   even=[]
   for i in range(1, n+1):
       if i%2 ==1:
           odd.append(i)
       else:
           even.append(i)
   print(odd,"第一組")
   print(even,"第二組")
grouping(n=24)
