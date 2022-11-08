import time
with open("DijkstraTest2.txt", 'r') as input:
    lines = input.readlines()

lengths = {}
vertices = []
for line in lines:
    contents = line.split("\t")
    vertices.append(contents[0])
    for content in contents:
        content = content.replace('\n', '')
        if ',' in content:
            edge = contents[0] + '-' + content.split(',')[0]
            lengths[edge] = int(content.split(',')[1])


def NaiveDijkstra(vertices, start_point, lengths):
    X = [start_point]
    shortest_paths = {}
    for vertex in vertices:
        if vertex == start_point:
            shortest_paths[vertex] = 0
        else:
            shortest_paths[vertex] = 999999999999
    subset = [key for key in lengths.keys() if start_point == key.split('-')[0]
              and key.split('-')[0] in X and key.split('-')[1] not in X]
    while len(subset) > 0:
        temp_min_dict = {}
        for edge in subset:
            temp_min = shortest_paths[edge.split('-')[0]] + lengths[edge]
            temp_min_dict[edge] = temp_min
        new_edge = min(temp_min_dict, key=temp_min_dict.get)
        X.append(new_edge.split('-')[1])
        shortest_paths[new_edge.split('-')[1]] = shortest_paths[new_edge.split('-')[0]] + lengths[new_edge]
        subset = []
        for key in lengths.keys():
            if key.split('-')[0] in X and key.split('-')[1] not in X:
                subset.append(key)
    return shortest_paths

start_time = time.time()
print(NaiveDijkstra(vertices = vertices, start_point = '1', lengths = lengths)['197'])
print(time.time() - start_time, "seconds")

