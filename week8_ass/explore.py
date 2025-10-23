import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the path to your file
file_path = 'metadata.csv'

# Load only the first 10,000 rows to save memory
try:
    df = pd.read_csv(file_path, nrows=10000)
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()


# 1. Examine the first few rows and data structure
print("--- First 5 Rows ---")
print(df.head())

# 2. Basic data exploration
print("\n--- DataFrame Dimensions (Rows, Columns) ---")
print(df.shape)

print("\n--- Data Types of Each Column ---")
print(df.info())

# 3. Check for missing values in important columns
print("\n--- Missing Values Count ---")

important_columns = ['title', 'abstract', 'publish_time', 'authors', 'journal', 'source_x']
print(df[important_columns].isnull().sum())

# 4. Generate basic statistics for numerical columns
print("\n--- Basic Statistics (Numerical Columns) ---")
print(df.describe())


# --- Part 2: Data Cleaning and Preparation ---

# Create a copy to avoid modifying the original dataframe
df_clean = df.copy()

# 1. Handle missing data
df_clean = df_clean.dropna(subset=['title', 'abstract', 'publish_time', 'journal'])

# 2. Convert date columns to datetime format
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean = df_clean.dropna(subset=['publish_time']) # Drop rows with bad dates

# 3. Extract year for time-based analysis
df_clean['year'] = df_clean['publish_time'].dt.year

# 4. Create new columns for analysis
df_clean['abstract_word_count'] = df_clean['abstract'].apply(lambda x: len(str(x).split()))

# Check the results
print("\n--- Cleaned Data Info ---")
print(df_clean.info())

print("\n--- Missing Values After Cleaning ---")
print(df_clean[important_columns].isnull().sum())

print("\n--- Example of New 'year' Column ---")
print(df_clean[['publish_time', 'year']].head())

# 5. Save the cleaned dataset for our app
df_clean.to_csv('cleaned_metadata.csv', index=False)
print("\nCleaned data saved to 'cleaned_metadata.csv'")


# --- Part 3: Data Analysis and Visualization ---

# Set a consistent style for plots
sns.set_style("whitegrid")

# 1. Plot: Number of publications over time
year_counts = df_clean['year'].value_counts().sort_index()

# Filter out potential bad data (e.g., very old years)
year_counts = year_counts[year_counts.index > 2000] 

plt.figure(figsize=(10, 6))
year_counts.plot(kind='line', marker='o')
plt.title('Number of Publications Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.grid(True)
plt.savefig('publications_over_time.png')
print("Saved publications_over_time.png")


# 2. Bar chart: Top 10 publishing journals
top_journals = df_clean['journal'].value_counts().head(10)

plt.figure(figsize=(10, 7))
top_journals.plot(kind='barh')
plt.title('Top 10 Publishing Journals')
plt.xlabel('Number of Papers')
plt.ylabel('Journal')
plt.gca().invert_yaxis() 
plt.savefig('top_journals.png')
print("Saved top_journals.png")


# 3. Word cloud: Most frequent words in titles
from wordcloud import WordCloud, STOPWORDS

title_text = ' '.join(df_clean['title'].dropna().str.lower())
common_words_to_remove = ['covid-19', 'sars-cov-2', 'coronavirus', 'study', 'based', 'analysis']
stopwords_set = set(STOPWORDS)
stopwords_set.update(common_words_to_remove)

wordcloud = WordCloud(width=800,
                      height=400,
                      stopwords=stopwords_set,
                      background_color='white').generate(title_text)

plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Frequent Words in Paper Titles')
plt.savefig('title_wordcloud.png')
print("Saved title_wordcloud.png")


# 4. Plot: Distribution of paper counts by source
top_sources = df_clean['source_x'].value_counts().head(5)

plt.figure(figsize=(8, 8))
top_sources.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Top 5 Paper Sources')
plt.ylabel('')
plt.savefig('source_distribution.png')
print("Saved source_distribution.png")

plt.show() 