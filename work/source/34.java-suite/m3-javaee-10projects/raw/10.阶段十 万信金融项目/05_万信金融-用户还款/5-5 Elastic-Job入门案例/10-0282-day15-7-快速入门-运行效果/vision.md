# 画面线理解：day15-7-快速入门-运行效果

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-5 Elastic-Job入门案例
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-5 Elastic-Job入门案例\day15-7-快速入门-运行效果_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:22, 01:09, 01:30, 01:39, 01:59, 02:08, 02:26, 02:50, 03:27, 04:37, 05:24, 05:41, 06:05, 06:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:34:00

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
spring.application.name = elastic-job-springboot
logging.level.root = info

spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/mp?useUnicode=true&characterEncoding=utf8&autoReconnect=true
spring.datasource.username=root
spring.datasource.password=123

# 设置Mapper接口所对应的XML文件位置
mybatis-plus.mapper-locations = classpath*:dao/*.xml
# 设置分页插件的包扫描路径
mybatis-plus.type-aliases-package = com.ithema.elasticjob.pojo

# zookeeper服务地址
zookeeper.connectString = localhost:2181
# 命名空间
myjob.namespace = elastic-job-example
# 分片总数
myjob.count = 3
# cron表达式(定时策略)
myjob.cron = 0/5 * * * * ?

画面5：
Using thread pool 'org.quartz.simpl.SimpleThreadPool' - with 1 threads.
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
# zookeeper服务地址
zookeeper.connectString = localhost:2181
# 命名空间
myjob.namespace = elastic-job-example
# 分片总数
myjob.count = 3
# cron表达式(定时策略)
myjob.cron = 0/5 * * * * ?

画面12：
# zookeeper服务地址
zookeeper.connectString = localhost:2181
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
画面1：PPT 标题“2.3 运行效果”，内容说明：由于在配置文件中设置的分片数量为3，所以这里启动了三个微服务，启动过程中会花费一些时间向 zookeeper 进行注册。运行起来后，我们会发现三个服务微服务每5秒钟执行一次数据库查询，并且进行了分片（平均分片）。
画面14：PPT 标题“2.3 运行效果”，内容说明：由于在配置文件中设置的分片数量为3，所以这里启动了三个微服务，启动过程中会花费一些时间向 zookeeper 进行注册。运行起来后，我们会发现三个服务微服务每5秒钟执行一次数据库查询，并且进行了分片（平均分片）。
画面8：Navicat for
