alg = input()

alg_str = [ ]
for s in alg.split():
    alg_str.append(s)
print(alg_str)

alg_int = [ ]
for i in alg.split():
    i = int(i) * 2
    alg_int.append(i)
print(alg_int)

alg_float = [ ]
for f in alg.split():
    f = float(f) / 2
    alg_float.append(f)
print(alg_float)

print(len(alg_str))