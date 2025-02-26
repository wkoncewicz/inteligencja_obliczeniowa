import datetime, math
def main():
     name = input("Podaj imie: ")
     rokUrodzenia = int(input("Podaj rok urodzenia: "))
     miesiącUrodzenia = int(input("Podaj miesiąc urodzenia: "))
     dzienUrodzenia = int(input("Podaj dzien urodzenia: "))
     print("Witaj", name)
     dataUrodzenia = datetime.date(rokUrodzenia, miesiącUrodzenia, dzienUrodzenia)
     dzisiaj = datetime.date.today()
     dni = (dzisiaj - dataUrodzenia).days
     print("Żyjesz już", dni, "dni")
     fizyczna = math.sin((2*math.pi*dni)/23)
     emocjonalna = math.sin((2*math.pi*dni)/28)
     intelektualna = math.sin((2 * math.pi * dni) / 33)
     if fizyczna > 0.5:
          print("Gratuluję dobrej fali fizycznej!")
     elif dni < 0.5:
          print("Słaba fala mój bracie w chrystusie")
          if math.sin((2*math.pi*(dni+1))/23) > 0.5:
               print("Jutro będzie lepiej!")
     if emocjonalna > 0.5:
          print("Gratuluję dobrej fali emocjonalnej!")
     elif dni < 0.5:
          print("Słaba fala emocjonalna mój bracie w chrystusie")
          if math.sin((2*math.pi*(dni+1))/28) > 0.5:
               print("Jutro będzie lepiej!")
     if intelektualna > 0.5:
          print("Gratuluję dobrej fali intelektualnej!")
     elif dni < 0.5:
          print("Słaba fala intelektualna mój bracie w chrystusie")
          if math.sin((2*math.pi*(dni+1))/33) > 0.5:
               print("Jutro będzie lepiej!")
     print("Twoja fizyczna fala:", fizyczna)
     print("Twoja emocjonalna fala:", emocjonalna)
     print("Twoja intelektualna fala:", intelektualna)
main()
#punkty a b zajęły około 30/40 minut