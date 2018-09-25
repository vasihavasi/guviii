S1 = 10
S2 = 20
S3 = 30

if (S1 >= S2) and (S1 >= S3):
   largest = S1
elif (S2 >= S1) and (S2 >= S3):
   largest = S2
else:
   largest = S3

print("The largest number between",S,",",S2,"and",S3,"is",largest)
