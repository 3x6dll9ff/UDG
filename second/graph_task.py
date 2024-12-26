import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()


edges = [
    ("Scepan Polje", "Bjeli Potok", ),
    ("Подгорица", "Цетине", 29),
    ("Подгорица", "Бар", 53),
    ("Подгорица", "Будва", 65),
    ("Подгорица", "Херцег-Нови", 118),
    ("Никшич", "Плевля", 104),
    ("Никшич", "Жабляк", 72),
    ("Никшич", "Херцег-Нови", 96),
    ("Цетине", "Будва", 31),
    ("Цетине", "Херцег-Нови", 91),
    ("Цетине", "Ульцинь", 25),
    ("Цетине", "Бар", 41),
    ("Будва", "Херцег-Нови", 58),
    ("Херцег-Нови", "Котор", 43),
]


for u, v, weight in edges:
    G.add_edge(u, v, weight=weight)


shortest_path = nx.shortest_path(G, source="Подгорица", target="Ульцинь", weight="weight")
shortest_distance = nx.shortest_path_length(G, source="Подгорица", target="Ульцинь", weight="weight")
print("Кратчайший путь от Подгорицы до Ульциня:", shortest_path)
print("Длина кратчайшего пути:", shortest_distance)


city_with_most_neighbors = max(G.degree, key=lambda x: x[1])
print("Город с наибольшим количеством соседей:", city_with_most_neighbors[0])
print("Количество соседей:", city_with_most_neighbors[1])


connected_to_podgorica = list(G.neighbors("Подгорица"))
print("Города, связанные с Подгорицей:", connected_to_podgorica)


pos = nx.spring_layout(G)  
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')  # Подписи для ребер (веса)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Граф связей городов в Черногории")
plt.show()
