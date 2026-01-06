import numpy as np
import matplotlib.pyplot as plt

# Parameters
dt = 0.01
alpha = 1.5

r = np.array([1.0, 0.2])
v = np.array([0.0, 1.0])

def force(r):
    x, y = r
    return np.array([
        -x + alpha * np.sin(y),
        -y + alpha * np.sin(x)
    ])

# Plot setup
plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.set_title("Particle in a Nonlinear Force Field")
ax.set_xlabel("X position")
ax.set_ylabel("Y position")

particle, = ax.plot([], [], 'ro', markersize=8)
trail_line, = ax.plot([], [], 'b-', alpha=0.25)
trail_x, trail_y = [], []

# Time evolution
for _ in range(5000):
    a = force(r)
    v += a * dt
    r += v * dt

    trail_x.append(r[0])
    trail_y.append(r[1])

    particle.set_data([r[0]], [r[1]])  # <-- FIX
    trail_line.set_data(trail_x, trail_y)

    plt.pause(0.001)


plt.ioff()
plt.show()
