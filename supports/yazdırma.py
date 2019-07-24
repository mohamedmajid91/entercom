tur = 0

while True:
    tur=tur+1
    ths = open("input.txt", "a")
    ths.write(str(tur)+","+str(log)+"\n")
    tsh = open("input.txt","r")
    print(tsh.read())
