# n1 = [1,2,5]
# n2 = [3,6,4]
# n1.extend(n2)
# lent = len(n1)
# i=0
# while i<(lent-1):
#   if n1[i]<n1[i+1]:
#     n1[i]=n1[i]
#     i=i+1
#   else:
#     n1[i]=n1[i+1]
#     i=i+1
# print(n1)
n1 = [3,2,5,4,1]
lent = len(n1)
empty = []
for i in range(lent):
  for j in range(lent):
    if n1[i]>n1[j]:
      n1[i]=n1[j]
      empty.append(n1[j])
    else:
      n1[i]=n1[i]
      empty.append(n1[i])
  print(empty)
    

