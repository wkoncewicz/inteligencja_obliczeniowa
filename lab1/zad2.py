from random import randint
import math
import matplotlib.pyplot as plt
import numpy as np
odleglosc = randint(50, 340)
print(f"Odległość do pokonania: {odleglosc}")
while True:
    alpha = int(input("Podaj kąt wystrzału: "))
    rad_alpha = math.radians(alpha)
    v = 50
    h = 100
    g = 9.8
    distance = ((v*math.sin(rad_alpha)) + math.sqrt((v*v*math.sin(rad_alpha)**2) + 2*g*h)) * ((v*math.cos(rad_alpha))/g)
    if distance >= odleglosc-10 and distance <= odleglosc+10:
        print("Cel trafiony!")
        break
    else:
        print("Nawet go nie zarysowaliśmy... Spróbuj ponownie")
        range_x = (v * math.cos(rad_alpha)) * (v * math.sin(rad_alpha) + math.sqrt(v**2 * math.sin(rad_alpha)**2 + 2 * g * h)) / g
        x = np.linspace(0, range_x, 100)
        y = x * math.tan(rad_alpha) - (g * x**2) / (2 * v**2 * math.cos(rad_alpha)**2) + h
        plt.plot(x, y, color="blue", label="Linia trajektorii")
        plt.xlabel("Długość (m)")
        plt.ylabel("Wysokość (m)")
        plt.title("Linia trajektorii")
        plt.grid(True)
        plt.legend()
        plt.show()
    

