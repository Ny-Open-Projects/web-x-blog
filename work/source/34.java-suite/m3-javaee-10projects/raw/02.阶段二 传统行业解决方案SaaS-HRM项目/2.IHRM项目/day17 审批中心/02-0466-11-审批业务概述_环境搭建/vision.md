# 画面线理解：11-审批业务概述：环境搭建

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\11-审批业务概述：环境搭建_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:50, 01:02, 01:10, 01:19, 01:47, 02:34, 02:56, 03:09, 03:38, 03:47, 03:58, 04:05, 04:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:07:13

1) 这一组画面整体在讲什么（一句话）：
在 ihrm 审核流程项目中，定义并实现流程实例、任务实例和用户组的实体类与数据访问层接口，并通过 Feign 客户端调用远程服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程目录结构，当前位于“2.1 审核流程”章节，介绍需要定义的列表包括审批列表查询、流程申请信息查询、发起流程、提交流程（通过、驳回、撤销）。
画面 2: 在 IntelliJ IDEA 中，展示 `ProcUserGroupDao` 接口定义，继承自 `JpaRepository` 和 `JpaSpecificationExecutor`。
画面 3: 展示 `ProcInstance` 实体类，包含 `processId`、`processDefinitionId`、`processState`、`userId`、`username`、`departmentId`、`deptName` 等字段。
画面 4: 弹出“Copy specified files”对话框，准备将 `ProcInstance` 实体类复制到 `dao` 包下。
画面 5: 展示 `ProcTaskInstanceDao` 接口，定义了 `findByProcessIdAndTaskKey` 和 `findByProcessId` 方法。
画面 6: 在 `ProcTaskInstanceDao` 接口中，注释掉 `findByProcessIdAndTaskKey` 方法，并添加 `findByProcessId` 方法。
画面 7: 展示 `ProcUserGroupDao` 接口，准备定义其方法。
画面 8: 展示 `ProcUserGroup` 实体类，包含 `id`、`name`、`param`、`sql` 字段。
画面 9: 在 Windows 资源管理器中，显示 `dao` 文件夹下的三个 Java 文件：`ProcInstanceDao.java`、`ProcTaskInstanceDao.java`、`ProcUserGroupDao.java`。
画面 10: 在 IntelliJ IDEA 中，右键点击 `ProcUserGroup` 类，弹出菜单并选择“Find Usages”。
画面 11: 展示 `FeignClientService` 类，定义了 `getUserInfoById` 和 `getDepartmentInfoByDepartmentId` 方法。
画面 12: 在 `FeignClientService` 类中，对 `getUserInfoById` 方法进行注释和修改。
画面 13: 展示 `SystemFeignClient` 接口，定义了 `findByid` 方法。
画面 14: 在 `FeignClientService` 类中，对 `getUserInfoById` 方法进行注释和修改。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package com.ihrm.audit.dao;
import ...
/**
 * @author itcast
 */
public interface ProcUserGroupDao extends JpaRepository<ProcUserGroup,String>,
        JpaSpecificationExecutor<ProcUserGroup> {

}
```

画面 3:
```java
package com.ihrm.audit.entity;
import ...
@Entity
@Table(name = "proc_instance")
@Data
@AllArgsConstructor
@Builder
public class ProcInstance {
    private static final long serialVersionUID = 1197639778202803403L;
    @Id
    private String processId; // 流程实例ID
    private String processDefinitionId; // 流程定义ID
    private String processKey; // 流程key
    private String processState; // 流程状态
    private String userId; // 申请人
    private String username; // 申请人
    private String departmentId; // 部门ID
    private String deptName; // 部门名称
}
```

画面 5:
```java
package com.ihrm.audit.dao;
import ...
/**
 * @author itcast
 */
public interface ProcTaskInstanceDao extends JpaRepository<ProcTaskInstance,String>, JpaSpecificationExecutor<ProcTaskInstance> {
    ProcTaskInstance findByProcessIdAndTaskKey(String processId, String taskKey);
    List<ProcTaskInstance> findByProcessId(String processId);
}
```

画面 6:
```java
package com.ihrm.audit.dao;
import ...
/**
 * @author itcast
 */
public interface ProcTaskInstanceDao extends JpaRepository<ProcTaskInstance,String>, JpaSpecificationExecutor<ProcTaskInstance> {
    ProcTaskInstance findByProcessIdAndTaskKey(String processId, String taskKey);
    //根据流程ID查询
    List<ProcTaskInstance> findByProcessId(String processId);
}
```

画面 8:
```java
package com.ihrm.audit.entity;
import ...
@Entity
@Table(name = "proc_user_group")
@Data
@AllArgsConstructor
@Builder
public class ProcUserGroup {
    private static final long serialVersionUID = 908432495284489553L;
    @Id
    private String id;
    private String name;
    private String param;
    private String sql;
}
```

画面 11:
```java
package com.ihrm.audit.client;
import ...
@Service
public class FeignClientService {
    @Autowired
    private SystemFeignClient systemFeignClient;

    // 查询用户信息
    public User getUserInfoById(String user_id) {
        Result result = systemFeignClient.findUserInfo(user_id);
        if (!result.isSuccess()) throw new RuntimeException("用户ID不存在，请联系管理员。" + user_id);
        return JSON.parseObject(JSON.toJSONString(result.getData()), User.class);
    }

    // 查询部门信息
    public Department getDepartmentInfoByDepartmentId(String departmentId) {
        if (departmentId == null) return null;
        Result result = departmentClient.findByid(departmentId);
        if (!result.isSuccess()) throw new RuntimeException("部门ID不存在，请联系管理员。" + departmentId);
        return JSON.parseObject(JSON.toJSONString(result.getData()), Department.class);
    }
}
```

画面 13:
```java
package com.ihrm.audit.client;
import ...
/**
 * 声明接口，通过Feign调用其他微服务
 */
@FeignClient("ihrm-system")
public interface SystemFeignClient {
    /**
     * 调用微服务的接口
     * @RequestMapping(value = "/sys/user/{id}", method = RequestMethod.GET)
     * Result findByid(@PathVariable(value = "id") String id);
     */
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
