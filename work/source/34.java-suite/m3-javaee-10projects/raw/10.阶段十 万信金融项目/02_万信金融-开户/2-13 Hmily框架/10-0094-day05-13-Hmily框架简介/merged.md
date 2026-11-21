# day05-13-Hmily框架简介

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-13-Hmily框架简介_【海量资源尽在 666java.com】.mp4
- 时长 3分45秒（音频 226s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 了解了TCC这个分布式事物解决方案之后呢我们接下来就要具体学习框架TCC框架我们前面不是提到了吗先是学习理论然后产生解决方案最终我们在开发过程当中使用的还是什么呀对框架那么在目前行业当中呢基于TCC这个解决方案产生的框架也好几种大概你看我们挑出来四种
[00:28] 这个后边是他在github上的地址这个我们就不再打开一个一看了啊我们这呢呃采用的是其中一个框架叫hemily这个单词什么意思呢这个他不是一个具体的一个单词这个一开始呢我也比较好奇我说这个单词什么意思呢查一下没查到那我查到这么一个东西啊在网上hemily什么意思呢是好错了啊hmi
[01:04] 是吧how much I love you这个首字母就是HMILY对吧网上查了这么一个东西那么它呢是一个高性能的分布式事物这个框架哪种方案呢TCC方案那么为什么选择它呢你看它有一些特性或者一些优点什么一支持续到GDK1.8对不对然后呢你看这个性能非常好
[01:36] 支持什么呀SpinBoot使用更简单支持各种这个RPC框架支持各种各样的数据库比如说谁呀对MySQLRedis都支持Zookeeper MongoDB支持各种这个日志的序列化技术内部也采用了什么呀AOP的思想跟Spin无缝结成天然知识集群还有一些什么事物恢复等等等等一些功能一些特性而且它性能呢也非常非常好这些呢大家整体了解一下就行
[02:06] 那下面这一块呢介绍里边我要重点给大家说这个这句话非常非常重要就说他说啊你在使用Harmony这个框架的时候呢你不需要单独再来一个什么什么事务协调服务不需要你看我们前面在讲这个TC的时候我们说了这里边有一个东西非常非常重要就是全局事务发起方或者协调管理就这个东西非常重要呃TC这个实验Harmony不是说不需要
[02:36] 他的意思是说你不需要单独因为这个在搞一个什么呀服务这是没有必要哈玛里这个框架本身就充当这个什么呀全局事务发行方或者他本身就充当这个什么呀事务管理协调监控你不需要单独在因为这个搞一个服务但是呢为了实现这个监控啊协调啊管理他需要你额外提供一个数据库一张表来存储一些什么呀日志
[03:03] 因为Harmony它内部在进行事务这个监控管理协调的时候它主要靠一个什么呀靠日志它的很多操作很多操作全部是存储在什么呀日志里边这个对于Harmony来说是非常重要而它这个日志呢是要求你用数据库来进行存储就是你得来个数据库来张表这是Harmony里边最关键的一点那么一会儿呢咱们在学习Harmony具体怎么使用的时候这里边就涉及到这个日志
[03:33] 涉及到一个库一个表这需要给大家提一下了这是它内部需要用到的一个东西这是整体我们对Harmony这个框架整体做了一个了解

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
介绍 TCC 框架的核心概念、常见实现方案及其在分布式事务中的作用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 PPT 页面标题为“3.2 TCC框架”。
- 页面内容包含：TCC 事务的定义（一手交钱，一手交货）、BASE理论、一致性（强一致性、最终一致性）、软状态、理论（解决方案—框架）、TCC（全局事务发起方 三个操作 两个阶段）。
- 画面中显示一个记事本窗口，内容为“转账：我要给班长转1万，拆分成若干个小事，我的账户扣1万，班长的账户加1万”、“交易：一手交钱，一手交货”、“分布式事务独有的名词：网络分区”、“BASE理论：是对CAP理论中的AP的补充”、“一致性：任何系统其实都要求数据一致性”、“强一致性”、“最终一致性”、“软状态：转账中... 退款中...”、“理论---解决方案---框架”、“TCC：全局事务发起方 三个操作 两个阶段”。

画面 2：
- PPT 页面标题为“3.2 TCC框架”。
- 页面内容包含一个表格，列标题为“框架名称”和“Github地址”。
- 表格内容：
  - 框架名称：tcc-transaction，Github地址：https://github.com/changmings/tcc-transaction
  - 框架名称：Hmily，Github地址：https://github.com/ya199195/hmily
  - 框架名称：ByteTCC，Github地址：https://github.com/liuyangeng/ByteTCC
  - 框架名称：EasyTransaction，Github地址：https://github.com/DNR-GROUP/EasyTransaction

画面 3：
- PPT 页面内容与画面 2 相同，为“3.2 TCC框架”下的框架列表表格。
- 画面中鼠标光标位于“Hmily”行的“Github地址”列。

画面 4：
- PPT 页面标题为“3.2 TCC框架”。
- 页面内容包含：TCC 事务的定义（一手交钱，一手交货）、BASE理论、一致性（强一致性、最终一致性）、软状态、理论（解决方案—框架）、TCC（全局事务发起方 三个操作 两个阶段）。
- 画面中显示一个记事本窗口，内容为“转账：我要给班长转1万，拆分成若干个小事，我的账户扣1万，班长的账户加1万”、“交易：一手交钱，一手交货”、“分布式事务独有的名词：网络分区”、“BASE理论：是对CAP理论中的AP的补充”、“一致性：任何系统其实都要求数据一致性”、“强一致性”、“最终一致性”、“软状态：转账中... 退款中...”、“理论---解决方案---框架”、“TCC：全局事务发起方 三个操作 两个阶段”。
- 记事本窗口中新增一行文字：“hmily: how much i love you”。

画面 5：
- PPT 页面标题为“3.2 TCC框架”。
- 页面内容包含：TCC 事务的定义（一手交钱，一手交货）、BASE理论、一致性（强一致性、最终一致性）、软状态、理论（解决方案—框架）、TCC（全局事务发起方 三个操作 两个阶段）。
- 画面中显示一个记事本窗口，内容为“转账：我要给班长转1万，拆分成若干个小事，我的账户扣1万，班长的账户加1万”、“交易：一手交钱，一手交货”、“分布式事务独有的名词：网络分区”、“BASE理论：是对CAP理论中的AP的补充”、“一致性：任何系统其实都要求数据一致性”、“强一致性”、“最终一致性”、“软状态：转账中... 退款中...”、“理论---解决方案---框架”、“TCC：全局事务发起方 三个操作 两个阶段”。
- 记事本窗口中新增一行文字：“hmily: how much i love you”。

画面 6：
- PPT 页面标题为“3.2 TCC框架”。
- 页面内容包含一个表格，列标题为“框架名称”和“Github地址”。
- 表格内容：
  - 框架名称：tcc-transaction，Github地址：https://github.com/changmings/tcc-transaction
  - 框架名称：Hmily，Github地址：https://github.com/ya199195/hmily
  - 框架名称：ByteTCC，Github地址：https://github.com/liuyangeng/ByteTCC
  - 框架名称：EasyTransaction，Github地址：https://github.com/DNR-GROUP/EasyTransaction

画面 7：
- PPT 页面标题为“3.2 TCC框架”。
- 页面内容包含一个表格，列标题为“框架名称”和“Github地址”。
- 表格内容：
  - 框架名称：tcc-transaction，Github地址：https://github.com/changmings/tcc-transaction
  - 框架名称：Hmily，Github地址：https://github.com/ya199195/hmily
  - 框架名称：ByteTCC，Github地址：https://github.com/liuyangeng/ByteTCC
  - 框架名称：EasyTransaction，Github地址：https://github.com/DNR-GROUP/EasyTransaction
- 页面下方文字内容：“Hmily是一个高性能分布式事务tcc开源框架，基于java语言开发（JDK 8），支持dubbo, Spring Cloud, motan 等rpc框架进行分布式事务。它目前支持以下特性：支持嵌套事务(Nested transaction support)、采用@Interruptor框架进行事务日志的异步写入，与RPC框架的性能无差别、支持Spring Boot starter 项目启动，使用简单、RPC框架支持：dubbo,motan,Spring Cloud、本地事务存储支持：redis,mongodb,ZooKeeper,file,mysql、事务日志异步化支持：java, hessian, kryo, protostuff、采用Aspect AOP 因而能够与Spring无缝集成，天然支持补偿、RPC事务重试，超时异常重试等。”

画面 8：
- PPT 页面标题为“3.2 TCC框架”。
- 页面内容包含一个表格，列标题为“框架名称”和“Github地址”。
- 表格内容：
  - 框架名称：tcc-transaction，Github地址：https://github.com/changmings/tcc-transaction
  - 框架名称：Hmily，Github地址：https://github.com/ya199195/hmily
  - 框架名称：ByteTCC，Github地址：https://github.com/liuyangeng/ByteTCC
  - 框架名称：EasyTransaction，Github地址：https://github.com/DNR-GROUP/EasyTransaction
- 页面下方文字内容：“Hmily是一个高性能分布式事务tcc开源框架，基于java语言开发（JDK 8），支持dubbo, Spring Cloud, motan 等rpc框架进行分布式事务。它目前支持以下特性：支持嵌套事务(Nested transaction support)、采用@Interruptor框架进行事务日志的异步写入，与RPC框架的性能无差别、支持Spring Boot starter 项目启动，使用简单、RPC框架支持：dubbo,motan,Spring Cloud、本地事务存储支持：redis,mongodb,ZooKeeper,file,mysql、事务日志异步化支持：java, hessian, kryo, protostuff、采用Aspect AOP 因而能够与Spring无缝集成，天然支持补偿、RPC事务重试，超时异常重试等。”

画面 9：
- PPT 页面标题为“3.2 TCC框架”。
- 页面内容包含一个流程图，展示 A 账户和 B 账户的 TCC 事务操作。
- 左侧框体（A账户）：
  - try：检查可用余额是否够30元，冻结金额30元，扣减可用余额30元
  - confirm：解冻金额30元
  - cancel：解冻金额30元，增加可用余额30元
- 右侧框体（B账户）：
  - try：检查账户状态
  - confirm：余额增加30元
  - cancel：空

画面 10：
- PPT 页面标题为“3.2 TCC框架”。
- 页面内容包含一个流程图，展示 A 账户和 B 账户的 TCC 事务操作。
- 左侧框体（A账户）：
  - try：检查可用余额是否够30元，冻结金额30元，扣减可用余额30元
  - confirm：解冻金额30元
  - cancel：解冻金额30元，增加可用余额30元
- 右侧框体（B账户）：
  - try：检查账户状态
  - confirm：余额增加30元
  - cancel：空
- 页面上方文字：“案例1：

