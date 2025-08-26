numbers = [3,7,2,9,5,7]
target = 7

found = False
index_found = -1
checks = 0

i = 0
while i  < len(numbers) and found == False:
    checks = checks + 1
    if numbers [i] == target:
        found = True
        index_found = i
    i = i + 1

if found ==True:
    print("Found", target, "at index", index_found)
else:
    print(target, "not found in the list")
print("Positions checked:", checks, "out of", len(numbers))