# 11-审批业务概述：环境搭建

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\11-审批业务概述：环境搭建_【海量资源尽在 ubkz.com】.mp4
- 时长 4分26秒（音频 267s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那刚才呢简单的对我们这个业务呢做了一个分析同时呢说明了一下数据库表的这个设计那这些我们看过了之后啊那接下来呢咱们就开始去着手写代码首先第一件事搭建一个小小的环境说的直白一点数据库当中我们多创建了三张表那接下来就把三张表所对应的实体类以及DU给它完善出来那这些内容呢都比较简单不需要各位再去一行一行的写了
[00:31] 在今天给各位提供好的资料当中咱们已经准备好了那在今天的资料当中有对应的do有三个那对应的实体类有三个跟我们刚才的数据库表一一对应那我们接下来要做的事情把对应的实体类control ccopy到我们审批模块当中的entity当中哎 扣回来了那除了实体类之外还需要一个对应do
[01:03] 那DU呢同样咱们找一下把DUCtrl C也给它copy过来那copy过来之后呢其实这个都是一些比较简单的DU那其中呢在这个任务DU当中呢给它补充了一个这么两个方法这两个方法第一个根据流程ID和任务的key来进行查询第二个就是根据流程ID来查询那不知道各位还有一没有印象其实对于这个DU呢
[01:36] 其中有一个方法就是根据流程ID来查询那为什么要有这个呢是这样的这个是为了我们最终展示每个节点数据的因为我们一个流程发起了之后每一个节点每一个步骤它都有不同的人来处理所以我们这边呢刚才也说过任务和实力是一个一对多关系那我们的任务是多的一方那一个流程有多个处理的节点
[02:11] 所以我们展示的时候为了更好的展示通过流程要查询出所有操作人就是这么一个方法好了那上面这个方法呢咱们先删掉了有的时候需要的时候咱们再说OK好了那接着还有一个Uder Group到这里面没什么可说的好了那接下来就是实体类那在实体类当中Intense代表的是我们流程实例所有相应的注释呢这边都有其中各位要注意的是我们申请的业务数据需要把
[02:43] 前端传递过来的这些内容转化为JSON转化成字符串再存到数据库那接下来还有任务那任务里面就一个各位注意的Boss ID这个代表的是外界好了接着还有一个User GroupUser Group里面ID CircleOK那除了这个DU和试解类之外为了我们方便操作那还给各位准备好了这么一个Client这个里面是
[03:14] 咱们相应的一些远程调用其他微服务的一些方法这些方法里面呢我们只需要用两个就够了因为我们可能会涉及到根据用户ID去查询用户所以要远程调用系统微服务那接下来呢我们这边呢也把这两个Ctrl Ccall到我们这边右键创建一个包CLI INT CLIENT那接着把这个call进去
[03:47] 好了把这些呢做一个小小的整理好了那这样一来呢我call过来了一个finclan的Service里面通过咱们的一个system finclan哎这是我们定义的一系列的接口OK把这些没用的我就先删掉了注意这个是跨服务调用系统为服务根据ID查询用户这个之前我们都学过了好了那这个就是我们所涉及到的环境搭建需要各位做的事情第一个
[04:19] 实体类第二个DL第三个远程调用其他微服务的这么两个工具类导进来即可

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

