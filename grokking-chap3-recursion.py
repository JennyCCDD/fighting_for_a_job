# In[]
# 递归函数由两部分组成，基线条件（base case）和递归条件（recursive case）
def countdown(i):
  # base case
  if i <= 0:
    return 0
  # recursive case
  else:
    print(i)
    return countdown(i-1)

countdown(5)

# In[]
# 调用栈
def greet2(name):
    print("how are you, ", name, "?")

def bye():
    print("ok bye!")

def greet(name):
    print("hello, ", name, "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

greet("adit")

# In[]
# 递归调用栈

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

print(fact(5))

# In[]
def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])

# In[]
def binary_search(arr, target):
    if not arr:
        return -1
    if len(arr) == 1 and arr[0] == target:
        return arr[0]
    if len(arr) == 1 and arr[0] != target:
        return -1
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    if arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid+1:], target)

# In[]
def find_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

# In[]
def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])
