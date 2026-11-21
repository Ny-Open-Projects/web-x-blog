# 画面线理解：19-发起申请：代码实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\19-发起申请：代码实现-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:08, 01:54, 02:34, 02:54, 03:19, 03:32, 03:44, 04:45, 05:03, 05:20, 05:36, 06:14, 06:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:14:11

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 项目中，通过 Java 代码实现请假流程的审批节点处理、任务分配和数据库操作，包括任务完成、候选人查询、SQL 构建与执行等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 IntelliJ IDEA 中 AuditService.java 文件的代码，聚焦于任务完成和保存流程实例的代码段。
- 代码内容：
  ```java
  //4.1 获取待执行的任务节点
  Task task = taskService.createTaskQuery().processInstanceId(processInstance.getlD()).singleResult();
  //4.2 获取下一个节点数据，填充业务数据中当前待审批人
  taskService.complete(task.getId());
  //5.获取下一个节点数据，填充业务数据中当前待审批人
  taskService.complete(task.getId());
  //5.获取下一个节点数据，填充业务数据中当前待审批人
  taskService.complete(task.getId());
  procInstanceDao.save(instance);
  ProcTaskInstance pti = new ProcTaskInstance();
  pti.setTaskId(idWorker.nextId()+"");
  pti.setProcessId(instance.getProcessId());
  pti.setHandleTime(new Date());
  pti.setHandleType("2");
  pti.setHandleUserId(user.getId());
  pti.setHandleUserName(user.getUsername());
  pti.setTaskKey(task.getTaskDefinitionKey());
  pti.setTaskName(task.getTaskName());
  pti.setHandleOpinion("发起申请");
  procTaskInstanceDao.save(pti);
  ```

画面 2：
- 代码与画面 1 几乎相同，但注释略有不同，显示了任务完成和获取下一个任务节点的逻辑。
- 代码内容：
  ```java
  if("process_leave".equals(processKey)) {
      //请假流程
  }
  ProcessInstance processInstance = runtimeService.startProcessInstanceById(definition.getId(), instance.getProcessId(), vars);
  //4.1 获取待执行的任务节点
  Task task = taskService.createTaskQuery().processInstanceId(processInstance.getlD()).singleResult();
  //4.2 获取下一个节点数据，填充业务数据中当前待审批人
  taskService.complete(task.getId());
  //5.获取下一个节点数据，填充业务数据中当前待审批人
  taskService.complete(task.getId());
  procInstanceDao.save(instance);
  ProcTaskInstance pti = new ProcTaskInstance();
  pti.setTaskId(idWorker.nextId()+"");
  pti.setProcessId(instance.getProcessId());
  pti.setHandleTime(new Date());
  pti.setHandleType("2");
  pti.setHandleUserId(user.getId());
  pti.setHandleUserName(user.getUsername());
  pti.setTaskKey(task.getTaskDefinitionKey());
  pti.setTaskName(task.getTaskName());
  pti.setHandleOpinion("发起申请");
  procTaskInstanceDao.save(pti);
  ```

画面 3：
- 显示 MySQL 数据库管理工具（SQLyog）中，查询 `proc_instance` 表，其中包含 `process_id`, `process_key`, `process_name`, `process_definition_id`, `process_state`, `user_id`, `username` 等字段。
- 数据库表结构：
  ```
  process_id | process_key | process_name | process_definition_id | process_state | user_id | username
  11756524677602046 | process_leave | 请假 | (NULL) | 1 | 16670598992622798 | itcast
  ```

画面 4：
- 显示 Windows 资源管理器中，右键点击一个文件夹，弹出菜单，显示“上传到阿里云盘”、“用 TortoiseSVN”、“上传到百度网盘”等选项。
- 无代码或配置内容。

画面 5：
- 显示 IntelliJ IDEA 中 AuditService.java 文件的代码，聚焦于 `findCurrUsers` 方法，用于根据任务 ID 查询当前任务的候选人。
- 代码内容：
  ```java
  private List<User> findCurrUsers(Task nextTask, User user) {
      List<IdentityLink> list = taskService.getIdentityLinksForTask(nextTask.getId());
      List<User> users = new ArrayList<>();
      for (IdentityLink identityLink : list) {
          String groupId = identityLink.getGroupId();
          ProcUserGroup userGroup = procUserGroupDao.findById(groupId).get();
          String param = userGroup.getParam();
          String paramValue = null;
          if ("user_id".equals(param)) {
              paramValue = user.getId();
          } else if ("department_id".equals(param)) {
              paramValue = user.getDepartmentId();
          } else if ("company_id".equals(param)) {
              paramValue = user.getCompanyId();
          }
          String sql = userGroup.getSql().replaceAll("\\\\(" + param + "\\)", paramValue);
          Query query = entityManager.createNativeQuery(sql);
          users.addAll(query.getResultList());
      }
      return users;
  }
  ```

画面 6：
- 显示 IntelliJ IDEA 中 `findCurrUsers` 方法的代码，但注释部分有中文注释，显示了“查询当前任务的候选人”。
- 代码内容：
  ```java
  private List<User> findCurrUsers(Task nextTask, User user) {
      List<IdentityLink> list = taskService.getIdentityLinksForTask(nextTask.getId());
      List<User> users = new ArrayList<>();
      for (IdentityLink identityLink : list) {
          String groupId = identityLink.getGroupId();
          ProcUserGroup userGroup = procUserGroupDao.findById(groupId).get();
          String param = userGroup.getParam();
          String paramValue = null;
          if ("user_id".equals(param)) {
              paramValue = user.getId();
          } else if ("department_id".equals(param)) {
              paramValue = user.getDepartmentId();
          } else if ("company_id".equals(param)) {
              paramValue = user.getCompanyId();
          }
          String sql = userGroup.getSql().replaceAll("\\\\(" + param + "\\)", paramValue);
          Query query = entityManager.createNativeQuery(sql);
          users.addAll(query.getResultList());
      }
      return users;
  }
  ```

画面 7：
- 显示 IntelliJ IDEA 中 AuditService.java 文件的代码，聚焦于 `getInstanceList` 方法，用于查询流程实例列表。
- 代码内容：
  ```java
  @Autowired
  private RepositoryService repositoryService;
  @Autowired
  private RuntimeService runtimeService;
  @Autowired
  private TaskService taskService;
  @Autowired
  private ProcUserGroupDao procUserGroupDao;
  @Autowired
  private EntityManager entityManager;
  // 实现所有的业务的申请流程
  public Page getInstanceList(ProcInstance instance, int page, int size) {
      //1.使用Specification查询，构建Specification
      Specification<ProcInstance> spec = new Specification<ProcInstance>() {
          public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder cb) {
              List<Predicate> list = new ArrayList<>();
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessKey())) {
                  list.add(cb.equal(root.get("processKey"), instance.getProcessKey()));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessState())) {
                  list.add(cb.equal(root.get("processState"), instance.getProcessState()));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessName())) {
                  list.add(cb.like(root.get("processName"), "%" + instance.getProcessName() + "%"));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessDefinitionId())) {
                  list.add(cb.equal(root.get("processDefinitionId"), instance.getProcessDefinitionId()));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessStartTime())) {
                  list.add(cb.greaterThanOrEqualTo(root.get("processStartTime"), instance.getProcessStartTime()));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessEndTime())) {
                  list.add(cb.lessThanOrEqualTo(root.get("processEndTime"), instance.getProcessEndTime()));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessUserId())) {
                  list.add(cb.equal(root.get("processUserId"), instance.getProcessUserId()));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessUserName())) {
                  list.add(cb.like(root.get("processUserName"), "%" + instance.getProcessUserName() + "%"));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessUserDepartmentId())) {
                  list.add(cb.equal(root.get("processUserDepartmentId"), instance.getProcessUserDepartmentId()));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessUserCompanyId())) {
                  list.add(cb.equal(root.get("processUserCompanyId"), instance.getProcessUserCompanyId()));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessUserGroup())) {
                  list.add(cb.like(root.get("processUserGroup"), "%" + instance.getProcessUserGroup() + "%"));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessUserGroupType())) {
                  list.add(cb.equal(root.get("processUserGroupType"), instance.getProcessUserGroupType()));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessUserGroupValue())) {
                  list.add(cb.like(root.get("processUserGroupValue"), "%" + instance.getProcessUserGroupValue() + "%"));
              }
              //查询状态
              if (!StringUtils.isEmpty(instance.getProcessUserGroupValueId())) {
                  list.add(cb
