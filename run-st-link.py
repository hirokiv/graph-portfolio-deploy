import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
import json
from packages.kg.filter import filter_unrelated_nodes, filter_connected_component

st.set_page_config(layout="wide")

# Load elements from graph_data.json
graph_data_file = "data/graph_data.json"
with open(graph_data_file, "r", encoding="utf-8") as f:
    elements = json.load(f)
elements = filter_connected_component(elements, 1)

# Load styles from styles.json
styles_file = "data/styles.json"
with open(styles_file, "r", encoding="utf-8") as f:
    styles = json.load(f)

# Load node styles dynamically
node_styles = [
    NodeStyle(style["type"], style["color"], style["attribute"], style["icon"])
    for style in styles["node_styles"]
]

# Load edge styles dynamically
edge_styles = [
    EdgeStyle(style["type"], caption=style["caption"], directed=style["directed"])
    for style in styles["edge_styles"]
]


# Render the component
st.markdown("### Graph Portfolio")
st_link_analysis(elements, "cose", node_styles, edge_styles)

