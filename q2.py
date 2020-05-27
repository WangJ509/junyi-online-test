n = input('Please enter a number: ')
if not n.isnumeric():
    print ('This is not a number')
    exit()
n = int(n)
ans = 0
for i in range(1, n+1):
    flag = 0
    if i % 3 == 0:
        flag += 1
    if i % 5 == 0:
        flag += 1
    if flag == 0 or flag == 2:
        ans += 1
print (ans)
print (n - (n//3) - (n//5) + 2*(n//15))
