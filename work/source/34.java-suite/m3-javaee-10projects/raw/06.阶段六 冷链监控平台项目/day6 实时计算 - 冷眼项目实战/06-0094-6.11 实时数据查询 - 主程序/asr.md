# 声音线转写：6.11 实时数据查询 - 主程序

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.11 实时数据查询 - 主程序_【海量资源尽在 666java.com】.mp4
- 时长：2分55秒（音频 175s）
- 转写：faster-whisper-large-v3 / 语言 zh / 6 段
- 生成时间：2026-10-28 16:32:02

## 逐段转写（教师原声）

[00:00] 好 根据我们这个代码的这个结构呢我们来开发我们这个CodeMonitor里边的主要的类主要的一些方法那首先的话我们看我们这个工程的这个application-yaml文件和application-dv的yaml文件这两个文件和其他的工程里边的这种yaml文件比较类似它使用了server-Tomcat然后端口以及我们的context-path也就是说我们URL的一个路径然后呢包括我们当前这个工程CodeMonitor它的一个名字在这里边都会
[00:30] 写上然后另外一个就是我们当前使用哪一个profile也就是说我们使用的是application-dv的-dv这个样本文件里边一个是说我们的这种Urequra服务制作中心它的一个地址另外一个是我们的Spring的一个就是GTBC的databasedatasource到底是配置的是什么样的它使用的是我们GTBC的mycircle然后连接用户名密码
[00:59] 这是我们的配置还有一些其他的配置属性这些和我们其他工程里边的查询MySQL数据库都比较类似在这里不得详细的讲解下面我们来开发我们的主程序那么这个主程序我们叫做MonitorApplication我们在这可以开发一个主要的我们先加上了一个package就是包名com.rtk码对吧com.rtk码在这里的时候
[01:30] 我们创建我们的Main函数这个Main函数叫MonitorApplicationOK这个MonitorApplication它是我们的主函数是一个Spring Boot的一个程序那么我们需要在这里边添加我们的Main函数然后呢我们再添加我们的这个注解这个注解的话一个是Spring Boot Application
[02:08] 这是一个注解那么另外一个的话是我们叫EnableDiscoveryPlant这个是我们把我们当前这个程序连把它注册到我们的Ulker服务注册中心里面去那下一步的话我们要添加在main函数里面添加我们的Spring Boot的一个程序程序体Spring Boot Application然后Spring Boot Application点Run在Run的话就是Run这个
[02:40] monitor当前类obligation.class然后args这样的时候我们当前的主程序其实就已经添加完了
