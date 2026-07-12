import collections
import random
import time
import networkx as nx

def bfsFarthestNode(graph, startNode):
    queue = collections.deque([(startNode, 0)])
    visited = {startNode}

    farthestNode = startNode
    maxDist = 0

    while queue:
        current, dist = queue.popleft()

        if dist > maxDist:
            maxDist = dist
            farthestNode = current

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return farthestNode, maxDist

def getTreeDiameter(adjList):
    if not adjList:
        return 0

    startNode = list(adjList.keys())[0]

    nodeV, _ = bfsFarthestNode(adjList, startNode)

    nodeW, diameter = bfsFarthestNode(adjList, nodeV)

    return diameter

def runSimulation(numTrees=30, minV=200, maxV=300):
    print(f"{'Vertices':<10} | {'Diameter':<10} | {'Time (ms)':<10}")
    print("-" * 35)

    results = []

    for _ in range(numTrees):
        size = random.randint(minV, maxV)

        G = nx.random_labeled_tree(size)
        
        adjList = nx.to_dict_of_lists(G)

        startTime = time.perf_counter()
        diameter = getTreeDiameter(adjList)
        endTime = time.perf_counter()

        durationMs = (endTime - startTime) * 1000
        
        results.append((size, durationMs))

        print(f"{size:<10} | {diameter:<10} | {durationMs:.4f}")

    return results

if __name__  == "__main__":
    simulation_data = runSimulation()
