# 画面线理解：day14-9-用户还款-第三阶段-发送消息

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-9-用户还款-第三阶段-发送消息_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:53, 01:07, 02:14, 02:41, 02:54, 03:05, 03:26, 04:14, 05:05, 05:52, 06:17, 06:53, 07:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:18:33

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 RocketMQ 的还款服务消息处理流程，包括消息生产者、消费者、数据库操作及系统间交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款服务与存管代理服务、存管系统的交互流程图，包含多个步骤如“1.1.查询到期的还款计划”、“1.7.冻结还款金额”等。
画面2：IDE中显示 `RepaymentService.java` 文件，其中 `preRepayment` 方法内有 `System.out.println("还款预处理成功");` 语句。
画面3：IDE中显示 `RepaymentProducer.java` 文件，准备编写消息生产者。
画面4：文件资源管理器中显示 `day14` 文件夹，包含 `elasticsearch-7.4` 等文件夹。
画面5：IDE中显示 `RepaymentRequest.java` 文件，其中 `@ApiModelProperty("请求流水号")` 注解的字段 `private String requestNo;` 被高亮。
画面6：展示还款服务与存管代理服务、存管系统的交互流程图，与画面1类似，但步骤编号和部分描述略有不同。
画面7：IDE中显示 `RepaymentRequest.java` 文件，其中 `@ApiModelProperty("业务id")` 注解的字段 `private Long id;` 被高亮。
画面8：显示 `RepaymentDetailRequest.java` 文件，包含多个 `@ApiModelProperty` 注解的字段，如 `@ApiModelProperty("投资人用户编码") private String userNo;`。
画面9：IDE中显示 `RepaymentProducer.java` 文件，正在编写 `@Component` 注解和 `RocketMQTemplate` 字段。
画面10：IDE中显示 `RepaymentProducer.java` 文件，正在编写 `confirmRepayment` 方法，其中 `//1.构造消息` 和 `//2.发送消息` 语句被高亮。
画面11：IDE中显示 `RepaymentProducer.java` 文件，正在使用 `JsonObject` 类的 `put` 方法构造消息体。
画面12：IDE中显示 `RepaymentProducer.java` 文件，正在使用 `Message` 类的构造方法 `Message(String topic, Object payload)`。
画面13：IDE中显示 `RepaymentProducer.java` 文件，正在使用 `rocketMQTemplate` 对象的 `send` 方法发送消息。
画面14：展示一个包含“还款服务”、“RocketMQ”、“存管服务”等节点的流程图，描述消息发送、接收、处理和状态更新的流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
Boolean preRepaymentResult = preRepayment(repaymentPlan, repaymentDetail.getPreRequestNo());
if (preRepaymentResult) {
    System.out.println("还款预处理成功");
}
```

画面5：
```java
@ApiModel(value = "还款请求信息")
public class RepaymentRequest {
    @ApiModelProperty("请求流水号")
    private String requestNo;
    @ApiModelProperty("预处理业务流水号")
    private String preRequestNo;
    @ApiModelProperty("标的编码")
    private String projectNo;
    @ApiModelProperty("平台佣金 -- 具体金额")
    private BigDecimal commission;
    @ApiModelProperty("放款明细")
    private List<RepaymentDetailRequest> details;
    @ApiModelProperty("业务id")
    private Long id;
    @ApiModelProperty("还款金额")
    private BigDecimal amount;
}
```

画面8：
```java
/**
 * @author wuzhao@itcast.cn
 * @since 2019/5/26
 */
@ApiModel(value = "RepaymentDetailRequest", description = "还款明细请求信息")
public class RepaymentDetailRequest {
    @ApiModelProperty("投资人用户编码")
    private String userNo;
    @ApiModelProperty("向投资人收取的佣金")
    private BigDecimal commission;
    @ApiModelProperty("利息")
    private BigDecimal dividend;
    @ApiModelProperty("投资人应得本金")
    private BigDecimal amount;
    @ApiModelProperty("投资人应得利息")
    private BigDecimal interest;
}
```

画面9：
```java
import cn.itcast.wanxingzp.api.depository.model.RepaymentRequest;
import cn.itcast.wanxingzp.repayment.entity.RepaymentPlan;
import org.springframework.stereotype.Component;

@Component
public class RepaymentProducer {
```

画面10：
```java
@Resource
private RocketMQTemplate rocketMQTemplate;

public void confirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
    //1.构造消息
    //2.发送消息
}
```

画面11：
```java
//1.构造消息
JsonObject jsonObject = new JsonObject();
jsonObject.put("requestNo", repaymentRequest.getRequestNo());
jsonObject.put("preRequestNo", repaymentRequest.getPreRequestNo());
jsonObject.put("projectNo", repaymentRequest.getProjectNo());
jsonObject.put("commission", repaymentRequest.getCommission());
jsonObject.put("details", repaymentRequest.getDetails());
jsonObject.put("id", repaymentRequest.getId());
jsonObject.put("amount", repaymentRequest.getAmount());
```

画面12：
```java
Message<String> message = new Message("repayment-topic", jsonObject.toString());
```

画面13：
```java
rocketMQTemplate.send("repayment-topic", message);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
- 标题：用户还款业务流程图
- 流程图结构：
  - “还款服务”指向“存管代理服务”（步骤1.1、1.2、1.3、1.4、1.5、1.6、1.7、1.8、1.9、1.10）
  - “存管代理服务”指向“存管系统”（步骤1.4、1.5、1.6、1.7、1.8、1.9）
  - “存管系统”指向“还款服务”（步骤1.7、1.8、1.9）

画面6：
- 标题：还款服务与存管代理服务、存管系统的交互流程图
- 流程图结构：
  - “还款服务”指向“存管代理服务”（步骤1.1、1.2、1.3、1.4、1.5、1.6、1.7、1.8、1.9、1.10）
  - “存管代理服务”指向“存管系统”（步骤1.4、1.5、1.6、1.7、1.8、1.9）
  - “存管系统”指向“还款服务”（步骤1.7、1.8、1.9）

画面14：
- 标题：还款服务与RocketMQ、存管服务的交互流程图
- 流程图结构：
  - “还款服务”指向“RocketMQ”（步骤1.发送确认还款事务消息）
  - “RocketMQ”指向“还款服务”（步骤2.消息接收成功，不可消费）
  - “还款服务”指向“存管服务”（步骤3.接收回调、4.执行本地事务、5.发送执行结果、6.修改消息状态为可消费、7.接收消息（重试）、8.通过Feign向存管）
  - “存管服务”指向“还款服务”（步骤8.通过Feign向存管）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
