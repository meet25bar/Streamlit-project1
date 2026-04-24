import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Iris Dataset Explorer")

st.sidebar.header("Filter Options")


url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/iris.csv"
df = pd.read_csv(url)

df.columns = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"]

# Sidebar multi-select for species filter
species_options = df["Species"].unique().tolist()
selected_species = st.sidebar.multiselect("Select Species", options=species_options, default=species_options)

# Sidebar selectors for X and Y axis (numeric columns)
numeric_columns = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]
x_axis = st.sidebar.selectbox("X-axis", options=numeric_columns, index=0)
y_axis = st.sidebar.selectbox("Y-axis", options=numeric_columns, index=1)


filtered_df = df[df["Species"].isin(selected_species)]


st.subheader(f"Scatter Plot: {x_axis} vs {y_axis}")
fig, ax = plt.subplots()
for species in selected_species:
    data = filtered_df[filtered_df["Species"] == species]
    ax.scatter(data[x_axis], data[y_axis], label=species)
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.legend()
st.pyplot(fig)


st.subheader("Average Measurements by Species")
avg_df = filtered_df.groupby("Species")[[x_axis, y_axis]].mean().reset_index()
avg_df = avg_df.set_index("Species")
st.bar_chart(avg_df)
