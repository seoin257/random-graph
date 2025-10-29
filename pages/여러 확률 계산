import streamlit as st
import math

st.title("랜덤 그래프의 여러 확률 계산")

# 입력
n=st.number_input("정점 수 n", 3, 30, 10, 1)
p=st.slider("간선 확률 p", 0.0, 1.0, 0.3, 0.01)
edge=n*(n-1)//2

# 전체 그래프 수
st.subheader("1. 전체 그래프 수")
st.write(f"가능한 간선 수: {edge}")
st.write(f"전체 그래프 수: 2^{edge} = {2**edge:,}")

# 특정 노드에 k개 간선 생길 확률
st.subheader("2. 특정 노드에 k개 간선이 생길 확률")
k1=st.number_input("k (특정 노드에 생기는 간선 수)", 0, n-1, 2, 1)

prob1=math.comb(n-1, k1)*(p**k1)*((1-p)**(n-1-k1))
st.write(f"C({n-1}, {k1}) * p^{k1} * (1-p)^{n-1-k1}")
st.success(f"{prob1:.5f}")

# 전체 간선이 k개일 확률
st.subheader("3. 전체 간선 수가 k개일 확률")
k2=st.number_input("k (그래프 전체 간선 수)", 0, edge, 3, 1)

prob2=math.comb(edge, k2)*(p**k2)*((1-p)**(edge-k2))
st.write(f"C({edge}, {k2}) * p^{k2} * (1-p)^{edge-k2}")
st.success(f"{prob2:.5f}")

# 특정 노드 고립 확률
st.subheader("4. 특정 노드가 고립될 확률")
prob3=(1-p)**(n-1)
st.write(f"(1-p)^{n-1}")
st.success(f"{prob3:.5f}")
