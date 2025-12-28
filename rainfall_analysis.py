import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("rainfall_data.csv")

print("Dataset loaded successfully")
print("Shape:", df.shape)
print(df.head())

# -----------------------------
# 2. Convert time to datetime
# -----------------------------
df['time'] = pd.to_datetime(df['time'])
df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month

# -----------------------------
# 3. Remove missing values
# -----------------------------
df = df.dropna(subset=['rain_sum'])

# -----------------------------
# 4. Basic Statistics
# -----------------------------
print("\nRainfall Statistics:")
print(df['rain_sum'].describe())

# -----------------------------
# 5. Yearly Rainfall Trend
# -----------------------------
yearly_rainfall = df.groupby('year')['rain_sum'].mean()

plt.figure(figsize=(10,5))
plt.plot(yearly_rainfall.index, yearly_rainfall.values)
plt.title("Average Yearly Rainfall in Sri Lanka")
plt.xlabel("Year")
plt.ylabel("Average Rainfall (mm)")
plt.grid(True)
plt.show()

# -----------------------------
# 6. Monthly Rainfall Pattern
# -----------------------------
monthly_rainfall = df.groupby('month')['rain_sum'].mean()

plt.figure(figsize=(10,5))
plt.bar(monthly_rainfall.index, monthly_rainfall.values)
plt.title("Average Monthly Rainfall Pattern")
plt.xlabel("Month")
plt.ylabel("Average Rainfall (mm)")
plt.show()

# -----------------------------
# 7. City-wise Rainfall (Top 10)
# -----------------------------
city_rainfall = df.groupby('city')['rain_sum'] \
                  .mean() \
                  .sort_values(ascending=False) \
                  .head(10)

plt.figure(figsize=(10,5))
city_rainfall.plot(kind='bar')
plt.title("Top 10 Cities by Average Rainfall")
plt.ylabel("Average Rainfall (mm)")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 8. Rainfall Distribution
# -----------------------------
plt.figure(figsize=(6,4))
plt.boxplot(df['rain_sum'])
plt.title("Rainfall Distribution")
plt.ylabel("Rainfall (mm)")
plt.show()
