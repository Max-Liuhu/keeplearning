- 设计目的：用于实现发送方与接收方（多个）之间的解耦。
- 注意点：
1. 责任链模式并不是创建出责任链，责任链的创建必须要系统的其他部分完成
2. 责任链可以是一条线  一个树  也可以是一个环，链的拓扑结构可以是单连通的或者多连通的，责任链模式并不指定责任链的拓扑结构
3. 责任链要求在同一个时间里，命令只可以被传给一个下家或被处理掉，而不可以同时传个多个下家



- 设计步骤：
1. 设计一个信息产生事件的对象
2. 定义一个公共基类及公共方法，作为事件输入的接口
3. 定义不同的对象，不同的对象可以处理特定事件端，
4. 将其中一个对象作为链的初始，其他依次连接
