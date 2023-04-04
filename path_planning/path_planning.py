from typing import List, Optional
from sortedcontainers import SortedKeyList

class Node:
    def __init__(self, grid_cost: int, coordinate_pt: tuple, parent) -> None:
        self.grid_cost = grid_cost # shortest distance from parent node 
        self.parent = parent
        self.coordinate_pt = coordinate_pt
    
    def update_grid_cost(self, val: int) -> None:
        if val >= 0:
            self.grid_cost = val
    
    def get_grid_cost(self) -> int:
        return self.grid_cost

    def get_parent(self):
        return self.parent
    
    def get_coordinate_pt(self):
        return self.coordinate_pt

    def __str__(self):
        return "Node with grid_cost = " + str(self.grid_cost) + " at starting pt: " + str(self.coordinate_pt)
    

def find_neighbours(node: Node, width: int, height: int, costmap, resolution) -> Optional[List[Node]]:
    ''' 
    Identifies neighboring nodes (at most 8)
    Parameters:
        node:       (Node):  neighboring nodes will be derived from this current node 
        width       (int):   grid width, specified as a positive scalar in meters.
        height      (int):   grid height, specified as a positive scalar in meters.
        costmap     (): ?
        resolution  (): ?

    Returns:
        neighbors (List[Nodes]): if neighbors can be found, else returns None
    '''
    pass


def return_shortest_path(start_point, goal_point, width, height, costmap, resolution, origin) -> Optional[List[Node]]:
    ''' 
    Performs Dijkstra's shortest path algorithm search on a costmap with a given start and goal node
    Parameters:
        start_point (tuple): starting point on the occupancy grid.
        goal_point  (tuple): destination point on the occupancy grid.
        width       (int):   grid width, specified as a positive scalar in meters.
        height      (int):   grid height, specified as a positive scalar in meters.
        costmap     (): ?
        resolution  (): ?
        origin      (): ?

    Returns:
        shortest_path (List[Nodes]): if destination can be found, else returns None

    Dijkstra's Algorithm can be implemented in 2 phases:
    Phase 1: From a starting point, we incrementally explore other neighboring nodes until the goal_node can be found 
    Phase 2: When goal_node is found, we recursively backtrack to the starting_node, given that each child node's parent attribute is a recursive structure
    '''

    shortest_path = list()
    current_node = None
    path_exists = False
    sort_func = lambda a: a.get_grid_cost()
    unvisited_queue = SortedKeyList(key = sort_func) # means of book-keeping to store list of unvisited nodes. Idealistically we want this to be a SortedSet so our selection favors nodes with minimum grid costs.
    visited_queue = list() # means of book-keeping to store list of visited nodes
    
    # intializing parent node and adding that to the beginning of frontier
    starting_node = Node(grid_cost=0, coordinate_pt=start_point, parent=None)
    unvisited_queue.add(starting_node)

    while(len(unvisited_queue) != 0):
        # remove current node from frontier and declare it as target node to explore
        current_node = unvisited_queue.pop(0)

        # check if current node is goal point
        if current_node.get_coordinate_pt() == goal_point:
            path_exists = True
            break

        # find the neighbors of the current node and add to frontier iff it's a new member to the set ... if it exists within set, re-evaluate smaller g_cost if necessary
        neighbors = find_neighbours(node=current_node, width=width, height=height, costmap=costmap, resolution=resolution)
        for neighbor in neighbors:
            if neighbor not in visited_queue:
                
                # update g_cost if current_node.g_cost < neighbor_node.g_cost
                if neighbor in unvisited_queue:
                    n_index = unvisited_queue.index(neighbor)
                    neighbor_node = unvisited_queue.pop(n_index)

                    if current_node.g_cost < neighbor_node.g_cost:
                        neighbor_node.update_grid_cost() # TODO: update val = step_cost + grid_cost
                        neighbor_node.parent = current_node

                    unvisited_queue.add(neighbor_node)

                # add new neighbor node to open list
                else:
                    new_node = Node(grid_cost=, coordinate_pt=, parent=current_node) # TODO: set first 2 params
                    unvisited_queue.add(new_node)

        # add target node to visited
        visited_queue.add(current_node)

    if path_exists:
        # building path by recursive backtracking
        while(current_node != None):
            shortest_path.append(current_node)
            current_node = current_node.parent
        shortest_path.reverse()
        return shortest_path
    return None


def main():
    # TESTING SORTEDKEYLIST with custom KEY!
    node1 = Node(0.1,(0,0), None)
    node2 = Node(1,(1,0), None)
    node3 = Node(2,(0,2), None)
    l = list()
    l.append(node2)
    l.append(node1)
    l.append(node3)
    ######################
    sort_list = SortedKeyList(key=lambda a: a.get_grid_cost())
    sort_list.add(node2)
    sort_list.add(node1)
    sort_list.add(node3)
    #######################
    # for ele in sort_list:
    #     print(ele)
    # for e in l:
    #     print(e.get_grid_cost())
    
    # TESTING SORTEDKEYLIST auto-sorts after updating a member's value!!
    # one way is to lookup index of item, pop by index, make manual update and re_add
    n_index = sort_list.index(node2)
    print("Index of Node1: " + str(n_index))
    popped_node = sort_list.pop(n_index)
    print(popped_node)
    print("*******")
    for ele in sort_list:
        print(ele)
    print("length after popped: " + str(len(sort_list)))
    popped_node.update_grid_cost(0.05)
    sort_list.add(popped_node)
    for ele in sort_list:
        print(ele)

    # TESTING membership in SORTEDKEYLIST!!
    print("MEMBERSHIP: " + str(node3 in sort_list))
if __name__ == '__main__':
    main()