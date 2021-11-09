#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

st.title("Okay-Means")

num_of_it = st.slider('Select number of iterations.',100,10**4)

st.write(f"You have chosen {num_of_it} iterations.")

X, _ = make_blobs(n_samples = num_of_it, centers = 5, n_features = 2, random_state = 1)

df = pd.DataFrame(X, columns = list("ab"))

starting_points = np.array([[0,0],[-2,0],[-4,0],[0,2],[0,4]])

kmeans = KMeans(n_clusters = 5, max_iter=1, init=starting_points, n_init = 1)

kmeans.fit(X);

df["c"] = kmeans.predict(X)

chart1 = alt.Chart(df).mark_circle().encode(
    x = "a",
    y = "b",
    color = "c:N"
)

df_centers = pd.DataFrame(kmeans.cluster_centers_, columns = list("ab"))

chart_centers = alt.Chart(df_centers).mark_point().encode(
    x = "a",
    y = "b",
    color = alt.value("black"),
    shape = alt.value("diamond"),
)

k = chart1 + chart_centers

st.altair_chart(k, use_container_width=True)

st.write(st.__version__)
st.write(np.__version__)
