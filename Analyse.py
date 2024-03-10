import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_edges_data(file_path):
    """
    Load edge data from a CSV file.

    Args:
    - file_path: Path to the CSV file containing edge data.

    Returns:
    - DataFrame: Pandas DataFrame containing edge data.
    """
    try:
        # Read edge data from CSV file
        df_edges = pd.read_csv(file_path)
        return df_edges
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Unable to parse data from file '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None

def plot_degree_distribution(G):
    """
    Plot the degree distribution of a graph.

    Args:
    - G: NetworkX graph object.

    Returns:
    - None
    """
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    degree_count = pd.Series(degree_sequence).value_counts()
    degree_count.sort_index(inplace=True)
    plt.bar(degree_count.index, degree_count.values)
    plt.title('Degree Distribution')
    plt.xlabel('Degree')
    plt.ylabel('Count')
    plt.show()

def plot_clustering_coefficient_distribution(G):
    """
    Plot the distribution of clustering coefficients in a graph.

    Args:
    - G: NetworkX graph object.

    Returns:
    - None
    """
    clustering = nx.clustering(G)
    clustering_count = pd.Series(clustering).value_counts()
    clustering_count.sort_index(inplace=True)
    plt.bar(clustering_count.index, clustering_count.values)
    plt.title('Distribution of Clustering Coefficients')
    plt.xlabel('Clustering Coefficient')
    plt.ylabel('Count')
    plt.show()

def plot_betweenness_centrality_distribution(G):
    """
    Plot the distribution of betweenness centrality in a graph.

    Args:
    - G: NetworkX graph object.

    Returns:
    - None
    """
    betweenness = nx.betweenness_centrality(G)
    betweenness_count = pd.Series(betweenness).value_counts()
    betweenness_count.sort_index(inplace=True)
    plt.bar(betweenness_count.index, betweenness_count.values)
    plt.title('Distribution of Betweenness Centrality')
    plt.xlabel('Betweenness Centrality')
    plt.ylabel('Count')
    plt.show()

def plot_pagerank_distribution(G):
    """
    Plot the distribution of PageRank values in a graph.

    Args:
    - G: NetworkX graph object.

    Returns:
    - None
    """
    pagerank = nx.pagerank(G)
    pagerank_values = list(pagerank.values())
    plt.hist(pagerank_values, bins=20, edgecolor='black', alpha=0.7)
    plt.title('Distribution of PageRank Values')
    plt.xlabel('PageRank')
    plt.ylabel('Count')
    plt.show()

def plot_closeness_centrality_distribution(G):
    """
    Plot the distribution of closeness centrality values in a graph.

    Args:
    - G: NetworkX graph object.

    Returns:
    - None
    """
    closeness = nx.closeness_centrality(G)
    closeness_values = list(closeness.values())
    plt.hist(closeness_values, bins=20, edgecolor='black', alpha=0.7)
    plt.title('Distribution of Closeness Centrality Values')
    plt.xlabel('Closeness Centrality')
    plt.ylabel('Count')
    plt.show()

def main():
    # Change directory to the current working directory
    os.chdir(os.getcwd())

    # Load edge data from CSV file
    df_edges = load_edges_data(os.getcwd() + '/user_node_edges.csv')

    # Proceed if edge data is successfully loaded
    if df_edges is not None:
        # Create a graph from edge data
        G = nx.from_pandas_edgelist(df_edges, 'user1', 'user2')

        # Plot degree distribution
        plot_degree_distribution(G)

        # Plot clustering coefficient distribution
        plot_clustering_coefficient_distribution(G)

        # Plot betweenness centrality distribution
        plot_betweenness_centrality_distribution(G)

        # Plot PageRank distribution
        plot_pagerank_distribution(G)

        # Plot closeness centrality distribution
        plot_closeness_centrality_distribution(G)

if __name__ == "__main__":
    main()
