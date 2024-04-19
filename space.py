a=input('enter string: ')
i=0
result=''
while i<len(a):
    char=a[i]
    if char==' ':
        result+='  '
    else:
        result+=char
    i+=1
print(result)