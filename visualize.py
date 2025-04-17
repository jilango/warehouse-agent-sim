import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
import numpy as np

def animate_agents(history, warehouse, skus):
    rows, cols = warehouse.shape
    fig, ax = plt.subplots(figsize=(cols / 2, rows / 2))

    def draw_grid():
        ax.clear()
        ax.set_xticks(np.arange(-0.5, cols, 1))
        ax.set_yticks(np.arange(-0.5, rows, 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.grid(True)
        ax.set_xlim(-0.5, cols - 0.5)
        ax.set_ylim(-0.5, rows - 0.5)
        ax.set_aspect("equal")

        for r in range(rows):
            for c in range(cols):
                if warehouse[r, c] == -1:  # Obstacle
                    ax.add_patch(plt.Rectangle((c - 0.5, r - 0.5), 1, 1, color="black"))
                elif warehouse[r, c] == 1:  # SKU
                    ax.add_patch(plt.Rectangle((c - 0.5, r - 0.5), 1, 1, color="yellow"))

    robot_patch = mpatches.Patch(color='blue', label='Robot')
    human_patch = mpatches.Patch(color='green', label='Human')
    sku_patch = mpatches.Patch(color='yellow', label='SKU')
    obstacle_patch = mpatches.Patch(color='black', label='Obstacle')

    def update(frame):
        draw_grid()
        step = history[frame]
        for agent_id, agent_type, pos in step:
            color = "blue" if agent_type == "robot" else "green"
            ax.plot(pos[1], pos[0], "o", color=color, markersize=12)
        ax.set_title(f"Step {frame + 1}/{len(history)}")
        ax.legend(handles=[robot_patch, human_patch, sku_patch, obstacle_patch], loc='upper right')

    ani = animation.FuncAnimation(fig, update, frames=len(history), interval=300, repeat=False)
    return fig 