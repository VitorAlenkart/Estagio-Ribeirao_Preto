entrada = input().lower();
count = 0

for i in range(0,len(entrada)):
    if entrada[i] == "a":
        count += 1

if count == 0:
    print("A letra 'a' não existe na palavra " + entrada)
else:
    print("A letra 'a' existe e se repete " + str(count) + " na palavra " + entrada)
