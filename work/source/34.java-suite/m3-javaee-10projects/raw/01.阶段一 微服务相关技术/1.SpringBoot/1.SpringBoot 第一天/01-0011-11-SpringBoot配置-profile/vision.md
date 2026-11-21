# 画面线理解：11-SpringBoot配置-profile

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\11-SpringBoot配置-profile_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 02:58, 04:50, 05:57, 07:31, 08:51, 10:01, 10:23, 12:08, 13:02, 14:08, 14:42, 15:32, 16:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 02:22:55

1) 这一组画面整体在讲什么（一句话）：
讲解 Spring Boot 中 profile（配置文件）机制，包括多文件配置方式和激活方式。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 页面，标题为“SpringBoot 配置”，子标题“profile”，内容介绍 profile 用于动态切换不同环境的配置。
画面 2: PPT 页面，列出 profile 配置方式（多 profile 文件方式、yml 多文档方式）和激活方式（配置文件、虚拟机参数、命令行参数）。
画面 3: IDE 中显示 Spring Boot 项目结构，包含多个 application.properties 文件，主类 SpringbootProfilesApplication。
画面 4: IDE 中打开 application-dev.properties 文件，内容为 server.port=8881。
画面 5: IDE 中右键点击 application.properties 文件，弹出菜单，选择“Run 'SpringbootProfilesApplication'”。
画面 6: IDE 中打开 application.yml 文件，内容为：
---
server:
  port: 8883
spring:
  profiles: dev
---
server:
  port: 8884
server:
  port: 8883
画面 7: IDE 中 application.yml 文件内容为：
---
server:
  port: 8883
spring:
  profiles: pro
---
server:
  port: 8884
spring:
  profiles:
    active: pro
画面 8: IDE 中 application.yml 文件内容为：
---
server:
  port: 8883
spring:
  profiles: dev
---
server:
  port: 8882
画面 9: IDE 中打开 Run/Debug Configurations，设置 VM options 为 -Dspring.profiles.active=dev。
画面 10: IDE 中 application.yml 文件内容为：
spring:
  profiles: test
server:
  port: 8881
---
spring:
  profiles: pro
---
spring:
  profiles:
    active: dev
画面 11: IDE 中打开 pom.xml 文件，显示项目依赖和插件配置。
画面 12: IDE 中打开 target 目录，右键点击 springboot-profiles-0.0.1-SNAPSHOT.jar。
画面 13: Windows PowerShell 中执行命令：java -jar springboot-profiles-0.0.1-SNAPSHOT.jar --spring.profiles.active=pro。
画面 14: PPT 页面，标题为“Profile-小结”，内容总结 profile 的作用、配置方式和激活方式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6:
---
server:
  port: 8883
spring:
  profiles: dev
---
server:
  port: 8884
server:
  port: 8883

画面 7:
---
server:
  port: 8883
spring:
  profiles: pro
---
server:
  port: 8884
spring:
  profiles:
    active: pro

画面 8:
---
server:
  port: 8883
spring:
  profiles: dev
---
server:
  port: 8882

画面 9:
VM options: -Dspring.profiles.active=dev

画面 10:
spring:
  profiles: test
server:
  port: 8881
---
spring:
  profiles: pro
---
spring:
  profiles:
    active: dev

画面 13:
java -jar springboot-profiles-0.0.1-SNAPSHOT.jar --spring.profiles.active=pro

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题“SpringBoot 配置”，子标题“profile”，正文内容。
画面 2: 标题“profile”，正文内容。
画面 14: 标题“Profile-小结”，内容：
1) profile 是用来完成不同环境下，配置动态切换功能的。
2) profile 配置方式：
   • 多 profile 文件方式：
      • application-dev.properties/yml 开发环境
      • application-test.properties/yml 测试环境
      • application-pro.properties/yml 生产环境
   • yml 多文档方式：
      • 在 yml 中使用 --- 分隔不同配置
3) profile 激活方式：
   • 配置文件：在配置文件中配置：spring.profiles.active=dev
   • 虚拟机参数：在 VM options 指定：-Dspring.profiles.active=dev
   • 命令行参数：java -jar xxx.jar --spring.profiles.active=dev

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
