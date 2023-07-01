time1 = input()
time2 = input()

sets1 = [int(p) for p in input().split()]
sets2 = [int(p) for p in input().split()]

vencedor = ""
num_sets = 0

if sum(sets1) > sum(sets2):
    vencedor = time1
    num_sets = len(sets1)
elif sum(sets2) > sum(sets1):
    vencedor = time2
    num_sets = len(sets2)

print(vencedor + " (total " + str(num_sets) + " sets)")

