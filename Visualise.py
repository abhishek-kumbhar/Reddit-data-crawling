import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_edge_data(file_path):
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

def visualize_graph(G):
    """
    Visualize a graph using NetworkX and matplotlib.

    Args:
    - G: NetworkX graph object.

    Returns:
    - None
    """
    try:
        # Calculate the layout of the graph
        pos = nx.spring_layout(G, k=0.15, iterations=20)
        
        # Draw nodes, edges, and labels
        nx.draw_networkx_nodes(G, pos, node_color='blue', alpha=0.7)
        nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.4)
        nx.draw_networkx_labels(G, pos, font_size=8, font_family='Arial')
        
        # Turn off axis
        plt.axis('off')
        
        # Show the graph
        plt.show()
    except Exception as e:
        print(f"Error: An unexpected error occurred while visualizing the graph: {e}")

def main():
    try:
        # Load edge data from CSV file
        df_edges = load_edge_data(os.getcwd() + '/user_node_edges.csv')

        # Proceed if edge data is successfully loaded
        if df_edges is not None:
            # Create a graph from edge data
            G = nx.Graph()
            for index, row in df_edges.iterrows():
                G.add_edge(row['user1'], row['user2'])

            # Visualize the graph
            visualize_graph(G)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
