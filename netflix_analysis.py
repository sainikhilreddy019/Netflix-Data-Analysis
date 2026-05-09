import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# -------------------------------
# BASIC DATA EXPLORATION
# -------------------------------

print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nSHAPE AFTER REMOVING DUPLICATES")
print(df.shape)

# -------------------------------
# MOST COMMON GENRES
# -------------------------------

print("\nTOP 10 GENRES")

genre_counts = df['listed_in'].value_counts().head(10)

print(genre_counts)

plt.figure(figsize=(10,5))

genre_counts.plot(kind='bar')

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genres")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.show()

# -------------------------------
# RATINGS ANALYSIS
# -------------------------------

print("\nMOST COMMON RATINGS")

rating_counts = df['rating'].value_counts().head(10)

print(rating_counts)

plt.figure(figsize=(8,8))

rating_counts.plot(kind='pie', autopct='%1.1f%%')

plt.title("Ratings Distribution on Netflix")

plt.ylabel("")

plt.show()

# -------------------------------
# RELEASE YEAR TREND
# -------------------------------

print("\nRELEASE YEAR TREND")

release_trend = df['release_year'].value_counts().sort_index()

print(release_trend)

plt.figure(figsize=(12,6))

plt.plot(release_trend.index, release_trend.values)

plt.title("Netflix Content Releases Over Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Releases")

plt.show()