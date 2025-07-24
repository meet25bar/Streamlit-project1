import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Iris Dataset Explorer")

# Sidebar for user input options
st.sidebar.header("Filter Options")

# Load Iris dataset from a public repository
url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/iris.csv"
df = pd.read_csv(url)

# Rename columns for convenience
df.columns = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"]

# Sidebar multi-select for species filter
species_options = df["Species"].unique().tolist()
selected_species = st.sidebar.multiselect("Select Species", options=species_options, default=species_options)

# Sidebar selectors for X and Y axis (numeric columns)
numeric_columns = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]
x_axis = st.sidebar.selectbox("X-axis", options=numeric_columns, index=0)
y_axis = st.sidebar.selectbox("Y-axis", options=numeric_columns, index=1)

# Filter the dataframe based on selected species
filtered_df = df[df["Species"].isin(selected_species)]

# Scatter plot of the selected axes
st.subheader(f"Scatter Plot: {x_axis} vs {y_axis}")
fig, ax = plt.subplots()
for species in selected_species:
    data = filtered_df[filtered_df["Species"] == species]
    ax.scatter(data[x_axis], data[y_axis], label=species)
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.legend()
st.pyplot(fig)

# Bar chart of average measurements by species (for chosen axes)
st.subheader("Average Measurements by Species")
avg_df = filtered_df.groupby("Species")[[x_axis, y_axis]].mean().reset_index()
avg_df = avg_df.set_index("Species")
st.bar_chart(avg_df)
