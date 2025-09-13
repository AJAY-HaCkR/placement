s = input().strip()
result = ""

for i in range(len(s)):
    duplicate = False
    for j in range(i):
        if s[i] == s[j]:
            duplicate = True
            break
    if not duplicate:
        result += s[i]

print(result)
