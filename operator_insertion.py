import random as r

#Parameter Setting
seq     = ['6','5','4','3','2']
op      = ['+','-','*','/']
Target  = 32
Iterations  = 1000    # Number of Inerations

finalSeq = []
finalSeq.append(seq[0])
print(finalSeq)

for i in seq[1:]:
  finalSeq.append(''.join(r.sample(op,1)))
  finalSeq.append(i)
  print(finalSeq)

exp=''.join(finalSeq)
print("\nExpression: ", exp)

print("Expression Value: ", eval(exp))

# Loop till number of Iterations

f=0
for i in range(Iterations):

  finalSeq = []
  finalSeq.append(seq[0])
  for i in seq[1:]:
    finalSeq.append(''.join(r.sample(op,1)))
    finalSeq.append(i)
  
  exp=''.join(finalSeq)

  if eval(exp) == Target:
    f=1
    print (exp, "  ", eval(exp))

    
if f==0:
  print("No Sequence found !!")