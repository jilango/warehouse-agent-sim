from simulation import run_simulation
from visualize import animate_agents
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Running default simulation...")

    history, warehouse, skus = run_simulation()

    fig = animate_agents(history, warehouse, skus)
    plt.show()
