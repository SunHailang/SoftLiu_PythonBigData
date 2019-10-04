import pandas

list1 = [1, 2, 3, 4, 5]
list2 = pandas.Series(list1)
print(list2)
'''
Series是一维的数据结构，用Series函数生成数组，其中能够很明显的看到，这里生成的数组和通过array函数生成的不一样。左边是索引，右边是标签。其实还是可以定义索引的。
'''
list3 = pandas.Series((list1), index=['a', 'b', 'c', 'd', 'e'])
print(list3)
# 获取一个数据或是一组数据， 根据索引获得
data1 = list3['c']
print(data1)
# 如果数据是字典，也可以直接通过字典创建列表, 其实字典key就是列表的索引.
dir1 = {
    'a': 'hello',
    'b': 'world',
    'c': 520
}
list4 = pandas.Series(dir1)
print(list4)

'''
DataFrame是一个表格型的数据结构，有不同的列，并且每一列都可以是不同的数据类型。我们可以把它类似于Excel或者是SQL
'''

dict1 = {
    'name': ['zhangsan', 'lisi', 'wangermazi', 'gun'],
    'sex': ['man', 'woman', 'woman', 'man'],
    'age': [12, 18, 18, 30]
}
list5 = pandas.DataFrame(dict1)
print(list5)

# DataFrame中通过info函数直接查看数据类型和统计
list5.info()

# 两种索引方式进行选取列
columns1 = list5.name
columns2 = list5['name']
print(columns1, columns2)
'''
.ix已弃用。 请用 .loc 用于基于标签的索引或 .iloc 用于位置索引
'''
columns3 = list5.loc[0]
columns4 = list5.iloc[1]
print(columns3)
print(columns4)
'''
当行和列需要同时选择的时候，用.loc，之间用逗号分割，逗号前是想要选择的行，逗号后是想要选择的列。
'''
data3 = list5.loc[1, 'age']
print('data3: ', data3)

'''
列可以通过赋值的方式修改和添加，当列的名称是全新，则会在DataFrame的最右边自动加上新的一列。
'''
list5['country'] = 'China'
print(list5)

data2 = list5[(list5.sex=='man') & (list5.age==30)]
print(data2)