import streamlit as st
from load_graph import load_graph, dijkstra_path, draw_graph
G=load_graph("metro_graph.json")
stations=list(G.nodes())

source=st.selectbox("select start station",stations)
target=st.selectbox("select destination station",stations)
if st.button("Find Shortest Path"):
    if source==target:
        st.warning("You are already at your destination!")
    else:
        path=dijkstra_path(G,source,target)
        if path:
            st.success(f"Shortest Path: {'->'.join(path)}")
            draw_graph(G,path)