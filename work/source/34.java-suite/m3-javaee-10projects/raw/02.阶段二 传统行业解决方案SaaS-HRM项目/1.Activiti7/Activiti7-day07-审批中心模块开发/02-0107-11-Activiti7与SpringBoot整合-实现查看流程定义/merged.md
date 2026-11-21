# 11-Activiti7与SpringBoot整合-实现查看流程定义

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\11-Activiti7与SpringBoot整合-实现查看流程定义_【海量资源尽在 ubkz.com】.mp4
- 时长 15分58秒（音频 958s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 现在我们开始来完成我们的Spring Boot与JUnit的整合的一个测试那要完成这个测试,首先我们需要去创建一个测试内那我们现在就到我们的这个Ideal工具中来创建我们的这个测试内测试内我是放在我们的这个测试包底下comit-activity然后在这里面我去新建一个Java Class比如说我这个部分就直接叫做activity
[00:29] 的test呢可以吧然后就ok这样呢我就创建好了一个这样的类啊那我们这个主要就是啊是实现我们的这个sprint boot啊与junit整合啊来实现测试测试的目标是什么测试我们的这个流程流程另一的相关啊操作以及我们的这个任务啊
[00:58] 以及我们的这个任务完成还有就是我们的这个任务的查询那作为一个测试类首先我们可以去把我们的这个run with加入进来吧run with然后在这个地方我们用的是我们的supreme run对吧supreme run.class这是一个然后下一个注解我们还可以加一个叫做supreme boot test就是它这样我们
[01:24] 关于我们的这个测试内的两个注解就加好了然后我们下一个工作就是在这里边我们要去注入相关的内容我第一个可以去注入的是我们的这个第一个可以注入的是我们的这个叫做ProcessRun这也是我们的这也是我们的这个activity7与我们的
[01:48] Spring Boot 整合提供给我们的一个这样的类叫 Process Runner我们就直接可以用它比如说叫 Process Runner这个地方是实现它的主要作用是实现我们的流程流程定义相关操作的相关操作以及我们的流程的流程的实力创建都是用它然后还有一个我们可以去注入的比如说来一个
[02:18] 叫做我们的这个task任务相关的一个runner啊run time好比如说我们叫做task run time那它主要就是啊实现我们任务相关操作啊操作的一个类啊好那把这两个部分加入进来那我们又说过我们的sprint boot和我们的activity整合的时候天然就会去使用我们的这个sprint securate啊
[02:43] 为了能够快速的实现我们的Circuit操作我们之前要求引入一个叫做AtaAutoValue的注入AtaAutoValue注入一个我们的叫做CircuitUtil
[03:09] 我这边直接把它注入进来它主要是我们的SpringSecuritySpringSecurity相关的一个工具类我们需要把它注入进来这样我们基本上就完成了我们所需要注入的一些内容我还可以在这里面去把我们要测试的方法添加进来比如说我们第一个主要是测试我们的定义
[03:38] 叫做Process DefiningTest Defining好这是我打算去加一个这样的具体的测试方法测试的这个效果将来会是什么样的对吧以及我们这里边应该要去写一些什么样的代码那各位同学你是否还记得我们这个部分如果要去做的是我们的这个流程定义信息的一个查看各位同学还记得我们要要写什么代码吗写什么样的代码
[04:06] 流程定义信息的查看这个部分我们肯定是需要用到我们的Process Runtime对不对Process Runtime刚刚我们在介绍给各位的时候又给他介绍了我们的Process Runtime在使用的时候所需要注意的所需要注意的这个点就是它对不对通过这种方式我可以快速的用我们的Process Runtime的Process Default
[04:34] 并且做出封页的效果我们可以这样copy我把代码直接拿过来我们来看一下通过这种方式我就快速的得到了一个封页查询出流程定义信息这个部分大家也会思考我们的流程都没有部署你怎么就可以去查看它的定义信息呢
[05:03] 要注意啊我们的这个流程只要你放在我们的Process这个目录下当我们程序一起动的时候它自动就会把我们的BPMN文件扔到我们的这个扔到我们的这个MySQL库里头去所以说我们的这个部署信息注意啊这一段我给各位写一下啊注意我们的这个流程部署啊流程部署工作在我们的这个activity7与Spring
[05:33] boot 整合,与我们的这个 sprint boot 整合后会自动实现它的这个部署但前提条件一定是放在哪个目录下呢放在我们的 resous 底下的这个 process必须是在这个目录下明白是吧然后是新点 bpmn这样我们就可以实现
[06:03] 我们的这个流程自动就会被部署进来好,当我完成在这里面完成这个枫叶查询工作之后呢那下一个环节我们可以通过我们的叫做通过我们的这个Process Definition Page里头的Get Total Intermediates通过这个方法能够查看到目前部署的流程总共有多少个
[06:33] 这个意思啊那我在这里要给各位写一下啊那我们这一句代码的主要意思就是呢查看查看啊这个已部署的已部署的流程过数也就是说get total int是总共有多少个这样的流程啊好那我们下一个环节可以接着来做操作再次回到这个地方来各位可以发现它在这里边使用我们的这个复循环来实现我们get content的
[07:02] GitContent的这个方法各位应该也是一看就能够明白的那这个方法是什么意思呢GitContent是得到我们具体的每一个流程定义信息对不对好我给各位记录一下那这个方法主要就是得到得到当前部署的每一个每一个流程定义信息所以呢
[07:31] 它的返回值其实是一个集合当我们做完这个工作,其实我们就已经就已经得到了一个就已经得到了一个叫做Process Defining的这样的一个对象,是不是?
[07:44] 而我们的这个Process Defining的这个对象各位,我看一下,刚才我们可能是导包导的有问题,我来再重新检查一下Process Defining,刚才我导的是这个,对吧?
[08:00] 当然他这边呢好像报的是有错啊那我可以重新再去更换一下啊在这个地方我重新啊再去导一个啊导一个比如说我把这个导进来好那这样我们基本上就已经这个地方是change parameter pdtypepdtype java.log object的啊他希望我们用object的来声明啊那没关系我在这个地方呢再去使用我们的这个salt
[08:35] 来输出它对不对输出我们的这个PD的对象啊好这样呢我基本上啊就完成了我们的这个流程定义信息的这个编码工作啊那现在我们可以一起来测试一下这个效果好我们要去关注一下啊我们的这个数据库表啊各位同学你会发现啊将来你会发现有一个问题会产生啊这个问题呢到目前为止我这边呢还没有完全的给它解决掉啊
[09:08] 什么样的问题就是我们的这个activity的表呢在activity7在我们的这个activity7与我们的Splitboot整合后我们的这个数据库的这个表原来activity7单独使用的时候或者说activity7与Splitboot整合的时候其实都是25张表对吧但我们这一次对应的这个表应该将来就没有历史记录相关的这个表会
[09:38] 就不会再出现我们可以看一下这边有一个这样的问题就是我们关于我们的authenticationobjectwas not found in the security context这句话是一个很关键的话现在主要告诉我们的就是没有权限所以说当我们的Spring Boot与我们的aggrativity整合之后
[10:09] 如果说你要想这个测试能通过的话那我们这个地方还必须有一件事情要做那就是我们需要去加入我们的这个登录信息那登录信息主要就是我们依赖于我们的secret邮条然后就可以去访问你看这里头写的是我们的system用户那我们这一次在这个部分我们的这一次这个流程叫做team01的这个流程当时我们是引入的是
[10:37] 我们这个组里头的是我们的这个Active Team里头的这个group对不对所以我们这个部分我可以去写上我们的celebrate所以可以把这个部分看巧为直接扔进来这样的话这个错误就会直接给我们屏蔽掉了这是这样的各位这一点我们一定要注意一下这是我们的SpringSpringCircuit
[11:06] CircleLit的这个认证认证工作那这样的话我们再去执行应该就可以成功了成功之后呢我们的这个数据库表啊这里面会少很多表好我们可以一起来看一下啊现在我重新再次执行我们观察一下这个运行的效果好这是我们啊正在执行现在我们再刷一下我们的这个数据库看一下效果啊好各位同学这个时候就可以看到啊
[11:39] 我们已经产生了很多表但是跟之前的25张表相比我们的历史history历史记录的相关的表在这里面都已经不见了这个地方针对这个问题我只能说我们目前是没有办法去解决因为我也去观察了然后我在这个部分也自己尝试着
[12:07] 把history的相关的表直接再重新自己手动给它创建出来但是我发现创建出来之后我们的history表其实我们的程序将来还是不会去往我们的history表中写入任何的数据这一点就比较奇怪了所以说在这个部分我给各位分享到的程度就只能到这个地方
[12:31] 咱们同学如果有时间的话可以去研究一下我们的History对应的那些历史记录表看看怎么样给它搞出来从这个角度我也再次说明一下因为我们这一次做的这个Activity7的尝试性工作是比较早不排除它自己本身就有这种问题存在所以从我们的角度上我只能说给各位
[13:00] 把我们的问题也给它抛出来了对不对但是呢目前是没有解决掉啊那这个部分我的态度是啊我会持续再去好好研究啊一旦我把这个问题的解决掉的话我呢会继续更新我们的这一次课程啊相当于这个这一段就这一小段的内容我可以再重新更新一下好这是我们在这个部分基本上啊就给各位啊实现了这个效果
[13:30] 同时我们可以看一下目前我们所发布的流程只有一个这个流程具体它长什么样这个部分各位就可以看到有一个叫做Process Definition这是我们的ID这是我们的Name这是我们的Key以及它的Version版本这是我们的流程定义信息当然如果说你感觉这样打出来的流程定义信息不对的话你其实
[13:58] 可以在前面加入一个流程定义对不对那这样再去输出肯定就没有任何问题啊当然这个地方你也可以在这里头再去加上一个啊就是比如说叫做啊流程啊定义的过速啊对吧这时候你再去运行的话应该说我们的这个效果就会非常的明显啊好这是基本上呢我们已经给过于完成了我们的这个流程定义信息的查看查看的时候啊
[14:29] 第一个点你要注意只要我们的BPMN文件在这个文件夹下它可以实现自动部署当我们部署成功如果你要去查看的话因为我们的SplintBoot与Activity其整合之后它默认强制性依赖SplintSecurator所以说我们在这个地方通过我们的工具类将来在这里面模拟一个我们的slab
[14:57] 在这里边它已经去做了这个认证只有认证通过我们才可以去完成我们的这个流程定义信息的查看那下面这就是我们查看我们这一次流程定义信息总共有多少过对不对而这个地方是把我们的这个流程定义信息都给它查询出来我们可以看一下目前我们的流程定义信息的过数只有一个真正的这个定义信息就是myprocess1对不对
[15:25] 是长成这样回到我们的数据库表一样我们也可以找到流程定义信息还是在这张表中在我们的byte array这张表中各位可以看到这是我们的部署流程定义信息当然你也可以去打开它来看一下是不是我们当时设置的是这个组active team这个组在这里面是完全可以看到的好
[15:52] 这样我们基本上给各位就完成了我们的流程定义信息的查看

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spring Boot 整合 JUnit 来测试 Activiti7 的流程定义信息。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PPT 页面“3.4 使用 Spring Boot 整合 Junit 方式测试新特性”，并显示项目结构，其中“3.4.1 创建测试类”部分展示了一个名为 `Activiti7DemoApplicationTests` 的测试类，包含 `processRuntime`、`taskRuntime`、`securityUtil` 三个私有字段。
画面2：展示 IDEA 编辑器中 `ActivitiTest.java` 文件，类名 `ActivitiTest`，使用 `@RunWith(SpringRunner.class)` 和 `@SpringBootTest` 注解，导入了 JUnit 和 Spring Boot 相关的测试类。
画面3：展示 `ActivitiTest` 类中添加了 `@Autowired` 注解的 `processRuntime` 和 `taskRuntime` 字段，并导入了 `org.activiti.api.process.runtime.ProcessRuntime` 和 `org.activiti.api.task.runtime.TaskRuntime`。
画面4：展示 `ActivitiTest` 类中添加了 `@Autowired` 注解的 `securityUtil` 字段，并导入了 `org.springframework.boot.test.autoconfigure.web.client.AutoConfigureWebClient`。
画面5：展示 `ActivitiTest` 类中定义了 `testDefinition()` 方法，使用 `processRuntime.processDefinitions(Pageable.of(startIndex: 0, maxItems: 10))` 获取流程定义分页数据。
画面6：展示 `testDefinition()` 方法中添加了 `System.out.println(processDefinitionPage.getTotalItems());` 用于打印流程定义总数。
画面7：展示 `testDefinition()` 方法中添加了 `for (ProcessDefinition pd : processDefinitionPage.getContent()) { System.out.println(pd); }` 用于遍历并打印每个流程定义。
画面8：展示测试运行失败，控制台输出 `1 test failed` 和异常堆栈信息。
画面9：展示 GitHub 页面，内容为 Activiti7 的示例代码，其中包含 `securityUtil.loginAs("system")` 用于登录系统。
画面10：展示在 `ActivitiTest` 类中添加了 `securityUtil.loginAs("salaboy")` 用于登录用户。
画面11：展示测试运行成功，控制台输出 `1 test passed` 和流程定义信息。
画面12：展示测试运行成功，控制台输出 `1 test passed` 和 Activiti7 启动日志。
画面13：展示测试运行成功，控制台输出 `1 test passed` 和流程定义信息。
画面14：展示 PPT 页面“3.4.2 查看流程定义信息”，并显示了 `processRuntime.processDefinitions(Pageable.of(0, 10))` 的代码示例。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```java
@ContextConfiguration(classes = Activiti7DemoApplication.class)
public class Activiti7DemoApplicationTests {
    @Autowired
    private ProcessRuntime processRuntime;
    @Autowired
    private TaskRuntime taskRuntime;
    @Autowired
    private SecurityUtil securityUtil;
}
```
画面2：
```java
package com.ithema.activiti;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
@RunWith(SpringRunner.class)
@SpringBootTest
public class ActivitiTest {
}
```
画面3：
```java
import org.activiti.api.process.runtime.ProcessRuntime;
import org.activiti.api.task.runtime.TaskRuntime;
import org.springframework.boot.test.autoconfigure.web.client.AutoConfigureWebClient;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
```
画面4：
```java
import org.springframework.boot.test.autoconfigure.web.client.AutoConfigureWebClient;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
```
画面5：
```java
public void testDefinition(){
    Page processDefinitionPage = processRuntime
            .processDefinitions(Pageable.of(startIndex: 0, maxItems: 10));
}
```
画面6：
```java
System.out.println(processDefinitionPage.getTotalItems());
```
画面7：
```java
for (ProcessDefinition pd : processDefinitionPage.getContent()) {
    System.out.println(pd);
}
```
画面9：
```java
securityUtil.loginAs("system");
```
画面10：
```java
securityUtil.loginAs("salaboy");
```
画面11：
```java
System.out.println(processDefinitionPage.getTotalItems());
for (Object pd : processDefinitionPage.getContent()) {
    System.out.println(pd);
}
```
画面12：
```java
ProcessDefinition(id='1752b335-fa98-11e8-81a4-5f870234484c', name='null', key='null', description='null', version=1)
```
画面14：
```java
processRuntime.processDefinitions(Pageable.of(0, 10));
System.out.println("可用的流程定义数量：" + processDefinitionPage.getTotalItems());
for (org.activiti.api.process.model.ProcessDefinition pd : processDefinitionPage.getContent()) {
    System.out.println(pd);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：标题“3.4 使用 Spring Boot 整合 Junit 方式测试新特性”，子标题“3.4.1 创建测试类”。
画面4：标题“3.4.2 查看流程定义信息”。
画面14：标题“3.4.2 查看流程定义信息”，下方有“北京市昌平区建材西路金燕办公楼一层 电话：400-618-9090”和“黑马程序员 传智播客旗下 高端IT教育品牌 改变中国IT教育，我们正在行动”字样。

5) 无。

