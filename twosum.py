
from typing import List, Union


def sum (data, target) -> Union[List[int], None]:
  prevMap = {}
  
  for i, n, in enumerate(data):
    diff = target - n
    if diff in prevMap:
      return [prevMap[diff], i]
    prevMap[n] = i
    return None

