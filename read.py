data = []
s = 0
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		s += len(data[count])
		count += 1   #count = count + 1
		if count % 100000 ==0: #%用來求餘數
			print(len(data))
print('檔案讀取玩了總共有',len(data),'筆資料')

print('每一筆資料的平均長度為:',s/len(data))