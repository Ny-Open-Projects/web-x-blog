# 画面线理解：day13-13-解决满标放款业务中的事务问题-还款服务

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-7 解决满标放款业务中的事务问题
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-7 解决满标放款业务中的事务问题\day13-13-解决满标放款业务中的事务问题-还款服务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:47, 01:31, 02:10, 02:38, 04:18, 05:22, 06:17, 06:38, 07:11, 08:04, 08:35, 09:11, 13:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:09:30

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 RocketMQ 消息队列实现还款服务的异步处理，包括消息消费者监听、业务逻辑处理、数据库事务管理及状态流转。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款流程图，重点在“接口⑤”和“接口⑥”，涉及状态变更和交易记录更新。
画面2：展示 RepaymentServiceImpl.java 代码，处理还款逻辑，包括计算月数、获取还款方式、生成还款计划。
画面3：继续展示 RepaymentServiceImpl.java 代码，重点在生成还款计划并保存到数据库。
画面4：展示 StartRepaymentMessageConsumer.java 文件，开始编写消息消费者类。
画面5：展示 StartRepaymentMessageConsumer.java 的 RocketMQ 相关配置注解。
画面6：展示 StartRepaymentMessageConsumer.java 中解析消息体并转换为 ProjectWithTendersDTO 对象。
画面7：展示 StartRepaymentMessageConsumer.java 的代码，准备调用业务服务。
画面8：展示 RepaymentServiceImpl.java 中 startRepayment 方法的业务逻辑。
画面9：展示 RepaymentServiceImpl.java 中 startRepayment 方法的事务注解。
画面10：展示 PPT 内容，讲解消息接收方（还款微服务）的实现，包括 @RocketMQMessageListener 注解和业务调用。
画面11：展示还款流程图，重点在“接口⑥”和“接口⑦”，涉及状态变更和交易记录更新。
画面12：展示 RepaymentServiceImpl.java 中 startRepayment 方法的业务逻辑。
画面13：展示 PPT 内容，讲解功能测试，包括数据库索引创建语句。
画面14：展示还款流程图，重点在“接口⑥”和“接口⑦”，涉及状态变更和交易记录更新。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
//1.2 获取投标信息
List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
//1.3 计算还款的月数
Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
Integer month = cell.intValue();
//1.4 还款方式，只针对等额本息
String repaymentWay = projectDTO.getRepaymentWay();
if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
    //1.5 生成还款计划
    EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getPeriod(), projectDTO.getTenders());
    //2.1 根据投资人生成明细
    tenders.forEach(tenderDTO -> {
        //2.2 保存应收明细到数据库
        List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
        planList.forEach(plan -> tenderDTO.receipt(plan));
    });
}
```

画面3：
```java
//2.2 保存应收明细到数据库
List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
planList.forEach(plan -> tenderDTO.receipt(plan));
```

画面4：
```java
package cn.itcast.wanxing2p.repayment.message;
import org.apache.rocketmq.spring.core.RocketMQListener;
```

画面5：
```java
@RocketMQMessageListener(topic = "TP_START_REPAYMENT", consumerGroup = "CID_START_REPAYMENT")
```

画面6：
```java
final JSONObject jsonObject = JSON.parseObject(new String(byte[]));
Project project = JSON.parseObject(jsonObject.getString("project"), Project.class);
```

画面7：
```java
@RocketMQMessageListener(topic = "TP_START_REPAYMENT", consumerGroup = "CID_START_REPAYMENT")
public class StartRepaymentMessageConsumer implements RocketMQListener<String> {
```

画面8：
```java
//1.1 获取投标信息
ProjectDTO projectDTO = projectWithTendersDTO.getProject();
//1.2 获取投标信息
List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
//1.3 计算还款的月数
Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
Integer month = cell.intValue();
//1.4 还款方式，只针对等额本息
String repaymentWay = projectDTO.getRepaymentWay();
if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
    //1.5 生成还款计划
    EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getPeriod(), projectDTO.getTenders());
    //2.1 根据投资人生成明细
    tenders.forEach(tenderDTO -> {
        //2.2 保存应收明细到数据库
        List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
        planList.forEach(plan -> tenderDTO.receipt(plan));
    });
}
```

画面9：
```java
@Transactional
public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
    //1.1 获取投标信息
    ProjectDTO projectDTO = projectWithTendersDTO.getProject();
    //1.2 获取投标信息
    List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
    //1.3 计算还款的月数
    Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
    Integer month = cell.intValue();
    //1.4 还款方式，只针对等额本息
    String repaymentWay = projectDTO.getRepaymentWay();
    if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
        //1.5 生成还款计划
        EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getPeriod(), projectDTO.getTenders());
        //2.1 根据投资人生成明细
        tenders.forEach(tenderDTO -> {
            //2.2 保存应收明细到数据库
            List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
            planList.forEach(plan -> tenderDTO.receipt(plan));
        });
    }
}
```

画面10：
```java
@RocketMQMessageListener(topic = "TP_START_REPAYMENT", consumerGroup = "CID_START_REPAYMENT")
public class StartRepaymentMessageConsumer implements RocketMQListener<String> {
    @Autowired
    private RepaymentService repaymentService;
    @Override
    public void onMessage(String projectStr) {
        System.out.println("消费消息：" + projectStr);
        JSONObject jsonObject = JSON.parseObject(projectStr);
        ProjectWithTendersDTO projectWithTendersDTO = JSON.parseObject(jsonObject.getString("projectWithTendersDTO"), ProjectWithTendersDTO.class);
        //2. 调用业务层执行本地事务
        repaymentService.startRepayment(projectWithTendersDTO);
    }
}
```

画面13：
```sql
use p2p_repayment . repayment_plan ;
ALTER TABLE .repayment_plan
ADD UNIQUE INDEX plan_unique ( CONSUMER_ID , PROJECT_ID ,
NUMBER_OF_PERIODS );
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面10：
标题：5.4.2 消息接收方：还款微服务
内容：
- 实现 RocketMQ 事务消息监听器，收到消息后，解析消息、调用业务层进行处理。
- 代码示例：
```java
@RocketMQMessageListener(topic = "TP_START_REPAYMENT", consumerGroup = "CID_START_REPAYMENT")
public class StartRepaymentMessageConsumer implements RocketMQListener<String> {
    @Autowired
    private RepaymentService repaymentService;
    @Override
    public void onMessage(String projectStr) {
        System.out.println("消费消息：" + projectStr);
        JSONObject jsonObject = JSON.parseObject(projectStr);
        ProjectWithTendersDTO projectWithTendersDTO = JSON.parseObject(jsonObject.getString("projectWithTendersDTO"), ProjectWithTendersDTO.class);
        //2. 调用业务层执行本地事务
        repaymentService.startRepayment(projectWithTendersDTO);
    }
}
```

画面13：
标题：5.4.3 功能测试
内容：
- 交易中心和还款服务都成功。
- 交易中心执行本地事务失败，则还款服务接收不到消息。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
