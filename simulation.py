from agents import RobotAgent, HumanAgent
from environment import generate_warehouse, place_skus, get_order_items
from pathfinding import a_star
import numpy as np

def run_simulation(rows=10, cols=10, num_robots=2, num_humans=1, num_skus=5, num_orders=3, steps=50):

    warehouse = generate_warehouse(rows, cols)
    skus = place_skus(warehouse, num_skus)
    orders = get_order_items(skus, num_orders)

    agents = []
    occupied = set()
    agent_id = 0

    def random_empty():
        while True:
            r, c = np.random.randint(0, rows), np.random.randint(0, cols)
            if warehouse[r, c] == 0 and (r, c) not in occupied:
                occupied.add((r, c))
                return (r, c)

    for _ in range(num_robots):
        pos = random_empty()
        agents.append(RobotAgent(agent_id, pos))
        agent_id += 1

    for _ in range(num_humans):
        pos = random_empty()
        agents.append(HumanAgent(agent_id, pos))
        agent_id += 1


    positions_history = []

    for _ in range(steps):
        step_positions = []

        for agent in agents:
            if not agent.is_busy and orders:
                target = orders.pop(0)
                path = a_star(agent.position, target, warehouse)
                if path:
                    agent.assign_task(target, path[1:])  # Exclude current pos

            agent.move_step()
            step_positions.append((agent.agent_id, agent.agent_type, agent.position))

        positions_history.append(step_positions)

    return positions_history, warehouse, skus
