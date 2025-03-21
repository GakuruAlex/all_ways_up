from copy import deepcopy
from typing import List
def all_ways_up(steps: List[int], height: int) -> List[List[int]]:
    """_find all the possible ways up the stairs given steps to take at a time_

    Args:
        steps (List[int]): _Allowed steps at a time_
        height (int): _Number of stairs_

    Returns:
        List[List[int]]: _A list of lof all the ways up_
    """
    all_ways_table: List[List[int]] = [None for _ in range(height + 1)]
    all_ways_table[0] = [[]]
    for index in range(height +1):
        if all_ways_table[index] != None:
            for step in steps:
                current: List[List[int]] = deepcopy(all_ways_table[index])
                for way in current:
                    way.append(step)
                if index + step < len(all_ways_table):
                    if all_ways_table[index + step] == None:
                        all_ways_table[index + step] = current
                    else:
                        all_ways_table[index + step].extend(current)
    return all_ways_table[height]

def main()-> None:
    steps: List[int] = [1, 2]
    height: int = 5
    all_ways: List[List[int]] = all_ways_up(steps= steps, height= height)
    print(f"All ways up {height} stairs given the steps {steps} are {all_ways}")

if __name__ == "__main__":
    main()