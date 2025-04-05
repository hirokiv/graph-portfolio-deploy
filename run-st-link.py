import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
import json
from packages.kg.filter import filter_unrelated_nodes, filter_connected_component

st.set_page_config(layout="wide")
# Add custom CSS to disable text selection
st.markdown(
    """
    <style>
    * {
        -webkit-user-select: none; /* Disable text selection in Safari/Chrome */
        -moz-user-select: none;    /* Disable text selection in Firefox */
        -ms-user-select: none;     /* Disable text selection in IE/Edge */
        user-select: none;         /* Disable text selection in modern browsers */
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Load elements from graph_data.json
# graph_data_file = "data/graph_data.json"
# with open(graph_data_file, "r", encoding="utf-8") as f:
#     elements = json.load(f)

# Read TOML back as elements
secrets = st.secrets
elements = filter_connected_component(secrets, 1)

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

# Extract unique labels from edges
unique_labels = set(edge["data"]["label"] for edge in elements["edges"])


# Render the component
st.markdown("### Graph Portfolio")
st_link_analysis(elements, "cose", node_styles, edge_styles)

# Q-A samples
st.markdown("### Graph Portfolio")
# Load query results from TOML
query_results = st.secrets["queries"]

# Replace the first layer of tabs with a dropdown
selected_question = st.selectbox(
    "Select a Question:",
    [result["query"] for result in query_results]
)
def remove_references_section(text):
    """
    Remove the "References" section from the given text.
    """
    if "### References" in text:
        return text.split("### References")[0].strip()
    return text

# Find the selected question's data
selected_result = next(result for result in query_results if result["query"] == selected_question)

# Display the selected question
st.markdown(f"### Question: {selected_result['query']}")

# Second layer of tabs: Global vs Hybrid
mode_tabs = st.tabs(["Global Mode", "Hybrid Mode"])
with mode_tabs[0]:
    st.markdown("#### Global Mode")
    st.markdown(remove_references_section(selected_result["results"]["global"]))
with mode_tabs[1]:
    st.markdown("#### Hybrid Mode")
    st.markdown(remove_references_section(selected_result["results"]["hybrid"]))