---

# Search Algorithms in Python

This repository contains Python implementations of various search algorithms.

## Search Algorithms Without Information

### Uniform Cost Search

Uniform Cost Search is an uninformed search that can be implemented as a Best-First Search where the frontier is implemented as a priority queue ordered by the cumulative path cost function.

#### Analysis:

- **Completeness:** Complete if the cost of each action is greater than a positive epsilon value.
- **Optimality:** Yes, if the cost of each action is non-decreasing.
- **Time Complexity:** \( O(b^{1 + \lfloor C^* / \epsilon \rfloor}) \), where \( C^* \) is the cost of the optimal solution and \( \epsilon \) is the smallest cost of an action.
- **Space Complexity:** \( O(b^{1 + \lfloor C^* / \epsilon \rfloor}) \), where \( C^* \) is the cost of the optimal solution and \( \epsilon \) is the smallest cost of an action.

### Dijkstra's Algorithm

#### Analysis:

- **Completeness:** Yes, if all path costs are positive.
- **Optimality:** Yes, if all path costs are positive.
- **Time Complexity:** \( O(b^{1 + \lfloor C^* / \epsilon \rfloor}) \), where \( C^* \) is the cost of the optimal solution and \( \epsilon \) is the smallest cost of an action.
- **Space Complexity:** \( O(b^{1 + \lfloor C^* / \epsilon \rfloor}) \), where \( C^* \) is the cost of the optimal solution and \( \epsilon \) is the smallest cost of an action.

### Breadth-First Search (BFS)

#### Analysis:

- **Completeness:** Yes, for finite trees.
- **Optimality:** Yes, for uniform path costs.
- **Time Complexity:** \( O(b^d) \), where \( b \) is the branching factor and \( d \) is the depth of the solution.
- **Space Complexity:** \( O(b^d) \), where \( b \) is the branching factor and \( d \) is the depth of the solution.

### Depth-First Search (DFS)

#### Analysis:

- **Completeness:** Not complete, can get stuck in infinite loops.
- **Optimality:** No, the solution found may not be optimal.
- **Time Complexity:** \( O(b^m) \), where \( b \) is the branching factor and \( m \) is the maximum depth of the state space.
- **Space Complexity:** \( O(bm) \), where \( b \) is the branching factor and \( m \) is the maximum depth of the state space.

### Depth-Limited Search (DLS)

#### Analysis:

- **Completeness:** Not complete, can get stuck in infinite loops or reach the depth limit before finding a solution.
- **Optimality:** No, the solution found may not be optimal.
- **Time Complexity:** \( O(b^l) \), where \( b \) is the branching factor and \( l \) is the depth limit.
- **Space Complexity:** \( O(bl) \), where \( b \) is the branching factor and \( l \) is the depth limit.

### Iterative Deepening Search (IDS)

#### Analysis:

- **Completeness:** Complete.
- **Optimality:** Yes, for uniform path costs.
- **Time Complexity:** \( O(b^d) \), where \( b \) is the branching factor and \( d \) is the depth of the solution.
- **Space Complexity:** \( O(bd) \), where \( b \) is the branching factor and \( d \) is the depth of the solution.

### Bidirectional Search

#### Analysis:

- **Completeness:** Yes, for finite trees.
- **Optimality:** Yes, for uniform path costs.
- **Time Complexity:** \( O(b^{d/2}) \), where \( b \) is the branching factor and \( d \) is the distance between the start and the goal.
- **Space Complexity:** \( O(b^{d/2}) \), where \( b \) is the branching factor and \( d \) is the distance between the start and the goal.

## Search Algorithms With Information

### Greedy Best-First Search (GBFS)

#### Analysis:

- **Completeness:** Not complete.
- **Optimality:** No, depends on the heuristic.
- **Time Complexity:** Depends on the heuristic.
- **Space Complexity:** \( O(b^d) \), where \( b \) is the branching factor and \( d \) is the depth of the solution.

### A* Search

#### Analysis:

- **Completeness:** Yes, for admissible heuristics.
- **Optimality:** Yes, for admissible heuristics.
- **Time Complexity:** \( O(b^d) \), where \( b \) is the branching factor and \( d \) is the depth of the solution.
- **Space Complexity:** \( O(b^d) \), where \( b \) is the branching factor and \( d \) is the depth of the solution.

### Weighted A* Search

#### Analysis:

- **Completeness:** Yes, for admissible heuristics.
- **Optimality:** Yes, for admissible heuristics.
- **Time Complexity:** Depends on the weight \( W \).
- **Space Complexity:** \( O(b^d) \), where \( b \) is the branching factor and \( d \) is the depth of the solution.

### Iterative Deepening A* (IDA*)

#### Analysis:

- **Completeness:** Yes.
- **Optimality:** Yes, for admissible heuristics.
- **Time Complexity:** Depends on the heuristic.
- **Space Complexity:** \( O(bd) \), where \( b \) is the branching factor and \( d \) is the depth of the solution.

### Recursive Best-First Search (RBFS)

#### Analysis:

- **Completeness:** Yes.
- **Optimality:** Yes, for admissible heuristics.
- **Time Complexity:** Depends on the heuristic.
- **Space Complexity:** Linear.

## Algorithm Comparison

- **Uniform Cost Search vs. Greedy Best-First Search:**
  - Uniform Cost Search is complete and delivers optimal solutions, while Greedy Best-First Search is not complete and does not guarantee optimal solutions.
  
- **A* Search vs. Uniform Cost Search:**
  - Both are complete and deliver optimal solutions, but A* Search is more efficient when an admissible heuristic is available.

- **A* Search vs. Weighted A* Search:**
  - Weighted A* Search introduces a weighting factor \( W \), which can affect the efficiency and optimality of the algorithm. For \( W = 1 \), it's equivalent to standard A* Search.

- **A* Search vs. Iterative Deepening A*:**
  - Iterative Deepening A* (IDA*) is useful when memory is a concern, while standard A* Search might be more efficient in terms of runtime.

- **A* Search vs. Recursive Best-First Search:**
  - Recursive Best-First Search is a recursive version of an A*-like algorithm, but it's more space-efficient as it uses only linear memory. However, it might be less efficient in terms of runtime, depending on the heuristic.
---
### Clone the Repository

Open a terminal or command prompt and run the following command:

```bash
git clone https://https://github.com/michel-j-j/SearchAlgorithms
```
