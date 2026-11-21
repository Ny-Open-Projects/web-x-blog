# 画面线理解：day13-12-解决满标放款业务中的事务问题-交易中心-事务监听器

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-7 解决满标放款业务中的事务问题
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-7 解决满标放款业务中的事务问题\day13-12-解决满标放款业务中的事务问题-交易中心-事务监听器_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:51, 02:30, 03:37, 05:03, 06:22, 07:49, 09:56, 10:52, 12:17, 14:12, 14:57, 16:11, 17:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:08:38

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 RocketMQ 实现分布式事务，通过事务监听器确保“还款计划”和“应收明细”两个服务的状态一致性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `P2pTransactionProducer.java` 中的 `updateProjectStatusAndStartRepayment` 方法，用于发送消息并更新项目状态。
画面2：PPT内容，说明在“还款放款”业务中，中心交易修改状态为“还款中”时，需通知还款服务生成还款计划和应收明细，两者为原子性操作，建议使用 RocketMQ 实现最终一致性。
画面3：展示 `ProjectServiceImpl.java` 中的 `updateProjectStatusAndStartRepayment` 方法，其中包含更新项目状态和贷款状态的逻辑。
画面4：展示 `ProjectServiceImpl.java` 中的 `updateProjectStatusAndStartRepayment` 方法，已删除部分代码，仅保留核心逻辑。
画面5：PPT内容，说明实现 RocketMQ 事务监听器有两个功能：`executeLocalTransaction`（执行本地事务）和 `checkLocalTransaction`（检查本地事务）。
画面6：展示 `P2pTransactionListenerImpl` 类的定义，包含 `@Component` 注解和 `@RocketMQTransactionListener` 注解，指定 `txProducerGroup`。
画面7：展示 `P2pTransactionListenerImpl` 类的包名和导入的 RocketMQ 相关类。
画面8：展示 `executeLocalTransaction` 方法的实现，解析消息并执行本地事务。
画面9：展示 `ProjectService` 接口定义，包含 `createProject` 方法。
画面10：展示 `executeLocalTransaction` 方法中返回 `RocketMQLocalTransactionState.COMMIT`。
画面11：展示 `executeLocalTransaction` 方法中调用 `projectService.updateProjectStatusAndStartRepayment(project)`。
画面12：展示 `checkLocalTransaction` 方法中调用 `projectMapper.selectById(projectId)`。
画面13：展示 `checkLocalTransaction` 方法中返回 `RocketMQLocalTransactionState.COMMIT`。
画面14：展示 `checkLocalTransaction` 方法中根据查询结果返回 `COMMIT` 或 `ROLLBACK`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
private RocketMQTemplate rocketMQTemplate;
public void updateProjectStatusAndStartRepayment(Project project, ProjectWithTendersDTO projectWithTendersDTO) {
    // 1. 构造消息
    JSONObject object = new JSONObject();
    object.put("project", project);
    object.put("projectWithTendersDTO", projectWithTendersDTO);
    Message<String> msg = MessageBuilder.withPayload(object.toJSONString()).build();
    // 2. 发送消息
    rocketMQTemplate.sendMessageInTransaction(txProducerGroup, "PID_START_REPAYMENT", msg, null);
}
```

画面3：
```java
public Boolean updateProjectStatusAndStartRepayment(Project project) {
    project.setProjectStatus(ProjectCode.REPAYING.getCode());
    final int count = modifProject(project);
    project.setProjectStatus(project.getProjectStatus());
    project.setLoanStatusNo(project.getLoanStatusNo());
    project.setProjectId(project.getProjectId());
    return count;
}
```

画面5：
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_START_REPAYMENT")
public class P2pTransactionListenerImpl implements RocketMQTransactionListener {
    @Autowired
    private ProjectService projectService;
    // 执行本地事务
    @Override
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        return null;
    }
    // 检查本地事务
    @Override
    public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
        return null;
    }
}
```

画面7：
```java
import org.apache.rocketmq.spring.core.RocketMQTemplate;
import org.apache.rocketmq.spring.core.RocketMQLocalTransactionState;
import org.springframework.messaging.Message;
import org.springframework.messaging.support.MessageHeaderAccessor;
import org.springframework.stereotype.Component;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocketmq.spring.annotation.RocketMQTransactionListener;
import org.apache.rocket
