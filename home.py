import streamlit as st
from pyvis.network import Network
import networkx as nx
import streamlit.components.v1 as comp

st.set_page_config(page_title="랜덤 그래프 생성")

# 제목
st.title("랜덤 그래프 시각화 (Erdős–Rényi)")

# 입력값
n=st.number_input("노드 수 n", 2, 100, 10, 1)
p = st.slider("간선 확률 p", 0.0, 1.0, 0.2, 0.01)

# 그래프 생성
G=nx.erdos_renyi_graph(n=n, p=p, seed=42)
net=Network(height="600px", width="100%", notebook=False)
net.from_nx(G)
net.repulsion(node_distance=120, central_gravity=0.3)

# HTML 저장 및 불러오기
net.save_graph("graph.html")
with open("graph.html", "r", encoding="utf-8") as f:
    html = f.read()
comp.html(html, height=650, scrolling=True)

# 정보 출력
st.subheader("그래프 정보")
st.write(f"노드 수: {G.number_of_nodes()} | 간선 수: {G.number_of_edges()}")

if nx.is_connected(G):
    st.success("연결된 그래프")
else:
    st.warning("연결되지 않은 그래프")

deg=sum(dict(G.degree()).values())
st.write(f"평균 차수: {deg/n:.2f}")