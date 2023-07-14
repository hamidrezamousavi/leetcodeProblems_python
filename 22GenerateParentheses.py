from typing import List
from itertools import product

def is_legal(parentheses:str)->bool:
  for _ in range(len(parentheses)//2):
    parentheses = parentheses.replace('()','')
  return False if len(parentheses) else True

def generateParenthesis(n: int) -> List[str]:
  total_combination  = [''.join(s) for s in product('()',repeat = n * 2)]
  legal_combinatio = [item for item in total_combination if is_legal(item)]
  return legal_combinatio

print(generateParenthesis(4))