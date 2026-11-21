# 画面线理解：day13-11-解决满标放款业务中的事务问题-交易中心-发送消息

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-7 解决满标放款业务中的事务问题
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-7 解决满标放款业务中的事务问题\day13-11-解决满标放款业务中的事务问题-交易中心-发送消息_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:28, 01:43, 02:33, 03:29, 04:19, 05:28, 06:35, 07:37, 08:39, 09:39, 10:14, 10:47, 11:17, 12:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:07:40

1) 这一组画面整体在讲什么（一句话）：
实现一个基于 RocketMQ 的分布式事务消息发送功能，具体是通过创建 P2PTransactionProducer 类来发送“项目状态变更并启动还款”消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 内容“5.4.2 功能实现”下的“5.4.2.1 消息发送方：交易中心微服务”，并列出“1. 检查pom.xml的依赖”，其中包含 RocketMQ 的 Maven 依赖配置。
画面2：PPT 内容继续，列出“2. 检查Apollo中交易中心项目的micro_service.rocketmq命名空间配置”，显示了 rocketmq.producer.group 和 rocketmq.name-server 的配置值。
画面3：在 IntelliJ IDEA 中，右键点击 pom.xml 文件，弹出菜单，显示了正在编辑的依赖项，包括 org.apache.rocketmq 和 org.springframework.boot 的依赖。
画面4：在 IntelliJ IDEA 中，显示了 P2PTransactionProducer.java 文件的代码，方法签名是 public void updateProjectStatusAndStartRepayment(Project project, ProjectWithTendersDTO projectWithTendersDTO)。
画面5：在 IntelliJ IDEA 中，代码编辑器中选中了方法签名中的 ProjectWithTendersDTO 参数。
画面6：在 IntelliJ IDEA 中，代码编辑器中选中了方法体中的 JSON 对象构造部分。
画面7：在 IntelliJ IDEA 中，代码编辑器中选中了 MessageBuilder 的 sendResult 方法。
画面8：在 IntelliJ IDEA 中，代码编辑器中显示了完整的消息构造和发送代码，包括创建 JSONObject、设置字段、构建 MessageBuilder 并发送。
画面9：PPT 内容继续，列出“3. 新建P2pTransactionProducer类，实现交易中心发送消息”，并显示了 P2PTransactionProducer 类的代码，包括 @Component 注解和 rocketMQTemplate 字段。
画面10：在 IntelliJ IDEA 中，显示了 ProjectServiceImpl.java 文件的代码，其中包含审核成功后的业务逻辑和异常处理。
画面11：显示了电脑桌面，多个窗口并排显示，包括 Apollo 配置中心、SQL 管理工具、项目代码编辑器等，用于展示系统架构和数据操作。
画面12：在 IntelliJ IDEA 中，显示了 ProjectServiceImpl.java 文件的代码，其中包含分页查询的逻辑。
画面13：在 IntelliJ IDEA 中，显示了 ProjectServiceImpl.java 文件的代码，其中包含调用 P2PTransactionProducer 的方法。
画面14：在 IntelliJ IDEA 中，显示了 ProjectServiceImpl.java 文件的代码，其中包含调用 P2PTransactionProducer 的方法，并在 else 分支中抛出异常。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
    <version>2.0.2</version>
</dependency>
```
画面2：
```properties
rocketmq.producer.group = producer_start_repayment
rocketmq.name-server = 127.0.0.1:9876
```
画面3：
```xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
    <version>2.0.2</version>
</dependency>
```
画面4：
```java
package cn.itcast.wanxingzp.transaction.message;

import cn.itcast.wanxingzp.api.repayment.model.ProjectWithTendersDTO;
import cn.itcast.wanxingzp.transaction.entity.Project;
import org.springframework.stereotype.Component;

@Component
public class P2pTransactionProducer {
    public void updateProjectStatusAndStartRepayment(Project project, ProjectWithTendersDTO projectWithTendersDTO) {
    }
}
```
画面5：
```java
public void updateProjectStatusAndStartRepayment(Project project, ProjectWithTendersDTO projectWithTendersDTO) {
```
画面6：
```java
//构造消息
JSONObject object = new JSONObject();
object.put("project", project);
object.put("projectWithTendersDTO", projectWithTendersDTO);
```
画面7：
```java
Message<String> msg = MessageBuilder
        .withPayload(object.toJSONString())
        .build();
```
画面8：
```java
//构造消息
JSONObject object = new JSONObject();
object.put("project", project);
object.put("projectWithTendersDTO", projectWithTendersDTO);
Message<String> msg = MessageBuilder
        .withPayload(object.toJSONString())
        .build();
```
画面9：
```java
@Component
public class P2pTransactionProducer {
    @Resource
    private RocketMQTemplate rocketMQTemplate;

    public void updateProjectStatusAndStartRepayment(Project project, ProjectWithTendersDTO projectWithTendersDTO) {
        // 1.构造消息
        JSONObject object = new JSONObject();
        object.put("project", project);
        object.put("projectWithTendersDTO", projectWithTendersDTO);
        Message<String> msg = MessageBuilder
                .withPayload(object.toJSONString())
                .build();
        // 2.发送消息
        SendResult sendResult = rocketMQTemplate
                .send(msg);
    }
}
```
画面10：
```java
//审核成功
return "审核成功";
} else {
    throw new BusinessException(TransactionErrorCode.E_150113);
}
```
画面11：
无代码或配置。
画面12：
```java
if (StringUtils.isNotBlank(order) && StringUtils.isNotBlank(sort)) {
    if (order.toLowerCase().equals("asc")) {
        queryWrapper.orderByAsc(sort);
    } else if (order.toLowerCase().equals("desc")) {
        queryWrapper.orderByDesc(sort);
    }
} else {
    queryWrapper.orderByDesc(Project::getCreateDate);
}
```
画面13：
```java
p2pTransactionProducer.updateProjectStatusAndStartRepayment(project, projectWithTendersDTO);
```
画面14：
```java
p2pTransactionProducer.updateProjectStatusAndStartRepayment(project, projectWithTendersDTO);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“5.4.2 功能实现”，子标题为“5.4.2.1 消息发送方：交易中心微服务”，并列出“1. 检查pom.xml的依赖”。
画面2：PPT 标题为“5.4.2 功能实现”，子标题为“5.4.2.1 消息发送方：交易中心微服务”，并列出“2. 检查Apollo中交易中心项目的micro_service.rocketmq命名空间配置”，并显示了配置项。
画面9：PPT 标题为“5.4.2 功能实现”，子标题为“5.4.2.1 消息发送方：交易中心微服务”，并列出“3. 新建P2pTransactionProducer类，实现交易中心发送消息”，并显示了类的代码。
画面11：无 PPT 标题或架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已满足）
