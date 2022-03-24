data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1   #count = count + 1
		if count % 100000 ==0: #%用來求餘數
			print(len(data))
print(len(data))
