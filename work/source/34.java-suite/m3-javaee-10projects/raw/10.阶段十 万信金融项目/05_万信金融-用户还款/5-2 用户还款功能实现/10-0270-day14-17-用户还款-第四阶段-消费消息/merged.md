# day14-17-用户还款-第四阶段-消费消息

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-17-用户还款-第四阶段-消费消息_【海量资源尽在 666java.com】.mp4
- 时长 8分17秒（音频 497s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来的话咱就应该把第四阶段最后一块这个代码给他编写出来哪一块代码呢就是我刚才反复说的啊就是这块我们缓缓服务这边是不是要作为消息的接收方先接收消息然后呢调用是不是我们刚才开发的这个什么呀方法在这个方案里边呢是不是通过飞影发起了这个什么呀请求然后呢这个
[00:28] 推进这个业务往后执行对不对所以咱现在是缺这么一个源头就是接收消息这个源头它呢其实是触发咱们整个第四阶段这个业务的一个什么呀入口那这个接收消息不就是跟之前一样还是写那个listen的那个监听器吗这个代码呢大家其实也比较熟悉咱把这个开发完之后咱整个第四阶段这个代码就全部开发完流程内全部打通了那咱先看一看这个讲义吧你看看
[00:58] 是不是还是这个什么呀消息的接收方吧这个监听器对不对那咱接下来参考讲一把这块代码写一下这块代码我先问大家一个问题这个代码应该写到哪哪边啊你可别搞糊涂了啊哪边呢咱之前很早的时候分析过我们说在咱们这个案例当中呢是还款服务发消息然后还款服务啊也要干什么接受消息就是自己发送自己在干什么呀消费所以我们这个代码应该写到repayment Service这边啊
[01:29] 这边我们还是在这个谁呀message这个包里边我们再新建一个类来接收消息名字呢我们跟讲义保持一致吧叫conform repayment consumer对不对好然后呢他要实现一个RocketMQ的一个什么呀接口应该叫叫什么呀叫RocketMQ listenerrocket mq listener
[02:06] 这里边有个范形范形呢都是字符串然后呢我们把这个上面必要的这个注记呢跟他加上我们给讲一保持一致吧呃那这里边呢有个细节咱们之前其实也反复强调过哪个地方呀这里边是不是有个指我们得跟发送方那边要保持一致是不是发送方我先给你找找发送消息的代码应该是这儿吧是不是跑丢丧了对不对
[02:42] 是不是应该跟这吧这一只这是我们当时这个目的地吗啊tp confirm 什么呀repayment 你看好啊哪了这个这个你不能乱写啊这是他自己的那个左边吗嗯这是住进我们家加上之后呢我们接下来是不是要重写他这里边的一个方法咱先把他这个方法先给他生成了这个方法里边这个参议是不是就是他接收到的这个消息对吧接收到消息之后呢这里边的代码咱应该比较熟悉啊第一步就是
[03:13] 还是解析消息第二步呢就是干什么呀对执行本地调是不是就这两步对吧那咱接下来一步一步来吧好第一步解析消息这一块呢还是那个先把这个String类型的这个消息转换成JSON Object对吧JSON第二我们要调用他的一个方法叫Parse Object
[03:43] 然后呢把这个消息给他扔进来然后呢返回的就是一个jsonobject这做了一个转换然后呢我们就要从这个什么呀jsonobject对象里边来取数据对吧我们当时发送的时候应该是就是发了几个数据传了几个数据你看这put put是不是put两个数据那咱接下来是不是要根据这两个键来取出来这两个值吗
[04:15] 那咱继续写jsonobject的点取数据应该是叫getgetstream对不对这个代码的话我们需要跟发送方这保持一致件的名字不能随便乱写是吧然后呢我们还需要把它转按成什么呀对象嘛转按成对象的话这个就要调用jsonjsonobject的一个方法叫
[04:49] 然后呢把整个这一块东西给他扔进去那我们拿到手的是不是就是这个repayment plan对象就取出来了大写对吧那取第二个东西是不是应该是跟这儿是一样的对不对这还少一个参数啊转成什么类型呢对不对repayment plan.class之前写的那时候就把这个参数给忘了
[05:27] 那第二个数据我们在取的时候应该也是一样的改改东西就行了第二个你看看这个发送方这边应该是这个什么呀repayment什么呀request对吧就是他我们改一改这个你要细心这要改这个件的名字对吧这个类型也得改是不是然后呢就是前面吧前面我们声明一个变量接收一下就行你看现在是不是我们就把这个
[06:03] 数据从这个消息当中给他干什么解析出来解析出来之后就该走第二执行本地业务本地业务大家看看这个图本地要不就是什么呀2.3对吧通过飞影发起点上请求然后推进后边这个代码是不是继续往后走就行了对不对那整个这一块咱是不是封装到了一要从一个方法里面你还有印象吗就是这个invoke conformal repayment
[06:28] 那咱就需要在这儿是不是把要层给他注入进来叫at.worldprivaterepaymentservice注进来之后呢我们调一下那个方法就完事了点叫invokeconformrepayment他要了两个参议呗是不是咱刚刚从消息里边解析出来往这儿一扔就搞定这个代码大家看没错吧
[07:06] 那这就是我们说的这个消息的接收方啊这块代码写完之后呢咱整个第四阶段代码就全部开完这个流程呢也全部打通了啊咱接下来大概把这个流程结合代码给回顾一下啊大家看一下首先呢就是他其实先走了就是这块代码就是这个监听器在监听这个什么呀Rocky的MQ一旦有消息的他是不是有接收放到这儿了对不对放到这儿之后呢我们从这里边开始
[07:31] 解析消息拿到我们想要的这个数据拿到数据之后呢我们就执行本地业务本地业务呢我们这个出发的代码放放到这个发表里边了你可以跟踪一下是不是进来之后你看这是不是通过飞行代理开始这个发请求了其实这呢就已经走到这个哪了2.3了就开始走这了啊开始走这了那再往后这个代码咱就不再跟了吧再往后的话是不是其实请求一发就发到哪边了呀是不是就发到这个什么呀
[08:02] 存款代理服务那边啊然后就往后走然后跟银行做交互最后这个返回结果做咱第四阶段整个代码这个呃开发完的流程也打通了那咱一会呢就要进行什么呀功能测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  import org.apache.RocketMQ.spring.core.RocketMQListener;
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

