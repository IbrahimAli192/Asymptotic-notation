scores = [85, 90, 78, 92, 88]

target = int(input("Enter a score to search for: "))

steps = 0

for score in scores:
    steps += 1
    if score == target:
        break

print("number found:", target)
print("checks needed:", steps)

print("best case: 1 check -> O(1)")
print("worst case: n checks -> O(n)")
print("average case: about n/2 checks -> O(n)")

print("final big-O: O(n)")