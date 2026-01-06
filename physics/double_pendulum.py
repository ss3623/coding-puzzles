import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----- Constants -----
g = 9.81
L1, L2 = 1.0, 1.0
m1, m2 = 1.0, 1.0
dt = 0.02

# Initial conditions
theta1, theta2 = np.pi / 2, np.pi / 2
omega1, omega2 = 0.0, 0.0

# ----- Figure -----
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_title("Double Pendulum (Chaos)")

line, = ax.plot([], [], 'o-', lw=2)

# ----- Equations of motion -----
def derivatives():
    global theta1, theta2, omega1, omega2

    delta = theta2 - theta1

    denom1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
    denom2 = (L2 / L1) * denom1

    a1 = (
        m2 * L1 * omega1**2 * np.sin(delta) * np.cos(delta) +
        m2 * g * np.sin(theta2) * np.cos(delta) +
        m2 * L2 * omega2**2 * np.sin(delta) -
        (m1 + m2) * g * np.sin(theta1)
    ) / denom1

    a2 = (
        -m2 * L2 * omega2**2 * np.sin(delta) * np.cos(delta) +
        (m1 + m2) * g * np.sin(theta1) * np.cos(delta) -
        (m1 + m2) * L1 * omega1**2 * np.sin(delta) -
        (m1 + m2) * g * np.sin(theta2)
    ) / denom2

    return a1, a2

# ----- Update -----
def update(frame):
    global theta1, theta2, omega1, omega2

    a1, a2 = derivatives()

    omega1 += a1 * dt
    omega2 += a2 * dt
    theta1 += omega1 * dt
    theta2 += omega2 * dt

    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)

    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    line.set_data([0, x1, x2], [0, y1, y2])
    return line,

ani = FuncAnimation(fig, update, interval=20)
plt.show()
