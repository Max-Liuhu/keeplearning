#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 11:03
# @Author  : liuhu
# @File    : 插入排序之insert_sort简单明白版本.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def insert_sort(nums):
    """直接插入排序
    :param nums:
    :return:
    """
    # 遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
    # 当nums元素数量为空或者1时，不会进入for循环
    for i in range(1, len(nums)):
        # 将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
        # range(i,0,-1):从i倒序循环到0，依次比较，
        # 每次比较如果小于会交换位置，正好按递减的顺序
        temp = nums[i]
        for j in range(i - 1, -1, -1):
            # 判断：如果符合条件则交换,并由此处可见直接插入排序为稳定性排序
            if nums[j] > temp:
                nums[j + 1] = nums[j]
            elif nums[j] == temp:
                j += 1
                break
            else:
                break
        # 最后插入点
        nums[j] = temp
    return nums


print(insert_sort([5, 3, 2, 2, 0]))
print(insert_sort([1]))
