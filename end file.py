a=input('write a string :')
vowels=''
constonant=''
position=0
while position< len(a):
    char = a[position]

    if char in('a','e','i','o','u'):
        vowels += char
    else:
        constonant+=char
    position+=1

print("vowels: ", len(vowels))
print("constonant:",len(constonant))