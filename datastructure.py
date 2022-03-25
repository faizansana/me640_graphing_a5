import heapq
from typing import List, Tuple

import graph


class PriorityQueue:
    """Priority Queue based on heaps. If the elements have the same priority, the latest one will go below the other one.
    """
    def __init__(self):
        self.element_num = 0
        self.elements: List[Tuple[int, int, graph.Vertex]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority: int):
        self.element_num += 1
        heapq.heappush(self.elements, (priority, self.element_num, item))

    def get(self):
        return heapq.heappop(self.elements)[2]
