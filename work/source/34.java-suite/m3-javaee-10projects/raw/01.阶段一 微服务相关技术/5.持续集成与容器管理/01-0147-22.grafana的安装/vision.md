# 画面线理解：22.grafana的安装

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\22.grafana的安装_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:18, 01:28, 01:31, 01:33, 02:04, 02:09, 02:13, 02:18, 02:21, 02:30, 02:35, 02:37, 02:48, 03:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:27:06

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 安装并访问 Grafana，同时展示其与 InfluxDB 数据源的集成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了技术课程文档中关于 Grafana 安装的章节，包含下载镜像、创建容器和访问地址的命令。
画面 2: 同画面 1，鼠标光标在“选择语言”按钮上。
画面 3: 在 IDEA 中打开 `application.yml` 配置文件，显示了 Spring Boot 应用的数据库配置（MySQL）。
画面 4: 在 SecureCRT 中执行了 `docker run` 命令，启动 Grafana 容器。
画面 5: SecureCRT 中显示了 Docker 容器列表，确认 Grafana 容器已运行。
画面 6: 同画面 1，显示了 Grafana 安装文档。
画面 7: SecureCRT 中再次显示了启动 Grafana 容器的命令。
画面 8: 在浏览器中访问 InfluxDB 的 Admin 界面，显示了数据库和测量值列表。
画面 9: 浏览器中显示了多个仪表板的概览页面，包括 Jenkins、Rancher、InfluxDB 等。
画面 10: 浏览器中显示了 Grafana 的登录页面，弹出“要翻译此页面吗？”的提示框。
画面 11: Grafana 登录页面，用户名下拉框显示了预设用户名。
画面 12: Grafana 登录页面，已输入用户名 "admin" 和密码。
画面 13: Grafana 登录页面，点击“Log In”按钮后成功登录，页面顶部显示“Logged in”。
画面 14: Grafana 主页，显示了“Home Dashboard”和“Add data source”等操作按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3: application.yml
server:
  port: 9001
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://192.168.184.144:3306/tensquare_base?characterEncoding=utf-8
    username: root
    password: 123456
    jpa:
      show-sql: true
      database: mysql

画面 1: (1) 下载镜像
docker pull grafana/grafana
(2) 创建容器
docker run -d -p 3001:3000 -e INFLUXDB_HOST=192.168.184.144 -e INFLUXDB_PORT=8086 -e INFLUXDB_NAME=cadvisor -e INFLUXDB_USER=cadvisor -e INFLUXDB_PASS=cadvisor -link influxdb:influxdb -name grafana grafana/grafana
(3) 访问
http://192.168.184.144:3001

画面 4: docker run -d -p 3001:3000 -e INFLUXDB_HOST=192.168.184.144 -e INFLUXDB_PORT=8086 -e INFLUXDB_NAME=cadvisor -e INFLUXDB_USER=cadvisor -e INFLUXDB_PASS=cadvisor -link influxdb:influxdb -name grafana grafana/grafana

画面 7: docker run -d -p 3001:3000 -e INFLUXDB_HOST=192.168.184.144 -e INFLUXDB_PORT=8086 -e INFLUXDB_NAME=cadvisor -e INFLUXDB_USER=cadvisor -e INFLUXDB_PASS=cadvisor -link influxdb:influxdb -name grafana grafana/grafana

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“6.1 什么是Grafana”和“6.2 Grafana安装”，内容为文字描述。
画面 9: 浏览器中显示了多个仪表板的概览页面，包括“Dashboard (jenkins)”、“网站”、“influxDB - Admin int”、“Docker监控告警图”等。
画面 14: Grafana 主页，显示了“Home Dashboard”和“Add data source”等操作按钮。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
