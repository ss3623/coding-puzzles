import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# ----- Physics -----
g = 9.8          # gravity
dt = 0.02
y = 8.0          # starting height
v = 0.0
radius = 0.3

# ----- Figure -----
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(0, 9)
ax.set_aspect('equal')
ax.set_title("Falling Ball with Gravity")

# Ground
ax.plot([-2, 2], [0, 0], color="brown", linewidth=3)

# Ball
ball = Circle((0, y), radius, color='dodgerblue')
ax.add_patch(ball)

# Trail
trail_x, trail_y = [], []
trail, = ax.plot([], [], 'k--', alpha=0.4)

# ----- Update function -----
def update(frame):
    global y, v

    v -= g * dt
    y += v * dt

    if y <= radius:   # hit ground
        y = radius
        v = 0

    ball.center = (0, y)

    trail_x.append(0)
    trail_y.append(y)
    trail.set_data(trail_x, trail_y)

    return ball, trail

# ----- Animate -----
ani = FuncAnimation(fig, update, frames=500, interval=20)

plt.show()
