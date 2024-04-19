a=input('write a string :')
digits=''
position=0
result = ''
while position< len(a):
    char = a[position]
    if char.isdigit():
        result += char
    position+=1

print("Digits: ", result)