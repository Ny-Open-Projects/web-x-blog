# 05-Activiti实现资源文件保存的实现步骤

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\05-Activiti实现资源文件保存的实现步骤_【海量资源尽在 ubkz.com】.mp4
- 时长 7分15秒（音频 435s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才我们已经将我们的需求就是读取我们的两个资源文件已经说清楚了,以及我们的技术方案对吧,应用的背景都说好了那现在我们就开始来看一下实现的步骤好,我们现在呢在这个里头把具体的步骤给各位写一下那第一步,我们不管怎么样我们应该都要去得到我们的Process Engine的对象Process Engine的对象
[00:27] 第二个步骤我们要做的工作就是得到我们因为我们这一次要查询的是我们的这个资源文件的信息对吧那通过我们前边的这个介绍啊我们的这个资源文件是放在我们的这个byte array这个这个这个这个表里头对吧所以呢现在我们要得到的是关我关于我们的这个部署相关的这个Service对吧因为我们在做部署的时候当时给各位说过啊
[00:55] 会影响的是我们的deployment表PLC以及我们的这个byte array这个表对不对所以呢现在呢我们要去读取byte array这个表中的数据那肯定就需要去需要去用到我们有一个对象那就是叫做相关的Service对吧那这个Service是什么呢叫做repository Service好那我们要获取到一个这样的对象
[01:22] 当这个对象得到那下一步我们就可以去得到一个查询这个表里头的有一个查询器那就得到我们的一个查询器那我们其实主要就是查什么的一个查询器呢我们查是查我们的这个流程定义信息对不对流程定义信息所以呢我们这边就需要去用到一个叫做流程啊定义
[01:51] 然后是查询器Q类对象啊得到一个这样的对象这是我们的第三个步骤第四个步骤那我们在得到这个执行器查询器之后啊那我们其实下一个步骤就可以去设置我们的这个查询条件设置我们的查询条件啊这是我们的第四个步骤那第五个步骤当我们的这个条件设置好第五个步骤我们就可以去真正的执行我们的这个查询操作啊
[02:20] 执行一次查询操作那执行这个查询操作最终我们就可以查询出我们想要的查询出啊想要的我们的这个查询这个这个流程定义啊查询出我们想要的流程定义啊而这个流程定义中肯定就会携带有我们的这个BPMN文件的信息和我们的PNG文件的信息啊这是第五个步骤第六个步骤
[02:50] 当我们把这个流程定义都查出来那我们就可以去得到我们的这个部署的ID号那就是通过我们的流程定义通过流程定义信息得到部署ID得到部署ID那有的人会思考这个工作我们之前做过没有呢通过我们的这个流程定义信息去得到我们的这个
[03:19] 部署的ID我们一起来看一下在早期我们做这个应该是有在实现我们的这个我找一下给各位找一下我们的这个Service各位可以看一下我们在做这个Service start instance的时候我们当时是通过这个是得到这个部署ID是通过runtime去得到的
[03:47] 那其实我们通过我们的这个流程定义信息也是可以同样可以得到我们的这个部署ID的啊我们可以看一下啊好这里头这里头我们直接是拿到1来做这个操作的对吧那如果说我们如果说我们不知道这个部署的ID那我们就需要去得到这个部署的ID各位可以看一下啊我们是在叫做processqliprocessdefinition在实现我们的这个
[04:16] 流程定义信息查询的时候我们其实这样的代码呢在前期已经给各位写过啊已经写过这样的代码所以其实这几个步骤都不是什么新的步骤对吧好我们再次切换到我们的这个切换到我们的这个BPMN文件的查询啊所以说呢这里面的这几个步骤都是我们之前已经学习过的啊大家可以参考一下我们的这个
[04:44] true process definition查询我们的这个流程定义啊就可以得到这个步骤那第七个步骤来了啊这个步骤相对于来说呢我们应该可以认为是一个新的步骤啊这个新的步骤就是通过我们的这个reported Service通过我们的这个repositoryreported Service的方法通过reported Service的
[05:15] 方法实现读取我们的图片信息实现读取我们的图片信息及我们的BPMN文件信息这就是我们要做的工作所以第七个步骤对于我们来说是新学习的一个步骤怎么去读通过Repository的哪个方法去读我们一会会详细给各位介绍一下当我读取到这个
[05:45] BPMN和文件的这个信息注意这里边这个文件信息主要就是流它是一个流是一个我们的这个输入流输入流input string那下一步我们就可以构造我们的这个alt put string对吧从而来实现我们的这个文件的读写对吧所以第八个步骤呢就是构造出我们的这个叫做alt put string
[06:14] output stream流那所以这是第八个步骤当我们构建了这样的流之后第九个步骤就是只需要去实现输入流与输出流的转换就可以实现我们真正的文件读写那就是我们的这个输入流输入流输出流的转换要说将输入流中这些数据的直接往具体的某一个文件中去实现输出对吧
[06:43] 这样我们就实现了向指定的某个目录下去实现去实现我们的这个文件的保存最后一个步骤那就是叫做关闭我们的关闭我们的这个流对吧关闭我们的这个输入流也好输出流也好我们都可以对它进行关闭这是我们对于activity来实现我们的这个BPMN文件以及我们的这个PNG文件
[07:11] 具体操作的大致步骤就是这样的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Activiti 工作流引擎的 API 查询、启动、完成任务及删除流程定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 QueryBpmFile.java 文件，注释说明了两种获取流程定义的方式，当前聚焦于第一种方式（使用 Activiti API）。代码中展示了 public class QueryBpmFile {} 的结构。
画面2：在 QueryBpmFile.java 中，光标位于 public class QueryBpmFile { 语句后，弹出 Java 类的继承方法列表，如 protected Object clone() 等。
画面3：在 QueryBpmFile.java 中，光标位于 main 方法的开头，注释提示“//1.博到ProcessEngine实例”，准备开始编写代码。
画面4：切换到 MySQL Workbench，展示 act_hi_taskinst 表的查询结果，包含 ID、NAME、DEPLOYMENT_ID_、SUSPENSION_STATE_ 等字段。
画面5：在 QueryBpmFile.java 中，光标位于 main 方法的注释“//5.执行查询操作，查询出想要的流程定义”处，准备编写查询逻辑。
画面6：切换到 ActivitiCompleteTask.java 文件，展示如何通过 TaskService 创建并完成一个任务，代码中包含 processEngine.getTaskService()、createTaskQuery()、complete() 等方法。
画面7：在 ActivitiCompleteTask.java 中，光标位于 taskService.complete(task.getId()); 语句后，展示任务完成后的输出。
画面8：切换到 ActivitiStartInstance.java 文件，展示如何通过 RuntimeService 启动流程实例，代码中包含 startProcessInstanceByKey("holiday") 方法。
画面9：切换到 DeleteProcessDefinition.java 文件，展示如何通过 RepositoryService 删除流程部署，代码中包含 deleteDeployment(deploymentId) 方法。
画面10：切换到 QueryProcessDefinition.java 文件，展示如何通过 RepositoryService 查询流程定义，代码中包含 createProcessDefinitionQuery().processDefinitionKey("holiday").orderByProcessDefinitionVersion().desc().list() 方法。
画面11：在 QueryBpmFile.java 中，光标位于 main 方法的注释“//5.执行查询操作，查询出想要的流程定义”处，准备编写查询逻辑。
画面12：在 QueryBpmFile.java 中，光标位于 main 方法的注释“//5.执行查询操作，查询出想要的流程定义”处，准备编写查询逻辑。
画面13：在 QueryBpmFile.java 中，光标位于 main 方法的注释“//7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)”处，准备编写获取流程定义信息的代码。
画面14：在 QueryBpmFile.java 中，光标位于 main 方法的注释“//8.转换成OutputStream流”处，准备编写将流程定义信息转换为输出流的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.ithema.day03.activiti;

/**
 * 1.从Activiti的act_ge_bytearray表中读取两个流程文件
 * 2.按两个流程文件的名称分别到目录：/Activiti/开始/Activiti/day01/资料
 * 技术方案：
 * 1.第一种方式：其实就是使用activiti的api来实现
 * 2.第二种方式：其实就是直接读取，可以使用jdbc的blob类型，clok类型读取数据，并保存
 * 10万条数据，最好commons-io.jar可以轻松解决此问题
 * 真实应用场景：用户想要查看这个请假流程有没有哪些步骤变更？
 *
 * public class QueryBpmFile {
```

画面2：
```java
public class QueryBpmFile {
    protected Object clone()
    public boolean equals(Object obj)
    public int hashCode()
    public String toString()
    protected void finalize()
    static final
    private static final
    main() method declaration
```

画面3：
```java
public class QueryBpmFile {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
    }
```

画面4：
SQL 查询语句未显示，但表结构显示：
```sql
SELECT * FROM act_hi_taskinst;
```

画面5：
```java
public class QueryBpmFile {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        //2.博到RepositoryService对象
        //3.博到查询器：ProcessDefinitionQuery对象
        //4.设置查询条件
        //5.执行查询操作，查询出想要的流程定义
        //6.通过流程定义信息，得到部署ID
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.转换成OutputStream流
        //9.输入流，输出流的转换
    }
```

画面6：
```java
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.博到TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.查询当前用户任务
        Task task = taskService.createTaskQuery()
                .processDefinitionKey("holiday")
                .taskAssignee("wanggu")
                .singleResult();
        //4.处理任务，结合当前用户任务的完成操作的流，任务ID.task.getId()
        taskService.complete(task.getId());
        //5.输出任务的id
        System.out.println(task.getId());
    }
}
```

画面7：
```java
//1.博到ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.博到TaskService对象
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户任务
Task task = taskService.createTaskQuery()
        .processDefinitionKey("holiday")
        .taskAssignee("wanggu")
        .singleResult();
//4.处理任务，结合当前用户任务的完成操作的流，任务ID.task.getId()
taskService.complete(task.getId());
//5.输出任务的id
System.out.println(task.getId());
```

画面8：
```java
public class ActivitiStartInstance {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.博到RuntimeService对象
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.创建流程实例，流程定义的key需要是 holiday
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
        //4.输出流程实例ID
        System.out.println("流程实例ID:"+processInstance.getId());
        //5.输出流程定义ID
        System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());
        //6.输出活动ID
        System.out.println("活动ID:"+processInstance.getActivityId());
    }
}
```

画面9：
```java
public class DeleteProcessDefinition {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.博到RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.删除流程部署，删除流程部署ID
        repositoryService.deleteDeployment(deploymentId);
    }
}
```

画面10：
```java
public class QueryProcessDefinition {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.博到RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.博到查询器：ProcessDefinitionQuery对象
        ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
        //4.设置条件：查询所有流程定义，查询方式：按流程定义的key查询
        List<ProcessDefinition> list = processDefinitionQuery.processDefinitionKey("holiday")
                .orderByProcessDefinitionVersion().desc().list();
        //5.输出流程定义信息
        for(ProcessDefinition processDefinition : list){
            System.out.println("流程定义ID:"+processDefinition.getId());
            System.out.println("流程定义的key:"+processDefinition.getKey());
            System.out.println("流程定义的版本:"+processDefinition.getVersion());
            System.out.println("流程部署的ID:"+processDefinition.getDeploymentId());
        }
    }
}
```

画面13：
```java
public class QueryBpmFile {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        //2.博到RepositoryService对象
        //3.博到查询器：ProcessDefinitionQuery对象
        //4.设置查询条件
        //5.执行查询操作，查询出想要的流程定义
        //6.通过流程定义信息，得到部署ID
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.转换成OutputStream流
        //9.输入流，输出流的转换
    }
}
```

画面14：
```java
public class QueryBpmFile {
    public

