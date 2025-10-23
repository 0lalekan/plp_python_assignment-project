# CORD-19 Data Explorer Assignment

This project is an analysis of the CORD-19 research dataset, built for the Python Frameworks assignment. It provides interactive visualization and exploration capabilities for COVID-19 research papers metadata.

## Overview

The goal of this project is to load, clean, and analyze the `metadata.csv` file from the CORD-19 dataset. The final product is a Streamlit web application that allows users to interactively explore research paper metadata, visualize publication trends, and identify key research areas in COVID-19 literature.

## Files in this Repository

* `explore.py` (or `analysis.ipynb`): Contains the Python code for Part 1, 2, and 3 (data loading, cleaning, and initial visualization).
* `app.py`: The Streamlit application (Part 4).
* `cleaned_metadata.csv`: The cleaned data subset used by the Streamlit app.
* `requirements.txt`: A list of all Python libraries needed to run this project.
* `.gitignore`: (Optional, but good practice) Add `metadata.csv` to this file to prevent uploading the 9GB raw data file.
* `publications_over_time.png`, `top_journals.png`, etc: (Optional) The static plots generated in Part 3.

## Setup and Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd week8
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Data Preparation:
   - If `cleaned_metadata.csv` is not present, run:
     ```bash
     python explore.py
     ```
   - This will process the raw data and generate the cleaned dataset

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   The app will open in your default web browser

## Features

* Interactive visualization of publication trends over time
* Analysis of top journals and authors in COVID-19 research
* Text analysis of paper titles and abstracts
* Filter and search capabilities across the dataset
* Dynamic data exploration through Streamlit widgets

## Data Privacy & Usage

* This project uses the CORD-19 dataset for academic and research purposes
* The cleaned dataset (`cleaned_metadata.csv`) contains only public metadata
* Please refer to the CORD-19 dataset's terms of use for data usage guidelines

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.