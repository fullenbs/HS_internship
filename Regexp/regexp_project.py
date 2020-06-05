import re
fname = input("Enter the file name:")
f = open(fname)

sum = 0
#values = 0

for l in f:
     nums = re.findall('([0-9]+)', l)
     print(nums)
     if len(nums) != 0:
         for i in nums:
             #values = values + 1
             tmp = int(i)
             sum = sum + tmp

print(sum)
#print(values)
