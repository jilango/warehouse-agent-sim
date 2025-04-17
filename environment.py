import numpy as np
import random


def generate_warehouse(rows=10, cols=10, num_obstacles=10):
    warehouse = np.zeros((rows, cols), dtype=int)

    obstacle_count = 0
    while obstacle_count < num_obstacles:
        r, c = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if warehouse[r, c] == 0:
            warehouse[r, c] = -1  # Obstacle
            obstacle_count += 1
    return warehouse


def place_skus(warehouse, num_skus=5):
    """Place SKU locations randomly on the warehouse grid."""
    rows, cols = warehouse.shape
    skus = []
    placed = 0

    while placed < num_skus:
        r, c = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if warehouse[r, c] == 0:
            warehouse[r, c] = 1  # SKU marker
            skus.append((r, c))
            placed += 1
    return skus


def get_order_items(skus, num_orders=3):
    return random.sample(skus, k=min(num_orders, len(skus)))
