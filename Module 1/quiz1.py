""""""


strs = ["a"]

min_len = min(len(word) for word in strs)

result = []

for j in range(min_len):
    tmp = set()
    for i in range(len(strs)):
        tmp.add(strs[i][j])
    result.append(tmp)

output = ''
for x in result:
    if len(x) == 1:
        output += list(x)[0]
    else:
        output += ""
        break

print(len(output))
