#3.3
print("3.3: (zakładając że 0 jest podzielne przez 3)")
for i in range(31):
    if i % 3 != 0:
        print(i)

#3.4
print("3.4: ")
while True:
    print("Type a float, if you want to stop, type: stop")
    line = input("Here:")
    if line == "stop":
        break
    else:
        sides = line.split(".")
        sides[0] = sides[0].lstrip('-')
        numbers = [i.isdigit() for i in sides]
        sides = line.split('.')
        if (len(sides) in range(1,3) and False not in numbers) or (sides[0] == '' and numbers[1]):
            nr = float(line)
            print("Number: ", nr)
            print("^3: ", pow(nr, 3))
        else:
            print("Write a float please...")

#3.5
print("3.5: ")
length = 12
top_line = ("|...." * length) + "|"
bottom_line = ""
for i in range(length):
    size = len(str(i + 1))
    bottom_line += (str(i) + (" " * (5 - size)))
bottom_line += str(length)
print(top_line)
print(bottom_line)
#3.6
print("3.6: ")
x = 4
y = 2
line_top = "+---" * (x) + "+"
line_bot = "|   " * (x) + "|"
line_all = (line_top + "\n" + line_bot+"\n") * y + line_top
print(line_all)

#3.8
print("3.8: ")
A = "abc123"
B = "cde321"
A_set = set(A)
B_set = set(B)
print("Wspolne: ", A_set.intersection(B_set))
print("Suma w obu: ", A_set.union(B_set))

#3.9
sequence = [[],[4],(1,2),[3,4],(5,6,7)]
result = [sum(i) for i in sequence]
print(result)

#3.10

#można też stworzyć funkcję z ifami biorącą znak za argument, a zwracającą int w arabskim
dictionary = {'I': 1, "V": 5, "X": 10, "L": 50, "C":100, "D":500, "M":1000}
def roman2int(roman, roman_dict):
    list_of_signs = list(roman)
    result = 0
    for i, sign in enumerate(list_of_signs):
        if i != len(list_of_signs) - 1:
            if roman_dict[sign] < roman_dict[list_of_signs[i + 1]]:
                result -= roman_dict[sign]
            else:
                result += roman_dict[sign]
        else:
            result += roman_dict[sign]
    return result
print(roman2int("MMV", dictionary))