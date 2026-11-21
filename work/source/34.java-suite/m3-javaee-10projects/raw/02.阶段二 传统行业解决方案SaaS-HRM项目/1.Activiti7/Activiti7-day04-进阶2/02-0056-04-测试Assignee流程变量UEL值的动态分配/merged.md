# 04-测试Assignee流程变量UEL值的动态分配

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\04-测试Assignee流程变量UEL值的动态分配_【海量资源尽在 ubkz.com】.mp4
- 时长 4分41秒（音频 281s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们为了测试这个效果首先我们可以把Holo的BPMN和我们的PNG文件要求我们部署到我们的MySQL Activity这个表里头去对吧那下面我们就可以一起来实现往这个Activity中来实现这个部署的工作那我们的BPMN文件和PNG文件这两个都已经有了下面其实我们只要做一个工作就是
[00:29] 把我们的这个activity deploy让这个代码重新再次更新一下那现在我可以来执行看一下这个运行的结果回到我们的这个表中我们一起可以来看一下这时候我应该是看看我们的这个XML文件R310 R310 R3102对吧这就是我们在这里边要求设置的这三个执行人对吧
[00:58] 为三个UEL表达式那我们呢再次回到我们的这个代码我们的这个代码呢就应该也应该改成我们的这个012这三个取值吧012这三个取值这三个值呢正好对应的就是我们的这个我们的这个流程从assign UEL表达式取的这012这三个key对不对那这三个key的值就已经有了
[01:27] 这三个K的值有了那下面我们直接就可以来在启动流程实例的时候跟上第二个常数那第二个常数其实就应该是我们这里面设置的具体的这三个执行人对吧当然你不一定就是张三里之王五这个值可以是我们动态的去从页面上给它给进来对吧好下面我们直接来运行看一下这个效果好这时候我们再回到我们的这个
[02:00] activity的表在activity的表里头我们有一个identity link我们看一下各位可以看到目前我们是走到张商这个节点上来了对吧按道理来说我们的这个beta ray里面其实是没有设置真实的这个联系的对吧只是这个设置了一个这样的表达式而这个表达式真正的值各位可以看到通过我们的第二个参数的map激活
[02:28] 给它负的sin0是张3而张3的这个值包括像李氏的这个值王武的这个值其实都已经给我们绑定到了我们的这个流程绑定到了我们的这个beta ray里面的这个BPMN文件的012这三个其实已经现在我们已经绑了有真正的值那按道理我们可以让张3
[02:57] 继续完成他的任务对吧当张三完成了任务下一个是不是在我们的这个identity这个表中又会多加一个多加入一个这个参与者对吧就是我们的李四各位呢这个可以啊我们再去执行一下我们的这个complete比如说holiday2这个是改单啊让张三执行完任务好我们走一下那这个时候张三就已经执行完了啊那张三执行完了我们再刷一下这个表对吧
[03:29] 刷一下这个表李斯就会参与工作了然后再走就是王武参与工作这个其实各位可以看到我们将来再去设置我们的流程流程的assign执行人的时候其实现在又多了一种新的方式这种方式可以让我们在设置我们的流程实例的时候让我们在设置我们的流程变量的时候这里面可以直接写我们的UEL给它是
[03:58] 当然如果是对象的话我们也可以啊也可以在这里边呢直接指定一个对象点对吧就是类似的这种写法啊对象点assign那这就要求我们有一个右左对象对吧同时呢这个右左对象呢它还有一个assign的这个取字对吧这样也是可以做到同样的效果啊那好这是我们啊给各位演示了一把啊
[04:27] 我们的使用流程变量来实现我们的任务分配基本上使用UEL表达式这个写法多罗大个号的写法是要求咱们要掌握的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Activiti 工作流引擎部署流程定义、启动流程实例、设置流程变量以及完成任务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 ActivitiDeployment.java 文件，代码用于部署名为“请假申请流程”的流程定义，包含添加 BPMN 文件和 PNG 图片资源。
画面2：展示 ActivitiDeployment.java 文件，代码用于打印部署的名称和 ID。
画面3：展示 MySQL GUI 工具，执行 SQL 语句删除名为 'activiti' 的数据库并重新创建。
画面4：展示 MySQL GUI 工具，查询 activiti 表，显示部署的 ID 和资源信息。
画面5：展示 AssigneeUI.java 文件，代码用于启动流程实例并设置 assignee 变量。
画面6：展示 AssigneeUI.java 文件，代码执行后在控制台输出流程引擎名称。
画面7：展示 MySQL GUI 工具，查询 activiti 表，显示部署的 ID 和资源信息。
画面8：展示 MySQL GUI 工具，界面空白，无操作。
画面9：展示 ActivitiCompleteTask.java 文件，代码用于查询并完成任务。
画面10：展示 ActivitiCompleteTask.java 文件，代码执行后在控制台输出日志信息。
画面11：展示 AssigneeUI.java 文件，代码用于启动流程实例并设置 assignee 变量。
画面12：展示 PPT 页面，讲解如何在启动流程实例时设置流程变量，提供代码示例。
画面13：展示 PPT 页面，讲解 user 和 assignee 变量的获取方式。
画面14：展示 PPT 页面，展示流程图中“用户任务”节点的配置选项。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//1. 引擎定义
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2. 获取RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3. 部署流程
Deployment deployment = repositoryService.createDeployment()
.addClasspathResource("diagram/holiday2.bpmn") //bpmn文件
.addClasspathResource("diagram/holiday2.png")
.name("请假申请流程")
.deploy();
```

画面2：
```java
//4. 打印出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```

画面3：
```sql
1 drop database activiti;
2
3 create database activiti;
```

画面4：
```sql
ID NAME DEPLOYMENT_ID BINARY/IMAGE GENERATED
0 diagram/holiday2.png 1
```

画面5：
```java
//1. 获取ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2. 获取RuntimeService实例
RuntimeService runtimeService = processEngine.getRuntimeService();
//3. 定义assignee的值，用户可以在界面上设置当前的执行人
Map<String, Object> map = new HashMap<>();
map.put("assignee1", "zhangsan");
map.put("assignee2", "lishi");
map.put("assignee3", "wangwu");
//4. 启动流程实例，同时设置没有定义的assignee的值
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday2", map);
//5. 输出
System.out.println(processEngine.getName());
```

画面6：
```java
//5. 输出
System.out.println(processEngine.getName());
```

画面9：
```java
//1. 获取当前流程引擎的实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2. 获取TaskService实例
TaskService taskService = processEngine.getTaskService();
//3. 查询当前用户任务
Task task = taskService.createTaskQuery()
.processDefinitionKey("holiday2")
.taskAssignee("zhangsan")
.singleResult();
//4. 完成任务，结合当前用户任务完成时的ID，作为ID，task.getId()
taskService.complete(task.getId());
```

画面12：
```java
//启动流程实例时设计流程变量
//定义流程变量
Map<String, Object> variables = new HashMap<String, Object>();
//设置流程变量assignee
variables.put("assignee", "张三");
ProcessInstance processInstance = runtimeService
.startProcessInstanceByKey(processDefinitionKey, variables);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面12：PPT 标题为“2.1.2.2 流程变量”，内容为“设置流程变量”，并提供代码示例。
画面13：PPT 标题为“2.1.2.2 流程变量”，内容为“user 也是 activiti 的一个流程变量，user.assignee 表示通过调用 user 的 getter 方法获取值。”
画面14：PPT 标题为“2.1.2.2 流程变量”，内容为“UEL-method 方式如下：”，并展示流程图中“用户任务”节点的配置选项。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

