- python中的list和array的不同之处
  - python中的list是python的内置数据类型，list中的数据类不必相同的，而array的中的类型必须全部相同。在list中的数据类型保存的是数据的存放的地址，简单的说就是指针，并非数据，这样保存一个list就太麻烦了，例如list1=[1,2,3,'a']需要4个指针和四个数据，增加了存储和消耗cpu。



  - list中需要实现的方法
    - append  insert  extend 方法
    - remove  pop方法
    - reverse  反转
    - len()
    - 根据索引查找
    - 清空列表
    - 修改元素的值
    - 可以实现切片操作


线性结构，内存连续，一开始就会分配一块固定的内存给它，可以通过下标去快速访问，当分配足够的空间，时间复杂度是O(1)，否则它就会resize操作重新开辟并拷贝原来的数据到新开辟的空间中去，这时就会退化，时间复杂度是O(n)
