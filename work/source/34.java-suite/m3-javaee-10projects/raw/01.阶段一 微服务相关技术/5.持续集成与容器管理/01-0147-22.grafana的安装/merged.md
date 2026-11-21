# 22.grafana的安装

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\22.grafana的安装_【海量资源尽在 ubkz.com】.mp4
- 时长 4分5秒（音频 246s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢我们已经完成了这么几步啊就是完成了一个时间序列库的一个安装以及我们的C-Advancer这个监控工具的安装而监控工具啊它主要是把监控出来的数据去插入到我们的InfluxDB之中但是InfluxDB这种数据呢我们查看起来并不是很方便对吧因为它都是一些零散的数据我们更希望是能够看到一个直观一些的数据比如说
[00:31] 我现在展示一个图表而这个图表呢就可以把每一个节点的一些数据给它穿起来比如说形成一个折线图曲线图类似于这样的一个报表这样一来看起来会更加的直观那么怎么样才能做呢这个时候这个就是由Graphana这个软件来实现了Graphana实际上是什么呢就是一个可视画面板也就是它可以去从什么呢
[01:01] 从influxdb等这些数据库作为数据源来展现一些图表就这么一个工具这个graphna也是比较常用的一个运维的一个工具那么首先来我们现在要做的就是一个graphna的一个安装安装这里需要下载一个叫镜像这个镜像就叫graphna-graphna在下载完镜像之后咱们现在需要去创建一个容器创建容器的话我们就是用宇居来创建就行了
[01:34] 这个语句呢其实指定了什么呢这里又指定了一些这个环境面量比如说这个influencedDB的这个host就是指定的这个容器的名称还有呢就是指定它的这个端口还有指定这个influenced数据库的名称等等就是还有数据库的用户名密码这样一来呢我们说它才可以去连接我们的influencedDB连接influencedDB
[02:03] 就这样一个这么一个软件我们在创建完成之后接下来要做的事就是要访问了因为我们在这里头创建语句是将3000端口映射为速度机的3001端口所以说我们现在可以通过3001去访问一下软件192.168.184.1443001好现在就已经进入了 graphnet 的一个登录界面
[02:37] 我们现在可以通过他的用户名称密码来登录叫admin默认是admin出示的密码是admin然后点登录登录之后他让你去修改一个密码去修改admin的密码这时候你可以选123456123456好save现在我们就已经进入到了我们Granfano的一个主界面了
[03:10] 那么主界面这里的呢,左侧呢,它有一个菜单,左侧有菜单,那么这些菜单呢,分别是什么意思呢?
[03:19] 第一个加号表示主要创建,我要创建什么东西,第二个呢,是一个什么呢?
[03:26] 第二个代表的是一个仪表盘,就是仪表盘的一些管理,那么这个呢,其实是比较主要的一个功能,第三个呢,就是告警管理,就可以设置一个告警,
[03:40] 那么下面我会详细说那么下面那个部分呢就是一些设置啊或者是一些配置可以配置一些数据库啊用户啊等等啊这些或者一些插件啊这些是它的一些主要的核心功能啊这就是我们说的gramfana的一个登录啊咱们就完成了那么接下来呢咱们就可以详细去讲解这个gramfana的一些常用操作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 安装并访问 Grafana，同时展示其与 InfluxDB 数据源的集成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了技术课程文档中关于 Grafana 安装的章节，包含下载镜像、创建容器和访问地址的命令。
画面 2: 同画面 1，鼠标光标在“选择语言”按钮上。
画面 3: 在 IDEA 中打开 `application.yml` 配置文件，显示了 Spring Boot 应用的数据库配置（MySQL）。
画面 4: 在 SecureCRT 中执行了 `Docker run` 命令，启动 Grafana 容器。
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
Docker pull grafana/grafana
(2) 创建容器
Docker run -d -p 3001:3000 -e INFLUXDB_HOST=192.168.184.144 -e INFLUXDB_PORT=8086 -e INFLUXDB_NAME=cadvisor -e INFLUXDB_USER=cadvisor -e INFLUXDB_PASS=cadvisor -link influxdb:influxdb -name grafana grafana/grafana
(3) 访问
http://192.168.184.144:3001

画面 4: Docker run -d -p 3001:3000 -e INFLUXDB_HOST=192.168.184.144 -e INFLUXDB_PORT=8086 -e INFLUXDB_NAME=cadvisor -e INFLUXDB_USER=cadvisor -e INFLUXDB_PASS=cadvisor -link influxdb:influxdb -name grafana grafana/grafana

画面 7: Docker run -d -p 3001:3000 -e INFLUXDB_HOST=192.168.184.144 -e INFLUXDB_PORT=8086 -e INFLUXDB_NAME=cadvisor -e INFLUXDB_USER=cadvisor -e INFLUXDB_PASS=cadvisor -link influxdb:influxdb -name grafana grafana/grafana

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“6.1 什么是Grafana”和“6.2 Grafana安装”，内容为文字描述。
画面 9: 浏览器中显示了多个仪表板的概览页面，包括“Dashboard (jenkins)”、“网站”、“influxDB - Admin int”、“Docker监控告警图”等。
画面 14: Grafana 主页，显示了“Home Dashboard”和“Add data source”等操作按钮。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

