from typing import List

def two_sum(nums: List, target: int) -> List:
    """Function determines the index of numbers in num whose sum equals target
    :type nums: List[int]
    :type target: int
    :rtype: List[int]    
    """
    num_index = {}
    two_sum_indexes = []
    for index, value in enumerate(nums):
        compliment_value = target - value
        compliment_index = num_index.get(compliment_value, None)
        if compliment_index is not None:
            two_sum_indexes = [index, compliment_index]
            break
        num_index[value] = index
    return two_sum_indexes


if __name__ == '__main__':
    indexes = two_sum(nums=[2, 7, 11, 15], target=9)
    print(indexes)
        