yt = 0
snap = 0
ttk = 0

while True:
    rede = input()
    
    if rede == 'Y':
        tempo = int(input())
        yt += tempo
    elif rede == 'S':
        tempo = int(input())
        snap += tempo
    elif rede == 'T':
        tempo = int(input())
        ttk += tempo
    
    total = yt + snap + ttk

    if rede == '.':
        break
print('tiktok:', ttk)
print('youtube:', yt)
print('snapchat:', snap)
print('total:', total)