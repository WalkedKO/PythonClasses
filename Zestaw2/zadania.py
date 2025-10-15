# 2.10
line = "abc   \tgfds\nabc"
print("2.10: ",len(line.split()))
# 2.11
word = "slowo"
print("2.11:", "_".join(list(word)))
# 2.12
from_first = "".join([i[0] for i in line.split()])
from_last = "".join([i[-1] for i in line.split()])
print("2.12: \nFrom first letters: ", from_first)
print("From last letters: ", from_last)
# 2.13
print("2.13: ", sum(len(i) for i in line.split()))
# 2.14
max_word = max(line.split(), key=len)
print("2.14:")
print("Max: ", max_word)
print("Max length: ", len(max_word))
# 2.15
print("2.15:")
L = ["abc", 12, "h", ("a", "b"), 15]
print("".join([str(i) for i in L if isinstance(i, int)]))
# 2.16
print("2.16:")
line = "abced GvR gvr dcee"
replaced = line.replace("GvR", "Guido van Rossum")
print("Original: ", line)
print("Replaced: ", replaced)
# 2.17
print("2.17:")
print("Original: ", line)
print("Alphabetically: ", " ".join(sorted(line.split(), key=str.lower)))
print("By length: ", " ".join(sorted(line.split(), key=len)))
# 2.18
print("2.18:")
number = 10421905010
print("Number: ", number)
print("Zeros: ", str(number).count('0'))
# 2.19
print("2.19:")
L = [1, 54, 143, 2]
L_str = [str(i) for i in L]
L_result = [i.zfill(3) for i in L_str]
print(L_result)