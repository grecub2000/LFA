def verificare(sinitiala,sfinale,cuvant,d):
    i=0
    ok=1
    j=sinitiala
    while ok and i<len(cuvant):
        if cuvant[i] in d[j].keys():
            j=d[j][cuvant[i]]
            i+=1
        else:
            if j not in sfinale or i!=len(cuvant):
                ok=0
    if j not in sfinale:
        ok=0
    if ok:
        print('Cuvant acceptat')
    else:
        print('Cuvant respins')
        
        


with open ('date.txt') as f:
    lstari=f.readline().split()
    d={}
    for i in lstari:
        d[i]={}
    sinitiala=f.readline()
    sinitiala=sinitiala.replace("\n", "")
    sfinale=f.readline().split()
    x=f.readline().split()
    while x:
        d[x[0]][x[1]]=x[2]
        x=f.readline().split()
with open('cuvant.txt') as g:
    cuvant=g.readline()
    print(cuvant)
    verificare(sinitiala,sfinale,cuvant,d)
        
        
