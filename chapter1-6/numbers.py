numbers_1 = range(0,1000000,2)
numbers_2 = range(1,1000001,2)
sums = []
for a in numbers_1:
	for b in numbers_2:
		if b==a+1:
			sums.append(a+b)

print(max(sums))
print(min(sums))
print(sum(sums))
