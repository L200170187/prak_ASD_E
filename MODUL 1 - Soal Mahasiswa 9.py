def Rotate(arr, string):
    return [string] + arr[:4]

lastanswers=['UMS', '  4', 'Phyton', '  2', '  1']


for a in lastanswers[::-1]:
    print(a, end=' ')

n = 6
for n in range(6,101):
    ans = ''
    if 'Phyton' in lastanswers[2] : ans += 'Phyton'
    if 'UMS' in lastanswers[4] : ans += 'UMS'
    if len(ans)==0 : ans = "{:3}".format(n)
    print(ans, end=" ")
    lastanswers = Rotate(lastanswers, ans)

    if n % 15 == 0 : print()

print(n)
