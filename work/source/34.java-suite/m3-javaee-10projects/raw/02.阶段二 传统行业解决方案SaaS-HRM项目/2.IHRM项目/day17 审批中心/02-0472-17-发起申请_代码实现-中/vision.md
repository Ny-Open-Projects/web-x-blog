# 画面线理解：17-发起申请：代码实现-中

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\17-发起申请：代码实现-中_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:22, 01:45, 02:47, 03:26, 03:48, 04:14, 04:40, 04:58, 05:22, 05:51, 06:21, 06:45, 07:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:12:32

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
