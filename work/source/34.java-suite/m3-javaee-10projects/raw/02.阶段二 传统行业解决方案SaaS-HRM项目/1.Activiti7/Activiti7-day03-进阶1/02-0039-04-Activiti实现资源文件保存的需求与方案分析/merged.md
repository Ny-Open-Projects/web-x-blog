# 04-Activiti实现资源文件保存的需求与方案分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\04-Activiti实现资源文件保存的需求与方案分析_【海量资源尽在 ubkz.com】.mp4
- 时长 8分55秒（音频 535s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那在我们介绍完这个流程定义的删除之后啊我们下一步呢开始来看我们的这个流程定义的资源文件的查看啊这个资源文件的查看主要指的就是我们的这个BPMN文件和我们的这个PNG文件啊这两个文件的一个查看操作那在这里面要去做我们的这个文件的查看操作那各位思考一下啊在我们的这个
[00:29] Bitarray这个表里头其实我们之前是看到过这两个文件的只要我们的这个流程部署成功之后这里面就会有这两个文件那现在呢如果说给你一个机会说我们要把这两个文件BPMN文件和我们的PNG文件直接借助于我们的这个加密代码把它
[00:56] 放到我们把它存入到我们指定的某个目录下去比如说就指定到指定到我们的activityD03放到我们的资料里下去现在假如说我要做一个这样的工作就是说我要把我们的流程部署之后的PNG文件和我们的BPMN文件要从我们的数据库里头读取到我们的
[01:26] 记盘的资料目录下去这就是我现在要做的工作啊那我们一起啊来思考一下啊这个工作应该怎么去做啊好我在这里边呢假如说我们再去新建了一个新的class啊比如说这个地方就是我们要做的工作啊主要就是去读取文件对吧比如说叫做curry啊curry我们的bp
[01:53] BPMN文件BPMN field这就是我们真正想去做的工作那要去做这个工作我们需求是什么样的需求是这样的从我们的activity的哪张表呢从我们的activity的byte array表中对吧byte array这个表中读取
[02:28] 两个资源文件这就是我们的这个真实的需求读取这两个资源这是第一步你读取出来那第二个步骤读取出来之后我们呢打算将两个资源将两个资源文件保存到我们的这个盘湖底下去就是这个路径下现在呢我们打算保存到这个路径下
[03:01] 保存到路径路径这个底下这就是我们的这个目标保存到这个资源目录下之后我们下一步其实就可以通过打开文件的方式看是否已经把我们的这个数据库中的两个资源文件直接给它挪移到我们的这个资料目录下去看是否做到这个效果了那有同学会思考这个业务又有什么用呢
[03:34] 对吧那这个地方其实是有用的啊我们来思考一下啊如果说现在呢呃用户用户啊用户想查看这个呃比如说请假流程这个请假流程具体有哪些步骤呃要要执行或者是有哪些步骤要走对不对这是用户他的需求就是我想看看
[04:03] 你的这个请假流程具体有三步还是四步还是五步对吧那这个时候我就必须从我们的这个服务器上将我们的这个PNG图片下载下来吧因为PNG图片里头保存的有我们具体的这个执行的步骤对吧所以这个地方这就是它真实的真实的这是真实的用用场景真实真实用用场景也是存在的
[04:36] 那下一个步骤我们就会思考如果我们要去做这个资源文件读取了那这个地方肯定是需要用到activity本身的内容对吧那如果说我不借助于activity本身的这一套API那我们会怎么做呢比如说那就是不使用叫做技术技术方案那我们肯定是真正场景下肯定是需要用我们的activity去做对吧
[05:05] 第一种方式第一种方式就是使用我们的activity的API对吧来实现那这种方式肯定是最简单的如果不用这种方式呢那各位就会思考那其实我们这里边存储的是一个byte的字节流对不对字节流或者是我们的这个字符流对吧那我们的字节流字符流将来如果要真正被读取出来的话那我们这个地方第二种方式那就是
[05:34] 原理或者说第二种方式其实其实就是我们的其实就是原理层面那从原理层面我们去思考的话假如说我们没有activity给你一个给你一个数据库表里头有这样的一个字节流对吧那我们怎么样去把它读取出来对不对那这个地方考验的就是我们的基本功那可以使用什么
[06:02] 可以使用我们JDBC对我们的这个Blob类型或者是我们的Glob类型数据的读取并保存那这个其实各位有时间的同学或者说你这个地方不是特别清楚的同学这个各位可以直接在百度里面去找JDBC对Blob
[06:32] 或者是club数据类型的读取那你就能够收到JDBC里头其实是可以读取可以读取我们的这种数据类型读取完了它是一个流对吧那下面我们要做的工作就是通过输入流和输出流的转换对吧来实现我们真正的这个读取工作这是我们这个底层实现就是这样的那要涉及到我们的这个输入流输入输出流的转换对不对
[07:00] 要输入IO流的转换那这个地方其实我们最好解决方案最好不要自己去写比如说一边读一边写这个方案其实是可以但是我们更加倾向于让各位去使用工具有一个common.io有一个这样的价包可以轻松解决
[07:29] 我们的这个IO操作啊所以呢我在这里边打算呢也把我们的CommerceIO引入到我们的项目中来啊那要注意要引入进来我们就需要第一步去把我们的这个CommerceIO的包引入进来吧那现在我可以这样做啊我们可以这样啊然后呢在这个地方去实现我们的这个实现我们的这个导包对吧实现我们这个导包那现在我就去添加一个dependence啊然后叫做Commerce
[07:59] GAMIO对吧好这时候我们就可以找到啊然后去选择它的版本比如说我就可以选择这个版本或者是更高的版本都可以的啊然后这样呢我们的这个版我们的这个CommerceIO就加入进来了它就可以很方便的去实现我们的这个文件的读写对吧这个就是啊文件啊文件的读写操作对吧那用它的话可以很轻松可以实现我们的目标
[08:27] 这样我们就完成了真正去读取一个文件的一些最基本的像需求 应用场景以及解决方案基本上的思路就清楚了真正再去走我们肯定会借助于activity相关的一些API来实现这个操作我们先把原理以及需求分析给各位就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码删除 Activiti 流程定义，并展示其在数据库中涉及的表及 Maven 依赖管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Activiti 项目结构，当前选中“6.4 流程定义删除”章节，代码中定义了删除流程部署的方法，其中部署 ID 为 "8801"，并设置了 true 以允许删除正在运行的流程实例。
画面 2: 在 MySQL Workbench 中，列出与流程定义相关的表，如 act_re_procdef、act_ge_bytearray，并注释说明了“背后影响的表”。
画面 3: 在 MySQL Workbench 中，继续列出“背后操作的表”，包括 act_hi_actinst、act_hi_identitylink 等。
画面 4: 显示了 Windows 资源管理器，路径为“Activiti7-day03”文件夹，内容为空。
画面 5: 在 IntelliJ IDEA 中，打开“DeleteProcessDefinition”类，执行了删除流程定义的操作，日志显示“DeleteDeployment finished”。
画面 6: 在 MySQL Workbench 中，显示了“act_re_procdef”表的查询结果，其中部署 ID 为 8801 的记录已被删除。
画面 7: 显示了 Windows 资源管理器，路径为“Activiti7-day03”文件夹，内容为空。
画面 8: 在 MySQL Workbench 中，显示了“act_re_procdef”表的查询结果，其中部署 ID 为 8801 的记录已被删除。
画面 9: 在 MySQL Workbench 中，显示了“act_re_procdef”表的查询结果，其中部署 ID 为 8801 的记录已被删除。
画面 10: 在 MySQL Workbench 中，显示了“act_re_procdef”表的查询结果，其中部署 ID 为 8801 的记录已被删除。
画面 11: 在 IntelliJ IDEA 中，打开“pom.xml”文件，展示了 Maven 依赖配置，包括 commons-dbcp 和 alfredresco 的仓库配置。
画面 12: 在 IntelliJ IDEA 中，打开 Maven Artifact Search 窗口，搜索“commons-io”，并显示了多个版本号。
画面 13: 在 IntelliJ IDEA 中，Maven Artifact Search 窗口显示“commons-io”版本号 1.0 被选中。
画面 14: 在 IntelliJ IDEA 中，打开“QueryBpmFile.java”文件，其中包含关于如何查询 BPMN 文件的注释和代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public void deleteDeployment() {
    // 流程部署id
    String deploymentId = "8801";
    // 通过流程引擎获取repositoryService
    RepositoryService repositoryService = processEngine
            .getRepositoryService();
    //删除流程定义，如果该流程定义，如果该流程实例启动删除时出错
    repositoryService.deleteDeployment(deploymentId);
    //设置true 级别删除定义，即使该流程有流程实例启动也可以删除，设置
    //为false非级别删除方式，如果流程
    //repositoryService.deleteDeployment(deploymentId, true);
}
```

画面 2:
```sql
act_re_procdef  流程定义的一些信息
act_ge_bytearray  流程定义的.bpmn文件及png文件
#背后影响的表：
act_hi_actinst  已完成的活动信息
act_hi_identitylink  参与者信息
act_hi_taskinst  任务实例
act_ru_execution  执行表
act_ru_identitylink  参与者信息
act_ru_task  任务
```

画面 3:
```sql
* 背后操作的表：
act_hi_actinst
act_hi_identitylink
act_hi_taskinst
act_ru_identitylink
act_ru_task
*/
act_ge_bytearray
act_re_deployment
act_re_procdef
```

画面 11:
```xml
<dependencies>
    <dependency>
        <groupId>commons-dbcp</groupId>
        <artifactId>commons-dbcp</artifactId>
        <version>1.6</version>
    </dependency>
</dependencies>

<repositories>
    <repository>
        <id>alfresco</id>
        <name>Activiti Releases</name>
        <url>https://artifacts.alfresco.com/nexus/content/repositories/activiti-releases/</url>
        <releases>
            <enabled>true</enabled>
        </releases>
    </repository>
</repositories>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

