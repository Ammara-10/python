age = 18
name = "muhammad"

# answer = "I am " + name + " and I am " + age + "years old"
# print(answer)

answer = f"I am {name} and I am {age} years old"
print(answer)

list_answer = answer.split(" ")
print(list_answer)

string_answer='  '.join(list_answer)
print(string_answer)