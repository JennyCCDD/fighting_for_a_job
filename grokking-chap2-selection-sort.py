"""
# 计算机内存犹如一大堆抽屉
# 需要存储多个元素时，可使用数组或链表。
# 数组的元素都在一起
# 链表的元素是分开的。其中每个元素都存储了下一个元素的地址。
# 数组的读取速度很快
# 链表的插入和删除速度很快
# 在同一个数组中，所有元素的类型都必须相同
"""

# Finds the smallest value in an array
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]
  return smallest_index

# Sort array
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))