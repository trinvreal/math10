#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
import altair as alt
import sklearn

st.title("Math 10 Final Project: Analysis of Macroeconomics")
st.markdown("[Trinity Villareal](https://github.com/trinvreal)")

df = pd.read_csv("/Users/trinityvillareal/Desktop/math10datasets/2019.csv", na_values = " ")
df2 = pd.read_csv("/Users/trinityvillareal/Desktop/math10datasets/final_demo.csv", na_values = " ")

def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
        
good_cols = [c for c in df.columns if can_be_numeric(c)]
df[good_cols] = df[good_cols].apply(pd.to_numeric, axis=0)


x_axis = st.selectbox("Choose an x-value.", good_cols)
y_axis = st.selectbox("Choose an y-value.", good_cols)

st.write(f'You have chosen {x_axis} for the x-value and {y_axis} for the y-value.')

k = alt.Chart(df).mark_circle().encode(
    x = 'x_axis',
    y = 'y_axis',
        #color = alt.Color('x_axis', scale = alt.Scale(scheme = 'turbo')),
       # tooltip = ['x_axis', 'y_axis']
    #).properties(
        #width = 400
)
        
st.altair_chart(k, use_container_width=True)