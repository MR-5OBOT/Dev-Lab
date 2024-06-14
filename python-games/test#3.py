import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Create a circle
circle = plt.Circle((0, 0), 1, fill=False)
ax.add_artist(circle)

# Animation function
def update(frame):
    circle.set_radius(5 * np.abs(np.sin(frame / 10)))
    return circle,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

# Save the animation as an MP4 file
ani.save('expanding_contracting_circle.mp4', writer='ffmpeg', fps=30)

print("Animation saved as 'expanding_contracting_circle.mp4'")
