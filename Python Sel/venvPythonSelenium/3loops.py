msg = "good morning"
if msg == "morning":
  print("in if")
else:
  print("in else")
print("outside if else")

values = [2,4,6,8]
for i in values:
  print(i)
  print(i*2)

add = 0
for j in range(1,6):    #range is range of number exclusive of last index. here it is 1 to 5
  print(j)
  add = add + j
print(add)

print("****jumping index******")
for k in range(1,10,2):  #jumping index 1 3 5 7 9
  print(k)

print("****skipping first index******")
for l in range(10):  #jumping first index. python takes default as 0. so will print 0-9
  print(l)

print("**********while*************")
it = 10
while it > 1:
  if it == 9:
    it = it-1   #this is imp. as if we dont do this, the loop is stuck in infinite loop coz it never changes from 9 as the iteration is skipped
    continue    #just skip the current iteration and start with the next iteration
  if it == 3:
    break       #come out of loop
  print(it)
  it = it-1