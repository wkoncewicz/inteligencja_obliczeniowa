import math
import matplotlib.pyplot as plt
import numpy as np
from random import randint

def calculate_trajectory(angle_deg, velocity, height, gravity=9.8):
    """Calculates the trajectory of the projectile."""
    angle_rad = math.radians(angle_deg)
    
    # Compute total horizontal range
    time_of_flight = (velocity * math.sin(angle_rad) + math.sqrt((velocity**2 * math.sin(angle_rad)**2) + 2 * gravity * height)) / gravity
    range_x = velocity * math.cos(angle_rad) * time_of_flight
    
    # Generate trajectory points
    x = np.linspace(0, range_x, 100)
    y = x * math.tan(angle_rad) - (gravity * x**2) / (2 * velocity**2 * math.cos(angle_rad)**2) + height
    
    return x, y, range_x

def plot_trajectory(x, y):
    """Plots the projectile's trajectory."""
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color="blue", label="Trajectory")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.title("Projectile Motion")
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    """Main function to run the projectile simulation."""
    target_distance = randint(50, 340)
    print(f"Target distance: {target_distance} meters")
    
    velocity = 50  # Initial velocity (m/s)
    height = 100   # Initial height (m)
    
    while True:
        try:
            angle = float(input("Enter the launch angle (degrees): "))
            x, y, impact_distance = calculate_trajectory(angle, velocity, height)
            
            if target_distance - 10 <= impact_distance <= target_distance + 10:
                print("Target hit!")
                break
            else:
                print("Missed the target. Try again!")
                plot_trajectory(x, y)
        except ValueError:
            print("Please enter a valid number for the angle.")

if __name__ == "__main__":
    main()