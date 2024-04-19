file = open('ammara.txt', 'r')
output = file.read().split('\n')

print(output)
file.close()

lines = []
for line in output:
    line += '\n'
    lines.append(line)

file = open('ammara2.txt', 'w')
file.writelines(lines)
file.close()
