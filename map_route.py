import math
from heapq import heappush, heappop

def get_g(intersections, node1, node2):
    x = intersections[node2][0] - intersections[node1][0]
    y = intersections[node2][1] - intersections[node1][1]

    g = math.sqrt(abs(x) + abs(y))
    return g

def get_h(intersections, node1, node2):
    x = intersections[node2][0] - intersections[node1][0]
    y = intersections[node2][1] - intersections[node1][1]
    
    h = math.sqrt(x*x + y*y)
    return h


def shortest_path(M,start,goal):
    minHeap = list()
    path_dict = dict()
    print("shortest path called")
    if (start not in M.intersections.keys()) or (goal not in M.intersections.keys()):
        return None
    
    if start == goal:
        return [start]
    # will hold f values, add 0 since the f value for start is zero
    heappush(minHeap, 0)
    # add 0:[start] as f:[path] to dict that represents the frontier
    path_dict[0] = [start]
    
    
    while len(minHeap) > 0:
    
        # extract min f from heap
        current_f = heappop(minHeap)
        path = path_dict[current_f]
        current_city = path[-1]
        
        # check for goal
        if current_city == goal:
            return path


        for road in M.roads[current_city]:
            new_f = current_f + get_g(M.intersections, current_city, road) + get_h(M.intersections, road, goal)
            path.append(road)
            # add new path to path_dict
            path_dict[new_f] = path
            # add new_f to minHeap
            heappush(minHeap, new_f)
            
            

        del path_dict[current_f]