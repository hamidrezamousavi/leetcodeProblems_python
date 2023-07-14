from typing import List
from itertools import product
def letterCombinations(digits: str) -> List[str]:
  key = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz',
          }
  
  digits_letter = [key[digit] for digit in digits]
  
  
  result = list(''.join(x) for x in product(*digits_letter))  
 
  return result
s = ''
print(letterCombinations(s))