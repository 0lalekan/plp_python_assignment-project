import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

# --- Page Configuration ---
st.set_page_config(
    page_title="CORD-19 Data Explorer",
    layout="wide"
)

# --- Data Loading ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('cleaned_metadata.csv')
        # Drop rows where year is missing (after conversion)
        df = df.dropna(subset=['year']) 
        # Convert year to integer for the slider
        df['year'] = df['year'].astype(int) 
        return df
    except FileNotFoundError:
        st.error("Error: 'cleaned_metadata.csv' not found. Please run the data cleaning script first.")
        return None

df = load_data()

if df is not None:
    # --- Title and Description ---
    st.title("CORD-19 Research Paper Explorer 🔬")
    st.write("This app explores the CORD-19 dataset to show trends in COVID-19 research.")

    # --- Sidebar for Filters ---
    st.sidebar.header("Filters")
    
    # Get min and max year from the data for the slider
    min_year = df['year'].min()
    max_year = df['year'].max()

    # Year range slider (as requested in the assignment)
    selected_year_range = st.sidebar.slider(
        "Select year range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )

    # Filter data based on slider
    df_filtered = df[
        (df['year'] >= selected_year_range[0]) & 
        (df['year'] <= selected_year_range[1])
    ]

    st.sidebar.info(f"Displaying {df_filtered.shape[0]} of {df.shape[0]} records.")

    # --- Main Page Layout ---
    
    # Top-level metrics
    st.header("Dashboard Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Papers Selected", f"{df_filtered.shape[0]:,}")
    col2.metric("Total Journals", f"{df_filtered['journal'].nunique():,}")
    col3.metric("Total Authors", f"{df_filtered['authors'].nunique():,}") 
    st.markdown("---")

    # --- Visualizations ---
    st.header("Visualizations")
    
    # Arrange plots in two columns
    fig_col1, fig_col2 = st.columns(2)

    with fig_col1:
        # Plot 1: Publications over time
        st.subheader("Publications Over Time")
        year_counts = df_filtered['year'].value_counts().sort_index()
        
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        sns.lineplot(x=year_counts.index, y=year_counts.values, marker='o', ax=ax1)
        ax1.set_title("Publications by Year")
        ax1.set_xlabel("Year")
        ax1.set_ylabel("Number of Papers")
        st.pyplot(fig1)

        # Plot 2: Source Distribution
        st.subheader("Top 5 Paper Sources")
        source_counts = df_filtered['source_x'].value_counts().head(5)
        
        fig3, ax3 = plt.subplots()
        ax3.pie(source_counts, labels=source_counts.index, autopct='%1.1f%%', startangle=90)
        ax3.axis('equal')
        st.pyplot(fig3)

    with fig_col2:
        # Plot 3: Top Journals
        st.subheader("Top 10 Publishing Journals")
        top_journals = df_filtered['journal'].value_counts().head(10)
        
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        sns.barplot(y=top_journals.index, x=top_journals.values, orient='h', ax=ax2)
        ax2.set_title("Top 10 Journals")
        ax2.set_xlabel("Number of Papers")
        st.pyplot(fig2)

        # Plot 4: Title Word Cloud
    st.subheader("Common Words in Paper Titles")
    
    # Combine all titles into one giant string
    title_text = ' '.join(df_filtered['title'].dropna().str.lower())
    
    # Define your custom words to remove
    common_words_to_remove = ['covid-19', 'sars-cov-2', 'coronavirus', 'study', 'based', 'analysis']

    # <-- FIX 1: Start with the built-in stopwords
    stopwords_set = set(STOPWORDS) 
    # <-- FIX 2: Add your custom words to the set
    stopwords_set.update(common_words_to_remove) 
    
    if title_text:
        wordcloud = WordCloud(width=400, height=200, 
                              stopwords=stopwords_set, # <-- FIX 3: Use the new set
                              background_color='white').generate(title_text)
        fig4, ax4 = plt.subplots()
        ax4.imshow(wordcloud, interpolation='bilinear')
        ax4.axis('off')
        st.pyplot(fig4)
    else:
        st.write("No titles to display for this year range.")

    # --- Show Sample Data ---
    st.markdown("---")
    st.header("Data Sample")
    st.write("A sample of the filtered data.")
    st.dataframe(df_filtered[['title', 'authors', 'journal', 'year', 'abstract_word_count']].head(10))