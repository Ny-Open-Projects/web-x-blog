# 画面线理解：20-Activiti流程变量-通过流程实例ID设置

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\20-Activiti流程变量-通过流程实例ID设置_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:18, 01:39, 01:58, 02:10, 02:35, 03:35, 04:11, 04:50, 05:38, 06:20, 07:29, 07:58, 08:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:05:33

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎中通过 Java 代码设置流程变量，包括设置局部变量、全局变量以及通过流程实例 ID 设置变量等操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“3.5.3.3 通过当前流程实例设置”章节内容，代码示例为通过流程实例 ID 设置全局变量，代码为：
public void setGlobalVariableByExecutionId(){
    //当前流程实例执行 Id，通常设置为当前执行的流程实例
    String executionId = "2601";
    RuntimeService runtimeService = processEngine.getRuntimeService();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    //通过流程实例 Id设置流程变量
    runtimeService.setVariable(executionId, "holiday", holiday);
    //一次设置多个值
    //runtimeService.setVariables(executionId, variables)
}

画面2：展示在 IntelliJ IDEA 中的 VariableTest3.java 文件，代码为：
public static void main(String[] args) {
    //1.获取流程引擎
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RepositoryService对象
    RepositoryService repositoryService = processEngine.getRepositoryService();
    //3.部署
    Deployment deploy = repositoryService.createDeployment()
            .addClasspathResource("diagram/holiday4.bpmn")
            .addClasspathResource("diagram/holiday4.png")
            .name("请假流程-流程安装")
            .deploy();
    System.out.println(deploy.getId());
    System.out.println(deploy.getName());
}

画面3：展示 VariableTest3.java 文件，代码为：
public static void main(String[] args) {
    //1.获取流程引擎
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RepositoryService对象
    RepositoryService repositoryService = processEngine.getRepositoryService();
    //3.部署
    Deployment deploy = repositoryService.createDeployment()
            .addClasspathResource("diagram/holiday4.bpmn")
            .addClasspathResource("diagram/holiday4.png")
            .name("请假流程-流程安装")
            .deploy();
    System.out.println(deploy.getId());
    System.out.println(deploy.getName());
}

画面4：展示 VariableTest3.java 文件，代码为：
public static void main(String[] args) {
    //1.获取流程引擎
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RepositoryService对象
    RepositoryService repositoryService = processEngine.getRepositoryService();
    //3.部署
    Deployment deploy = repositoryService.createDeployment()
            .addClasspathResource("diagram/holiday4.bpmn")
            .addClasspathResource("diagram/holiday4.png")
            .name("请假流程-流程安装")
            .deploy();
    System.out.println(deploy.getId());
    System.out.println(deploy.getName());
}

画面5：展示 MySQL 命令行界面，执行的 SQL 语句为：
drop database activiti;
create database activiti;
act_ge_bytearray
act_ru_variable

画面6：展示 VariableTest3.java 文件，代码为：
public static void main(String[] args) {
    //1.获取流程引擎
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService对象
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值 myProcess_1
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    map.put("holiday", holiday);
    //4.启动流程实例
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key);
    //5.输出流程信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
    System.out.println(processInstance.getId());
}

画面7：展示 VariableTest3.java 文件，代码为：
public static void main(String[] args) {
    //1.获取流程引擎
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService对象
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值 myProcess_1
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    map.put("holiday", holiday);
    //4.启动流程实例
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key);
    //5.输出流程信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
    System.out.println(processInstance.getId());
}

画面8：展示 VariableTest3.java 文件，代码为：
public static void main(String[] args) {
    //1.获取流程引擎
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService对象
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值 myProcess_1
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    map.put("holiday", holiday);
    //4.启动流程实例
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key);
    //5.输出流程信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
    System.out.println(processInstance.getId());
}

画面9：展示 VariableTest3.java 文件，代码为：
Map<String, Object> map = new HashMap<>();
Holiday holiday = new Holiday();
holiday.setNum(3);
if(task != null){
    taskService.complete(task.getId(), map); //完成任务时，设置流程实例变量
    System.out.println("任务执行完毕");
}
//有加班时：通过流程实例id，来修改流程变量

画面10：展示 VariableTest3.java 文件，代码为：
public static void main(String[] args) {
    //1.获取流程引擎
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService对象
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值 myProcess_1
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    map.put("holiday", holiday);
    //4.启动流程实例
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key);
    //5.输出流程信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
    System.out.println(processInstance.getId());
}

画面11：展示 VariableTest3.java 文件，代码为：
public static void main(String[] args) {
    //1.获取流程引擎
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService对象
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值 myProcess_1
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    map.put("holiday", holiday);
    //4.启动流程实例
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key);
    //5.输出流程信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
    System.out.println(processInstance.getId());
}

画面12：展示 VariableTest3.java 文件，代码为：
public static void main(String[] args) {
    //1.获取流程引擎
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService对象
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值 myProcess_1
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    map.put("holiday", holiday);
    //4.启动流程实例
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key);
    //5.输出流程信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
    System.out.println(processInstance.getId());
}

画面13：展示 VariableTest3.java 文件，代码为：
public static void main(String[] args) {
    //1.获取流程引擎
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService对象
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值 myProcess_1
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    map.put("holiday", holiday);
    //4.通过流程实例id，来设置流程变量
    runtimeService.setVariable("2581", "holiday", holiday);
    //5.输出流程信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
    System.out.println(processInstance.getId());
}

画面14：展示“3.5.3.3 通过当前流程实例设置”章节内容，代码为：
public void setGlobalVariableByExecutionId(){
    //
