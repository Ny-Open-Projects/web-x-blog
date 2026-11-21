# 2-MapReduce的构思和框架结构

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\2-MapReduce的构思和框架结构【海量资源尽在 ubkz.com】.mp4
- 时长 7分17秒（音频 437s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习MapReduce的一个设计构思和框架结构MapReduce是一个非常优秀的分布式计算框架它的核心功能其实是将我们用户自己编写的业务逻辑代码和它自带的一些组件可以完美的整合在一起并且把它运行在Hadoop集群上这里什么是用户自己编写的业务逻辑代码呢大家来看我刚才画的这张图
[00:29] 在这个图里边呢这里边有个加尔程序这个加尔程序的目的呢是对每一个block里边的这个数据进行一个单词统计那这个呢就是自己需要去编写的这就是所谓的自己编写的EUROG代码那它呢可以和我们myproduce自带的一些组件呢整合在一起OK那第二个的话呢myproduce作为一个计算框架那么计算数据肯定有输入和输出
[00:58] 也就是input和output这个待会呢咱们在编写myproduce代码的时候呢就会看到来接下来我们来看一下myproduce一个构思它只有两个方面第一个是分而治之也就是说分而治之呢就是把一个大的计算任务呢进行划分成小的计算任务但是注意这个把大的任务划分成小的任务有个前提这些小任务之间呢不能产生依赖关系什么意思呢
[01:27] 你比如说呢我刚才呢把一个大的单次统计呢化成小的单次统计这些之间呢不能有依赖关系它们之间可以并行的执行OK这是一个前提好那么还有呢这个统一一个架构隐藏细节这个怎么理解呢就是说我们呢要实现分布式计算如果说一些底层代码都需要我们写这是非常复杂的那myproduce呢它给我们统一个它给我们提供了一个统一的计算框架
[01:56] 我们不需要考虑那么多细节的东西只需要把我们该干的事干好那么一些细节的东西交给底交给这个框架那他就会给你处理所以说这里有句话他说呢MapReduce最大的亮点呢是通过抽象模型和计算框架把需要做什么与具体怎么做分开了我们呢只需要去告诉MapReduce我们要做什么而具体怎么做
[02:26] 不用管有MapReduce给你去实现那是不是就大大降低了我们编程的一个任务量OK这是它一个特点那接下来呢还有一个这个构建的一个抽象模型这个里边呢有一个Map一个Reduce这个我们刚才提过了这个MapReduce呢它里边呢在实现这个编程的时候呢用了一个函数式语言那这里边呢它有几点我们来看一下第一呢Map
[02:52] 是对一组数据呢进行某些重复式的一个处理你比如说我把一个大的计算任务划分之后呢划分成多个小任务那它分别对每个小任务呢进行重复的一个处理而Reduce呢对我们Map产生的中间结果呢进行汇总那这个刚才这个图呢就很明确的把这个思想给大家体现了好MapReduce呢还提供了一个东西就是说它给我们提供了一堆的接口
[03:22] 我们只需要去实现这个接口并且重写里边一些方法那就可以去进行MapReduce一个调用OKMapReduce一个处理的数据类型呢是什么呢是一个K-Value对也就是它在处理的时候呢会产生很多的K-Value对也就是建制对这个建制对呢你就可以理解成一个Map集合之类的你比如说呢在这个MapReduce计算的时候呢它给我们提供了两个阶段
[03:51] 一个是MAP阶段一个是REDUCE阶段在这两个阶段里边呢会产生三种简单的对你比如说在MAP阶段它是呢将K1和V1变成K2和V2这个K1和V1是什么K2和V2是什么大家不用关心马上咱们就会咱们就会看到OK那REDUCE阶段呢是将K2和V2变成K3和V3
[04:16] 也就是说MAP和REDUCE的计算你可以理解成其实就是建制对的一种转换我只要把K1和V1这种建制对变成了K3和V3这种建制对那相当于我们的处理任务就结束了那就可以这样理解OK那接下来咱们再看一下MAP和REDUCE的一个框架结构也要它的一个处理流程这个MAP和REDUCE它是基于样子集群的
[04:44] 所以说呢它的整个的计算任务呢都是在一二集群上这里有一个图我把这个图呢放大我放在我的画图里边呢我们来一起看一下首先呢这是一个处理的流程我们来看一下那这边呢是一个客户端当这个客户端呢向我们的这个客户端呢提出一个处理任务之后呢首先是resource managerresource manager也就是我们一二集群的主节点来接收这个任务
[05:12] 当他接收这个任务之后啊他就会启动一个进程叫Applications Manager那他来管理这个应用管理这个任务OK那么这个Application Manager呢就会在某一台机子上比如说这个台机子有个Node ManagerNode Manager是不是我们样子集群的一个重解链OK那么在这里面呢会启动一个程序可以启动一个一个程序叫什么呢叫MRAppMaster
[05:41] 也就是说MapReduce AppMaster他来管理这个任务那管理这个任务他主要干嘛呢他主要是向我们的Resource Manager申请资源申请资源OK申请什么资源呢比如说我们处理一个任务我们是不是需要内存呢需要我们的这个CPU啊那这个时候呢他就向我们的Resource Manager申请资源而在Resource Manager还有一个组件叫Resource Schedule那这个呢他会
[06:10] 把这个资源呢给下发给我们的APP masterAPP master拿到这个资源之后呢他就会把这个资源呢分派给各个node manager然后呢让他们去让他们去呢去启动这个去拿到这个资源调遣之后呢去具体的分配这个资源分配这个资源之后呢会在每一个node manager呢启动对应的map task然后呢或者说呢一些reduce taskOK
[06:39] 那么这个map task这个reduce task呢会产生一些结果那这些结果呢最后再汇总给App MasterApp Master呢又会把这个结果呢上报给Application Manager它是通过这样的一个套路呢去对我们的一个大数据呢进行计算OK这是它一个简单的一个计算流程OK咱们先有一个简单的认识等我们呢
[07:03] 把这个MapReduce整个的一个体系讲完之后呢你会对这个图呢有更深刻的理解OK关于MapReduce一个构思呢和它一个框架呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 MapReduce 的设计思想、框架结构及其核心组件（Map 和 Reduce）的工作原理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示文档标题“Hadoop Day 03”和目录结构，当前章节为“1.1. MapReduce 设计思想和框架结构”，并显示了“MapReduce 框架结构”PPT 的预览图。
画面 2: 文档内容聚焦于“MapReduce 是一个分布式运算程序的编程框架”，并解释其核心功能是将用户业务逻辑与默认组件整合。
画面 3: 文档内容继续阐述 MapReduce 的“分而治之”思想，包括“统一抽象，隐藏系统细节”和“抽象描述模型：Map和Reduce”。
画面 4: 文档内容进一步展开“抽象描述模型：Map和Reduce”，并列出 Map 和 Reduce 的功能描述。
画面 5: 文档内容继续展示“抽象描述模型：Map和Reduce”，并列出 Map 和 Reduce 的功能描述。
画面 6: 文档内容展示“MapReduce 框架结构”部分，列出“一个完整的 mapreduce 程序在分布式运行时有三类实例进程”。
画面 7: 文档内容展示“MapReduce 框架结构”部分，列出“一个完整的 mapreduce 程序在分布式运行时有三类实例进程”。
画面 8: 文档内容展示“MapReduce 框架结构”部分，列出“一个完整的 mapreduce 程序在分布式运行时有三类实例进程”。
画面 9: 文档内容展示“MapReduce 框架结构”部分，列出“一个完整的 mapreduce 程序在分布式运行时有三类实例进程”。
画面 10: 文档内容展示“MapReduce 框架结构”部分，列出“一个完整的 mapreduce 程序在分布式运行时有三类实例进程”，并显示了“MapReduce 框架结构”的架构图。
画面 11: 文档内容展示“MapReduce 框架结构”部分，列出“一个完整的 mapreduce 程序在分布式运行时有三类实例进程”，并显示了“MapReduce 框架结构”的架构图。
画面 12: 文档内容展示“MapReduce 框架结构”部分，列出“一个完整的 mapreduce 程序在分布式运行时有三类实例进程”，并显示了“MapReduce 框架结构”的架构图。
画面 13: 文档内容展示“MapReduce 框架结构”部分，列出“一个完整的 mapreduce 程序在分布式运行时有三类实例进程”，并显示了“MapReduce 框架结构”的架构图。
画面 14: 展示“MapReduce的计算架构”PPT，包含一个详细的架构图，图中包含 Client、ResourceManager、Node Manager、Container、Map Task、Reduce Task 等组件，并标注了各组件间的交互关系。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
PPT 标题：
- “MapReduce 设计思想和框架结构”
- “MapReduce 框架结构”

架构图/流程图结构：
画面 10-14 显示的架构图中包含以下组件和连接关系：
- Client → ResourceManager (Applications Manager, Resource Scheduler)
- Client → Node Manager (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task, Reduce Task)
- Container → Map Task
- Container → Reduce Task
- Node Manager → Container (Map Task, Reduce Task)
- ResourceManager → Node Manager (Applications Manager, Resource Scheduler)
- Node Manager → Container (Map Task,

