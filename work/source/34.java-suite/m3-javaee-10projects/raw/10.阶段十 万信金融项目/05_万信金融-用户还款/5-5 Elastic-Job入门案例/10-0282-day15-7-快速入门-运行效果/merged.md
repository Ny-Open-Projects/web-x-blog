# day15-7-快速入门-运行效果

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-5 Elastic-Job入门案例
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-5 Elastic-Job入门案例\day15-7-快速入门-运行效果_【海量资源尽在 666java.com】.mp4
- 时长 6分46秒（音频 407s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 截止到目前呢我们已经把elastic job分布式任务调度的入门案例呢全部搞定了那咱接下来就要测试一下看看这个运行效果那么这里边首先大家要注意的啊前面呢咱在编码过程当中大家也知道我们设置的这个分片数量是多少啊三啊大家看一下这儿是不是那理论上我应该启动几个微幅啊对三个微幅
[00:32] 就是因为这个分辨数量是三嘛对不对也就意味着我需要分给三台服务器去完成这个任务所以我需要启动三个微服大家看一下这儿呢你需要这个再增加两个微服我这儿都已经配过了大家看一下57082对吧这个是什么呀57083本身我们配的那个端口是57081吧对吧81 82和什么呀83你需要在这儿
[01:05] 给多出来的这两个微服务再配置一下什么呀端口号就行了你看默认是不是57081嘛对不对所以你看我一会儿呢是不是要把这三个微服务全都干什么呀启动这就是三片嘛那么另外呢你还要注意啊我们要想看到这个效果我得先把什么启动起来这是什么呀对Zookeeper这个咱以前说过ElasticJob内部是要使用这个什么呀
[01:34] 对zookeyper所以说你看我这zookeyper呢也已经启动了那咱接下来就可以把这三个微幅都给它干什么呀启动起来好这是启动了一个了然后再启动一个这是第二个对吧然后再启动一个好这是第三个你看这是不是一个两个三个对不对你看第一个是不是已经开始工作了对不对你看一开始的话大家注意啊一开始的话还是这样子的你启动一个微幅啊它就往zookeyper进行什么呀
[02:18] 注册一注册他就开始干什么呀干活那么第一台服务器干活的时候有可能后边这两台还没有进行什么注册所以一开始呢你看他可能是不是这些活都干了你看有分片二的有分片零的有分片什么呀一的对不对这个是由elastic job他会进行协调那慢慢慢慢后来呢这台服务器包括这台服务器是不是全都启动起来现在是不是一共有三台服务器那有了三台服务器之后呢这个就该进行什么呀
[02:47] 平均分配啊是不是你看咱这个表里边一共是六条数据三台服务器应该每台服务器是不是应该是两条嘛是不是这个咱以前是在写那条思考语句的时候是不是分析过对不对那么这个呢也是靠他自己进行协调那咱让他运行一段时间之后呢咱看看最终的这个效果是不是平均分配啊你先看第一台服务器我们往下看啊你看是不是只剩作业分片0了是不是然后你看他查出来是不是3636ID
[03:17] 是不是363636两条数据对吧你再看第二台这个服务器上它就是作业分片1你看它查出来数据是什么呀14141414对不对最后一台服务器你看它的作业分片是2它查出来数据是25252525大家看看有没有进行平均分配有吧是不是三台服务器共同完成了一个定时任务然后呢这个任务没有重复的执行而且进行了平均的一个什么呀分配
[03:46] 那咱这就是咱们想要的这个什么最终的一个效果对不对那有的学生会说呢老师万一有一台服务器挂了呢是不是现在他们三个都好好的那就各干各的活对不对那万一其中一条万一其中一个服务器挂了怎么办是不是那咱试试他会怎么办啊你看我把最后一台服务器给他停掉故意的啊给他停了现在就剩两台服务器了但是我分片的这个数量还是几个呀
[04:19] 三个是不是但是我就两台服务器一会不够用是不是那不够用的话这个elastic job它会怎么着呢是不是有两条数据这这个我就不管它了是不是那我服务器不够用嘛那我们接下来看会怎么着那这时候你会发现它这个暂停了对不对你看没反应两边都没反应不动了不动了啊为啥不动呢这跟zookip有关系那么之前呢我们其实给大家说过这个elastic job内部是不是会
[04:48] 用到Zookeeper利用他的选举机制对不对那这时候呢你在启动服务器的时候或者说呢有一台服务器这个当机了对吧在这个过程当中呢Zookeeper会进行这个什么呀选举那么在选举过程当中所有的这个任务都会进行阻塞这咱之前在哪提到过一次呀你看这如果谁谁下线了对吧他会重新进行选举选举出下个leader之前所有的任务会被什么呀阻塞当然这个时间不会太长啊
[05:20] 但是的确是有这么一个过程的嗯然后咱接下来看他们应该又有动静了有变化吗哎你看有动静了是不是你看这个时候你看呃第一台服务器他可不是就两条数据的他应该是四条对不对你看是不是3625是不是3625你看3625那这边呢他仍然还是什么呀1414对不对那两台服务器加起来是不是还是查了几条数据六条数据对不对
[05:48] 所以说呢你即使有服务器这个某台服务器当机了你不用担心这个任务呢他还会进行这个什么重新的一个分配了包括我接下来把这台服务器如果关了你会发现那六条数据全都被这台服务器进行什么呀查询这个你下去可以自己测试呃这是咱把这个什么呀咱们elastic job这个入门案例吧整体给大家做了一个这个
[06:14] 测试这里边大家一定要注意啊第一个呢就是这个分片的数量是三那你尽量要启动相同数量的这个什么呀微幅啊搞成一个分布式架构嘛这个大家一定要注意第二个呢就是它内部用到了什么呀Zookeeper这个注册需要花时间那么选举对吧它也需要花一定的时间所以说你在测试过程当中中间有时候它会对吧停顿对吧这也是很正常的那咱这个入门案例的这个测试吧咱就说到这儿

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Elastic-Job 分片任务的运行效果，通过修改配置文件中的分片数量，观察三个微服务实例如何平均分片执行数据库查询任务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“2.3 运行效果”，说明配置文件中分片数量为3，启动三个微服务实例，每5秒执行一次数据库查询并进行分片（平均分片）。
画面2：在 IDEA 中配置运行参数，设置 Main class 为 com.ithema.elasticjob.SchedulingBootstrap，Environment 为 local，Working directory 为项目路径，Active profiles 为 local，点击 OK。
画面3：终端窗口显示 Zookeeper 会话连接和断开日志，以及作业分片0的执行结果：User(id=3, userName=wangwu, password=123, name=王五, age=28)。
画面4：IDEA 中显示 application.properties 配置文件内容，包含数据库连接、日志级别、MyBatis 映射文件路径、Zookeeper 地址、命名空间和分片数量等配置。
画面5：IDEA 中调试窗口显示 Quartz Scheduler 初始化日志，以及作业分片0的执行结果。
画面6：IDEA 中 Console 窗口显示作业分片0、1、2的执行结果，分别对应不同的用户数据。
画面7：IDEA 中 Console 窗口显示作业分片0、1、2的执行结果，分别对应不同的用户数据。
画面8：Navicat for MySQL 窗口显示用户表数据，执行 SQL 查询语句：SELECT * FROM `t_user` WHERE MOD(id,3) = 1，结果为 id=1,3,6 的用户记录。
画面9：IDEA 中 Console 窗口显示作业分片0、1、2的执行结果，分别对应不同的用户数据。
画面10：IDEA 中 Console 窗口显示作业分片0、1、2的执行结果，分别对应不同的用户数据。
画面11：IDEA 中 application.properties 配置文件内容，显示 myjob.count=3，myjob.cron=0/5 * * * * ?。
画面12：IDEA 中 application.properties 配置文件内容，显示 myjob.count=3，myjob.cron=0/5 * * * * ?。
画面13：IDEA 中 Console 窗口显示作业分片0、1、2的执行结果，分别对应不同的用户数据。
画面14：展示 PPT 页面“2.3 运行效果”，说明配置文件中分片数量为3，启动三个微服务实例，每5秒执行一次数据库查询并进行分片（平均分片）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
server.port=${PORT:57081}
spring.application.name = elastic-job-Spring Boot
logging.level.root = info

spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/mp?useUnicode=true&characterEncoding=utf8&autoReconnect=true
spring.datasource.username=root
spring.datasource.password=123

# 设置Mapper接口所对应的XML文件位置
mybatis-plus.Mapper-locations = classpath*:dao/*.xml
# 设置分页插件的包扫描路径
mybatis-plus.type-aliases-package = com.ithema.elasticjob.pojo

# ZooKeeper服务地址
ZooKeeper.connectString = localhost:2181
# 命名空间
myjob.namespace = elastic-job-example
# 分片总数
myjob.count = 3
# cron表达式(定时策略)
myjob.cron = 0/5 * * * * ?

画面5：
Using Thread pool 'org.quartz.simpl.SimpleThreadPool' - with 1 threads.
Using job-store 'org.quartz.simpl.RAMJobStore' - which does not support persistence, and is not clustered.

画面6：
作业分片:0--User(id=3, userName=wangwu, password=123, name=王五, age=28)
作业分片:1--User(id=4, userName=zhangsan, password=123, name=张三, age=18)
作业分片:2--User(id=5, userName=zhaolu, password=123, name=赵六, age=21)
作业分片:0--User(id=3, userName=wangwu, password=123, name=王五, age=28)
作业分片:1--User(id=4, userName=zhangsan, password=123, name=张三, age=18)
作业分片:2--User(id=5, userName=zhaolu, password=123, name=赵六, age=21)
作业分片:0--User(id=3, userName=wangwu, password=123, name=王五, age=28)
作业分片:1--User(id=4, userName=zhangsan, password=123, name=张三, age=18)
作业分片:2--User(id=5, userName=zhaolu, password=123, name=赵六, age=21)
作业分片:0--User(id=3, userName=wangwu, password=123, name=王五, age=28)
作业分片:1--User(id=4, userName=zhangsan, password=123, name=张三, age=18)
作业分片:2--User(id=5, userName=zhaolu, password=123, name=赵六, age=21)

画面8：
SELECT * FROM `t_user` WHERE MOD(id,3) = 1

画面11：
# ZooKeeper服务地址
ZooKeeper.connectString = localhost:2181
# 命名空间
myjob.namespace = elastic-job-example
# 分片总数
myjob.count = 3
# cron表达式(定时策略)
myjob.cron = 0/5 * * * * ?

画面12：
# ZooKeeper服务地址
ZooKeeper.connectString = localhost:2181
# 命名空间
myjob.namespace = elastic-job-example
# 分片总数
myjob.count = 3
# cron表达式(定时策略)
myjob.cron = 0/5 * * * * ?

画面13：
作业分片:0--User(id=3, userName=wangwu, password=123, name=王五, age=28)
作业分片:1--User(id=4, userName=zhangsan, password=123, name=张三, age=18)
作业分片:2--User(id=5, userName=zhaolu, password=123, name=赵六, age=21)
作业分片:0--User(id=3, userName=wangwu, password=123, name=王五, age=28)
作业分片:1--User(id=4, userName=zhangsan, password=123, name=张三, age=18)
作业分片:2--User(id=5, userName=zhaolu, password=123, name=赵六, age=21)
作业分片:0--User(id=3, userName=wangwu, password=123, name=王五, age=28)
作业分片:1--User(id=4, userName=zhangsan, password=123, name=张三, age=18)
作业分片:2--User(id=5, userName=zhaolu, password=123, name=赵六, age=21)
作业分片:0--User(id=3, userName=wangwu, password=123, name=王五, age=28)
作业分片:1--User(id=4, userName=zhangsan, password=123, name=张三, age=18)
作业分片:2--User(id=5, userName=zhaolu, password=123, name=赵六, age=21)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题“2.3 运行效果”，内容说明：由于在配置文件中设置的分片数量为3，所以这里启动了三个微服务，启动过程中会花费一些时间向 ZooKeeper 进行注册。运行起来后，我们会发现三个服务微服务每5秒钟执行一次数据库查询，并且进行了分片（平均分片）。
画面14：PPT 标题“2.3 运行效果”，内容说明：由于在配置文件中设置的分片数量为3，所以这里启动了三个微服务，启动过程中会花费一些时间向 ZooKeeper 进行注册。运行起来后，我们会发现三个服务微服务每5秒钟执行一次数据库查询，并且进行了分片（平均分片）。
画面8：Navicat for

