import streamlit as st
from simulation import run_simulation
from visualize import animate_agents
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")
st.title("Multi-Agent Warehouse Simulator")


st.sidebar.header("Simulation Settings")
rows = st.sidebar.slider("Warehouse Rows", 5, 20, 10)
cols = st.sidebar.slider("Warehouse Columns", 5, 20, 10)
num_robots = st.sidebar.slider("Number of Robots", 1, 5, 2)
num_humans = st.sidebar.slider("Number of Humans", 0, 5, 1)
num_skus = st.sidebar.slider("Number of SKUs", 1, 10, 5)
num_orders = st.sidebar.slider("Number of Orders", 1, 10, 3)
steps = st.sidebar.slider("Simulation Steps", 10, 100, 50)

if st.button("Run Simulation"):
    with st.spinner("Running simulation..."):
        history, warehouse, skus = run_simulation(
            rows=rows,
            cols=cols,
            num_robots=num_robots,
            num_humans=num_humans,
            num_skus=num_skus,
            num_orders=num_orders,
            steps=steps,
        )

    st.success("Simulation complete! Rendering animation...")

    gif_path = animate_agents(history, warehouse, skus)
    st.image(gif_path)

