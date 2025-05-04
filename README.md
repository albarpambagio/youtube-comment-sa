# YouTube Comment Sentiment Analysis (youtube-comment-sa)

This project focuses on scraping comments from YouTube videos and performing sentiment analysis on them. It combines web scraping techniques with natural language processing (NLP) to analyze the sentiments expressed in YouTube comments.

## Features

* **Comment Scraping**: Extract comments from YouTube videos using the `scraping.py` script.
* **Sentiment Analysis**: Analyze the sentiment of scraped comments using NLP techniques.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/albarpambagio/youtube-comment-sa.git
   cd youtube-comment-sa
   ```


2. **Set Up a Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```


3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```



## Project Structure

```plaintext
youtube-comment-sa/
├── notebooks/
│   └── sentiment_analysis.ipynb  # Jupyter notebook for sentiment analysis
├── scraping.py                   # Script to scrape YouTube comments
├── requirements.txt              # Python dependencies
├── pyproject.toml                # Project metadata and configuration
├── .gitignore                    # Git ignore file
└── README.md                     # Project documentation
```


## Acknowledgments

This project was developed as part of a ML development course by Dicoding




