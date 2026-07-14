<<<<<<< HEAD
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Ford GoBike EDA", layout="wide")

st.title("🚲 Ford GoBike 2018 EDA Dashboard")
st.write("Exploratory Data Analysis for Ford Bike Sharing Data")

# 1. LOAD DATA
@st.cache_data
def load_data():
    file_path = "FordGoBike_2018_All_Merged.csv"
    df = pd.read_csv(file_path)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    df['trip_duration_min'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60
    df['hour'] = df['start_time'].dt.hour
    df['day'] = df['start_time'].dt.day_name()
    df['month'] = df['start_time'].dt.month_name()
    df['date'] = df['start_time'].dt.date
    df = df[(df['trip_duration_min'] > 1) & (df['trip_duration_min'] < 180)]
    return df

try:
    df = load_data()
    st.success(f"Data loaded successfully! Shape: {df.shape}")
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()

# 2. BASIC INFO
st.header("1. Dataset Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Rows", df.shape[0])
col2.metric("Total Columns", df.shape[1])
col3.metric("Avg Trip Duration", f"{df['trip_duration_min'].mean():.1f} min")

st.dataframe(df.head())

# 3. UNIVARIATE
st.header("2. Trip Duration Distribution")
fig, ax = plt.subplots(figsize=(5, 3)) # SMALLER
sns.histplot(df['trip_duration_min'], bins=50, kde=True, ax=ax, color='teal')
ax.set_xlabel("Trip Duration (min)")
ax.set_title("Trip Duration Dist", fontsize=10)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

st.header("3. Rides by Hour")
fig, ax = plt.subplots(figsize=(6, 3)) # SMALLER
sns.countplot(x='hour', data=df, palette='coolwarm', ax=ax)
ax.set_title("Rides by Hour", fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

st.header("4. User Type Distribution")
fig, ax = plt.subplots(figsize=(4, 3)) # SMALLER
sns.countplot(x='user_type', data=df, palette='viridis', ax=ax)
ax.set_title("User Type", fontsize=10)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

# 4. BIVARIATE
st.header("5. Trip Duration by User Type")
fig, ax = plt.subplots(figsize=(4, 3)) # SMALLER
sns.boxplot(x='user_type', y='trip_duration_min', data=df, ax=ax)
ax.set_title("Duration by User Type", fontsize=10)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

st.header("6. Top 10 Start Stations")
top_start = df['start_station_name'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(5, 3.5)) # SMALLER
top_start.plot(kind='barh', ax=ax, color='skyblue')
ax.invert_yaxis()
ax.set_title("Top 10 Stations", fontsize=10)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

st.header("7. Heatmap: Day vs Hour")
pivot = df.pivot_table(index='day', columns='hour', values='trip_duration_min', aggfunc='count')
fig, ax = plt.subplots(figsize=(8, 3)) # SMALLER - was 12,4
sns.heatmap(pivot, cmap='YlGnBu', ax=ax, cbar_kws={'shrink': 0.6})
ax.set_title("Day vs Hour Heatmap", fontsize=10)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)


#  5. WEATHER ANALYSIS 
st.header("8. Trip Duration by Month 📅")

# 1. Group by month and calculate avg duration
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

df['month'] = df['start_time'].dt.month_name()
df_month = df.groupby('month')['trip_duration_min'].mean().reset_index()
df_month['month'] = pd.Categorical(df_month['month'], categories=month_order, ordered=True)
df_month = df_month.sort_values('month')

# 2. BAR CHART - Avg Trip Duration by Month
fig, ax = plt.subplots(figsize=(8, 3.5))
sns.barplot(data=df_month, x='month', y='trip_duration_min', ax=ax, palette='viridis')
ax.set_xlabel("Month")
ax.set_ylabel("Avg Trip Duration (min)")
ax.set_title("Average Trip Duration per Month")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

# 3. LINE CHART - Trend over months
st.subheader("Trip Duration Trend")
fig, ax = plt.subplots(figsize=(8, 3))
sns.lineplot(data=df_month, x='month', y='trip_duration_min', marker='o', ax=ax, color='teal')
ax.set_xlabel("Month")
ax.set_ylabel("Avg Trip Duration (min)")
ax.set_title("Do rides get longer in summer?")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

# 4. Show the numbers in a table
st.dataframe(df_month.rename(columns={'trip_duration_min': 'Avg Duration (min)'}).round(2))
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Ford GoBike EDA", layout="wide")

st.title("🚲 Ford GoBike 2018 EDA Dashboard")
st.write("Exploratory Data Analysis for Ford Bike Sharing Data")

# 1. LOAD DATA
@st.cache_data
def load_data():
    file_path = "FordGoBike_2018_All_Merged.csv"
    df = pd.read_csv(file_path)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    df['trip_duration_min'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60
    df['hour'] = df['start_time'].dt.hour
    df['day'] = df['start_time'].dt.day_name()
    df['month'] = df['start_time'].dt.month_name()
    df['date'] = df['start_time'].dt.date
    df = df[(df['trip_duration_min'] > 1) & (df['trip_duration_min'] < 180)]
    return df

try:
    df = load_data()
    st.success(f"Data loaded successfully! Shape: {df.shape}")
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()

# 2. BASIC INFO
st.header("1. Dataset Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Rows", df.shape[0])
col2.metric("Total Columns", df.shape[1])
col3.metric("Avg Trip Duration", f"{df['trip_duration_min'].mean():.1f} min")

st.dataframe(df.head())

# 3. UNIVARIATE
st.header("2. Trip Duration Distribution")
fig, ax = plt.subplots(figsize=(5, 3)) # SMALLER
sns.histplot(df['trip_duration_min'], bins=50, kde=True, ax=ax, color='teal')
ax.set_xlabel("Trip Duration (min)")
ax.set_title("Trip Duration Dist", fontsize=10)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

st.header("3. Rides by Hour")
fig, ax = plt.subplots(figsize=(6, 3)) # SMALLER
sns.countplot(x='hour', data=df, palette='coolwarm', ax=ax)
ax.set_title("Rides by Hour", fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

st.header("4. User Type Distribution")
fig, ax = plt.subplots(figsize=(4, 3)) # SMALLER
sns.countplot(x='user_type', data=df, palette='viridis', ax=ax)
ax.set_title("User Type", fontsize=10)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

# 4. BIVARIATE
st.header("5. Trip Duration by User Type")
fig, ax = plt.subplots(figsize=(4, 3)) # SMALLER
sns.boxplot(x='user_type', y='trip_duration_min', data=df, ax=ax)
ax.set_title("Duration by User Type", fontsize=10)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

st.header("6. Top 10 Start Stations")
top_start = df['start_station_name'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(5, 3.5)) # SMALLER
top_start.plot(kind='barh', ax=ax, color='skyblue')
ax.invert_yaxis()
ax.set_title("Top 10 Stations", fontsize=10)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

st.header("7. Heatmap: Day vs Hour")
pivot = df.pivot_table(index='day', columns='hour', values='trip_duration_min', aggfunc='count')
fig, ax = plt.subplots(figsize=(8, 3)) # SMALLER - was 12,4
sns.heatmap(pivot, cmap='YlGnBu', ax=ax, cbar_kws={'shrink': 0.6})
ax.set_title("Day vs Hour Heatmap", fontsize=10)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)


#  5. WEATHER ANALYSIS 
st.header("8. Trip Duration by Month 📅")

# 1. Group by month and calculate avg duration
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

df['month'] = df['start_time'].dt.month_name()
df_month = df.groupby('month')['trip_duration_min'].mean().reset_index()
df_month['month'] = pd.Categorical(df_month['month'], categories=month_order, ordered=True)
df_month = df_month.sort_values('month')

# 2. BAR CHART - Avg Trip Duration by Month
fig, ax = plt.subplots(figsize=(8, 3.5))
sns.barplot(data=df_month, x='month', y='trip_duration_min', ax=ax, palette='viridis')
ax.set_xlabel("Month")
ax.set_ylabel("Avg Trip Duration (min)")
ax.set_title("Average Trip Duration per Month")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

# 3. LINE CHART - Trend over months
st.subheader("Trip Duration Trend")
fig, ax = plt.subplots(figsize=(8, 3))
sns.lineplot(data=df_month, x='month', y='trip_duration_min', marker='o', ax=ax, color='teal')
ax.set_xlabel("Month")
ax.set_ylabel("Avg Trip Duration (min)")
ax.set_title("Do rides get longer in summer?")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig, use_container_width=False)

# 4. Show the numbers in a table
st.dataframe(df_month.rename(columns={'trip_duration_min': 'Avg Duration (min)'}).round(2))

