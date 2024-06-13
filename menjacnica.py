valuta1=input("unesite prvu valutu,izbori su rs,eur,usd")
valuta1=input("unesite drugu valutu,izbori su rs,eur,usd")
kolicina=int(input("kolicina:"))
dinuevr=0.0085
evrudin=117.08
dinuusd=0.0092
usdudin=108.82
evruusd=1.08
usduevr=0.93
if(valuta1=="rs" and valuta2=="eur"):
    resenje=kolicina*dinuevr
if(valuta1=="eur" and valuta2=="rs"):
    resenje=kolicina*evrudin
if(valuta1=="rs" and valuta2=="usd"):
    resenje=kolicina*dinuusd
if(valuta1=="usd" and valuta2=="rs"):
    resenje=kolicina*usdudin
if(valuta1=="eur" and valuta2=="usd"):
    resenje=kolicina*evruusd
if(valuta1=="usd" and valuta2=="rs"):
    resenje=kolicina*usduevr
print(resenje)
