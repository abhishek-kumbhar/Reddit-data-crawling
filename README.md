
# Reddit Community Analysis

"Reddit Tech News Community Analysis" is a Python project that scrapes and analyzes user interactions within the "technews" subreddit. It constructs a graph to visualize community dynamics, providing insights into user engagement and interaction patterns. Ideal for understanding online community behavior and trends.

This project aims to analyze user interactions within the "technews" subreddit on Reddit. It consists of three main scripts: `Scrapper.py`, `Analyse.py`, and `Visualise.py`, each serving a specific purpose in the analysis process.

## Overview

- **Scrapper.py**: This script is responsible for scraping comments from the "technews" subreddit, constructing a graph representation of user interactions, and storing the data in CSV files. It utilizes the PRAW library to interact with Reddit's API and provides estimated execution time.

- **Analyse.py**: Once the data is collected, the `Analyse.py` script loads the edge data from the CSV files, constructs a graph using NetworkX, and analyzes various metrics such as degree distribution, clustering coefficient, betweenness centrality, PageRank, and closeness centrality.

- **Visualise.py**: The `Visualise.py` script visualizes the constructed graph using Matplotlib and NetworkX. This visualization provides a clear representation of user relationships and community dynamics.

## Requirements

- Python 3.x
- praw library
- networkx library
- pandas library
- matplotlib library


## Execution

To execute the entire analysis process, simply run `execute_script.py`. This script automates the execution of all three main scripts in the correct sequence. It checks for the existence of data files to avoid unnecessary execution of the scraping script if the data already exists.

Estimated execution time for `Scrapper.py`: roughly 10 mins

## Usage

1. Clone this repository to your local machine.
2. Ensure you have Python 3 installed.
3. Install the required libraries: `pip install praw networkx pandas matplotlib`
4. Run `execute_script.py` using the command `python3 execute_script.py`.

## Note

- Make sure to review the code in each script file and customize it as needed for your specific use case.
- Feel free to modify the execution sequence or add additional scripts as per your requirements.

