def generate(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1,1]]
    result = [[1], [1,1]]
    for i in range(2,numRows):
        last_item = result[-1]
        temp = [1]
        for j in range(len(last_item)-1):
            temp.append(last_item[j] + last_item[j + 1])
        temp.append(1)
        result.append(temp)
    return result
