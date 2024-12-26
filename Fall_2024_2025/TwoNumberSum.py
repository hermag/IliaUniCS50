"""
Two Number Sum
Write a function that takes in non-empty array of distinct integers and an integer representing a target sum. If any two numbers
in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up
to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself
in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

array = [3,5,-4,8,11,1,-1,6]
targetSum = 10

output
[-1,11]


Test Cases
1. Input: {
  "array": [3, 5, -4, 8, 11, 1, -1, 6],
  "targetSum": 10
   }
   output: [11,-1]

2. Input: {
   "array": [4, 6],
   "targetSum": 10
   }
   Output: [4, 6]

3. Input: {
  "array": [4, 6, 1],
  "targetSum": 5 
   }
   Output: [4, 1]

4. Input: {
  "array": [4, 6, 1, -3],
  "targetSum": 3
   }
   Output: [6, -3]

5. Input: {
  "array": [1, 2, 3, 4, 5, 6, 7, 8, 9],
  "targetSum": 17
   }
   Output: [8, 9]

6. Input: {
  "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 15],
  "targetSum": 18
   }
   Output: [3, 15]

7. Input: {
  "array": [-7, -5, -3, -1, 0, 1, 3, 5, 7],
  "targetSum": -5
   }
   Output: [-5, 0]

8. Input: {
  "array": [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47],
  "targetSum": 163
   }
   Output: [210, -47]

9. Input: {
  "array": [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47],
  "targetSum": 164
   }
   Output: []

10.Input: {
  "array": [3, 5, -4, 8, 11, 1, -1, 6],
  "targetSum": 15
   }
   Output: []

11. Input: {
  "array": [14],
  "targetSum": 15
   }
   Output:  []

12. Input: {
  "array": [15],
  "targetSum": 15
   }
   Output: []   

"""

#My first solution
def twoNumberSum(array, targetSum):
    array_to_return=[]
    for item1 in array[:-1]:
        for item2 in array[array.index(item1)+1:]:
            tmp_sum=int(item1)+int(item2)
            if tmp_sum == targetSum:
                if item1 not in array_to_return:
                    array_to_return.append(item1)
                    array_to_return.append(item2)
                else:
                    array_to_return.append(item2)
            else:
                pass
        array.pop(array.index(item1))
    pass
    return array_to_return

#My second solution
def twoNumberSum(array, targetSum):
    result_dict = {}
    for item in array:
        if int(targetSum)-int(item) not in result_dict.keys():
            result_dict[item]=True
        else:
            return [int(item),int(targetSum)-int(item)]
    pass
    return []
   
#My third solution
def twoNumberSum(array, targetSum):
    array.sort()
    n = len(array)
    resulting_array=[]
    i=0
    j=1
    while i < n-j:      
      print("array[",i,"]=",array[i]," array[",n-j,"]=",array[n-j])
      if int(array[i]) + int(array[n-j]) == targetSum:
        resulting_array.append(array[i])
        resulting_array.append(array[n-j])
        i=i+1
      elif int(array[i]) + int(array[n-j]) > targetSum:
        j=j+1
      elif int(array[i]) + int(array[n-j]) < targetSum:
        i=i+1
    return resulting_array
