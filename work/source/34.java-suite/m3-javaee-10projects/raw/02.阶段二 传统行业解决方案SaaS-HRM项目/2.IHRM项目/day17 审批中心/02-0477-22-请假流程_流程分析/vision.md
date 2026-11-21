# 画面线理解：22-请假流程：流程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\22-请假流程：流程分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:45, 02:19, 02:37, 02:56, 04:11, 04:35, 05:10, 06:22, 07:11, 08:24, 09:31, 10:27, 11:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:16:47

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
