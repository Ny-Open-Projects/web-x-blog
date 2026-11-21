# 画面线理解：10-Acitviti实现启动流程实例的过程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\10-Acitviti实现启动流程实例的过程分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:08, 00:54, 01:11, 01:15, 01:25, 01:31, 06:50, 06:58, 07:02, 07:59, 08:15, 08:20, 08:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:25:08

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码启动一个 Activiti 工作流实例，并展示其在数据库中创建的表结构和运行时日志。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

画面 2：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

画面 3：
- 显示 MySQL 数据库管理工具界面。
- SQL 语句：drop database activiti; create database activiti;。
- 该语句用于删除并重新创建名为 activiti 的数据库。

画面 4：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

画面 5：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

画面 6：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

画面 7：
- 显示 MySQL 数据库管理工具界面。
- SQL 语句：drop database activiti; create database activiti;。
- 该语句用于删除并重新创建名为 activiti 的数据库。

画面 8：
- 显示 MySQL 数据库管理工具界面。
- 列出了 activiti 数据库中的表，包括 act_hi_actinst, act_hi_identitylink, act_hi_procinst, act_hi_taskinst, act_ru_execution, act_ru_identitylink, act_ru_task 等。

画面 9：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

画面 10：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

画面 11：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

画面 12：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

画面 13：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

画面 14：
- 显示 Java 代码，用于启动流程实例。
- 代码中打印了流程部署 ID、流程定义 ID、流程实例 ID 和活动 ID。
- 控制台输出显示流程启动成功，退出码为 0。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RuntimeService服务
RuntimeService runtimeService = processEngine.getRuntimeService();
//3.创建流程实例，流程定义的key需要知道 holiday
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
//4.输出流程相关信息
System.out.println("流程部署ID"+processInstance.getDeploymentId());
System.out.println("流程定义ID"+processInstance.getProcessDefinitionId());
System.out.println("流程实例ID"+processInstance.getId());
System.out.println("活动ID"+processInstance.getActivityId());
```

画面 3：
```sql
drop database activiti;
create database activiti;
```

画面 4：
```java
System.out.println("流程部署ID"+processInstance.getDeploymentId());//holiday:1:4
System.out.println("流程定义ID"+processInstance.getProcessDefinitionId());//holiday:1:4
System.out.println("流程实例ID"+processInstance.getId());//2001
System.out.println("活动ID"+processInstance.getActivityId());//null
```

画面 5：
```java
public class ActivitiStartInstance {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefault(ProcessEngine());
        //2.得到RuntimeService服务
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.创建流程实例，流程定义的key需要知道 holiday
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
        //4.输出流程相关信息
        System.out.println("流程部署ID"+processInstance.getDeploymentId());
        System.out.println("流程定义ID"+processInstance.getProcessDefinitionId());
        System.out.println("流程实例ID"+processInstance.getId());
        System.out.println("活动ID"+processInstance.getActivityId());
    }
}
```

画面 6：
```java
public class ActivitiStartInstance {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefault(ProcessEngine());
        //2.得到RuntimeService服务
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.创建流程实例，流程定义的key需要知道 holiday
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
        //4.输出流程相关信息
        System.out.println("流程部署ID"+processInstance.getDeploymentId());
        System.out.println("流程定义ID"+processInstance.getProcessDefinitionId());
        System.out.println("流程实例ID"+processInstance.getId());
        System.out.println("活动ID"+processInstance.getActivityId());
    }
}
```

画面 7：
```sql
drop database activiti;
create database activiti;
```

画面 8：
```sql
act_hi_actinst
act_hi_identitylink
act_hi_procinst
act_hi_taskinst
act_ru_execution
act_ru_identitylink
act_ru_task
```

画面 9：
```java
public class ActivitiStartInstance {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefault(ProcessEngine());
        //2.得到RuntimeService服务
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.创建流程实例，流程定义的key需要知道 holiday
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
        //4.输出流程相关信息
        System.out.println("流程部署ID"+processInstance.getDeploymentId());
        System.out.println("流程定义ID"+processInstance.getProcessDefinitionId());
        System.out.println("流程实例ID"+processInstance.getId());
        System.out.println("活动ID"+processInstance.getActivityId());
    }
}
```

画面 10：
```java
public class ActivitiStartInstance {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefault(ProcessEngine());
        //2.得到RuntimeService服务
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.创建流程实例，流程定义的key需要知道 holiday
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
        //4.输出流程相关信息
        System.out.println("流程部署ID"+processInstance.getDeploymentId());
        System.out.println("流程定义ID"+processInstance.getProcessDefinitionId());
        System.out.println("流程实例ID"+processInstance.getId());
        System.out.println("活动ID"+processInstance.getActivityId());
    }
}
```

画面 11：
```java
public class ActivitiStartInstance {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefault(ProcessEngine());
        //2.得到RuntimeService服务
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.创建流程实例，流程定义的key需要知道 holiday
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
        //4.输出流程相关信息
        System.out.println("流程部署ID"+processInstance.getDeploymentId());
        System.out.println("流程定义ID"+processInstance.getProcessDefinitionId());
        System.out.println("流程实例ID"+processInstance.getId());
        System.out.println("活动ID"+processInstance.getActivityId());
    }
}
```

画面 12：
```java
import org.activiti.engine.ProcessEngines;
import org.activiti.engine.RuntimeService;
import org.activiti.engine.runtime.ProcessInstance;

public class ActivitiStartInstance {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefault
