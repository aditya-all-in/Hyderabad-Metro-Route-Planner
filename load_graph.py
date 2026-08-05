import json
import networkx as nx
import matplotlib.pyplot as plt

def load_graph(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    G = nx.Graph()
    for station in data['stations']:
        G.add_node(station)

    for edge in data['edges']:
        G.add_edge(edge['from'], edge['to'], weight=edge['weight'])

    return G

def dijkstra_path(G, source, target):
    try:
        return nx.dijkstra_path(G, source, target)
    except nx.NetworkXNoPath:
        return None

def draw_graph(G, path=None):
    # Define fixed layout for each station (you can expand this dictionary)
    pos = {
        "Miyapur": (40, 0),
        "JNTUcollege": (40, 1),
        "KPHBcolony": (39, 2),
        "Kukatpally": (38, 3),
        "DR_BRambedkar": (37, 3),
        "Moosapet": (36, 3),
        "Bharatnagar": (35, 3),
        "Erragadda": (34, 3),
        "ESIhospital": (33, 3),
        "SRnagar": (32, 3),
        "Ameerpet": (31, 4),
        "Panjagutta": (30, 5),
        "Irrummanzil": (29, 6),
        "Khairtabad": (28, 7),
        "Lakdikapool": (27, 8),
        "Assembly": (26, 9),
        "GandhiBhavan": (26, 10),
        "MG BusStation": (25, 11),
        "Malakpet": (24, 12),
        "New Market": (23, 13),
        "Moosrambagh": (22, 14),
        "Dilshukhnagar": (21, 14),
        "Chaitanyapuri": (20, 14),
        "Victoria_memorial": (19, 14),
        "LBnagar": (18, 14),
        "Osmania_medical":(17,14),
        "Yusufguda": (16, 14),
        "Jubliehills": (15, 14),
        "JH-checkpost": (33, 4),
        "Peddamagudi": (33, 5),
        "Madhapur": (33, 6),
        "Dugamcheruvu": (33, 7),
        "Hitechcity": (33, 8),
        "Raidurg": (33, 9),

        "Paradeground": (33, 10),
        "SecundrabadWest": (33, 11),
        "Gandhihospital": (41, 6),
        "Musheerabad": (40, 7),
        "RTCxroads": (39, 8),
        "Chikkadpali": (38, 9),
        "Narayanguda": (37, 10),
        "Sultanbazar": (36, 11),

        "Nagole": (35, 11),
        "Uppal": (34, 11),
        "stadium": (33, 11),
        "NGRI": (32, 11),
        "Habsiguda": (31, 11),
        "Tarnaka": (30, 11),
        "Mettuguda": (29, 11),
        "SecuderabadeEast": (28, 11),
        "Paradise": (27, 11),
        "Rasoolpura": (26, 11),
        "PrakashNagar": (25, 11),
        "Begumpet": (24, 12),
        "MathuraNagar": (23, 13),
    }

    edge_labels = nx.get_edge_attributes(G, 'weight')
    node_color = ['lightblue' if not path or node not in path else 'lightgreen' for node in G.nodes]

    nx.draw(G, pos, with_labels=True, node_size=300, node_color=node_color, font_size=7, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

    if path:
        edges_in_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2)

    plt.title("HYD Metro Network")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    G = load_graph("metro_graph.json")
    path = dijkstra_path(G, "Miyapur", "Panjagutta")
    print("Path:", path)
    draw_graph(G, path)
