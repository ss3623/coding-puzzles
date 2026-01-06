import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import random

# ----- Physics -----
g = 9.8
dt = 0.02
restitution = 0.8   # bounciness (1 = perfect bounce)

x, y = 0.0, 6.0
vx, vy = 2.5, 0.0
radius = 0.3

# ----- Figure -----
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.set_title("Bouncing Ball Playground")

# Ground & walls
ax.plot([-5, 5], [0, 0], color="black")
ax.plot([-5, -5], [0, 7], color="black")
ax.plot([5, 5], [0, 7], color="black")

# Ball
ball = Circle((x, y), radius, color='dodgerblue')
ax.add_patch(ball)

# ----- Update -----
def update(frame):
    global x, y, vx, vy

    # Gravity
    vy -= g * dt

    # Move
    x += vx * dt
    y += vy * dt

    # Ground collision
    if y <= radius:
        y = radius
        vy = -vy * restitution
        ball.set_color(np.random.rand(3,))  # change color!

    # Wall collisions
    if x <= -5 + radius or x >= 5 - radius:
        vx = -vx
        ball.set_color(np.random.rand(3,))

    ball.center = (x, y)
    return ball,

ani = FuncAnimation(fig, update, frames=1000, interval=20)
plt.show()
