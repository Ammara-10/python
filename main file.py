from functinnn import sum,subtract,multiply,divide

a = int(input('enter a: '))
b = int(input('enter b: '))
op= input('enter op: ')
if op == '+':
    print('result is', sum(a ,b))
elif op == '-':
    print('result is', subtract(a, b))
elif op == '*':
    print('result is', multiply(a ,b))
elif op == '/':
    print('result is', divide(a, b))

else:
    print('invalid op')
