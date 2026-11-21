# 画面线理解：15-Activti7与SpringBoot整合-测试整个流程执行

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\15-Activti7与SpringBoot整合-测试整个流程执行_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:20, 00:24, 00:38, 00:57, 01:10, 01:18, 01:20, 01:23, 01:51, 02:04, 02:23, 02:40, 03:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:44:00

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
画面14：展示 PPT 页面，标题为“第4章 Activiti7+ SpringBoot+SpringMVC 开发”，内容说明了 TaskRuntime 接口的 tasks()、claim()、complete() 方法的用途。

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
