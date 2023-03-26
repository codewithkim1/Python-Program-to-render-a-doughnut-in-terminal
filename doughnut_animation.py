import math
import time

def render_doughnut(doughnut_radius, hole_radius, theta_increment, phi_increment):
    for theta in range(0, 360, theta_increment):
        for phi in range(0, 360, phi_increment):
            theta_r = math.radians(theta)
            phi_r = math.radians(phi)
            x = (doughnut_radius + hole_radius*math.cos(theta_r))*math.cos(phi_r)
            y = (doughnut_radius + hole_radius*math.cos(theta_r))*math.sin(phi_r)
            z = hole_radius*math.sin(theta_r)
            print(f"\033[{int(25+z)};{int(50+x)}H\033[31mO", end="") # 3D rendering of doughnut using ASCII art
        print()
    time.sleep(0.1) # Animation delay

# Define the parameters of the doughnut
R = 15
r = 7

# Render the doughnut
while True:
    render_doughnut(R, r, 5, 15)
