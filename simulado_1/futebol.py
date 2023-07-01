time1 = input()
time2 = input()

gols_time1 = int(input())
gols_time2 = int(input())

if gols_time1 > gols_time2:
    print('vitoria:', time1)
elif gols_time2 > gols_time1:
    print('vitoria:', time2)
elif gols_time1 == gols_time2:
    print('prorrogação!')

    p_gols_time1 = input()
    p_gols_time2 = input()

    if p_gols_time1 > p_gols_time2:
        print('vitoria:', time1)
    elif p_gols_time2 > p_gols_time1:
        print('vitoria', time2)
    elif p_gols_time1 == p_gols_time2:
        print('disputa de penaltis!')
