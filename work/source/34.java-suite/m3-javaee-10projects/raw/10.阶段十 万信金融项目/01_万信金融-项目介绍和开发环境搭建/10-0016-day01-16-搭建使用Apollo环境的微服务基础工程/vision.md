# 画面线理解：day01-16-搭建使用Apollo环境的微服务基础工程

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-16-搭建使用Apollo环境的微服务基础工程_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:25, 03:25, 03:47, 05:22, 06:18, 06:52, 08:18, 09:24, 10:11, 10:45, 11:57, 13:54, 14:12, 15:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:10:00

1) 这一组画面整体在讲如何搭建和测试 Apollo 配置中心环境，包括数据库初始化、服务启动、配置管理界面操作及项目代码配置。

2) 按时间顺序列出每张画面的要点：
画面1：展示“资料”文件夹下的“p2p_apollo环境”目录，包含多个文件，如 p2p_apollo.sql、p2p_apollo.bat 等。
画面2：进入“p2p_apollo环境”目录，选中并高亮显示“runApollo.bat”文件。
画面3：在命令行窗口中执行“runApollo.bat”，显示 Apollo 服务启动日志。
画面4：浏览器访问 http://localhost:8070/config.html?appid=common-template，页面为空白。
画面5：浏览器访问 http://localhost:8070/config.html?appid=consumer-service，页面为空白。
画面6：浏览器访问 http://localhost:8070/config.html?appid=consumer-service，页面显示 Apollo 配置管理界面，包含多个配置项。
画面7：IntelliJ IDEA 加载项目，显示“Preparing workspace...”进度条。
画面8：IntelliJ IDEA 中打开“application.yml”文件，显示配置内容。
画面9：浏览器访问 Apollo 配置中心，显示“DEV”环境下的多个配置项。
画面10：查看 PDF 文档，内容为“1.4 微服务基础工程(Apollo环境)”章节，包含环境搭建和测试步骤。
画面11：PDF 文档页面，内容与画面10相同。
画面12：IntelliJ IDEA 中“application.yml”文件，光标在“apollo”配置项上。
画面13：浏览器访问 http://localhost:8080/QRCodeDemo/index1.html，显示多个服务图标。
画面14：PDF 文档页面，内容与画面10相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面8 和 画面12 中的 YAML 配置：
app:
  id: consumer-service
apollo:
  bootstrap:
    enabled: true
    namespaces: application,micro_service.spring-boot-druid,micro_service.spring-boot-http
spring:
  application:
    name: consumer-service
logging:
  config: classpath:log4j2-dev.xml

画面2 中的文件名：
runApollo.bat

画面3 中的命令行日志：
# 无具体命令，仅显示日志信息。

画面1 中的文件名：
p2p_apollo.sql
p2p_apollo.bat
p2p_apollo环境

画面10 和 画面14 中的 PDF 文档内容：
1.4 微服务基础工程(Apollo环境)
1.4.1 Apollo环境搭建
1. 进入“资料\p2p_apollo环境”文件夹中，执行 p2p_apollo.sql (包含有基础工程的初始配置)
2. 用记事本打开 runApollo.bat，修改其中的 MySQL 密码
3. 双击 runApollo.bat，启动 Apollo，启动完毕后访问 http://localhost:8070

1.4.2 打开基础工程(Apollo环境)并测试
在“代码”文件夹中，有一个“wanningp2_apollo”项目，这是使用 Apollo 环境的微服务基础工程，直接右键使用 IDEA 打开即可，可以浏览一下这些基础工程与前面的变化。

4) PPT 标题、架构图/流程图的结构、表格数据：
画面10、11、14 中的 PDF 文档标题：
1.4 微服务基础工程(Apollo环境)
1.4.1 Apollo环境搭建
1.4.2 打开基础工程(Apollo环境)并测试

5) 无其他内容。
