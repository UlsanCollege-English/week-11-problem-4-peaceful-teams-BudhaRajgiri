"""
HW04 — Peaceful Teams (Bipartite Check)

Implement:
- bipartition(graph)
"""

from collections import deque

def bipartition(graph):
    """Return (left_set, right_set) if bipartite; else None.

    Use BFS coloring over all components.

    Hints:
    - Maintain color: dict node -> 0/1
    - On seeing same-color neighbors, return None
    """

    color = {}
    left = set()
    right = set()

    for start in graph:
        if start not in color:
            # Start BFS for this component
            queue = deque([start])
            color[start] = 0  # initial color
            left.add(start)

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        # Assign opposite color to neighbor
                        color[v] = 1 - color[u]
                        if color[v] == 0:
                            left.add(v)
                        else:
                            right.add(v)
                        queue.append(v)

                    # Conflict: neighbor has same color
                    elif color[v] == color[u]:
                        return None

    return (left, right)