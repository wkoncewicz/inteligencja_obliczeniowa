import math
import datetime


def calculate_days_lived(year, month, day):
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()
    return (today - birth_date).days


def calculate_wave(days_lived, cycle):
    return math.sin((2 * math.pi * days_lived) / cycle)


def print_wave_status(wave_value, wave_name, days_lived, cycle):
    if wave_value > 0.5:
        print(f"Congratulations on the high value of {wave_name} wave!")
    elif wave_value < -0.5:
        print(f"That's a bummer, your {wave_name} wave is low.")
        next_day_wave = calculate_wave(days_lived + 1, cycle)
        if next_day_wave > 0.5:
            print("It will be better tomorrow!")


def main():
    name = input("Enter your name: ")
    year = int(input("Enter your year of birth: "))
    month = int(input("Enter your month of birth: "))
    day = int(input("Enter your day of birth: "))

    days_lived = calculate_days_lived(year, month, day)
    print(f"{name}, you have lived {days_lived} days.")

    physical_wave = calculate_wave(days_lived, 23)
    emotional_wave = calculate_wave(days_lived, 28)
    intellectual_wave = calculate_wave(days_lived, 33)

    print_wave_status(physical_wave, "physical", days_lived, 23)
    print_wave_status(emotional_wave, "emotional", days_lived, 28)
    print_wave_status(intellectual_wave, "intellectual", days_lived, 33)


if __name__ == "__main__":
    main()

#napisanie prompta zajęło ok. 3 minut