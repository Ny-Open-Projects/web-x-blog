# 23-其他流程的测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\23-其他流程的测试_【海量资源尽在 ubkz.com】.mp4
- 时长 4分31秒（音频 271s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 当呢在我们这边呢除了有请假流程之外呢还有就是这边的加班流程还有我们的离职流程没错吧那其实这几个流程咱们已经部署上去了那我们接下来呢就以这个加班的流程为例咱们简单的来看一下那在我们这边在我们的这套体系当中那怎么完成这个流程的一个处理那首先呢就是说在我们这边加班流程呢涉及到这么几个节点申请提交提交不用管那还有部门审批是吧还有人事审批
[00:30] 那对应的这几个节点呢我已经在我这边group这个里面准备好了好了比如说这边有加班申请人这条sql语句其实我们用不到可以把它删掉啊好那接下来呢就是还有两个流程第一个就是加班部门的用户组好了第二个就是加班人士的这个审批的这个用户组那其实对应我们来说主要关注的就是这个sql语句没错吧那对于加班的这个
[00:58] 这个部门的审批谁呢就是你加班你的部门主管要进行操作那我们查询的表是不是跟刚才这个一样那根据部门找到当前提交人他的部门ID那其实就是这就是这条搜索语句把这条搜索语句呢Ctrl C T换过来Ctrl V好了那注意各位那这边呢由于我这边配置了一个Param
[01:24] 后来这边也有对应的pairing那在我们的Java代码当中呢它就会自己的进行Circle语句的一个替换你发现这边得到一条Circle语句那Circle语句替换其实替换的就是把大括号这一大堆中间这个内容是不是给替换掉啊没错吧好了那接下来呢这个内容呢究竟是什么比如说是Department ID那如果是Department ID我就用当前操作人的Department ID来替换
[01:51] 那如果当前操作人是1那我们就把这玩意替换成了1没错吧如果是2咱们就替换成了2能接受吗好了那既然这个能够看到的话那接下来第二个流程就是要交给人事审批那交给人事审批我们来看一下那我们要查询的呢其实就是查询所有的用户这位查询所有用户那查询所有用户我们要找的是
[02:16] 人事部门的所有用户那我们看一下部门找到人事部人事部的IDCtrl C拿的过来还是回到我们刚才这个组的表里人事组审批好了这回呢部门ID这回就写死了不让他进行替换了那当然了不让他进行替换其实这样一来也可以当然你可以把这个参数给他删掉好了那接着我保存一下那保存好了之后回到我们这边找到我们的这个页面还是
[02:48] 以ZBZ来进行一个流程申请审批呃员工页面啊好了我们这边呢可以通过ZBZ这个用户来发起一个加班的这么一个就是加班啊这么一个申请好了随便填一下时间OK好了加班原因随便填随便填就行了好了那接着点击提交那这边呢已经提交成功了我们来看一下我们的审批列表其中就一条哎ZBZ的那我发起的
[03:24] 哎 加班那接下来呢是不是就流转到了我的部门领导ITcast来进行审批啊好了那接下来退出登录ITcast没问题那找到我的代审批哎 有一条是代表代审批的那接下来呢我给他审批成功 审批通过通过那确定那接下来呢我们还有一个就是要经过人事审批人事审批刚才我们就看过了LL就是我们的人事审批审批
[03:55] 你会发现是不是有这么一条那对于我们这个加班流程呢比较简单部门领导审批通过那人事审批通过那整个流程就已经结束了那我们这边通过确定那接着来看其中有一条加班的是不是已经审批通过了没错吧好了那这个其实就是要跟各位简单的来说一下我们整个的这些流程现在由于有了用户组剩下都是一样的都比较统一那我们只需要对Circle语句进行
[04:26] 组的良好的控制其实就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

