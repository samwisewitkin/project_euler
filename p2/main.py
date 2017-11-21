fibs = [1, 2]
while True:
    if fibs[-1] > 4000000:
        break
    fibs.append(fibs[-1] + fibs[-2])

fibs = fibs[:-1]

total = 0
for f in fibs:
    if f % 2 == 0:
        total += f

print(total)