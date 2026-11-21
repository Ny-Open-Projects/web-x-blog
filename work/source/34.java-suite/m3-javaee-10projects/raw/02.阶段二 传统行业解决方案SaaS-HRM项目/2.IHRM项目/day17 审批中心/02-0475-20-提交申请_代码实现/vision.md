# 画面线理解：20-提交申请：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\20-提交申请：代码实现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:27, 02:11, 03:58, 07:21, 08:14, 09:06, 10:50, 12:37, 13:18, 13:59, 14:43, 15:15, 15:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:15:12

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 iHRM 系统中通过代码实现审批流程的发起与提交，包括前端请求、后端控制器与服务层的代码逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前位于“3.3 发起申请”下的“3.3.1 需求分析”，内容包括业务数据构造、开启动作、执行第一个Task等需求说明。
画面2：前端页面显示审批列表，弹窗提示“通过审核”，同时浏览器开发者工具显示了提交的请求体，包含 handleOpinion、processId、handleType 等字段。
画面3：IntelliJ IDEA 中展示 ProcessController.java 的代码，包含 @RequestMapping 注解的两个方法：instanceDetail 和 startProcess。
画面4：展示 AuditService.java 中的 commit 方法，其中包含根据 department_id 和 company_id 获取参数值的逻辑，以及构建 SQL 查询语句。
画面5：在 commit 方法中，通过 String 类型的 handleType 判断审批类型（2=通过，3=不通过，4=撤销），并开始构建业务逻辑。
画面6：在 commit 方法中，使用 StringBuilder 构建 SQL 语句，并调用 userGroup.getSql() 方法获取 SQL 模板。
画面7：在 commit 方法中，使用 runtimeService 的 deleteParticipantGroup、deleteProcessInstance、deleteEvent 等方法处理流程实例。
画面8：在 commit 方法中，根据 handleType 的值（2 或 3）分别调用 runtimeService 的 deleteProcessInstance 方法或 createTaskQuery 方法。
画面9：展示 commit 方法中，通过 taskInstance.getHandleType() 获取处理类型，并设置 processInstance 的状态。
画面10：在 commit 方法中，通过 runtimeService.createProcessInstanceQuery() 查询流程实例，并根据 handleType 设置状态。
画面11：展示 startProcess 方法，用于发起流程，包括构建 ProcessInstance 对象、设置属性、查询流程定义并启动流程。
画面12：在 startProcess 方法中，通过 runtimeService.createProcessInstanceQuery() 查询流程实例，并根据 handleType 设置状态。
画面13：在 startProcess 方法中，通过 taskService.createTaskQuery() 查询任务，并根据是否存在下一个节点设置流程状态。
画面14：在 startProcess 方法中，通过 runtimeService.createProcessInstanceQuery() 查询流程实例，并根据 handleType 设置状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
//查询申请的详情数据
/**
 * 会签：申请对象的id
 */
@RequestMapping(value = "/instance/{id}", method = RequestMethod.GET)
public Result instanceDetail(@PathVariable String id) throws IOException {
    //调用service层查询id配置
    ProcInstance instance = auditService.findInstanceDetail(id);
    return new Result(ResultCode.SUCCESS,instance);
}

//流程申请
@RequestMapping(value = "/startProcess", method = RequestMethod.POST)
public Result startProcess(@RequestBody Map map) throws IOException {
    //调用service
    auditService.startProcess(map,companyId);
    return new Result(ResultCode.SUCCESS);
}

//提交审核
```

画面4：
```java
else if (department_id.equals(param)) {
    paramValue = user.getDepartmentId();
}
else if (company_id.equals(param)) {
    paramValue = user.getCompanyId();
}
String sql = userGroup.getSql().replaceAll("\\$\\{", "+" + param + "\\}", paramValue);
Query query = entityManager.createNativeQuery(sql);
query.unwrap().setResultTransformer(Transformers.aliasToBean(User.class));
users.addAll(query.getResultList());
return users;
```

画面5：
```java
//提交审核
handleType; // 处理类型（2审批通过，3审批不通过，4撤销）
ProcTaskInstance
handleOpinion: "xxxxxx"
handleType: "4"
handleUserId: "1863785989926227968"
processId: "11755933854653552192"
```

画面6：
```java
public void commit(ProcTaskInstance taskInstance, String companyId) {
    //1.查询当前流程对象
    String processId = taskInstance.getProcessId();
    ProcInstance instance = procInstanceDao.findById(processId).get();
    //2.设置业务流程状态
    instance.setProcessState(taskInstance.getHandleType());
    //3.根据不同操作类型，完成不同的业务处理
    if ("2".equals(taskInstance.getHandleType())) {
        //3.1 如果审批通过，完成当前的任务
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
        //3.2 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    } else {
        //3.3 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    }
}
```

画面7：
```java
public void commit(ProcTaskInstance taskInstance, String companyId) {
    //1.查询当前流程对象
    String processId = taskInstance.getProcessId();
    ProcInstance instance = procInstanceDao.findById(processId).get();
    //2.设置业务流程状态
    instance.setProcessState(taskInstance.getHandleType());
    //3.根据不同操作类型，完成不同的业务处理
    if ("2".equals(taskInstance.getHandleType())) {
        //3.1 如果审批通过，完成当前的任务
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
        //3.2 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    } else {
        //3.3 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    }
}
```

画面8：
```java
public void commit(ProcTaskInstance taskInstance, String companyId) {
    //1.查询当前流程对象
    String processId = taskInstance.getProcessId();
    ProcInstance instance = procInstanceDao.findById(processId).get();
    //2.设置业务流程状态
    instance.setProcessState(taskInstance.getHandleType());
    //3.根据不同操作类型，完成不同的业务处理
    if ("2".equals(taskInstance.getHandleType())) {
        //3.1 如果审批通过，完成当前的任务
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
        //3.2 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    } else {
        //3.3 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    }
}
```

画面9：
```java
//提交审核
handleType; // 处理类型（2审批通过，3审批不通过，4撤销）
ProcTaskInstance
handleOpinion: "xxxxxx"
handleType: "4"
handleUserId: "1863785989926227968"
processId: "11755933854653552192"
```

画面10：
```java
public void commit(ProcTaskInstance taskInstance, String companyId) {
    //1.查询当前流程对象
    String processId = taskInstance.getProcessId();
    ProcInstance instance = procInstanceDao.findById(processId).get();
    //2.设置业务流程状态
    instance.setProcessState(taskInstance.getHandleType());
    //3.根据不同操作类型，完成不同的业务处理
    if ("2".equals(taskInstance.getHandleType())) {
        //3.1 如果审批通过，完成当前的任务
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
        //3.2 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    } else {
        //3.3 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    }
}
```

画面11：
```java
public void startProcess(Map map, String companyId) {
    //1.构造业务数据
    String userId = (String) map.get("userId");
    String processKey = (String) map.get("processKey");
    String processName = (String) map.get("processName");
    User user = FeignClientService.getUserInfoByUserId(userId);
    ProcInstance instance = new ProcInstance();
    BeanUtils.copyProperties(user, instance);
    instance.setUserId(userId);
    instance.setProcessId(IdGenerator.nextId());
    instance.setProcessKey(processKey);
    instance.setProcessName(processName);
    instance.setApplyTime(new Date());
    instance.setProcessState("1");
    instance.setData(JSON.toJSONString(map));
    instance.setCompanyId(companyId);
    //2.查询流程定义
    ProcessDefinition definition = repositoryService.createProcessDefinitionQuery()
            .processDefinitionKey(processKey)
            .latestVersion()
            .singleResult();
    //3.并启动流程
    Map vars = new HashMap<>();
    vars.put("days", map.get("duration"));
    ProcessInstance process
