# 画面线理解：day14-17-用户还款-第四阶段-消费消息

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-17-用户还款-第四阶段-消费消息_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:56, 01:30, 01:45, 02:11, 02:41, 04:06, 04:44, 05:18, 05:33, 06:22, 06:47, 07:21, 07:41, 08:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:25:45

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 RocketMQ 实现还款确认消息的生产、消费与业务处理，包含消息生产者、消费者、服务调用及数据库状态更新等环节。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 `RepaymentServiceImp.java` 中的 `onMessage` 方法，用于解析消息并调用业务方法。
- 代码片段：
  ```java
  @Override
  public void onMessage(String msg) {
      //1.解析消息
      JSONObject jsonObject = JSON.parseObject(msg);
      RepaymentPlan repaymentPlan = JSONObject.parseObject("repaymentPlan",
          RepaymentPlan.class);
      RepaymentRequest repaymentRequest = JSONObject.parseObject(jsonObject.getString("repaymentRequest"),
          RepaymentRequest.class);
  ```

画面 2：
- 展示了 `RepaymentServiceImpl.java` 中的 `invokeConfirmRepayment` 方法，用于调用代理服务确认还款。
- 代码片段：
  ```java
  public void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
      RestResponse<String> repaymentResponse = depositoryAgentApiAgent.confirmRepayment(repaymentPlan, repaymentRequest);
      if (!repaymentResponse.getRetResult().equals(DepositoryAgentReturnCode.RETURN_CODE_00000.getRetCode())) {
          throw new RuntimeException("还款失败");
      }
  ```

画面 3：
- 展示了 `ConfirmRepaymentConsumer.java` 的类定义，用于监听 RocketMQ 消息。
- 代码片段：
  ```java
  @Component
  @RocketMQMessageListener(topic = "TP_CONFIRM_REPAYMENT", consumerGroup = "CID_CONFIRM_REPAYMENT")
  public class ConfirmRepaymentConsumer implements RocketMQListener<String> {
  ```

画面 4：
- 展示了 `ConfirmRepaymentConsumer.java` 的包声明和导入语句。
- 代码片段：
  ```java
  package cn.itcast.wanxingzp.repayment.message;
  import org.apache.rocketmq.spring.core.RocketMQListener;
  public class ConfirmRepaymentConsumer implements RocketMQListener<String> {
  ```

画面 5：
- 展示了 `RepaymentProducer.java` 的类定义，用于发送还款确认消息。
- 代码片段：
  ```java
  @Component
  public class RepaymentProducer {
      @Resource
      private RocketMQTemplate rocketMQTemplate;
  ```

画面 6：
- 展示了 `RepaymentProducer.java` 中的 `confirmRepayment` 方法，用于构建并发送消息。
- 代码片段：
  ```java
  public void confirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
      JSONObject jsonObject = new JSONObject();
      jsonObject.put("repaymentPlan", repaymentPlan);
      jsonObject.put("repaymentRequest", repaymentRequest);
      Message<String> msg = MessageBuilder.withPayload(jsonObject.toJSONString()).build();
      rocketMQTemplate.sendMessagesInTransaction("TP_CONFIRM_REPAYMENT", msg, null);
  ```

画面 7：
- 展示了 `ConfirmRepaymentConsumer.java` 中的 `onMessage` 方法，用于解析消息并执行本地业务。
- 代码片段：
  ```java
  //2.执行本地业务
  RepaymentPlan repaymentPlan = JSONObject.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
  ```

画面 8：
- 展示了 `ConfirmRepaymentConsumer.java` 中的 `onMessage` 方法，用于解析消息并执行本地业务。
- 代码片段：
  ```java
  RepaymentPlan repaymentPlan = JSONObject.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
  ```

画面 9：
- 展示了 `ConfirmRepaymentConsumer.java` 中的 `onMessage` 方法，用于解析消息并执行本地业务。
- 代码片段：
  ```java
  @Override
  public void onMessage(String message) {
      //1.解析消息
      JSONObject jsonObject = JSON.parseObject(message);
      RepaymentPlan repaymentPlan = JSONObject.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
      RepaymentRequest repaymentRequest = JSONObject.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
      //2.执行本地业务
  ```

画面 10：
- 展示了 `RepaymentServiceImpl.java` 中的 `invokeConfirmRepayment` 方法，用于调用代理服务确认还款。
- 代码片段：
  ```java
  public void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
      RestResponse<String> repaymentResponse = depositoryAgentApiAgent.confirmRepayment(repaymentPlan, repaymentRequest);
      if (!repaymentResponse.getRetResult().equals(DepositoryAgentReturnCode.RETURN_CODE_00000.getRetCode())) {
          throw new RuntimeException("还款失败");
      }
  ```

画面 11：
- 展示了 `ConfirmRepaymentConsumer.java` 中的 `onMessage` 方法，用于解析消息并执行本地业务。
- 代码片段：
  ```java
  @Override
  public void onMessage(String message) {
      //1.解析消息
      JSONObject jsonObject = JSON.parseObject(message);
      RepaymentPlan repaymentPlan = JSONObject.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
      RepaymentRequest repaymentRequest = JSONObject.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
      //2.执行本地业务
      repaymentService.invokeConfirmRepayment(repaymentPlan, repaymentRequest);
  ```

画面 12：
- 展示了 `ConfirmRepaymentConsumer.java` 中的 `onMessage` 方法，用于解析消息并执行本地业务。
- 代码片段：
  ```java
  @Override
  public void onMessage(String message) {
      //1.解析消息
      JSONObject jsonObject = JSON.parseObject(message);
      RepaymentPlan repaymentPlan = JSONObject.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
      RepaymentRequest repaymentRequest = JSONObject.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
      //2.执行本地业务
      repaymentService.invokeConfirmRepayment(repaymentPlan, repaymentRequest);
  ```

画面 13：
- 展示了 `RepaymentServiceImpl.java` 中的 `invokeConfirmRepayment` 方法，用于调用代理服务确认还款。
- 代码片段：
  ```java
  public void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
      RestResponse<String> repaymentResponse = depositoryAgentApiAgent.confirmRepayment(repaymentPlan, repaymentRequest);
      if (!repaymentResponse.getRetResult().equals(DepositoryAgentReturnCode.RETURN_CODE_00000.getRetCode())) {
          throw new RuntimeException("还款失败");
      }
  ```

画面 14：
- 展示了还款业务的流程图，描述了从还款服务到存管代理服务再到存管系统的交互流程。
- 流程图结构：
  - 还款服务 → 存管代理服务 → 存管系统
  - 还款服务调用存管代理服务的接口，存管代理服务调用存管系统的接口。
  - 存管系统返回结果，存管代理服务更新状态，还款服务更新状态。
