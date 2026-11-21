# 18-部署流程：环境搭建

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\18-部署流程：环境搭建_【海量资源尽在 ubkz.com】.mp4
- 时长 7分24秒（音频 444s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了刚才呢我们通过这个activity app呢咱们自己绘制了一个测试的请假流程那对于这个工具使用起来相对来说还是比较简单的那我们这个请假流程的绘制完成了之后接下来呢别忘了咱们刚才说过我们要想去完成activity的一个开发咱们现在关注的是第一个阶段叫做流程制作
[00:27] 那除了有流程制作之外是不是还有就是一个流程部署指的是把我们制作好的流程部署到activity当中没错吧那接下来呢我们要做的就是这么一个阶段我找到咱们这边讲义一起简单的来看一下那这边呢讲义上也说过了通常情况下这些流程呢都是我们提前规划好的也就是提前要把这些流程也就是这些文件我们制作好准备好
[00:54] 那接下来呢我们准备好了这些流程或者我们把这流程设计出来之后那接着那当前你的工程当中还没有activity那我们怎么办我们就需要将这些流程通过文件上传的形式上传到你的这个工程当中哎这边说了要先上传到服务器
[01:15] 同时要把这些流程文件部署到activity引擎当中当然这是一个上传加部署一个完整的流程那所以接下来呢还有第二个小的步骤那第一个我们已经制作好了接着第二个是不是就开始写一些代码把我们的activity绘制好的这个流程的模型把它上传并且部署到我们的系统当中啊
[01:45] 没错吧OK那好了接下来呢我们来看一下咱要进行流程部署应该如何去做好了我们要完成这个流程部署的话注意流程部署的话那我们要做的事情第一个就是要搭建一个小小的环境那我们搭建环境是这样的就是说啊在我们的IHRM人力资源管理系统当中我们是使用微服务的形式我去创建一个微服务里面编写的全部都是跟审批
[02:15] 全部都是跟工作流相关的这些内容所以我要配置一个环境那这个环境创建好了之后那接下来对于activity而言它自己有自己的数据库相关的配置所以我们要把activity的数据库也给它准备好那这是第二件事那接着第三件事我们这个环境搭建了之后那有相应的请求的路径
[02:41] 那这些请求的路径是不是需要将它设置到我们的网关工程当中没错吧这个就是我们要做的一些流程部署之前的准备工作好那接下来呢回到我们的idea当中咱们就开始把这个准备工作呢给它编写完成好了回到idea那在这边右键我去创建一个新的modelnext
[03:11] 其一个名字呢我们这边就叫做IHMIHM小线AUDIT我们的审批中心的这个模块点击next点击finish好了模块创建出来了之后里面有相应的碰文件的一些依赖还有一些page那这些呢我就不啰嗦了找到今天的资料在这边呢有我们审批相关的这些基本的配置代码那接下来呢咱们开始拿过来碰文件打开
[03:44] 把里面的内容呢直接Ctrl Ccall到我们这边Ctrl VOK好了这边呢咱们不管了接下来呢还有在我这个审批模块当中咱们还需要去创建对应的启动类来一个包com.ihim.audit审批模块对应的代码那对于相应的启动类来说呢比较简单我在今天资料当中也给各位准备好了
[04:16] 那在这边把相当代码呢Ctrl C 拷到我们的这个包下Ctrl V 拷过来好了这个其实就是我们一个常规的启动类在这个常规的启动类当中需要各位一定要注意这用 exclude 的形式排除了一个注解是这样的在ActiveT 7当中啊它自动的是使用Spring Security进行安全配置的那我们都知道我们系统当中是不是用Shadow啊所以如果说你要去扫描这个
[04:47] Spring Security相关的内容其实就会有一个小小的冲突那我们这边要做的事情就是把这个Spring Security相应的内容给它排除掉就这么一个需要和各位做解释的好了那这个咱们拷过来了之后接下来呢还有就是对于这方向工程可能会涉及到相应的一些配置那这些配置文件资料当中也准备好了回到这边Ctrl C把application.yml给它copy过来
[05:17] Ctrl V拿过来那拿过来之后简单的来看一下这个我们指定服务名称没问题注意这回呢我们有两个数据库一个代表的是我们IHM人力资源管理系统相关的那第二个我们要用Activity那Activity需要自己的数据库表那我们可以把这两套表呢放到一个系统当中没问题
[05:42] 当然了我们为了方便为了清晰我用两个数据库来描述一个描述的是activity一个描述的是我们的人力资源管理系统那咱们继续往下看这边呢有一块activity数据库相应的一些配置内容OK那这个就是我们整个的这个环境搭建其实咱们现在做的呢还是相对来说比较简单的这么一个步骤当然了别忘了
[06:10] 我们所有的请求呢还需要找到对应的网关把网关的配置也给他添加上那找到网关部分那这段网关的配置直接从讲义当中给他copy过来哎就可以了好了control c拿到我们这边control vok做一个小小的调整好了没问题好了没问题好了需要各位一定要注意的是
[06:47] 用户的所有审批的相关内容呢咱们请求的路径都是以-user来开头的OK好了那这样一来咱们基本的这个环境搭建的工作呢其实已经准备的差不多了当然了这是代码成分那除了代码之外还有一个就是数据库那ActiveT7呢需要依赖很多的数据库表那这些数据库表我已经提前准备好了当然了这些会随着我们的今天资料一起下发下去
[07:17] OK好了那至此我们环境搭建相关的过程就已经结束了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Activiti 工作流引擎进行请假流程的设计、部署与配置，包括使用官方 Web 工具绘制流程图、在 Spring Boot 项目中集成 Activiti、配置数据库及服务注册等。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Activiti Editor 中的请假流程图，包含“提交申请”、“中间审批”、“复审”三个任务节点，以及一个“否”分支指向“领导审批”节点，最终汇入结束节点。
画面2：PPT 页面，标题为“4.2 流程制作工具”，列出制作流程的几种方式：手写XML文件、基于DEA的activiti插件、通过Java编程生成XML文件、基于Activiti官方提供的activiti-app工具包。
画面3：PPT 页面，标题为“4.4 流程部署”，说明在流程设计完成后，可先上传文件到服务器，再将流程定义文件部署到Activiti引擎中。
画面4：PPT 页面，标题为“4.4.2 流程部署”，展示“网关中加入相应配置”的代码片段，包含“path”、“serviceId”、“stripPrefix”、“customSensitiveHeaders”等配置项。
画面5：IntelliJ IDEA 中打开项目“ihrm_parent”的界面，显示项目结构。
画面6：Windows 资源管理器中，右键点击“04请假流程”文件夹，弹出菜单，显示“复制”、“粘贴”等选项。
画面7：IntelliJ IDEA 中打开“ihrm_audit”模块的“pom.xml”文件，显示引入的依赖项，包括“spring-cloud-starter-openfeign”、“activiti-spring-boot-starter”、“junit”、“commons-fileupload”等。
画面8：IntelliJ IDEA 中弹出“Copy”对话框，提示将文件复制到“E:\ihrm\ihrm_parent\ihrm_audit\src\main\java\com\ihrm\audit”目录。
画面9：IntelliJ IDEA 中弹出“Copy”对话框，提示将文件复制到“E:\ihrm\ihrm_parent\ihrm_audit\src\main\resources”目录，新文件名为“application.yml”。
画面10：IntelliJ IDEA 中打开“application.yml”文件，显示数据库配置（act、ihrm、redis）和Activiti配置（history-level、db-history-used）。
画面11：PPT 页面，标题为“4.4.1 环境搭建”，显示“ihrm_audit”模块的目录结构和依赖项。
画面12：IntelliJ IDEA 中打开“ihrm_gate”模块的“application.yml”文件，显示多个服务的配置，如“ihrm-employee”、“ihrm-social-securitys”、“ihrm-attendance”等。
画面13：SQLyog 数据库管理工具界面，显示“CREATE TABLE”语句，创建“act_ge_bytearray”表，以及“act_re_procdef”表的“ID_”字段值。
画面14：PPT 页面，标题为“4.4.1 环境搭建”，显示“ihrm_audit”模块的目录结构和依赖项。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：无代码或配置。
画面2：无代码或配置。
画面3：无代码或配置。
画面4：
```
ihrm-user-audit:
  path: /user/** #配置URL和URL的请求头
  serviceId: ihrm-audit #指定Eureka注册中心中的服务id
  stripPrefix: false
  sensitiveHeaders:
    customSensitiveHeaders: true
```
画面5：无代码或配置。
画面6：无代码或配置。
画面7：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring-boot-starter</artifactId>
    <version>7.0.0.1</version>
</dependency>
<dependency>
    <groupId>org.junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
</dependency>
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-image-generator</artifactId>
    <version>7.1.0.M2</version>
    <exclusions>
        <exclusion>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>commons-fileupload</groupId>
    <artifactId>commons-fileupload</artifactId>
    <version>1.3.3</version>
</dependency>
```
画面8：无代码或配置。
画面9：无代码或配置。
画面10：
```yaml
datasource:
  act:
    jdbc-url: jdbc:mysql://localhost:3306/act?useUnicode=true&characterEncoding=utf8&serverTimezone=GMT
    username: root
    password: 111111
    driver-class-name: com.mysql.jdbc.Driver
  ihrm:
    jdbc-url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8&serverTimezone=GMT
    username: root
    password: 111111
    driver-class-name: com.mysql.jdbc.Driver
  redis:
    host: 127.0.0.1
    port: 6379
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true
  activiti:
    history-level: full
    db-history-used: true
  Eureka:
    client:
      serviceUrl: http://localhost:8888/Eureka/
      instance:
        preferIpAddress: true
        instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
```
画面11：无代码或配置。
画面12：
```yaml
ihrm-employee:
  path: /employees/** #配置URL的请求规则
  serviceId: ihrm-employee #指定Eureka注册中心中的服务id
  stripPrefix: false
  sensitiveHeaders:
    customSensitiveHeaders: true
ihrm-social-securitys:
  path: /social-securitys/** #配置URL的请求规则
  serviceId: ihrm-social-securitys #指定Eureka注册中心中的服务id
  stripPrefix: false
  sensitiveHeaders:
    customSensitiveHeaders: true
ihrm-attendance:
  path: /cfg/** #配置URL的请求规则
  serviceId: ihrm-attendance #指定Eureka注册中心中的服务id
  stripPrefix: false
  sensitiveHeaders:
    customSensitiveHeaders: true
```
画面13：
```sql
CREATE TABLE `act_ge_bytearray` (
  `ID_` varchar(64) NOT NULL COMMENT '主键',
  `REV_` int(11) DEFAULT NULL COMMENT '版本',
  `NAME_` varchar(255) DEFAULT NULL COMMENT '名称',
  `DEPLOYMENT_ID_` varchar(64) DEFAULT NULL COMMENT '部署ID',
  `BYTES_` longblob COMMENT '字节',
  `CREATE_TIME_` datetime DEFAULT NULL COMMENT '创建时间',
  `UPDATE_TIME_` datetime DEFAULT NULL COMMENT '更新时间',
  `DELETE_TIME_` datetime DEFAULT NULL COMMENT '删除时间',
  PRIMARY KEY (`ID_`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
```
画面14：无代码或配置。

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：PPT 标题为“4.2 流程制作工具”，内容为制作流程的几种方式。
画面3：PPT 标题为“4.4 流程部署”，内容为流程部署的步骤。
画面4：PPT 标题为“4.4.2 流程部署”，内容为网关中加入的配置。
画面11：PPT 标题为“4.4.1 环境搭建”，内容为“ihrm_audit”模块的目录结构和依赖项。
画面12：PPT 标题为“4.4.1 环境搭建”，内容为“ihrm_audit”模块的目录结构和依赖项。
画面13：无PPT标题或架构图。

5) 无评价，无无关内容。

