import numpy
'''

numpy是Python的数值计算扩展，专门用来处理矩阵，你可能也会想Python本身不是有list吗，为什么不直接用呢，答案是numpy的运算效率要远比列表要高效的多。
numpy是n维的数组对象，叫做ndarray.其中创建数组用的函数是numpy包中的array函数。


'''

list1 = [1, 2, 3, 4, 5]

array1 = numpy.array(list1)

print("array1 List:", array1)
# 数组的批量计算
array2 = array1 * array1
print("array1 * array1: ", array2)

# 数组的查找，和索引是一样的
data1 = array2[2]
print("data1: ", data1)

# 数组的转置
list2 = numpy.arange(15).reshape((3, 5))
print("list2: ", list2)
list3 = list2.T
print("list3: ", list3)