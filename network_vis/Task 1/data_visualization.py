import jgraph

import json

with open('network_vis/Task 1/edges_convertcsv.json') as f:
  edges = json.load(f)

with open('network_vis/Task 1/nodes_convertcsv.json') as f:
  nodes = json.load(f)

# remove column.
for node in range(len(nodes)):
    nodes[node].pop('FIELD4', None)

dict_nodes = {}

for i in range(len(nodes)):

    new_key = str(nodes[i]['node_id'])


    nodes[i].pop('node_id', None)

    nodes[i]['color'] = nodes[i]['node_color'].replace('#', '0x')
    nodes[i].pop('node_color', None)
    
    nodes[i].pop('node_label', None)
     
    dict_nodes[new_key] = nodes[i]

new_edges = []

for i in range(len(edges)):
    temp = edges[i]
    
    temp['source'] = str(temp['source_id'])
    temp.pop('source_id', None)
    
    temp['target'] = str(temp['target_id'])
    temp.pop('target_id', None)
    
    temp['size'] = str(temp['weights'])
    temp.pop('weights', None)
    
    
    new_edges.append(temp)
    
graph = {'nodes': dict_nodes, 'edges': new_edges}

jgraph.draw(graph, size=(1000, 800), node_size=2.0, edge_size=0.1, shader='toon')
