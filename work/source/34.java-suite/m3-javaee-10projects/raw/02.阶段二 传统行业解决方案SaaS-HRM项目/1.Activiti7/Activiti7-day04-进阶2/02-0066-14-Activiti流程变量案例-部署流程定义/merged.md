# 14-Activiti流程变量案例-部署流程定义

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\14-Activiti流程变量案例-部署流程定义_【海量资源尽在 ubkz.com】.mp4
- 时长 5分40秒（音频 341s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下面呢我们就继续啊到这边来创建一个新的class啊它的这个主要作用就是完成我们的这个流程的部署对吧以及我们流程变量的设置啊那现在我们可以这样啊就直接给它起一个名字啊就比如说就是叫做ValueValue我们的这个流程变量的一个测试的事例对吧我们就直接起一个这个名字嘛叫Value Test啊
[00:30] OK这样我们先把这个类创建出来它的主要作用就是我们的流程流程变量的测试流程变量我们如果要去测试的话第一个我们也一样可以到这里面按照这个步骤来做比如说第一个我们要去把我们的新的流程新的请假流程请假流程定义的步数
[01:00] 首先我们要去完成它的部署的工作对吧现在我们就可以来做这件事情要去做部署的话第一个我们可以一起再回顾一下我们要去得到我们的 process engine对吧process engine而这个 process engine我们应该说很简单就可以得到process engine是点get default process engine对吧于是我们这边就可以得到一个 process engine
[01:29] 这是第一步我们第二个步骤这个时候就是得到我们的这个叫做reported对吧reported Service的这个对象这个对象我们可以通过我们的这个process engine.getreported Service这样我们就一样的可以得到我们的这个process得到我们的这个reported Service
[01:58] 好得到他之后第三个步骤我们就可以来实现我们的部署在工作了对吧实现我们的部署部署的话我们主要通过主要通过我们的reported Service底头去调用他的adclad我们在这边reported Service可以去createcreate deployment我们这个时候得到一个
[02:26] deployment build的对象然后我们可以在这里面再去.aid去添加我们的class path resource这个地方我们添加的class path resource主要是我们的holo4的BPMN文件和他的PNG文件这两文件我们这两文件是在我们的diagram底下的叫holo
[02:55] holiday4.vpmn文件对吧除了这一项我们还可以再去add class pass resource添加的是我们的diggramdiggram底下的叫holiday4.png文件对吧然后我们再去做一个叫做做一个真正的部署比如说我部署的名字叫什么对吧我们这个就是叫做请假
[03:24] 叫做请假流程啊请假流程但是这个流程中已经带上了有我们的这个流程变量对不对已经带上了我们的流程变量啊好这是我们的这个名字然后呢我们再去做一个啊 deploy 对不对这样我们就可以实现了这个部署啊当然我们这个部署呢最终就可以得到一个局部变量比如说叫做 deploy deploy然后呢我们就可以来输出我们的这个部署信息对吧也是 out
[03:53] 我们就可以用 deploy 点去输出比如说我们的 id好这是一下那我们同时还可以再去输出一个叫做 deploy 点 data 来说我们的名字好这样我们就可以做到我们的流程定义的部署了我们一会可以测试看一下我们的部署信息是否已经添加进来对不对好你可以看一下好目前应该库已经被我删了所以说
[04:22] 如果咱们在刷新的时候这里面没有任何的表没有任何的表现在我们可以一起来看一下当我们部署成功当我们部署成功了我们的这个activity这23张表会创建出来还有一个就是我们的battery这个表里头应该会存储有我们的两个资源信息对吧你可以看到我们的请假流程带上流程变量的就已经部署进去了于是我们可以再次发行一下对吧
[04:52] 我们来看一下battery好这里边呢各位就可以看到这是我们刚刚所添加进来的这个png的图对不对我们也可以看它啊你看它的话这个时候我们可以看到对吧这是我们张三李四王武造六对不对而真正我们在这里边所添加的这个表达式各位这时候你也可以看到我们在这个线上面对吧就有有有带上这个表达式了啊这是我们这边呢应该说流程部署
[05:21] 最新的这个请假流程就被我们已经部署进来了那下一步其实我们要做的工作就应该是真正去设置我们的这个流程定义的变量对不对好我们先把这个新的这个请假流程的部署先给各位说到这里面

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码部署 Activiti 工作流定义（BPMN 图）到数据库中。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Activiti 项目结构，右侧是 BPMN 流程图，包含“开始事件”、“用户任务”、“排他网关”、“结束事件”等节点，右侧工具栏列出所有可用的 BPMN 元素。
画面2: 显示 `VariableTest.java` 文件，代码中注释“流程变量的测试”，并展示 `Object` 类的继承结构。
画面3: 在 `VariableTest.java` 中，代码注释“1. 模拟流程引擎”，并调用 `ProcessEngines.getDefaultProcessEngine()` 获取默认流程引擎。
画面4: 在 `VariableTest.java` 中，代码注释“2. 模拟RepositoryService”，并调用 `processEngine.getRepositoryService()` 获取仓库服务。
画面5: 在 `VariableTest.java` 中，代码注释“3. 部署”，并调用 `repositoryService.createDeployment()` 开始部署。
画面6: 在 `VariableTest.java` 中，代码注释“2.2. 添加BPMN模型”，并调用 `DeploymentBuilder.addBpmnModel()` 方法。
画面7: 在 `VariableTest.java` 中，代码注释“2.2. 添加BPMN模型”，并调用 `DeploymentBuilder.addBpmnModel()` 方法。
画面8: 在 `VariableTest.java` 中，代码注释“2.2. 添加BPMN模型”，并调用 `DeploymentBuilder.addBpmnModel()` 方法。
画面9: 在 MySQL GUI 中，执行 SQL 语句 `drop database activiti;`，但提示错误“Table activiti.act_ge_bytearray doesn't exist”。
画面10: 在 `VariableTest.java` 中，右键点击 `ProcessEngine` 变量，选择“Run 'VariableTest.main()'”。
画面11: 在 `VariableTest.java` 中，代码注释“2.2. 添加BPMN模型”，并调用 `DeploymentBuilder.addBpmnModel()` 方法。
画面12: 在 MySQL GUI 中，执行 SQL 语句 `create database activiti;`，并成功创建数据库。
画面13: 在 MySQL GUI 中，执行 SQL 语句 `create database activiti;`，并成功创建数据库。
画面14: 在 `VariableTest.java` 中，代码注释“2.2. 添加BPMN模型”，并调用 `DeploymentBuilder.addBpmnModel()` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3:
```java
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
```
画面4:
```java
RepositoryService repositoryService = processEngine.getRepositoryService();
```
画面5:
```java
repositoryService.createDeployment()
```
画面6:
```java
DeploymentBuilder.addBpmnModel()
```
画面7:
```java
DeploymentBuilder.addBpmnModel()
```
画面8:
```java
Deployment deploy = repositoryService.createDeployment()
    .addClasspathResource("diagram/holiday4.bpmn")
    .name("请假流程-流程变量")
    .deploy();
```
画面9:
```sql
drop database activiti;
```
画面10:
```java
// Run 'VariableTest.main()'
```
画面11:
```java
Deployment deploy = repositoryService.createDeployment()
    .addClasspathResource("diagram/holiday4.bpmn")
    .name("请假流程-流程变量")
    .deploy();
```
画面12:
```sql
create database activiti;
```
画面13:
```sql
create database activiti;
```
画面14:
```java
Deployment deploy = repositoryService.createDeployment()
    .addClasspathResource("diagram/holiday4.bpmn")
    .name("请假流程-流程变量")
    .deploy();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

