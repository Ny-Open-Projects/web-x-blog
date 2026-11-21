# 15-Activti7与SpringBoot整合-测试整个流程执行

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\15-Activti7与SpringBoot整合-测试整个流程执行_【海量资源尽在 ubkz.com】.mp4
- 时长 3分13秒（音频 193s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,刚才我们已经完成了这个任务啊那我们可以看到我们的这个MySQL数据库中啊现在呢执行的这个节点是我们的这个second对吧那我可以呢把我们的这个任务啊再让它执行一遍而这一遍执行呢我们将会看到啊我们的这个second的这个任务也会被执行完成啊比如说当我们的second的这个任务已经执行完成的时候那最终就会执行到我们的end event对吧
[00:30] 从而整个这个流程就全部都执行完了啊所以呢现在我们可以再来做一个简单的测试啊那就回到这个部分那我把我们的这个login ads的执行人我可以给他改一下啊因为我们只要是在这个activity team这个组里面的都可以对吧那现在我可以给他改成啊叫做这个名称对不对好copy一下啊然后再回到
[00:58] 看巧威,人道再来啊那这时候再去执行那我们刚才呢在执行的时候就已经执行完了对吧我呢这个时候可以重新啊再去执行一遍这个时候我们基本上就可以看到啊他再次运行的这个结果啊这次正常的这个结果呢应该是我们可以看到啊这边的这个任务呢全部都执行完了对吧我们可以再刷新一下啊
[01:28] 好,再看到这个task目前呢我们我们看见的啊好,目前我们所看见的这个这个表中现在已经执行完了啊那应该是正常来说已经没有任何的任务了所以我们正常在查询的时候呢任务一里边其实是有一个任务那这个任务就是应该是我们的这个second的这个任务对不对而任务二并没有做出任何的输出
[02:01] 任务二没有做出任何的输出的主要原因是我们这一次在做这个查询的时候它已经没有任何的这个任务要去执行了所以我们的任务二应该是不会做任何的输出因为if条件已经不再成立这就是我们基本上把这个把这个BPMN文件上的这个流程从开始到最终的这个end event节点全都给它执行了一遍
[02:31] 基本上我们就完成了整个这个流程的测试这是我们在这里边还是重点给各位强调就是这几个点吧第一个字点task这个方法可以完成我们的这个任务的查询而我们可以使用这个climb这个方法来实现我们任务的拾取通过这个complete的方法完成整个这个任务那这是我们基本上
[03:01] 给各位介绍的这个给各位介绍的这个使用activity7和splintboot整合之后啊来完成我们的这个任务的相关测试工作啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spring Boot 集成 Activiti7 实现工作流任务的查询、领取和完成操作。

2) 按时间顺序列出每张画面的要点：
画面1：展示 MySQL 数据库中 activiti 表结构，查询到一个名为 "second" 的流程定义。
画面2：展示 IDEA 中 ActivitiTest.java 代码，包含登录、分页查询任务、领取和完成任务的逻辑。
画面3：展示 BPMN 图，流程从 StartEvent 开始，经过 UserTask "task"，再到 ServiceTask "second"，最后到 EndEvent。
画面4：展示 BPMN 图编辑界面，左侧属性面板显示 "second" 任务的配置，右侧是可用的流程元素。
画面5：展示 ActivitiTest.java 代码，包含登录、分页查询任务、领取和完成任务的逻辑。
画面6：展示 ActivitiTest.java 代码，鼠标悬停在代码行上，弹出上下文菜单。
画面7：展示 ActivitiTest.java 代码，执行测试方法，控制台显示 "Instantiating beans..."。
画面8：展示 ActivitiTest.java 代码，执行测试方法，控制台显示测试通过日志。
画面9：展示 MySQL 数据库中 activiti 表结构，查询到一个名为 "second" 的流程定义。
画面10：展示 ActivitiTest.java 代码，执行测试方法，控制台显示测试通过日志。
画面11：展示 ActivitiTest.java 代码，包含登录、分页查询任务、领取和完成任务的逻辑。
画面12：展示 BPMN 图编辑界面，左侧属性面板显示 "second" 任务的配置，右侧是可用的流程元素。
画面13：展示 ActivitiTest.java 代码，包含登录、分页查询任务、领取和完成任务的逻辑。
画面14：展示 PPT 页面，标题为“第4章 Activiti7+ Spring Boot+SpringMVC 开发”，内容说明了 TaskRuntime 接口的 tasks()、claim()、complete() 方法的用途。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1 SQL：
```sql
PROC_INST_ID_ PROC_DEF_ID_ NAME BARENT_TASK_ID_ DESCRIPTION TASK_DEF_KEY_
46c01182 fa00-11c8-8005-9070b02444e4 myProcess_011:762DB915-C095-11c8-81a4-5070b02444e4 second (NULL) (NULL) _4
(NULL) (NULL) (NULL) (NULL) (NULL)
```

画面2 代码：
```java
public void testTask() {
    //1.登录
    securityUtil.loginAs("ryandaosonuk");//指定用户认证
    PageTask taskPage = taskRuntime.tasks(Pageable.of(startIndex: 0, maxItems: 10));//分页查询任务列表
    if(taskPage.getTotalItems()>0){
        //遍历任务列表
        for(Task task:taskPage.getContent()){
            System.out.println("任务1:"+task);
        }
    }
    //2.领取任务
    taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
    //3.执行任务
    taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
}
```

画面3 BPMN 图结构：
StartEvent → UserTask (task) → ServiceTask (second) → EndEvent

画面4 BPMN 图结构：
StartEvent → UserTask (task) → ServiceTask (second) → EndEvent

画面5 代码：
```java
public void testTask() {
    //1.登录
    securityUtil.loginAs("ryandaosonuk");//指定用户认证
    PageTask taskPage = taskRuntime.tasks(Pageable.of(startIndex: 0, maxItems: 10));//分页查询任务列表
    if(taskPage.getTotalItems()>0){
        //遍历任务列表
        for(Task task:taskPage.getContent()){
            System.out.println("任务1:"+task);
        }
    }
    //2.领取任务
    taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
    //3.执行任务
    taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
}
```

画面6 代码：
```java
public void testTask() {
    //1.登录
    securityUtil.loginAs("ryandaosonuk");//指定用户认证
    PageTask taskPage = taskRuntime.tasks(Pageable.of(startIndex: 0, maxItems: 10));//分页查询任务列表
    if(taskPage.getTotalItems()>0){
        //遍历任务列表
        for(Task task:taskPage.getContent()){
            System.out.println("任务1:"+task);
        }
    }
    //2.领取任务
    taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
    //3.执行任务
    taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
}
```

画面7 代码：
```java
public void testTask() {
    //1.登录
    securityUtil.loginAs("ryandaosonuk");//指定用户认证
    PageTask taskPage = taskRuntime.tasks(Pageable.of(startIndex: 0, maxItems: 10));//分页查询任务列表
    if(taskPage.getTotalItems()>0){
        //遍历任务列表
        for(Task task:taskPage.getContent()){
            System.out.println("任务1:"+task);
        }
    }
    //2.领取任务
    taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
    //3.执行任务
    taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
}
```

画面8 代码：
```java
public void testTask() {
    //1.登录
    securityUtil.loginAs("ryandaosonuk");//指定用户认证
    PageTask taskPage = taskRuntime.tasks(Pageable.of(startIndex: 0, maxItems: 10));//分页查询任务列表
    if(taskPage.getTotalItems()>0){
        //遍历任务列表
        for(Task task:taskPage.getContent()){
            System.out.println("任务1:"+task);
        }
    }
    //2.领取任务
    taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
    //3.执行任务
    taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
}
```

画面9 SQL：
```sql
PROC_INST_ID_ PROC_DEF_ID_ NAME BARENT_TASK_ID_ DESCRIPTION TASK_DEF_KEY_
46c01182 fa00-11c8-8005-9070b02444e4 myProcess_011:762DB915-C095-11c8-81a4-5070b02444e4 second (NULL) (NULL) _4
(NULL) (NULL) (NULL) (NULL) (NULL)
```

画面10 代码：
```java
public void testTask() {
    //1.登录
    securityUtil.loginAs("ryandaosonuk");//指定用户认证
    PageTask taskPage = taskRuntime.tasks(Pageable.of(startIndex: 0, maxItems: 10));//分页查询任务列表
    if(taskPage.getTotalItems()>0){
        //遍历任务列表
        for(Task task:taskPage.getContent()){
            System.out.println("任务1:"+task);
        }
    }
    //2.领取任务
    taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
    //3.执行任务
    taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
}
```

画面11 代码：
```java
public void testTask() {
    //1.登录
    securityUtil.loginAs("ryandaosonuk");//指定用户认证
    PageTask taskPage = taskRuntime.tasks(Pageable.of(startIndex: 0, maxItems: 10));//分页查询任务列表
    if(taskPage.getTotalItems()>0){
        //遍历任务列表
        for(Task task:taskPage.getContent()){
            System.out.println("任务1:"+task);
        }
    }
    //2.领取任务
    taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
    //3.执行任务
    taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
}
```

画面12 BPMN 图结构：
StartEvent → UserTask (task) → ServiceTask (second) → EndEvent

画面13 代码：
```java
public void testTask() {
    //1.登录
    securityUtil.loginAs("ryandaosonuk");//指定用户认证
    PageTask taskPage = taskRuntime.tasks(Pageable.of(startIndex: 0, maxItems: 10));//分页查询任务列表
    if(taskPage.getTotalItems()>0){
        //遍历任务列表
        for(Task task:taskPage.getContent()){
            System.out.println("任务1:"+task);
        }
    }
    //2.领取任务
    taskRuntime.cl

