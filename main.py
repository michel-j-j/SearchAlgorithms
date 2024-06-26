from model.BestFirstSearch import BestFirstSearch
from model.BreadthFirstSearch import BreadthFirstSearch
from model.DepthFirstSearch import DepthFirstSearch
from model.BidirectionalBestFirstSearch import BidirectionalBestFirstSearch

from model.agent.Problem import Problem 


def main():
    states = ['Arad', 'Zerind', 'Oradea', 'Sibiu', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Rimnicu Vilcea', 'Fagaras', 'Pitesti', 'Bucharest', 'Giurgiu', 'Urziceni', 'Hirsova', 'Eforie', 'Vaslui', 'Iasi', 'Neamt']
    initial = 'Arad'

    goal = 'Bucharest'

    actions = {
    'Arad': ['toZerind', 'toSibiu', 'toTimisoara'],
    'Zerind': ['toArad', 'toOradea'],
    'Oradea': ['toZerind', 'toSibiu'],
    'Sibiu': ['toArad', 'toOradea', 'toFagaras', 'toRimnicu Vilcea'], 
    'Timisoara': ['toArad', 'toLugoj'],
    'Lugoj': ['toTimisoara', 'toMehadia'], 
    'Mehadia': ['toLugoj', 'toDrobeta'],
    'Drobeta': ['toMehadia', 'toCraiova'],
    'Craiova': ['toDrobeta', 'toRimnicu Vilcea', 'toPitesti'],
    'Rimnicu Vilcea': ['toSibiu', 'toCraiova', 'toPitesti'],
    'Fagaras': ['toSibiu', 'toBucharest'],
    'Pitesti': ['toRimnicu Vilcea', 'toCraiova', 'toBucharest'], 
    'Bucharest': ['toFagaras', 'toPitesti', 'toGiurgiu', 'toUrziceni'], 'Giurgiu': ['toBucharest'],
    'Urziceni': ['toBucharest', 'toHirsova', 'toVaslui'],
    'Hirsova': ['toUrziceni', 'toEforie'],
    'Eforie': ['toHirsova'],
    'Vaslui': ['toUrziceni', 'toIasi'], 'Iasi': ['toVaslui', 'toNeamt'],
    'Neamt': ['toIasi']}

    transition_model = {
    'Arad': {'toZerind': 'Zerind', 'toSibiu': 'Sibiu', 'toTimisoara': 'Timisoara'},
    'Zerind': {'toArad': 'Arad', 'toOradea': 'Oradea'},
    'Oradea': {'toZerind': 'Zerind', 'toSibiu': 'Sibiu'},
    'Sibiu': {'toArad': 'Arad', 'toOradea': 'Oradea', 'toFagaras': 'Fagaras', 'toRimnicu Vilcea': 'Rimnicu Vilcea'}, 
    'Timisoara': {'toArad': 'Arad', 'toLugoj': 'Lugoj'},
    'Lugoj': {'toTimisoara': 'Timisoara', 'toMehadia': 'Mehadia'},
    'Mehadia': {'toLugoj': 'Lugoj', 'toDrobeta': 'Drobeta'},
    'Drobeta': {'toMehadia': 'Mehadia', 'toCraiova': 'Craiova'},
    'Craiova': {'toDrobeta': 'Drobeta', 'toRimnicu Vilcea': 'Rimnicu Vilcea', 'toPitesti': 'Pitesti'},
    'Rimnicu Vilcea': {'toSibiu': 'Sibiu', 'toCraiova': 'Craiova', 'toPitesti': 'Pitesti'},
    'Fagaras': {'toSibiu': 'Sibiu', 'toBucharest': 'Bucharest'},
    'Pitesti': {'toRimnicu Vilcea': 'Rimnicu Vilcea', 'toCraiova': 'Craiova', 'toBucharest': 'Bucharest'},
    'Bucharest': {'toFagaras': 'Fagaras', 'toPitesti': 'Pitesti', 'toGiurgiu': 'Giurgiu', 'toUrziceni': 'Urziceni'}, 
    'Giurgiu': {'toBucharest': 'Bucharest'},
    'Urziceni':{'toBucharest': 'Bucharest', 'toHirsova': 'Hirsova', 'toVaslui': 'Vaslui'},
    'Hirsova': {'toUrziceni': 'Urziceni', 'toEforie': 'Eforie'},
    'Eforie': {'toHirsova': 'Hirsova'},
    'Vaslui': {'toUrziceni': 'Urziceni', 'tolasi': 'Iasi'},
    'Iasi': {'toVaslui': 'Vaslui', 'toNeamt': 'Neamt'},
    'Neamt': {'tolasi': 'Iasi'}
    }
    
    cost = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80}, 
    'Timisoara':{ 'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70}, 'Mehadia':{'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi' : 87}}

    Arad2Bucarest = Problem(states, initial, goal, actions, transition_model, cost)
  
  ##busca = BestFirstSearch(Arad2Bucarest, lambda node: node.path_cost)
  ##print("Best First Search (Arad -> Bucharest):")
  ##node = busca.search()
  ##print(node.state, node.path_cost)
  ##print("Solution:")
  ##for step in busca.path(node):
  ## print(step.state, step. path_cost)
    
  ## busca = BreadthFirstSearch(Arad2Bucarest)
  ## print("Breadth-first search (Arad -> Bucharest):")
  ## node = busca.search()
  ## print(node.state, node.path_cost)
  ## print("Solution:")
  ## for step in busca.path(node):
  ##  print(step.state, step. path_cost)
   

  ## busca = DepthFirstSearch(Arad2Bucarest)
  ## print("Depth-First search (Arad -> Bucharest):")
  ## node = busca.search()
  ## print(node.state, node.path_cost)
  ## print("Solution:")
  ## for step in busca.path(node):
  ##  print(step.state, step. path_cost)
     
    print("__________________________")
    print("Bidirectional search (Arad -> Bucharest):")
    Bucarest2Arad = Problem(states, goal, initial, actions, transition_model, cost)
    busca = BidirectionalBestFirstSearch(Arad2Bucarest, lambda node: node.path_cost, 
                                         Bucarest2Arad, lambda node: node.path_cost)
    nodes = busca.search()
    print(nodes[0].state, nodes[0].path_cost, 
          nodes[1].state, nodes[1].path_cost, nodes[0].path_cost + nodes[1].path_cost)
    print("Solution:")
    for step in busca.path(nodes[0]):
        print(step.state, step.path_cost)
    for step in busca.path(nodes[1])[::-1]:
        print(step.state, step.path_cost)


main()