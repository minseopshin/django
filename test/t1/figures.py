import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def my_figure(figure):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.2, 1.2)

    x, y = [], []
    line, = plt.plot([], [], 'bo')

    def update(frame):
        x.append(frame)
        y.append(np.sin(frame))
        line.set_data(x, y)
        return line,

    ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 128))
    return ani