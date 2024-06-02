X = int(input())
N = int(input())
total = 0
for i in range(N):
  a,b = input().split()
  total += int(a)*int(b)
  
if X == total:
   print("Yes")
else:
  print("No")
  