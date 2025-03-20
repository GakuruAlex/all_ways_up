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
    ...
    return all_ways_table[height]