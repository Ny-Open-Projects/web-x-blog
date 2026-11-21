# 画面线理解：06-SpringBoot配置-配置文件分类

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\06-SpringBoot配置-配置文件分类_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 03:43, 04:44, 04:54, 05:19, 05:26, 05:33, 06:11, 06:22, 06:37, 07:07, 08:02, 09:28, 09:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 02:08:51

1) 这一组画面整体在讲什么（一句话）：
演示 Spring Boot 中配置文件的类型、内容、加载顺序及优先级。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示课程目录，包含“配置文件分类”、“yam1”、“读取配置文件内容”、“profile”、“内部配置加载顺序”、“外部配置加载顺序”等主题。
画面 2: IDE 中显示项目结构，`application.properties` 文件被打开，准备编辑。
画面 3: 在 `application.properties` 文件中，光标位于 `server.port=8080` 这一行，下方显示了 Spring Boot 的配置属性列表。
画面 4: 在 `application.properties` 文件中，光标位于 `server.port=` 后，准备输入新端口值。
画面 5: 浏览器打开 Spring Boot 官方文档首页。
画面 6: 浏览器访问 `localhost:8081/hello`，页面显示“hello Spring Boot 222!”，表明服务已启动并响应。
画面 7: IDE 中 `application.properties` 文件显示 `server.port=8081`，控制台日志显示 Tomcat 初始化并启动在端口 8081。
画面 8: IDE 中 `application.properties` 文件显示 `server.port=8081` 和 `name=abc`，控制台日志显示 Tomcat 启动在端口 8081。
画面 9: IDE 中 `application.yml` 文件被打开，光标位于 `port: ` 后，准备输入端口值。
画面 10: IDE 中 `application.properties` 文件显示 `server.port=8080` 和 `name=abc`，控制台日志显示 Tomcat 启动在端口 8080。
画面 11: IDE 中 `application.yml` 文件显示 `server: port: 8082`，准备保存。
画面 12: IDE 中 `application.yml` 文件显示 `server: port: 8082`，控制台日志显示 Tomcat 启动在端口 8082。
画面 13: IDE 中 `application.yml` 文件显示 `server: port: 8082`，控制台日志显示 Tomcat 启动在端口 8082。
画面 14: PPT 页面标题为“SpringBoot 配置”，小结内容为：
- SpringBoot提供了2种配置文件类型：properties和yaml
- 默认配置文件名称：application
- 在同一级目录下优先级为：properties > yml > yaml

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3: `server.port=8080`
画面 4: `server.port=`
画面 7: `server.port=8081`
画面 8: `server.port=8081`
画面 8: `name=abc`
画面 9: `server: port: `
画面 10: `server.port=8080`
画面 11: `server: port: 8082`
画面 12: `server: port: 8082`
画面 13: `server: port: 8082`
画面 14: `SpringBoot提供了2种配置文件类型：properties和yaml`
画面 14: `默认配置文件名称：application`
画面 14: `在同一级目录下优先级为：properties > yml > yaml`

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“目录”，内容为：
- 配置文件分类
- yam1
- 读取配置文件内容
- profile
- 内部配置加载顺序
- 外部配置加载顺序
画面 14: PPT 标题为“SpringBoot 配置”，小结内容为：
- SpringBoot提供了2种配置文件类型：properties和yaml
- 默认配置文件名称：application
- 在同一级目录下优先级为：properties > yml > yaml

5) 不要评价画面美观，不要输出与课程无关的内容。
（以上内容已按要求输出）
