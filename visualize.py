import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
import numpy as np

def animate_agents(history, warehouse, skus, save_path="animation.gif"):
    rows, cols = warehouse.shape
    fig, ax = plt.subplots(figsize=(cols * 0.5, rows * 0.5), dpi=100)

    COLORS = {
        "background": "#F9FAFB",
        "grid": "#E5E7EB",
        "obstacle": "#1F2937",
        "sku": "#FBBF24",
        "robot": "#3B82F6",
        "human": "#10B981",
        "text": "#111827"
    }

    def draw_grid():
        ax.clear()
        ax.set_facecolor(COLORS["background"])
        ax.set_xticks(np.arange(-0.5, cols, 1))
        ax.set_yticks(np.arange(-0.5, rows, 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.grid(color=COLORS["grid"], linestyle='-', linewidth=1)
        ax.set_xlim(-0.5, cols - 0.5)
        ax.set_ylim(-0.5, rows - 0.5)
        ax.set_aspect("equal")

        for r in range(rows):
            for c in range(cols):
                if warehouse[r, c] == -1:
                    ax.add_patch(plt.Rectangle((c - 0.5, r - 0.5), 1, 1, color=COLORS["obstacle"]))
                elif warehouse[r, c] == 1:
                    ax.add_patch(plt.Rectangle((c - 0.5, r - 0.5), 1, 1, color=COLORS["sku"]))

    def update(frame):
        draw_grid()
        step = history[frame]
        for agent_id, agent_type, pos in step:
            color = COLORS["robot"] if agent_type == "robot" else COLORS["human"]
            circle = plt.Circle((pos[1], pos[0]), 0.3, color=color, zorder=2)
            ax.add_patch(circle)
            ax.text(pos[1], pos[0], str(agent_id), color='white', ha='center', va='center', fontsize=8, weight='bold', zorder=3)
        ax.set_title(f"Step {frame + 1}/{len(history)}", fontsize=12, color=COLORS["text"], weight='bold')

    ani = animation.FuncAnimation(fig, update, frames=len(history), interval=500, repeat=False)
    ani.save(save_path, writer='pillow')  # Save as GIF
    plt.close(fig)
    return save_path

