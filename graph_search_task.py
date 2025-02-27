# ##################################################
# 1) Load workpiece graph and feature graph data from  json file
# ##################################################

# Note: Available files are: workpiece_graph.json, feature_graph.json

# TODO
import json

# Read the JSON file
with open("workpiece_graph.json", "r") as file:
    workpiece_graph = json.load(file)
    
with open("feature_graph.json", "r") as file:
    feature_graph = json.load(file)
# ##################################################
# 2) Create graphs from loaded data
# ##################################################

# Hint: The library networkx helps you to create a graph. You can use the nx.Graph() class to create a graph.
# Note: Other appraoches are also possible.

# TODO
import networkx as nx
workpiece = nx.Graph()
for node_id, attributes in workpiece_graph["nodes"]:
    workpiece.add_node(node_id, **attributes)

# Add edges with angular type as an attribute
for source, target, attributes in workpiece_graph["edges"]:
    workpiece.add_edge(source, target, angular_type=attributes["angular_type"])

feature = nx.Graph()

for node_id, attributes in feature_graph["nodes"]:
    feature.add_node(node_id, **attributes)

# Add edges with angular type as an attribute
for source, target, attributes in feature_graph["edges"]:
    feature.add_edge(source, target, angular_type=attributes["angular_type"])
# Note: Optional task - Visualize the graph
# Example code:
# from pyvis.network import Network
# nt = Network()
# nt.from_nx(workpiece_graph)
# nt.show("graph.html", notebook=False)

from pyvis.network import Network

nt = Network()
nt.from_nx(workpiece)
nt.show("workpiecegraph.html", notebook=False)

featurent = Network()
featurent.from_nx(feature)
featurent.show("featuregraph.html", notebook=False)
# ##################################################
# 3) Check if the feature graph is a subgraph of the workpiece workpiece and find any other matching subgraphs
# ##################################################


# TODO
# ##################################################
# 4) Results
# ##################################################

# Print results if matches are found. Return the number of matches and the node ids.

# TODO
