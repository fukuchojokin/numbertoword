import inflect
p = inflect.engine()
x = int(input("Enter number: "))
i = 0
list = []
while True:
    words = p.number_to_words(i)
    i += 1
    y = words.capitalize()
    list.append(y)
    if i >= x:
        break
print(list)

