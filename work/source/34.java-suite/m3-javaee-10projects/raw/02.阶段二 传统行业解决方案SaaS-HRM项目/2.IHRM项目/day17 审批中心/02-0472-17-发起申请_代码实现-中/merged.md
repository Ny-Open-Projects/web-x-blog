# 17-发起申请：代码实现-中

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\17-发起申请：代码实现-中_【海量资源尽在 ubkz.com】.mp4
- 时长 7分16秒（音频 437s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那咱们写到这个程度咱们继续往下看那接下来呢就是说调用它这个start process intense by id它会自动的帮助我们开启这个流程那开启流程之后它会有对应的一个返回值那各位这边呢希望注意一下这边呢它的返回值叫做process intense跟我们自己写那个proc很像啊这个千万别搞混啊
[00:27] 这个比较长的是人甲的叫做流程实例我们这边呢其实起立名字也叫做流程实例其实就是对这个人家官方的这个做了一个小型的扩展咱们把它理解为我们自己的业务数据那接下来呢咱们就继续往下去看了自动执行第一个节点那自动执行第一个节点那怎么做呢很简单那如果说你开启了流程之后注意啊这边我一直让图为例你开启了这个流程之后它自动的就会流转到第一个
[00:55] 用户任务让他去执行我们第一个用户任务其实就叫做申请没错吧所以我们开启之后立马把第一个节点给他提交了申请那怎么办很简单咱们要做的事情获取获取待执行的任务节点好了接下来呢4.2咱们执行即可没错吧那怎么获取这个待执行的任务节点需要注入一个新的Service
[01:24] at auto where叫做privatetaskservice这也是activity为我们提供的那这个就是用来获取执行任务的那可以通过taskservice点好了create querytask query就是任务的传言器点pulse instance id注意啊这边我们用的是instance id用的是我们上边得到的这个流程定义
[01:56] 来留成实例的id.get id那这样一来咱们就能够得到对应的这么一个任务其实通过抱歉咱们继续点single result获取唯一的这个节点其实它的都差不多那其实各位能够看到人家自己有PulseIntense自己有Task他们之间是不是也有这种一对多的关系上面是一个一方底下是不是一个多方那只不过呢获取到哪一个任务咱们从哪个任务拿
[02:26] 就可以了好了咱们现在拿到了第一个节点叫做task那接下来呢咱们开始执行当前的这个task那执行当前这个任务也很简单那用什么来执行这边呢咱们可以借助task Service点complete哎直接把当前的这个task的ID放进去就已经执行完成了点get ID那这样一来那这样一来
[02:51] 咱们其实就已经把当前的这些最主要的代码呢咱们就已经写好了那注意还有第五步第五步呢相对来说有一点点麻烦咱们一会儿再写咱们先看目前它能够执行的这个程度究竟是什么样子那就目前我们这个代码当中呢现在啊已经Intense已经有了这边呢咱们就需要进行数据库的相应保存那数据库的相应保存呢相对来说比较简单
[03:20] 我们只需要把我们自己的业务流程保存进去当了我们这边呢你写一个人家的task我们就需要自己的一个哎任务详情所以我们这边呢先把对应的do注进去intense do注进来了好了接着还有注入一个at out to wheregravit poctask intense do那这个是我们自己的一对多关系那好了control c call过来
[03:53] 点save把我们自己的intents保存进去那接下来呢我们还要保存我们自己的这个第一个节点点save那这边呢各位要注意的是我们需要自己去构造出这么的一个PoCPath Instant对象Pti等于你有一个Intent对象
[04:23] 拿过来那接下来呢这里面的数据从哪来其实就是从我们已执行的task里面获取就可以了点set这里面的内容会比较多啊我们分屏显示一个一个构造就可以了好了拿过来点setididworker.nextid好构造成此句那接下来pdi.set
[04:58] Pulse ID是我们自己的Intense ID点GetPulse ID没问题那接下来里面还有处理时间点点SetHandlerTimeNew一个Data传递过来没问题接下来呢继续这个就稍微有点麻烦点Set就是HandlerTime那HandlerTime这边说了那第一个就是申请所以我们就叫做
[05:38] 就是审批通就是审批通过吧第一个节点其实叫做申请更合适啊那继续再来pti.setHandlerUserId那就是我们当前的userID谁发起的请求我们就写谁嘛处理人嘛pti.setHandlerUserName就是我们的useruser.getUserName没问题
[06:12] 那接下来呢底下还有比如说呢task keytask name继续再来pti.set task key那这个task key就从上面获取就可以了task.get我们的key好了继续再来pti.set task nametask name也是从上面获取到就可以了task.get nameOK那这边呢好像还少一个这个处理意见处理意见我们这边写上吧
[06:47] 点set handler option随随随便写了就是没意见就是就是发发起申请的了OK那最终把这个PTI保存起来就可以了注意啊各位咱们是一起来简单的试一下我这个请求流程那注意有一步我还没写咱们一会儿再说可以吧好了这个代码呢写到这个程度我们可以重新启动一下我们这个服务来看一下效果

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 Activiti 工作流引擎，通过代码启动流程实例、获取任务并完成任务，同时展示相关实体类的定义。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 AuditService.java 中的 startProcess 方法，用于启动流程实例。代码中调用 runtimeService.startProcessInstanceById，并通过 taskService.createTaskQuery 获取任务。
画面2: 展示了 AuditService.java 中的 findInstanceDetail 方法，用于根据 ID 查询流程实例详情。
画面3: 展示了 AuditService.java 中的 startProcess 方法，代码中调用 taskService.createTaskQuery 来获取任务。
画面4: 展示了 AuditService.java 中的 startProcess 方法，代码中调用 taskService.complete(task.getId()) 来完成任务。
画面5: 展示了 AuditService.java 中的 startProcess 方法，代码中调用 taskService.createTaskQuery 来获取任务。
画面6: 展示了 AuditService.java 中的 @Service 注解和 @Autowired 注解，用于注入各种服务，如 procInstanceDao、feignClientService、idWorker、repositoryService、runtimeService、taskService。
画面7: 展示了 AuditService.java 中的 startProcess 方法，代码中调用 procInstanceDao.save(instance) 保存流程实例。
画面8: 展示了 ProcTaskInstance.java 实体类的定义，包含多个私有字段如 taskId、handleTime、processId、taskName 等。
画面9: 展示了 ProcTaskInstance.java 实体类的定义，代码中调用 procInstanceDao.save(instance) 保存流程实例。
画面10: 展示了 ProcTaskInstance.java 实体类的定义，代码中调用 procInstanceDao.save(instance) 保存流程实例。
画面11: 展示了 ProcTaskInstance.java 实体类的定义，代码中调用 procInstanceDao.save(instance) 保存流程实例。
画面12: 展示了 ProcTaskInstance.java 实体类的定义，代码中调用 procInstanceDao.save(instance) 保存流程实例。
画面13: 展示了 ProcTaskInstance.java 实体类的定义，代码中调用 procInstanceDao.save(instance) 保存流程实例。
画面14: 展示了项目结构和控制台日志，显示流程执行完成，退出码为 0。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
String processName = (String) map.get("processName");
User user = FeignClientService.getUserInfoByUserId(userId);
BeanUtils.copyProperties(user, instance);
instance.setUserId(userId);
instance.setProcessId(IdWorker.nextId());
instance.setProcApplyTime(new Date());
instance.setProcessKey(processKey);
instance.setProcessName(processName);
instance.setProcessState("1");
String data = JSON.toJSONString(map);
instance.setProcData(data);
ProcessDefinition definition = repositoryService.createProcessDefinitionQuery().processDefinitionKey(processKey)
        .processDefinitionTenantId(companyId).latestVersion().singleResult();
Map vars = new HashMap();
if("process_leave".equals(processKey)) {
    //请假
    vars.put("days",map.get("duration"));
}
ProcessInstance processInstance = runtimeService.startProcessInstanceById(definition.getId(), instance.getProcessId(), vars);
Task task = taskService.createTaskQuery().processInstanceId(processInstance.getId()).singleResult();
taskService.complete(task.getId());
procInstanceDao.save(instance);
```

画面6:
```java
@Service
public class AuditService {

    @Autowired
    private ProcInstanceDao procInstanceDao;

    @Autowired
    private FeignClientService feignClientService;

    @Autowired
    private IdWorker idWorker;

    @Autowired
    private RepositoryService repositoryService;

    @Autowired
    private RuntimeService runtimeService;

    @Autowired
    private TaskService taskService;

    //...其他方法
}
```

画面8:
```java
package com.ihrm.audit.entity;

import ...
@Entity
@Table(name = "proc_task_instance")
@Data
@AllArgsConstructor
public class ProcTaskInstance implements Serializable {

    private static final long serialVersionUID = 1197839778202849L;

    @Id
    private String taskId; // 任务实例ID
    private String handleTime; // 处理时间
    private Date handleDate; // 处理日期
    private String handleType; // 处理类型（2审批通过，3审批不通过）
    private String handleUserId; // 处理人ID
    private String processId; // 流程实例ID
    private String taskKey; // 任务Key
    private String taskName; // 任务名称
}
```

画面14:
```java
Process finished with exit code 0
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

