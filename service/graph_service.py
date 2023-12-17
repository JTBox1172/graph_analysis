import networkx as nx 
import matplotlib.pyplot as plt
import pandas as pd
from networkx.readwrite import json_graph
from typing import List
import json

def get_graph(df, src: str, dest: str):
    G = nx.from_pandas_edgelist(df, src, dest)
    G.name = "graph from pandas adjacency matrix"
    jsonGraph = json_graph.node_link_data(G)
    json.dumps(jsonGraph)
    print(jsonGraph)
    return jsonGraph

def convert_csv_to_dataframe(filePath):
    df = pd.read_csv(filePath)
    return df

def convert_xls_to_dataframe(filePath):
    df = pd.read_excel(filePath)
    return df
