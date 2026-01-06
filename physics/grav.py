import numpy as np
import matplotlib.pyplot as plt

# ----- Parameters -----
dt = 0.01
k = 5.0

# Particle 1
r1 = np.array([-1.0, 0.0])
v1 = np.array([0.0, 1.0])

# Particle 2
r2 = np.array([1.0, 0.0])
v2 = np.array([0.0, -1.0])

def force(rA, rB):
    """Force on A due to B"""
    diff = rA - rB
    dist = np.linalg.norm(diff)
    return -k * diff / dist**3

# ----- Plot setup -----
plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Two Particles Attracting Each Other")

p1_plot, = ax.plot([], [], 'ro', markersize=8)
p2_plot, = ax.plot([], [], 'go', markersize=8)
trail1, = ax.plot([], [], 'r-', alpha=0.5)
trail2, = ax.plot([], [], 'g-', alpha=0.5)

trail1_x, trail1_y = [], []
trail2_x, trail2_y = [], []

# ----- Time evolution -----
for _ in range(3000):
    # Compute forces
    F1 = force(r1, r2)
    F2 = -F1  # Newton's 3rd law

    # Update velocities
    v1 += F1 * dt
    v2 += F2 * dt

    # Update positions
    r1 += v1 * dt
    r2 += v2 * dt

    # Update trails
    trail1_x.append(r1[0])
    trail1_y.append(r1[1])
    trail2_x.append(r2[0])
    trail2_y.append(r2[1])

    # Update plots
    p1_plot.set_data([r1[0]], [r1[1]])
    p2_plot.set_data([r2[0]], [r2[1]])
    trail1.set_data(trail1_x, trail1_y)
    trail2.set_data(trail2_x, trail2_y)

    plt.pause(0.001)

plt.ioff()
plt.show()
