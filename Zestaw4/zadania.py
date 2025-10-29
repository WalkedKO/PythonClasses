#4.2
def make_ruler(n):
    top_line = ("|...." * n) + "|"
    bottom_line = ""
    for i in range(n):
        size = len(str(i + 1))
        bottom_line += (str(i) + (" " * (5 - size)))
    bottom_line += str(n)
    return top_line + '\n' + bottom_line

def make_grid(rows, cols):
    line_top = "+---" * (cols) + "+"
    line_bot = "|   " * (cols) + "|"
    line_all = (line_top + "\n" + line_bot + "\n") * rows + line_top
    return line_all

# 4.3
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

#4.4
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    first = 0
    second = 1
    for i in range(1, n):
        rep = second
        second = first + second
        first = rep
    return second

#4.5
def odwracanie_iter(L, left, right):
    i = left
    j = right
    while i < j:
        pom = L[i]
        L[i] = L[j]
        L[j] = pom
        i += 1
        j -= 1

def odwracanie_rek(L, left, right):
    if left >= right:
        return L
    pom = L[left]
    L[left] = L[right]
    L[right] = pom
    odwracanie_rek(L, left + 1, right - 1)
    return L

#4.6
def sum_seq(sequence):
    result = 0
    if isinstance(sequence, (list, tuple)):
        result = sum(sum_seq(i) for i in sequence)
    else:
        result = sequence
    return result

#4.7
def flatten(sequence):
    result = []
    for element in sequence:
        if isinstance(element, (list, tuple)):
            result += flatten(element)
        else:
            result.append(element)
    return result
print("\n4.2")
print(make_ruler(15))
print(make_grid(6,4))

print("\n4.3")
n = 4
print("Factorial of ", n, " is ", factorial(n))

print("\n4.4")
n = 7
print(n, " element of fibonacci sequence is: ", fibonacci(n))

print("\n4.5")
L = [1,2,3,4,5,6,7]
left = 1
right = 5
odwracanie_iter(L, left, right)
print("Iteracyjnie: ", L)
L = [1,2,3,4,5,6,7]
odwracanie_rek(L, left, right)
print("Rekurencyjnie: ", L)

print("\n4.6")
seq = [1, 2, [3, 4, [5], [6, 7]], 8, [9]]
print(sum_seq(seq))

print("\n4,7")
sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]