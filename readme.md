# Sentiment Analysis of Restaurant Reviews

This is a Streamlit application for performing sentiment analysis on restaurant reviews using a pre-trained machine learning model. The application allows users to input a review and receive a sentiment prediction (Positive or Negative).
The code of the model is present in the .ipynb file.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Features

- User-friendly web interface to input restaurant reviews.
- Sentiment prediction based on pre-trained machine learning model.
- Text preprocessing including stemming and stopword removal.

## Technologies Used

- [Streamlit](https://streamlit.io/) - For creating the web application interface.
- [NLTK](https://www.nltk.org/) - For natural language processing tasks(stemming, vectorization).
- [Scikit-learn](https://scikit-learn.org/) - For machine learning model handling.
- [Pickle](https://docs.python.org/3/library/pickle.html) - For loading the pre-trained model and vectorizer.

## Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
