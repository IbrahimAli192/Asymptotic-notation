n = 10
input("O(1): one calculation. press Enter to continue...")

steps = 1
print("steps = ", steps, "-> O(1)")
print("same number of steps even if n increases to 1000 or 1,000,000")
input("O(n): one step for every item. press Enter")

steps = 0
for i in range(n):
    steps += 1
print("steps = ", steps, "-> O(n)")
print("steps increase when n increases to 1000 or 1,000,000")

input("O(n^2): two loops. press Enter to continue...")

steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print("steps = ", steps, "-> O(n^2)")
print("for n = 10, steps = 10 x 10 = 100")
input("other big O termns. press Enter to continue...")

print("O(1): constant")
print("O(n): linear")
print("O(n^2): quadratic")