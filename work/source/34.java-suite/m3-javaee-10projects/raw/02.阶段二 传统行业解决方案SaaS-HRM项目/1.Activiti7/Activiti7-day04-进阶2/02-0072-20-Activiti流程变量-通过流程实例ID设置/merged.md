# 20-Activiti流程变量-通过流程实例ID设置

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\20-Activiti流程变量-通过流程实例ID设置_【海量资源尽在 ubkz.com】.mp4
- 时长 9分23秒（音频 563s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们一起来学习一下我们Global类型的流程变量它的第三种设置方式那就是通过我们当前的流程实例来进行设置这个具体怎么样来做我们大致看一下步骤首先第一个我们把这个Runtime Service拿到然后我们去给我们的流程变量设置一个定一个具体的这样的变量
[00:27] 然后再通过run time serviceset variable的方式主要呢第一个参数是我们的这个流程实例的ID第二个是我们的key第三个是它所对应的value那这样做只能够一次性设置一个对象那如果要一次性设置多个对象的话我们可以考虑用set variables这样的话我们的第二个参数依然为一个map类型的集合
[00:56] 好我们大致上可以一起来测试看一下效果那我们再回到这个类上面来可以这样做我呢先在这里面把我们的这个test改一个名叫做Valuable Test 3我们的第三种方式这种方式具体怎么样来操作第一个我们基本上按这个顺序来改就可以了第一个呢我们先将这个卖方法先给它跑起来
[01:27] 可以吧你比如说如果我们要这样做的话那我们可以把这个地方给它改一下这样呢我们就来跑我们的第一个部分就是我们的这个流程流程定义的部署为了能够重新去发布我们的这个流程定义那我们在这边呢应该说我之前做了一个前期的操作就是把我们的这个库重新给它创建了一下
[01:55] 那下面我们就可以直接啊重新再来部署一把对吧因为我希望啊我们能够看到更加直观的这个效果啊好这边这个库就已经部署好了啊我们再回到这边刷新一下对吧这个表就已经好了啊而且呢我们去观察我们的这个BitArray这张表呢应该说我们的这个流程定义的BPMN文件和PNG文件都已经部署进来啊那下面呢
[02:25] 我们开始来做下一个环节那下一个环节主要的工作是做什么我们一起来看一下我们应该是流程部署完了我们就应该要去启动我们的这个流程对不对启动一个流程实例那启动流程实例我们可以按原有的这个方法直接在这里要这样走但是我们这一次要做的目标是希望通过流程实例的ID来设置我们的全局变量对吧
[02:55] 那我们就应该要有这个具体的这个流程实例对吧当然这个流程实例肯定是必须没有没有执行完成啊如果已经执行完毕了那这个流程实例都执行完毕了那你这个变量都还没设置肯定是不行的对吧所以呢我们在这个地方我就先还是来做我们的这个流程实例的启动啊那启动的过程中我为了能够看到我们的这个实例的ID
[03:25] process.instance.getid对吧那这样将来我们就能够知道它的这个ID号是多少了对不对好我们这个时候重新再执行显然啊这次我们在启动流程实例的时候并没有去设置它的变量所以说我们的这个battery这个表中应该不会多出我们变量的值对吧或者是这个表中不会多出变量的值啊那我们可以一起来看一下啊这个如果它执行完了对不对
[03:55] 我们变量RuValue中并没有任何的记录说明我们并没有设置我们的这个流程变量对吧那下面我们就开始来设置我们的这个流程变量好为了能够做这个流程变量的设置我在这里边需要去专门再去搞出一个新的方法好比如说我这样做我这样做Prop复制一下那这个部分刚才是我们已经用过的一个方法
[04:25] 那现在我在这里头再给各位加出一个方法它的这个主要作用是这是我们新加入的新加入的那它的这个主要作用就是在我们的这个通过通过我们的这个流程实例的ID来来测试我们的这个流程变量测试我们的流程变量好那现在我把这个方法直接复制过来了那把它去掉对不对
[04:55] 那它就可以运行了那它运行的时候我们呢如果只是设置一个变量的话大家注意啊我们如果设置一个变量的话这个MAP集合的这两行其实我们都可以不要对不对然后呢我们还有一个就是要去知道我们的当前这个变量我们刚刚啊跑的这个流程实例它的这个它的这个Process Instance ID
[05:23] 我们具体等于多少对不对各位可以看到是2501对吧那我们呢就相当于在这边呢我们可以我们可以做一个这样的工作啊因为我们的流程实例已经启动完成了对吧已经启动完成了那现在我就直接通过我们的这个这个呢就不叫启动流程实例了啊是通过我们的这个实例的ID来设置我们的这个流程变量啊
[05:53] 这是我们想要达到的目标那我就可以通过run time Service里头有一个setValue的方法那各位可以看到我们直接可以用这个方法如果说你要一次性设置多个变量那你应该用setValue之setValue之然后第二个参数是一个map激活而map激活中就可以指定多个key和value的建筑队那如果说你只是设置一个变量那我们用这个其中第一个参数
[06:23] 为我们的实力ID第二个参数为我们的这个变量的key第三个参数就是变量的value值了是这个意思啊那我们刚才已经看了我们的这个变我们的这个实力的实力的这个ID是2501对吧好我在这里头给各位写一下啊我们的第一个参数啊第一个参数为我们的这个流程啊实力流程啊实力的ID而我们的第二个参数
[06:53] 第二个第二个参数啊这个就代表的是我们的这个流程啊变量流程变量的名称第三个参数就是啊我们的这个第三个参数啊就是这个变量所对应的值啊就是流程变量啊流程变量所对应的所对应的value啊所对应的这个值这个意思啊
[07:20] 那我们现在就可以来给出我们的第二个参数第一个参数是2501是我们的实力ID这个部分在刚才这个人就可以看到对吧然后我们现在来看第二个参数第二个参数呢我们当时起的这个流程我们的这个流程上是不是应该是一个叫做holiday的一个这样的变量所以这是我们的这个key而真正对的value值就是我们这里头设置的这个对象对不对通过这种方式呢我们也一样可以完成
[07:50] 我们在知道我们的实例在知道我们的实例ID的情况下我们一样也可以通过这种方式来设置我们的流程变量好我们执行一把来看一下这个直媒执行成功我们只要去观察我们的这个RUValue各位同学可以看到又多了一个Servizable对吧
[08:18] 因为我们是一个Holiday的对象存进来的这个对象具体存在了存在我们的ByteArray这时候各位就可以看到有一个变量Holiday它就存好了这样我们基本上完成了我们的第三种方式来设置我们的流程变量它是在我们的通过Runtime来设置这种方式一次性只能设置一个Key和Value
[08:43] 如果是多过key和value我们应该用这个setValue保值这个方法而第二个参数是一个map集合map集合中再去指定多过建制队这样我们就可以一次性做到多过建制队也就是多过流程定义变量一次性复制这个要注意的一点刚才我们也说了就是你这个流程实力不能够必须是未执行完成对不对要不然的话这个变量将来你设置的话这个实力都跑完了那肯定不行对吧
[09:12] 这是我们刚才给各位又讲了一下我们的具体如何设置以及设置的具体的注意事项对不对

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

