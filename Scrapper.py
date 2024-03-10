import praw
import time
import pandas as pd
import networkx as nx

# Initialize Reddit instance
reddit = praw.Reddit(client_id='n_TmFW89AwUmkiuiHzn6Yg',
                     client_secret='-Zmd3vRFNTDWs0JerWKEcqd_Ycs4RA',
                     user_agent='OSNA-Project-1')

# Define subreddit
subreddit = reddit.subreddit('technews')

# Initialize empty graph and DataFrames
G = nx.Graph()
df_nodes = pd.DataFrame(columns=['user'])
df_edges = pd.DataFrame(columns=['user1', 'user2'])

# Lists to store node and edge data
nodes_data = []
edges_data = []

def fetch_comments(subreddit, limit):
    """
    Fetch comments from a subreddit up to the specified limit.

    Args:
    - subreddit: Reddit subreddit object.
    - limit: Maximum number of comments to fetch.

    Returns:
    - List: List of comment objects.
    """
    comments = []
    for comment in subreddit.comments(limit=limit):
        comments.append(comment)
        time.sleep(1)  # Sleep to avoid hitting rate limits
    return comments

# Parameters for fetching comments
comments_batch_size = 100
total_comments_to_fetch = 500
comments_fetched = 0

# Fetch comments in batches until the specified limit is reached
while comments_fetched < total_comments_to_fetch:
    batch_size = min(comments_batch_size, total_comments_to_fetch - comments_fetched)
    comments = fetch_comments(subreddit, batch_size)
    for comment in comments:
        try:
            user = comment.author
            parent = comment.parent()
            parent_user = None

            # Determine the author of the parent comment or submission
            if isinstance(parent, praw.models.reddit.comment.Comment):
                parent_user = parent.author
            elif isinstance(parent, praw.models.reddit.submission.Submission):
                parent_user = parent.author

            # Add nodes and edges if both user and parent_user exist
            if user is not None and parent_user is not None:
                G.add_node(user)
                G.add_node(parent_user)
                G.add_edge(user, parent_user)

            # Append user and parent_user data to nodes_data list
            nodes_data.append({'user': user})
            nodes_data.append({'user': parent_user})

            # Append edge data to edges_data list
            edges_data.append({'user1': user, 'user2': parent_user})
        except AttributeError as e:
            # Skip missing or deleted comments
            print("Skipping missing or deleted comment:", e)

    comments_fetched += batch_size

# Create DataFrames from nodes and edges data
df_nodes = pd.DataFrame(nodes_data)
df_edges = pd.DataFrame(edges_data)

# Write DataFrames to CSV files
df_edges.to_csv("user_node_edges.csv")
df_nodes.to_csv("user_nodes.csv")
