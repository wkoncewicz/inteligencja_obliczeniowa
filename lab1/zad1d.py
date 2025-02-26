import datetime
import math


def calculate_biorhythm(dni, cycle):
    """Calculate the biorhythm wave based on the cycle length."""
    return math.sin((2 * math.pi * dni) / cycle)


def main():
    name = input("Podaj imię: ")

    try:
        rokUrodzenia = int(input("Podaj rok urodzenia: "))
        miesiącUrodzenia = int(input("Podaj miesiąc urodzenia: "))
        dzienUrodzenia = int(input("Podaj dzień urodzenia: "))

        dataUrodzenia = datetime.date(rokUrodzenia, miesiącUrodzenia, dzienUrodzenia)
        dzisiaj = datetime.date.today()
        dni = (dzisiaj - dataUrodzenia).days

        print(f"Witaj, {name}!")
        print(f"Żyjesz już {dni} dni.")

        # Calculate biorhythms
        fizyczna = calculate_biorhythm(dni, 23)
        emocjonalna = calculate_biorhythm(dni, 28)
        intelektualna = calculate_biorhythm(dni, 33)

        # Function to check and print wave messages
        def check_wave(wave, name):
            if wave > 0.5:
                print(f"Gratuluję dobrej fali {name}!")
            elif wave < -0.5:
                print(f"Słaba fala {name}, ale jutro może być lepiej!")
                if calculate_biorhythm(dni + 1, {"fizyczna": 23, "emocjonalna": 28, "intelektualna": 33}[name]) > 0.5:
                    print("Jutro będzie lepiej!")

        check_wave(fizyczna, "fizyczna")
        check_wave(emocjonalna, "emocjonalna")
        check_wave(intelektualna, "intelektualna")

        # Print wave values
        print(f"Twoja fizyczna fala: {fizyczna:.2f}")
        print(f"Twoja emocjonalna fala: {emocjonalna:.2f}")
        print(f"Twoja intelektualna fala: {intelektualna:.2f}")

    except ValueError:
        print("Błąd: Wprowadź poprawne liczby!")


if __name__ == "__main__":
    main()
