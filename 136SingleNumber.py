def singleNumber(nums):
    d = dict()
    for item in nums:
        d[item] = d.setdefault(item, 0) + 1
   
    for k, v in d.items():
        if v == 1:
            return k
    return 0
