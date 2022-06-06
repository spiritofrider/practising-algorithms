from concurrent.futures import process


graph={}
graph['start']={}
graph['start']['a']=5
graph['start']['c']=2
graph['a']={}
graph['a']['b']=4
graph['a']['d']=2
graph['c']={}
graph['c']['d']=7
graph['b']={}
graph['b']['finish']=3
graph['b']['d']=6
graph['c']={}
graph['c']['d']=7
graph['d']={}
graph['d']['finish']=1
graph['finish']={}

infinity = float("inf")
costs={}
costs['a']=5
costs['c']=2
costs['d']=infinity
costs['b']=infinity
costs['finish']=infinity

parents={}
parents['a']="start"
parents['c']="start"
parents['finish']=None

processed=[]

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost=costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node = node
    return lowest_cost_node

def djikstra(graph):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost=costs[node]
        neighbours=graph[node]
        for n in neighbours.keys():
            new_cost=cost+neighbours[n]
            if costs[n]>new_cost:
                costs[n]=new_cost
                parents[n]=node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs

print(djikstra(graph))















