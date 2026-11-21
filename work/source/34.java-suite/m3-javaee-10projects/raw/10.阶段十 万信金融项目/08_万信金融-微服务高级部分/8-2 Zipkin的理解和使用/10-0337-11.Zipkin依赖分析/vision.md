# 画面线理解：11.Zipkin依赖分析

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-2 Zipkin的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-2 Zipkin的理解和使用\11.Zipkin依赖分析_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:45, 01:59, 02:41, 05:22, 05:52, 06:20, 06:36, 07:01, 08:06, 08:24, 08:53, 09:08, 10:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:11:11

1) 这一组画面整体在讲什么（一句话）：
演示如何通过集成 Zipkin 与 Spring Cloud Sleuth 实现分布式服务链路追踪，并展示如何使用 zipkin-dependencies 工具进行依赖分析。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT目录结构，当前章节为“3.2 Sleuth & Zipkin集成”，子章节“3.2.1 案例简介”介绍项目改造目标：使用Eureka作为服务注册与发现中心，使用Feign实现服务间调用，并将日志上报至Zipkin服务端，最终使用Zipkin图形化展示链路追踪情况。
画面2：浏览器访问Zipkin服务的“/service”页面，显示服务名、Span名称、时间等筛选条件，当前显示0个服务。
画面3：浏览器访问Zipkin的“/dependency”页面，显示服务调用关系图，包含“sleuth-with-zipkin-service-a”和“sleuth-with-zipkin-service-b”两个服务节点，但无连接线。
画面4：浏览器页面中“sleuth-with-zipkin-service-a”与“sleuth-with-zipkin-service-b”之间出现一条连接线，表示服务调用关系。
画面5：Windows PowerShell窗口中执行命令启动Zipkin Server，命令为：java -jar zipkin-server-2.12.9-exec.jar，输出显示Zipkin Server已启动。
画面6：Windows PowerShell窗口中执行命令下载zipkin-dependencies-2.4.1.jar，命令为：java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-server-2.12.9-exec.jar，但提示无法访问jarfile。
画面7：Windows PowerShell窗口中执行命令启动zipkin-dependencies，命令为：java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-dependencies-2.4.1.jar，输出显示Zipkin Server已启动。
画面8：浏览器访问Zipkin的根路径，显示“Zipkin Investigate system behavior”。
画面9：浏览器地址栏显示访问Zipkin的“/dependency”页面，参数包含startTs和endTs。
画面10：展示课程PPT内容，介绍当日志存储到ES后，依赖分析功能无法使用，需要通过zipkin-dependencies解决，命令为：java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-dependencies-2.4.1.jar。
画面11：Windows PowerShell窗口中执行命令启动zipkin-dependencies，命令为：java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-dependencies-2.4.1.jar，输出显示Zipkin Server已启动。
画面12：浏览器访问Zipkin的“/dependency”页面，点击“Analyze Dependencies”按钮。
画面13：浏览器页面显示服务调用关系图，包含“sleuth-with-zipkin-service-a”和“sleuth-with-zipkin-service-b”两个服务节点，但无连接线。
画面14：展示课程PPT内容，介绍zipkin-dependencies命令：java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-dependencies-2.4.1.jar。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面10、画面14：
java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-dependencies-2.4.1.jar

画面6：
java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-server-2.12.9-exec.jar

画面5：
java -jar zipkin-server-2.12.9-exec.jar

画面11：
java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-dependencies-2.4.1.jar

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“3.2 Sleuth & Zipkin集成”，子标题“3.2.1 案例简介”，内容描述项目改造目标。
画面10：PPT标题“4. 万信金融P2P项目集成服务链路追踪”，内容描述当日志存储到ES后，依赖分析功能无法使用，需要通过zipkin-dependencies解决，命令为：java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-dependencies-2.4.1.jar。
画面14：PPT标题“4. 万信金融P2P项目集成服务链路追踪”，内容描述zipkin-dependencies命令：java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-dependencies-2.4.1.jar。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
