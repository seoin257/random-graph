import random
import numpy as np
import itertools
import matplotlib.pyplot as plt
import streamlit as st

# 통계적 확률
def check(lis):
    n=len(lis)
    visit=[False]*n
    def dfs(u):
        visit[u]=True
        for v in range(n):
            if lis[u][v] and not visit[v]:
                dfs(v)
    dfs(0)
    return all(visit)

def make(n, p):
    edge=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if random.random()<p:
                edge[i][j]=1
                edge[j][i]=1
    return edge

# 고립노드로 근사
def isolate(n, p):
    iso=(1-p)**(n-1)
    return (1-iso)**n

# 모든 연결 그래프 확률계산
def allgraph(n, p):
    edge=[(i,j) for i in range(n) for j in range(i+1,n)]
    total=0.0
    for pat in itertools.product([0,1], repeat=len(edge)):
        a=[[0]*n for _ in range(n)]
        for k,val in enumerate(pat):
            if val==1:
                i,j=edge[k]
                a[i][j]=a[j][i]=1
        if check(a):
            count=sum(pat)
            total += (p**count) * ((1-p)**(len(edge)-count))
    return total

# 화면
st.title("랜덤그래프 연결확률 계산")
n=st.number_input("노드 수 n", 1, 1000, 5, 1)
col1, col2, col3, col4=st.columns(4)
result=st.empty()

# 설정
ps=[i/20 for i in range(21)]

# 통계적확률
if col1.button("통계적 확률"):
    if n>100:
        result.write("100이하의 n만 가능합니다...")
    else:
        connect=[]
        for p in ps:
            count=0
            for _ in range(1000):
                G=make(n, p)
                if check(G):
                    count+=1
            connect.append(count/1000)
        fig, ax=plt.subplots()
        ax.plot(ps, connect, marker='o')
        ax.set_xlabel("p")
        ax.set_ylabel("connected prob")
        ax.set_title(f"Monte Carlo (n={n})")
        ax.grid(True)
        result.pyplot(fig)

# 고립노드로 근사
if col2.button("고립노드 근사"):
    prob=[isolate(n, p) for p in ps]
    fig, ax=plt.subplots()
    ax.plot(ps, prob, marker='o', color='orange')
    ax.set_xlabel("p")
    ax.set_ylabel("connected prob")
    ax.set_title(f"isolated node (n={n})")
    ax.grid(True)
    result.pyplot(fig)

# 정확계산
if col3.button("정확한 계산"):
    if n>=7:
        result.write("6이하의 n만 가능합니다...")
    else:
        exact=[allgraph(n, p) for p in ps]
        fig, ax=plt.subplots()
        ax.plot(ps, exact, marker='o', color='green')
        ax.set_xlabel("p")
        ax.set_ylabel("connected prob")
        ax.set_title(f"Exact (n={n})")
        ax.grid(True)
        result.pyplot(fig)

# 전체비교
if col4.button("전체 비교"):
    if n>=7:
        result.write("6이하의 n만 가능합니다...")
    else:
        connect=[]
        for p in ps:
            count=0
            for _ in range(1000):
                G=make(n, p)
                if check(G):
                    count+=1
            connect.append(count/1000)
        prob=[isolate(n, p) for p in ps]
        exact=[allgraph(n, p) for p in ps]
        fig, ax=plt.subplots()
        ax.plot(ps, connect, marker='o', label="Monte Carlo")
        ax.plot(ps, prob, marker='x', linestyle='--', color='orange', label="isolated node")
        ax.plot(ps, exact, marker='s', linestyle=':', color='green', label="Exact")
        ax.set_xlabel("p")
        ax.set_ylabel("connected prob")
        ax.set_title(f"Compare (n={n})")
        ax.grid(True)
        ax.legend()
        result.pyplot(fig)
