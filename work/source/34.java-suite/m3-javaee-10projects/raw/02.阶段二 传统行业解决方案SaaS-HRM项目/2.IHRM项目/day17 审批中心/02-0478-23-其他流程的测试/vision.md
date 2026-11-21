# 画面线理解：23-其他流程的测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\23-其他流程的测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:35, 00:54, 01:29, 02:19, 02:43, 02:53, 03:01, 03:18, 03:33, 03:42, 03:52, 04:08, 04:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:17:33

1) 这一组画面整体在讲什么（一句话）：
演示一个基于流程引擎的离职审批系统，包括业务流程分析、数据库表结构、Java 代码实现以及前端审批操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 页面“1.4 离职流程分析”，内容为离职流程涉及的人员角色（当事人、直属领导、人事HR、人事负责人、财务人员）及流程步骤（当事人发起申请 → 直属领导审批 → 人事负责人审批 → 财务人员审批）。
画面 2: 展示数据库表 `process` 中的 SQL 语句，用于查询部门负责人信息，SQL 为 `SELECT manager_username, manager_id FROM bo_department WHERE id = ?department_id`。
画面 3: 展示数据库表 `process` 中的 SQL 语句，用于查询部门负责人信息，SQL 为 `SELECT manager_username, manager_id FROM bo_department WHERE id = ?department_id`。
画面 4: 展示 Java 代码片段，位于 `AuditService.java` 文件中，处理流程节点跳转和任务实例保存，代码包含 `instance.setProcessState("2");` 和 `procTaskInstanceDao.save(taskInstance);`。
画面 5: 展示数据库表 `department` 的数据，包含公司ID、部门ID、名称、负责人、创建时间等字段。
画面 6: 展示 Java 代码片段，位于 `AuditService.java` 文件中，用于根据用户组ID查询用户，代码包含 `String sql = userGroup.getSql().replaceAll("\\{\\$\\{ + param + \\}\\}", paramValue);`。
画面 7: 展示 HR 系统前端界面，显示“工作日历”和“快速开始”导航，包括“人事月报”、“考勤查询”、“员工审核”等入口。
画面 8: 展示 HR 系统前端界面，弹出“加班申请”表单，包含“申请类型”、“加班开始时间”、“加班结束时间”、“补偿方式”、“加班原因”等字段。
画面 9: 展示 HR 系统前端界面，显示“操作成功！”提示，表示加班申请已提交。
画面 10: 展示 HR 系统前端界面，显示“工作日历”和“快速开始”导航。
画面 11: 展示 HR 系统前端界面，弹出“通过审批”对话框，用于审批加班申请。
画面 12: 展示 HR 系统前端界面，显示“工作日历”和“快速开始”导航。
画面 13: 展示 HR 系统前端界面，弹出“通过审批”对话框，用于审批加班申请。
画面 14: 展示数据库表 `process` 中的 SQL 语句，用于查询部门负责人信息，SQL 为 `SELECT manager_username, manager_id FROM bo_department WHERE id = ?department_id`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 4 代码：
```java
instance.setProcCurrNodeUserId(userID);
instance.setProcCurrNodeUserName(usernames);
instance.setProcessState("1");
else {
    //如果不存在下一个节点，任务结束
    instance.setProcessState("2");
}
else {
    //如果不能跳过，改变当前任务对象
    runtimeService.deleteProcessInstance(processInstance.getProcessId(), taskInstance.getHandleOpinion());
}
//更好的业务流程，保存业务任务对象
procInstance.setTaskId(idWorker.nextId()+"");
taskInstance.setHandleUserName(user.getUserName());
taskInstance.setHandleTime(new Date());
procTaskInstanceDao.save(taskInstance);
```

画面 6 代码：
```java
private List<User> findCurrUsers(Task nextTask, User user) {
    List<IdentityLink> list = taskService.getIdentityLinksForTask(nextTask.getId());
    List<User> users = new ArrayList<>();
    for (IdentityLink identityLink : list) {
        ProcUserGroup userGroup = procUserGroupDao.findById(identityLink.getGroupId()).get();
        String param = userGroup.getParam();
        String paramValue = null;
        if ("user_id".equals(param)) {
            paramValue = user.getId();
        } else if ("department_id".equals(param)) {
            paramValue = user.getDepartmentId();
        } else if ("company_id".equals(param)) {
            paramValue = user.getCompanyId();
        }
        String sql = userGroup.getSql().replaceAll("\\{\\$\\{ + param + \\}\\}", paramValue);
        Query query = entityManager.createNativeQuery(sql, Transformers.aliasToBean(User.class));
        query.unwrap(NativeQueryImpl.class).setResultTransformer(Transformers.aliasToBean(User.class));
        users.addAll(query.getResultList());
    }
    return users;
}
```

画面 2 SQL：
```sql
SELECT manager_username, manager_id FROM bo_department WHERE id = ?department_id
```

画面 5 SQL：
```sql
SELECT id, username FROM bo_user WHERE department_id = ?department_id
```

画面 14 SQL：
```sql
SELECT manager_username, manager_id FROM bo_department WHERE id = ?department_id
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 PPT 标题：
- 1.4 离职流程分析
- 业务流程概述
- 北京市昌平区建材城西路金燕办公楼一层 电话：400-618-9090

流程图结构：
- 开始 → 当事人发起离职申请 → 直属领导审批 → 人事负责人审批 → 财务人员审批 → 结束

表格数据：
- 表格列：company_id, department_id, name, code, manager, introduce, create_time, manage_id
- 表格数据：
  - 117531219740626886, 1, 117531219740626886, 1, 117531219740626886, 117531219740626886, 117531219740626886, 117531219740626886
  - 117531219740626886, 1, 117531219740626886, 1, 117531219740626886, 117531219740626886, 117531219740626886, 117531219740626886

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
