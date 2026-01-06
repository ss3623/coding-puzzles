import numpy as np
import matplotlib.pyplot as plt

# Parameters
dt = 0.01
k = 5.0    # strength of the central force
r = np.array([1.5, 0.0])  # initial position
v = np.array([0.0, 1.2])  # initial velocity

def force(r):
    dist = np.linalg.norm(r)
    return -k * r / (dist**3)  # central attractive force

# Plot setup
plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.set_title("Particle Orbiting Center")

particle, = ax.plot([], [], 'ro', markersize=8)
trail_line, = ax.plot([], [], 'b-', alpha=0.5)
trail_x, trail_y = [], []

# Time evolution
for _ in range(3000):
    a = force(r)
    v += a * dt
    r += v * dt

    trail_x.append(r[0])
    trail_y.append(r[1])

    particle.set_data([r[0]], [r[1]])
    trail_line.set_data(trail_x, trail_y)

    plt.pause(0.001)

plt.ioff()
plt.show()
