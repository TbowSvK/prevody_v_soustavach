Vstup=int(input("Vstupní hodota: "))
Vstupni_soustava=int(input("Vstupní soustava: "))
Vystupni_soustava=int(input("Do soustavy: "))

def Prevod_hodnot(x):
    if x == 10:
        return("A")
    elif x == 11:
        return("B")
    elif x == 12:
        return("C")
    elif x == 13:
        return("D")
    elif x == 14:
        return("E")
    elif x == 15:
        return("F")
    else:
        return(x)

def Prevod_do_desitkove_soustavy(pocatecni_vystupni_soustava, prevadena_hodnota):
    prevadena_hodnota=list(map(int, str(prevadena_hodnota)))
    prevadena_hodnota.reverse()
    Vysledek=0
    j=0
    for i in prevadena_hodnota:
        print(f"{i} * {str(pocatecni_vystupni_soustava)}^{j} = {i*(pocatecni_vystupni_soustava**j)}")
        Vysledek += i*(pocatecni_vystupni_soustava**j)
        j+=1
    print("Výsledek v 10 soustavě: "+str(Vysledek))
    return(Vysledek)

def Prevod_z_desitkove_soustavy_do_x_soustavy(vstupni_hodnota, soustava):
    Vysledek=[]
    while vstupni_hodnota >= soustava:
        print(f"{vstupni_hodnota} % {soustava} = {Prevod_hodnot(Vstup % soustava)}")
        Vysledek.insert(0, Prevod_hodnot(vstupni_hodnota % soustava))
        vstupni_hodnota = vstupni_hodnota//soustava
    else:
        print(f"{vstupni_hodnota} % {soustava} = {Prevod_hodnot(vstupni_hodnota)}")
        Vysledek.insert(0, Prevod_hodnot(vstupni_hodnota))
        print(f"{Vysledek} v {str(soustava)} soustavě.")

if Vstupni_soustava == 2:
    Binarni=list(map(int, str(Vstup)))
    Vstupni_string = ""
    Vystupni_string = ""

    if Vystupni_soustava == 10:
        Prevod_do_desitkove_soustavy(Vstupni_soustava, Binarni)

    elif Vystupni_soustava == 8:
        Vysledek=[]
        while len(Binarni) % 3 != 0:
            Binarni.insert(0, 0)
        for n in range(int(len(Binarni)/3)):
            Mezi_vysledek = 0
            
            Mezi_vysledek += Binarni[(n*3)] * 2**2
            Mezi_vysledek += Binarni[(n*3)+1] * 2**1
            Mezi_vysledek += Binarni[(n*3)+2] * 2**0
            Vysledek.append(Mezi_vysledek)
            Vstupni_string += (f"{Binarni[(n*3)]} {Binarni[(n*3)+1]} {Binarni[(n*3)+2]} |")
            Vystupni_string += (f"{Binarni[(n*3)] * 2**2} {Binarni[(n*3)+1] * 2**1} {Binarni[(n*3)+2] * 2**0} |")

        print(Vstupni_string)
        print(Vystupni_string)
        print(Vysledek)

    elif Vystupni_soustava == 16:
        Vysledek=[]
        while len(Binarni) % 4 != 0:
            Binarni.insert(0, 0)
        for n in range(int(len(Binarni)/4)):
            Mezi_vysledek = 0
            
            Mezi_vysledek += Binarni[(n*4)] * 2**3
            Mezi_vysledek += Binarni[(n*4)+1] * 2**2
            Mezi_vysledek += Binarni[(n*4)+2] * 2**1
            Mezi_vysledek += Binarni[(n*4)+3] * 2**0
            Vysledek.append(Prevod_hodnot(Mezi_vysledek))
            Vstupni_string += (f"{Binarni[(n*4)]} {Binarni[(n*4)+1]} {Binarni[(n*4)+2]} {Binarni[(n*4)+3]} |")
            Vystupni_string += (f"{Binarni[(n*4)] * 2**3} {Binarni[(n*4)+1] * 2**2} {Binarni[(n*4)+2] * 2**1} {Binarni[(n*4)+3] * 2**0} |")

        print(Vstupni_string)
        print(Vystupni_string)
        print(Vysledek)

elif Vstupni_soustava == 8:
    if Vystupni_soustava == 10:
        Prevod_do_desitkove_soustavy(Vstupni_soustava, Vstup)
    elif Vystupni_soustava == 2 or Vystupni_soustava == 16:
        Prevod_z_desitkove_soustavy_do_x_soustavy(Prevod_do_desitkove_soustavy(Vstupni_soustava, Vstup), Vystupni_soustava)

elif Vstupni_soustava == 10:
    Prevod_z_desitkove_soustavy_do_x_soustavy(Vstup, Vystupni_soustava)

elif Vstupni_soustava == 16:
    if Vystupni_soustava == 2 or Vystupni_soustava == 8:
        Prevod_z_desitkove_soustavy_do_x_soustavy(Prevod_do_desitkove_soustavy(Vstupni_soustava, Vstup), Vystupni_soustava)
    elif Vystupni_soustava == 10:
        Prevod_do_desitkove_soustavy(Vstupni_soustava, Vstup)