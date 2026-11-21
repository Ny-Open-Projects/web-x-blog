# 画面线理解：10.Zipkin&Elasticsearch集成

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-2 Zipkin的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-2 Zipkin的理解和使用\10.Zipkin&Elasticsearch集成_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:34, 00:49, 05:09, 05:33, 05:48, 06:24, 07:06, 07:17, 07:32, 08:02, 08:28, 08:53, 09:31, 10:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:10:32

1) 这一组画面整体在讲什么（一句话）：
演示如何将 Zipkin 与 Elasticsearch 集成，以实现监控数据的持久化存储。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档“3.3 Zipkin&Elasticsearch集成”章节，其中包含集成步骤：自行下载并启动 Elasticsearch 及 head 插件（注意：Elasticsearch 版本不要超过 6.0），并通过命令启动 Zipkin 服务端。命令为：java -DSTORAGE_TYPE=elasticsearch -D ES_HOSTS=http://localhost:9200 -jar zipkin-server-2.12.9-exec.jar。
画面 2: 同画面 1，内容无变化。
画面 3: PDF 文档中新增“3.3.2 集成测试”小节，内容包括：1. 再次通过浏览器访问 http://localhost:9021/service-a/service1；2. 在 Ees-head (http://localhost:9100/) 中观察到产生了如下索引。
画面 4: 展示 Windows 文件资源管理器，路径为“.../warenhp2p/资料/”，显示 Elasticsearch 5.6.16 的安装目录，其中包含多个 .bat 文件和 .zip 文件。
画面 5: 展示 Windows 桌面，桌面上有多个快捷方式图标，包括“project.p...”、“wandp2p”、“SpringCloud”、“elastic...”等，以及“黑马程序员”和“博学谷”的标志。
画面 6: 展示 Windows 文件资源管理器，路径为“.../warenhp2p/资料/”，显示多个文件，包括“zipkin-server-2.12.9-exec.jar”，并提示“在此处打开 PowerShell 窗口(S)”。
画面 7: 展示 Windows 文件资源管理器，路径为“.../elasticsearch-head”，显示“elasticsearch-head”文件夹的内容，包括 .gitignore、Dockerfile-alpine、package.json 等文件。
画面 8: 展示桌面，显示“zipkin-server-2.12.9-exec.jar”文件，同时在任务栏中有一个“Elasticsearch 5.6.16”的命令行窗口。
画面 9: 展示 PowerShell 窗口，显示启动 Zipkin 服务的命令行输出，包括版本信息、启动日志和配置参数。
画面 10: 展示 PDF 文档“3.3.2 集成测试”小节，内容包括：1. 再次通过浏览器访问 http://localhost:9021/service-a/service1；2. 在 Ees-head (http://localhost:9100/) 中观察到产生了如下索引。同时，浏览器窗口显示“Elasticsearch http://localhost:9200/”页面。
画面 11: 展示 IntelliJ IDEA 开发环境，打开项目“SleuthWithZipkinDemo”，显示“ServiceController.java”文件中的代码。
画面 12: 展示浏览器窗口，地址栏显示“localhost:9100”，页面为空白。
画面 13: 展示浏览器窗口，显示“Elasticsearch http://localhost:9200/”页面，其中包含一个表格，显示了多个 span 的数据，包括“id”、“name”、“parentid”、“timestamp”等字段。
画面 14: 展示 PDF 文档“3.3.1 集成步骤”和“3.3.2 集成测试”小节，内容与画面 1 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1: java -DSTORAGE_TYPE=elasticsearch -D ES_HOSTS=http://localhost:9200 -jar zipkin-server-2.12.9-exec.jar
画面 3: http://localhost:9021/service-a/service1
画面 9: java -DSTORAGE_TYPE=elasticsearch -D ES_HOSTS=http://localhost:9200 -jar zipkin-server-2.12.9-exec.jar
画面 11: public String service() {
String service=serviceAgent.service();
//System.out.println(1/0);
return "service-b-service" + "===" + service;
}
画面 13: 表格数据：
| id | name | parentid | timestamp |
|----|------|----------|-----------|
| 35aec22138/beb51 | sleuth-with-zipkin-service-b | 5990290058a0b51 | 1573138206281 |
| 5680330b5a014 | sleuth-with-zipkin-service-a | 71ab753245aa1194 | 1573138205541 |
| 5090290058a0b51 | sleuth-with-zipkin-service-b | 71ab753245aa1194 | 1573138205706 |

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“3.3 Zipkin&Elasticsearch集成”，内容包括“Zipkin默认是将监控数据存储在内存的，如果Zipkin服务挂掉或重启的话，那么监控数据就会丢失。如果想要搭建生产环境下可用的Zipkin，就需要实现监控数据的持久化。前面提到过，Zipkin提供了可插拔数据存储方式，如In-Memory、MySQL、Cassandra以及Elasticsearch。接下来演示如何使用Elasticsearch作为Zipkin的持久化方案。”
画面 3: PPT 标题为“3.3.2 集成测试”，内容包括“1. 再次通过浏览器访问 http://localhost:9021/service-a/service1；2. 在 Ees-head (http://localhost:9100/) 中观察到产生了如下索引。”
画面 13: 表格数据如上所述。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
