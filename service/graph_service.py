import networkx as nx 
import matplotlib.pyplot as plt
import pandas as pd
import csv
from networkx.readwrite import json_graph
from typing import List
import json

def get_graph(df, src: str, dest: str):
    G = nx.from_pandas_edgelist(df, src, dest)
    G.name = "graph from pandas adjacency matrix"
    jsonGraph = json_graph.node_link_data(G)
    json.dumps(jsonGraph)
    return jsonGraph

def convert_csv_to_dataframe(filePath):
    df = pd.read_csv(filePath)
    return df

def convert_xls_to_dataframe(filePath):
    df = pd.read_excel(filePath)
    return df

def getHeaders(filePath, fileType):
    if(fileType == ".csv"):
        with open(filePath, 'r') as infile:
            reader = csv.DictReader(infile)
            headers = reader.fieldnames
    elif(fileType == ".xls" or fileType == ".xlsx"):
        headers = []
        # todo
    else:
        headers = []
    return list(headers)
