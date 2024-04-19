while True:
   try:
     a=int(input('enter a: '))
   except ValueError:
       print('invalid a')
       continue

   try:
       b=int(input('enter b: '))
   except ValueError:
       print('invalid b')
       continue
   op=(input('enter op'))

   if op=='+':
      print('result is', int(a+b))
      break
   elif op=='-':
      print('result is',int(a-b))
      break
   elif op=='*':
      print('result is',int(a*b))
      break
   elif op=='/':
      print('result is',int(a/b))
      break
   else:
      print('invalid op')
