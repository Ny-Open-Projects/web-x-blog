# 19-发起申请：代码实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\19-发起申请：代码实现-下_【海量资源尽在 ubkz.com】.mp4
- 时长 6分43秒（音频 403s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们已经把这个发起申请的大部分功能都已经实现了但是我们发现当前审批人这边是不是没有啊因为我们可以借助当前审批人去查询一个人待审批的这些申请那我们接下来呢就开始来看一下当前审批人应该怎么做那是这样的这个当前审批人呢我们可以跟着这张讲义这张图来看
[00:24] 当前的这个审批人其实就是用户提交申请之后那当前审批人是不是就是下一个节点或者下一个用户任务这些人啊所以在我们这边回到代码咱们要做的事情很简单就是获取下一个节点那获取这个下一个节点怎么获取呢是这样的我们可以根据上面一样也是调用这个方法提个名字就叫做next那这个方法呢
[00:52] 就是process intense什么ID什么single result什么意思这个永远获取的都是待处理的节点信息因为我们上面这个节点已经处理过了相当于我们讲一场第一个节点处理过了我们再用这个方法获取的就是下一个节点那我们对于每一个节点得到的这个节点信息里面有什么咱们可以通过咱之前给各位提供好的这个资料里面的BPM文件我们来看一下比如说就以请假为例
[01:22] 其中的第一个节点呢我们已经完成了那第二个节点里面这边是不是有一个叫做初审那初审我们是不是给他指了一个候选人组啊那对于这个候选人组其实我们就可以给他查询出来那查询出来候选人组那接下来根据不同的系统可能有不同的要求候选人组有了在你的系统当中可以以候选人组的形式查询用户可以以候选人组的形式去查询任何你想要的
[01:48] 那在我们这个系统当中给各位提供了一个其他的思路那我们这个候选人组对应的是我们自己拓展的一个表这个表叫做PLC User Loop那是不是跟他这个ID是保持一致的那我们来看一下叫做Liu True User好了咱们就是Liu True Users是不是跟他一致那各位来看这个后面是不是对应的是一条Circle语句啊所以我们这个候选人组呢其实很清晰
[02:16] 那根据下一个节点得到组名称那查询这个表得到搜索语句接着执行搜索语句查询数据库得到用户对象就是这么一个逻辑那对于这些代码呢其实写起来比较简单在今天的资料当中把这些基本的代码给各位准备好了这边有一个查询候选人好了我把这一段Ctrl Ccall到我们的代码里注意这个因为是
[02:42] 因人而异因项目而异去查询这个候选组所以我们这边是给各位提供这么一个思路就可以了好了那接下来呢还有一段把这一段呢也call过来control c拿到我们这边那call过来之后简单的说一下我们这个代码的一个小小的执行逻辑好了那各位来看在我们这边先去获取下一个节点那下一个节点如果不为难哎我调用了一下底下这个方法那这个方法呢需要这么两个参数一个叫做啊
[03:10] 什么user group deal还有一个这边是我们的user class那我把这两个注入进去at autoware private好了接着再来一个at autoware private entity manager注意这个是在SpringData JPA里面你想要自己执行Circle就需要用EntityManager好了既然回到我们这里面简单的来看一下我们这个业务逻辑
[03:47] 那对于这个业务逻辑呢相对来说没有那么复杂首先呢第一个我们可以通过Task Service的形式查询任务的任务的节点数据那这样一来你就能够查进这个任务的这个节点数据当然了这个节点数据主要指的是他的候选人候选人组数据那对于这个候选人组呢可能有多个所以我底下就做了一个循环
[04:16] 那循环之后这边得到的是我们候选人组ID那根据候选人组ID这边是不是就查询查询我们的usergroup那查询usergroup里面呢就能根据这边得到一个circle语句那这个circle语句可能需要一些参数注意来看我这个circle语句里面是不是可能需要一个参数那这个参数呢我们就需要替换
[04:44] 就这个意思所以这就是一个小小的执行流程那执行完成之后返回的就是你查询好的所有的users那前面这边users list查询出来之后构造users的用户名字符串ID的字符串存到intents里面完成保存操作这就是我们的一个小小的发起的一个流程好了这段代码呢我们给它简单的解释了一下这边呢有一个错误不用管它因为这个是idea这边可能有小小问题没有识别到
[05:14] 那接下来我们重新启动一下咱们这个服务发起一个请假流程我们来看一下效果这边我先暂停一下好了我现在的微服务已经启动成功了那接下来呢回到我们的页面部分刷新一把有点慢啊刷新一把好了那接下来呢我们在这边再去提交一个请假申请再去提交一个请假申请时长叉叉叉好了那接下来咱们开始走提交
[05:49] 那这个可能是有点慢其实已经成功了我们来看一下审批这边好像还是没有进去没错吧没进去我们来看一下这个call来这段代码这段代码可能有点问题在这儿确实有问题就是这应该存的是user name啊OK那我们看一下我们的数据库数据吧来Intense过来之后你会发现这个是不是这儿
[06:20] 已经进来了但是是由于我这个代码有一个小小问题其实是已经查到了没错了并且我们这边可以看一下执行的sql语句确确实实这边已经slag新from这个表执行了我们自己的一条sql语句没错了OK好了这个呢我已经改好了我这边不再快上测试了咱们一会儿再去玩流程的时候再说OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

