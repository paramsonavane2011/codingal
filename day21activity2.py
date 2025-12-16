series = ["hello", "fw", "uiojhirghou"]
count = 0

for a in series:
    if len(a) > 2:
        if a[0] == a[-1]:
            count += 1

print(count)