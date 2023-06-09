import csv

with open('Zeszyt.csv', 'r') as f:          #pobieranie danych z pliku Zeszyt.csf i przypisanie ich do zmiennej o nazwie lista wartości odzielone są średnikiem
    odczyt = csv.reader(f, delimiter=';')
    lista = list(odczyt)
with open('2020.csv','r')as g:
    wczytaj=csv.reader(g,delimiter=';') #ta sama sytuacja tylko pobieranie pliku 2020
    listaUbieglo=list(wczytaj)

def wyswietlPowiatyz2020():     #funkcja o nazwie wyswi.. ma za zadanie wyswietlic wszystkie powiaty i ich dane z roku 2020
    for kolumna in listaUbieglo:    #petla iteruje po wszytkich wartościach ze zmiennehj listaUbieglo
        print(kolumna)              #wypisuje te wartosci
        przerwa()                   #metoda przerwa jest zdefioniowana na samym ońcu skryptu i ma za zadanie wypisywać --------------- czyli taka linie przerywajaca

def wyswietlWszystkiePowiiaty():    #taka sama sytuacja jak wyzej tylko z 2021
    for kolimna in lista:
        print(kolimna)
        przerwa()

def obliczŚredniąWPolsce():     #funkcja oblicz.. ma za zadanie obliczyc sredniaProcentowa bezrobocia w polsce a takze srednia w tys
    sumaProcenty = 0            #deklaruje zmienna o nazwie sumaProcent i przypisuje 0 ma ona za zadanie sumowac procennty kazdego z powiatow
    sumaIloscWTys = 0           # ta sama sytuacja tylko z iloscia w tys
    iloscPowiatow = 0           # zmienna podliczajaca iloscPowiatow
    for kolumna in lista:       #petla iterujaca po wszystkich wartosciach  z lista i przypisujaca ich wartosci do zmiennej kolumna
        sumaProcenty += float(kolumna[2].replace(',', '.'))    #w petli po kazdej iteracji dodawana jets wartosc znajdujaca sie po drugim sredniku kolumna[2] czyli dla przykladu
        # tczewski;1,1;2,3;pomorskie czyli dodaje w tym wypdaku 2,3 metoda replace(',','.') wywolywana na kolumna[2] powoduje zamiane przecinka w . tak ze np. przy wartosic 2,3
        # zmienia ja 2.3 dzieki czemu program moze obliczyc gdyy zostawic wartosc w postaci z pzecinkiem powstalby blad
        sumaIloscWTys += float(kolumna[1].replace(',', '.')) # taka sama sytuacja tylko podliczajaca iloscWtyts ktore znajduje sie po pierwszym sredniku
        iloscPowiatow = iloscPowiatow + 1   # po kazdej itercji liczba zwieksza sie o jeden  czyli tczewski;2,3;1,3;pomorskie i dodaje 1 podliczajac powiaty czyli liczbe kolumn w pliku
    sredniaProcent = sumaProcenty / iloscPowiatow   #obliczanie sredniejPorcentowej czyli dzielenie sumyProcentowej ktora nam wyszla przez liczbe powiatow
    sredniaWTys = sumaIloscWTys / iloscPowiatow     #taka sama sytuacja tylko z tys
    przerwa()   #funkcja przerwa czyli ta powodujaca linie przerywnae

    return (sredniaProcent, sredniaWTys)     #na samym koncu funkcja zwraca wartosci sredniaProcent, sredniaWTys


def ileBezrobotnychWPolsce():  #funckja majaca za zadanie podliczanie ilosci bezrobotnych w polsce
    ileBezrobotnychWTys = 0 #poczatkowa wartosc
    for kolumna in lista:   #petla wykonujaca sie na kazdej z kolumn
        ileBezrobotnychWTys += float(kolumna[1].replace(',', '.')) #sumowanie ilosci

    return ileBezrobotnychWTys #funkcja zwraca ilosc


def ilemieszkańcówWPolsce(): #funkcja podliczajaca ile ludzi jest w polsce
    ileMieszkańcówWTys = 0
    for kolumna in lista:
        ileBezrobotnychWPowiecie = float(kolumna[1].replace(',', '.'))
        procentBezrobotnych = float(kolumna[2].replace(',', '.'))
        liczbaMieszkanowPowiatu = ileBezrobotnychWPowiecie * 100.0 / procentBezrobotnych

        ileMieszkańcówWTys += liczbaMieszkanowPowiatu
    return ileMieszkańcówWTys


def bezrobocieWPolsce():
    return ileBezrobotnychWPolsce() / ilemieszkańcówWPolsce() #funkcja obliczajaca poziom bezrobovia w procentach


def daneOWojewodztwie(wojewodztwo): #funcja majaca na celu zwrocenie danych o konkretnym wojewodztwie
    sumaProcent = 0
    sumaIlosc = 0
    iloscPowiatowWWojewodztwie = 0
    listaa = ileMieszkancowWWojewodztwach() #wywolanie metody ileMie.. ktora zwraca iloscMieszkancow znajdyuje ona sie 235 linijce i zwraca iloscMiesz
    print("Ilość mieszkańców:")
    print(listaa.get(wojewodztwo.upper()))
    for kolumna in lista:
        if wojewodztwo.upper() == kolumna[3].upper():
            print("Nazwa Powiatu"+kolumna[0]+" Ilosć bezrobotnych w tys "+kolumna[1]+" co stanowi "+kolumna[2]+"%")
            sumaIlosc += float(kolumna[1].replace(',', '.'))
            sumaProcent += float(kolumna[2].replace(',', '.'))
            iloscPowiatowWWojewodztwie = iloscPowiatowWWojewodztwie + 1

    sredniaProcent = sumaProcent / iloscPowiatowWWojewodztwie
    sredniaWTys = sumaIlosc / iloscPowiatowWWojewodztwie
    przerwa()

    return sredniaProcent, sredniaWTys #funkcja zwraca ilosci

def daneOPowiecie(powiat): #ta sama sytuacja tylko na powiatach
    for kolumna in lista:
        if powiat.upper() == kolumna[0].upper():
            print(kolumna)
            przerwa()
            return powiat


def sortujPoIlosc(): #funckja majaca na celu posortowanie kolumn po ilosci
    lista.sort(key=lambda lista: lista[1].replace(',', '.'))


def sortujPoProcencie(): #funckja sortowana po porcencie
    lista.sort(key=lambda lista: lista[2].replace(',', '.'))


def RankingPoiatowPoIlosci(): #funckja wypisujaca powiatu po sortowaniu
    sortujPoIlosc() #wywolanie funcji z 88 linijki
    for kolumna in lista:
        print(kolumna[0]) #wypisywanie w petli posortowanych danych
        przerwa()


def RankingPowiatowPoProcencie():
    sortujPoProcencie() #podobna sytuacja tylko po procentach
    for kolumna in lista:
        print(kolumna[0])
        przerwa()

def czyIstniejePowiat(powiat): #funckaj sprawdzajaca czy powiat ktory wpisze uzytkownik istnieje
    for i in lista:
        if(i[0].upper() == powiat.upper()): #jezeli istnieje funkcja zwroci 0
            return 0
    return 1 #jezeli nie zwrocci 1

def czyIstniejeWojewodztwo(wojew): #taka sama sytucja tylko na wojewodztwie
    for i in lista:
        if(i[3].upper() == wojew.upper()):
            return 0
    return 1
def dzialanieProgramu(): #glowana funkcja
    wybor = 0
    while wybor != 7: #uzytkownik ma mozliwosc wyboru dzialania program bedzie dzialala w petli dopoki uzytkownik nie wpisze 7 wtedy program sie skonczy
        przerwa()
        print('1.Informacje o Polsce')
        print('2.Dane o Województwie')
        print('3.Dane o Powiecie')
        print('4.Ranking Województw')
        print('5.Ranking powiatow')
        print('6.Porównanie obecnego bezrobocia względem 2020')
        print('7.Wyjscie')
        try:
            wybor = int(input('Wybierz dzialanie ')) #tutaj uzytkownik dokonuej wybory linijka wyzej ten try to poczatek wyjatku na wypadek gdyby uzytkownik wypisal np litere a program oczekuje liczby calkowitej
        except ValueError: #kontynuacja wyjatku oczekiwany blad to niezgodnosc danych oczekujemy ze uzytkownk wypisze liczbe calkowita
            #jezli nie zastosowalissmy wyjjatyku i uzytkownik wypisalby np. litere program by sie rozsypal
            print("Błąd") #jezeli wystapi blad w konsoli wypiszemy informacje
        finally: #jezli nie wystapi blad to ..
            if(wybor < 1 or wybor > 7): #sprawdzamy czy uzytkownik wpisal liczbe od 1 do 7 bo tyle jest opcji
                przerwa()
                print("Wybierz działanie od 1 do 7") # jezli wpisal liczbe wieksza od 7 albo mniejsza od 1 to wypiszemy mu info
            if (wybor == 1): #uzytkownik wybiera opcje 1...
                srednieBezrobocieNaPowiatWProcentach, srednieBezrobocieNaPowiatWTys = obliczŚredniąWPolsce() #do zmiennych sredniaBez.. i srednwtys... przypisujemy to co zwrocila funkcja
                #obliczSrredniaWpolsce znajduje sie ona w 20 linijce
                print("Srednia ilosc bezrobotnych na 1 powiat: ",
                      "{:.3f}".format(srednieBezrobocieNaPowiatWProcentach) + " tys.") #wypisujemy srednia i ja formatuje do 3 liczb po przecinku
                print("Sredni procent bezrobocia na 1 powiat: ", "{:.2f}".format(srednieBezrobocieNaPowiatWTys) + "%. ") #ta sama sytuacja tylko w procen
                print("Ile badanych w Polsce : ", "{:.3f}".format(ilemieszkańcówWPolsce()) + " tys.")
                print("Ile bezrobotnych w Polsce: ", "{:.3f}".format(ileBezrobotnychWPolsce()) + " tys.")
                print("Procent bezrobotnych w Polsce", "{:.2f}".format(bezrobocieWPolsce() * 100) + "%.")
            if (wybor == 2): #opcja nr 2
                    wojewodztwo = input("Podaj nazwę województwa") #pobieramy od uzytkownika nazwe wojewodzta z ktorego chce dane
                    if(czyIstniejeWojewodztwo(wojewodztwo.upper()) == 0): #sprawdzamy czy takie wojewodztwo istnieje wywolujac funnkcje czyIstniejeWo funkcja znajduje sie w 115 linicje
                        #jezeli istnieje wywolujemy funckje o nazwie daneOWoejwodz zznajduje sie ona w 60 linijce
                        daneOWojewodztwie(wojewodztwo)
                    else:
                        print("Takie wojewodztw nie istnieje") # podonae wojewodztwo nie istnieje
            if (wybor == 3): #wybor nr 3
                powiat = input("Podaj nazwę powiatu") #pobieramy nazwe powiatu
                if(czyIstniejePowiat(powiat) == 0): #sprawdzamy czy istnieje
                    daneOPowiecie(powiat) #jezeli istnieje wywolujemy funckje z linijki 80
                else:
                    print("Powiat nie istnieje") #nie istnieje
            if (wybor == 4): #wybor nr 4
                wojewodztwaRanking() #wywolujemy funckje z linijki 219
            if (wybor == 5): #nr 5
                RankingPowiatowPoProcencie() #wywolujemy funckje z linijki 103 zwroci ona posortowane po ilosci powaity
                RankingPoiatowPoIlosci() #funckja z linijki z 96 zwroci na posortowane po iloci powiaty
            if(wybor ==6): # nr 6
                powiat = input("Podaj nazwę powiatu") #taka sdama sytuacja pobieramy nazwe poiatu i poyem sprawdzamy czy istnieje
                if(czyIstniejePowiat(powiat.upper()) == 0): #jezli istnije to..
                    porownajDaneztegoiPoprezedniego(powiat) #wywolujemy funkcje z 190 linijki ma ona za zadanie pobrac dane z dwoc  pilikow i zobaczyc czy np.bezrobocie zmalalo wzroslo w stosunku do roku poprzedniego
                else:
                    print("Powiat nie istnieje")
            if (wybor == 7):
                #nr zakonczenie pracy petli czyli zakonczenie programu
                print("Koniec")


def ileBezrobotnychWWojewodztwach(): #funcka zwracajaca ilosc wartowsci ilosc bezrobocia  z kazdego z wojewodztw
    ileBezrobotnych = {} #bedzie to zbior danych
    for kolumna in lista: #iterowanie po kazdej z kolumn
        nazwaWojewodztwa = kolumna[3] #nazwa wojewodztwa
        ileBezrobotnychWPowiecie = float(kolumna[1].replace(',', '.')) #ilosc znajduje sie po 1 srdninku

        if nazwaWojewodztwa in ileBezrobotnych:
            ileBezrobotnych[nazwaWojewodztwa] += ileBezrobotnychWPowiecie #podliczaie ilsci bezrobotnych z kazdego z powiatow jezli maj takie sama nazwe
        else:
            ileBezrobotnych[nazwaWojewodztwa] = ileBezrobotnychWPowiecie

    return ileBezrobotnych

def porownajDaneztegoiPoprezedniego(powiat): #funkcja ma za zadanie pobranie danych z obu plikow czyli z 2020 i 2021 i porownanie ich ale z konkretnego powiatu
    wynik1=0 #zmienna reprezentujaca ilosc bezrobo z 2021
    wynik2=0 #reprezentuje procent z 2021
    wynik1pr=0 #reprezentuje ilosc z 2020
    wynik2pr=0 #procent z 2020 wszystkie wartsoci na poczatku maja wartosc 0
    for kolumna in lista: # iterowanie przez wszytkie kolumny pliku z 2021
        if powiat.upper() == kolumna[0].upper():
            wynik1=float(kolumna[1].replace(',', '.')) #przypisanie wartosci
            wynik1pr=float(kolumna[2].replace(',', '.'))

    for kolumna in listaUbieglo: #ta sama sytuacja tylko z 2020
        if powiat.upper() == kolumna[0].upper():
            wynik2=float(kolumna[1].replace(',', '.'))
            wynik2pr=float(kolumna[2].replace(',', '.'))
    if wynik1>wynik2: #porownywnaie jezeli ilosc bezrobocia z 2021 bylo wieksze niz w ubieglym roku to
        roznicapr=wynik1pr-wynik2pr #oblicznie roznicy ilosciowo
        procent=wynik1*100/wynik2 #oblicanie roznicy procentowo
        print("Bezrobocie spadło o :")
        print(roznicapr) #wypisywanie info
        print("Zmalało o:")
        print(procent-100)
    if wynik2>wynik1: #sytuacja przeciwna czyli w 2020 bezrobocie bylo wieksze
        roznicapr=wynik2pr-wynik1pr
        print("Bezrobocie wzrosło o (tys):")
        print(roznicapr*100)
        procent = wynik2 * 100 / wynik1
        print("Wzrosło o(%):")
        print(procent - 100)
        przerwa()
def wojewodztwaRanking(): #funckaj ma za zadanie stworzenie rankingu wojewodztw
    ileBezrobotnych = ileBezrobotnychWWojewodztwach() #przypisanie do zmiennej wartosci ktora zwrocila funkcja ileBezrobotnychWWojewodztwach znajduje sie ona w 178 linijce
    print("Ilosc bezrobotnych w tys. w kazdym z wojewodztw:")
    print(ileBezrobotnych) #wypisaiie wartsosci

    ileMieszkancow = ileMieszkancowWWojewodztwach() #wartosci z funckji ileMieszkancowWWojewodztwach z 239 linijce
    print("Ilosc mieszkancow w tys. w kazdym z wojewodztw:")
    print(ileMieszkancow)
    srednieBezrobocie = srednieBezrobocieWWojewodztwach(ileBezrobotnych, ileMieszkancow) # przypisanie wartosci z funckji srednieBezrobocieWWojewodztwach z 256 llinijki
    srednieBezrobocieLista = []
    for wojewodztwo in srednieBezrobocie: #iterowanie po wszystkich wartosciach z srednieBezrobocie
        srednieBezrobocieLista.append((wojewodztwo, srednieBezrobocie[wojewodztwo]))
    srednieBezrobocieLista.sort(key=lambda para: float(para[1][:-1])) #sortowanie wartosci i ponizej ich wypisanie
    print("Bezrobocie wg wojewodztw od najmniejszego: ", srednieBezrobocieLista)
    print("Najwieksze bezrobocie:", srednieBezrobocieLista[-1])
    print("Najmniejsze bezrobocie:", srednieBezrobocieLista[0])
    przerwa()


def ileMieszkancowWWojewodztwach(): #funckja podliczajaca i zwracjaaca ilosc mieszkancow z kadego z wjewodztw
    ileLudzi = {}
    for kolumna in lista:
        nazwaWojewodztwa = kolumna[3]
        ileBezrobotnychWPowiecie = float(kolumna[1].replace(',', '.'))
        procentBezrobotnych = float(kolumna[2].replace(',', '.'))

        liczbaMieszkanowPowiatu = ileBezrobotnychWPowiecie * 100.0 / procentBezrobotnych

        if nazwaWojewodztwa in ileLudzi:
            ileLudzi[nazwaWojewodztwa] += liczbaMieszkanowPowiatu
        else:
            ileLudzi[nazwaWojewodztwa] = liczbaMieszkanowPowiatu

    return ileLudzi


def srednieBezrobocieWWojewodztwach(ileBezrobotnych, ileMieszkancow):
    bezrobocieWWojewodztwie = {}

    for wojewodztwo in ileBezrobotnych:
        procent = ileBezrobotnych[wojewodztwo] / ileMieszkancow[wojewodztwo] * 100

        bezrobocieWWojewodztwie[wojewodztwo.lower()] = "{:.2f}".format(procent) + "%"

    return bezrobocieWWojewodztwie
def przerwa():
    print('----------------------------------------')
dzialanieProgramu()
