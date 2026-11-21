# 22-请假流程：流程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\22-请假流程：流程分析_【海量资源尽在 ubkz.com】.mp4
- 时长 11分34秒（音频 695s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们简单的对请假流程发起提交等等的环节呢做了一个测试那接下来呢我们就以这个流程为例简单的来看一下我们代码处理上的一些细节问题以及它的一个流转过程那首先呢就是在这边咱们要说明的是页面上这边不管是全部我发起的代审批咱们查询的是不是都是我们自己的流程实例表啊好了那在这边我以一个
[00:32] 图形的形式和各位来分析一下好了这边是我们的业务流程这个表这个业务流程表proc下划线instanceinstance这么一张表那这张表里面呢有很多的字段那其中会有咱们的一些业务字段比如说id这个不用多啰嗦了那除了这个之外会有状态的这么一个字段那除了状态字字段还有发起人以及我们这边哎
[01:01] 代处理人当然了我们叫做当前节点的处理人就叫做代处理人可以吧好了那接下来呢这个状态呢其实有很多比如说呢有一代表的是沈和中好了那接下来二代表的是通过那三代表的是驳回四代表的是撤销没错吧撤销撤销好了那接下来呢发起人这个不用多啰嗦了
[01:31] 这边有一个代处理人那接下来呢咱们这个代处理人就是说你发起了之后下一个下一个节点应该交给谁处理所以呢由于我们的数据库表里面有了这些字段那我们整个页面上不管是全部我发起的代审批的其实都是用刚才咱们分析的这几个字段来处理就够了那如果是我发起的那我们只需要查询这边发起人等于ABC的是不是就可以啊
[02:01] 如果是你要查询代处理的代审批的那代审批是不是就处理一下我这个代审批人是谁是不是就可以了没错吧好了这个就是我们查询上面的一些细节问题那除了查询之外接下来呢我们这边要做请求的一个申请流程的申请所以接下来呢回到我们这边接下来就来看一下就是流程申请那流程申请把我们的所有的请求会发送到
[02:31] 把我们的请求会发送到我们的Service当中当然了我们是经过了咱们这边的Controller回到代码里找到我们这边找到对应的Controller流程申请那流程申请进入到startporsche好了进来之后上面就是构造一些数据这个没什么可说的我们要开启流程就是查询流程定义接着开启流程接着自动获取第一个节点处理节点
[03:03] 没错了那第一个节点我们处理完成了之后接下来我是不是又为了获取下一个节点的数据来了一个下一个节点那这边呢需要各位一定一定要注意最最专业的最最重要的就是流程申请当中咱们有三步第一个就是处理处理业务数据好了那接着第二件事第二件事呢就是我们开启我们的ACTI VITI流程
[03:30] 这个是第三步并且处理我们的当前审批节点审批节点好了这是我们的第二步那注意第三步是我们最最最最关键的因为为了我们这边能够查询出待处理的这个订单在待处理的这些流程我们在这边是不是需要对待处理这个人员的字段附上值没错吧所以怎么办呢我们就是查询下一个节点因为我们上边把第一个节点处理掉了
[03:57] active里面自动就会流转到下一个节点我们查询下一个节点那查询下一个节点我们的方法呢刚才也说过了这个不用我们多啰嗦那在下一个节点里面会有很多的数据那这些数据呢我们叫做identity links那代表的是我们的候选人组那根据我们之前的处理回到我们的数据库里面以咱们刚才
[04:28] 的请假流程为例请假流程请假流程我们来看一下那请假流程提交申请我们处理完了之后接下来呢初审是不是进入到这么一个哎抱歉不是这个是这个初审呢是不是进入到一个Parses利用初user啊所以我们这边把它拿过来回到这边利用初user这是初审哎那接下来呢还有一个利用副user这个是我们的副审
[05:10] 好了那接下来呢还有一个力物Puser这个代表的是我们的最终审批那注意那对于我们来说呢其实这一共有四个第一个叫做upline就是申请申请没错吧一共有这么四个节点那我们一发起请求的时候那我们这边的申请节点是不是就已经处理完成了那处理完成了之后
[05:38] 张三发起一个那接下来发起了之后代处理人是不是就应该是初审阶段那我们的初审阶段是什么其实就是我们自己定义的定义的流程发起人的部门主管没错了好了那接下来呢咱们能够通过下一个流程注意得到的其实是左边这句话那得到了左边的这句话就在这儿得到了这么一个玩意儿那这个玩意儿从哪来怎么得那注意啊
[06:11] 那在我们这边我们自己创建了一个数据库的表是我们的业务数据库表拿过来这个表呢叫做groupgroup那这玩意儿你会发现对应的是这么一大堆东西没错了所以呢根据他们之间这个对应关系你拿到了下一个节点这个名字那这个节点的名字对应的其实在我们这边利用出user那这边是不是一条私人语句啊没错了
[06:45] 所以呢,我们的执行很简单,就是根据下一个节点的候选组获取我们的带执行Circle语句。
[06:58] 那这个Circle语句究竟是什么呢?
[07:03] 咱们来看一下,回到我们这边的数据库,那Circle语句在这儿,底下在这儿,那这条Circle语句拿上来。
[07:18] Select Manager起这个编名User NameManager ID起这个编名ID那CO Department那后面你会发现我们自己定义了一个条件那这个条件从哪来这个代表的就是我们的当前用户当前申请用户的部门ID那我们这边通过Java代码的形式做了一个替换各位会发现没错吧那这边做了一个替换那这个值从哪来各位来看是不是User这个人的部门ID
[07:48] 你会发现把user这个人的部门ID替换到了我们这条sql上那user是什么部门我们就查询什么部门那在我们的部门当中这个是我们的部门表CO department在这个CO department各位来看其中我们发起的就是这一条部门ID就是这玩意儿那我们得到的是什么呢得到的就是这里面的manager得到的是里面的manager ID而这个代表的是部门的主管可以吧那这样一来呢咱们第一个
[08:21] 发起流程申请的时候我们就已经获取了部门主管的内容接着把部门主管的这个名称放到代处理人这边比如说我们就得到的是ITCAS当然了还有user ID那这样一来流程申请我们搞定了接下来还有一个流程的叫做审批那流程审批呢其实是同样的道理那首先的流程审批第一项就是我们要区分一下我们这个审批的
[08:55] 流程提交啊就是区分一下区分我们的这个操作类型那我们只对只对操作只对操作类型等于二的完成只对操作类型等于二的代表的是我们的审批通过审批通过那其他的类型呢我们这回就代表的是这个流程已经结束了那我们这边的做法就是删除流程
[09:29] 好了各位回到我们的代码当中再来看一下commit如果是2我们才做处理剩下的全部都是认为流程结束没错吧好了那接着来就是说呢在我们这边如果是2的话我们怎么做那接下来呢就是处理当前节点就把它完成掉那完成掉了之后比如说itcast已经完成了那itcast完成了之后接下来呢是不是要流转到刚才我们测试的ll来完成那这个ll是不是也要查询出来啊
[10:00] 那所以这边的处理是不是跟刚才一样接下来第三个就是查询下一个节点那这边呢做一个判断如果有如果存在那这个时候呢就是根据刚才流程查询sircow执行sircow然后呢替换我们的代处理人没错吧如果如果如果不存在那这个时候呢我们就认为认为流程已经结束了其实就是这么一个处理的一个逻辑在里面
[10:30] 那其实在我们这边最最最最重要的没别的其实就是这条Circle语句那这条Circle语句在我这边呢其实是我一条一条自己已经写好的那我们可以来验证一下那比如说刚才请假初审用户组查询的是部门找到当前登录用户部门的主管那复审用户组那我这边查询的直接就查询的user因为user里面咱们用户表里面是不是有当前所在部门啊
[10:58] 没错了那我根据部门ID查询一下那这个部门呢咱们根据我们的流程分析得知这玩意儿代表啥呢代表的是所有的人事部门那这样一来我查询的就是所有人事部门的用户那最后这个流程代表的是如果三天以上我要查询一下总裁办所有的人员其实就是这个流程当然了除了我们这个请假流程之外什么加班什么离职其实都是一样的
[11:25] 重点不是刚才的那些代码了重点其实就是说你要流转到哪把circle与g对应的补全上就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 和 Activiti 的请假审批系统，从前端界面操作到后端代码实现，再到数据库表结构和流程定义的配置过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 iHRM 系统的员工请假审批主界面，左侧导航栏选中“员工”下的“审批”，右侧显示“工作日历”和“快捷入口”按钮。
画面 2: 点击“待审批”标签页，显示审批列表，包含“审批类型”和“审批状态”筛选条件，当前无数据。
画面 3: 点击“申请”按钮，弹出请假申请表单，可选择请假类型、开始/结束日期、时长等。
画面 4: 在 IntelliJ IDEA 中打开 `AuditService.java` 文件，展示处理审批流程的 Java 代码，包含 SQL 查询和流程状态处理逻辑。
画面 5: 在 IntelliJ IDEA 中展示 `ProcessController.java` 文件，重点是 `startProcess` 方法，用于启动流程实例并设置流程变量。
画面 6: 继续展示 `AuditService.java` 文件，代码逻辑包括获取下一个节点、查询用户、设置流程节点用户等。
画面 7: 在 IDEA 中打开 `process_leave.bpmn` 文件，展示请假流程的 BPMN 2.0 XML 定义，包含多个用户任务和条件流。
画面 8: 在 IDEA 中继续编辑 `process_leave.bpmn` 文件，对流程定义进行调整，添加条件判断。
画面 9: 在 SQLyog 中打开数据库，查看 `pro` 表结构，准备执行 SQL。
画面 10: 在 SQLyog 中查询 `pro` 表，显示多个请假流程的定义，包括 `PROCESS_LEAVE_APPLY_USERS`、`PROCESS_LEAVE_CHU_USERS` 等。
画面 11: 在 Word 文档中绘制请假流程图，标注了“审批中”、“通过”、“驳回”、“撤销”四个状态，以及“PROCESS_LEAVE_CHU_USERS”等节点。
画面 12: 在 Word 文档中继续编辑流程图，添加“根据下一个节点的筛选组执行SQL语句”的说明。
画面 13: 在 Word 文档中进一步完善流程图，添加“如果不存在，认为流程结束”的说明。
画面 14: 在 SQLyog 中执行 SQL 查询，查询 `pro` 表中 `PROCESS_LEAVE_CHU_USERS` 的数据，结果为 NULL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4 代码：
```java
else if ("company_id".equals(param)) {
    paramValue = user.getCompanyId();
    String sql = userGroup.getSql().replaceAll(regex, paramValue);
    query = entityManager.createNativeQuery(sql);
    query.unwrap(NativeQueryImpl.class).setResultTransformer(Transformers.aliasToBean(User.class));
    users.addAll(query.getResultList());
}
return users;
```
画面 5 代码：
```java
public void startProcess(Map map, String companyId) {
    //1.构造业务数据
    String userId = (String) map.get("userId");
    String processKey = (String) map.get("processKey");
    String processName = (String) map.get("processName");
    User user = feignClientService.getUserInfoByUserId(userId);
    ProcInstance instance = new ProcInstance();
    BeanUtils.copyProperties(user, instance);
    instance.setUserId(userId);
    instance.setProcessId(Workflow.nextId()+"");
    instance.setProcessKey(processKey);
    instance.setProcessName(processName);
    instance.setProcessState("1");
    String data = JSON.toJSONString(map);
    instance.setProcessData(data);
    //2.查询流程定义
    ProcessDefinition definition = repositoryService.createProcessDefinitionQuery()
            .processDefinitionKey(processKey)
            .processDefinitionTenantId(companyId)
            .latestVersion()
            .singleResult();
    //3.开启流程实例
    Map vars = new HashMap();
    if ("process_leave".equals(processKey)) {
        vars.put("days", map.get("duration"));
    }
    ProcessInstance processInstance = runtimeService.startProcessInstanceById(definition.getId(), instance.getProcessId(), vars);
    //4.自动跳转第一个节点
    Task task = taskService.createTaskQuery()
            .processInstanceId(processInstance.getId())
            .singleResult();
    //5.获取第一个节点数据，填充当前审批人
    Task next = taskService.createTaskQuery()
            .processInstanceId(processInstance.getId())
            .singleResult();
    if (next != null) {
        List<User> users = findCurrUsers(next, user);
        String usernames = "";
        for (User user1 : users) {
            usernames += user1.getUsername() + ",";
            userIds += user1.getId();
        }
        instance.setProcCurrNodeUserIds(userIds);
        instance.setProcCurrNodeUserName(usernames);
        procInstanceDao.save(instance);
        ProcTaskInstance pti = new ProcTaskInstance();
        pti.setTaskId(Workflow.nextId()+"");
        pti.setProcessId(instance.getProcessId());
        pti.setProcInstance(instance);
        pti.setProcTaskId(next.getId());
        pti.setProcTaskName(next.getName());
        pti.setProcTaskType(next.getTaskType());
        pti.setProcTaskAssignee(next.getAssignee());
        pti.setProcTaskCreateTime(new Date());
        pti.setProcTaskUpdateTime(new Date());
        pti.setProcTaskStatus("1");
        pti.setProcTaskComment("");
        pti.setProcTaskPriority(next.getPriority());
        pti.setProcTaskAssignee(next.getAssignee());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssigneeType(next.getAssigneeType());
        pti.setProcTaskAssigneeId(next.getAssigneeId());
        pti.setProcTaskAssigneeName(next.getAssigneeName());
        pti.setProcTaskAssign

