# 画面线理解：20.获取支付结果-支付结果更新

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\20.获取支付结果-支付结果更新【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:54, 03:36, 04:53, 05:51, 07:20, 08:20, 09:31, 10:30, 11:43, 13:08, 14:44, 16:53, 17:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:17:19

1) 这一组画面整体在讲什么（一句话）：
讲解支付结果更新的交互流程，包括通过MQ发送消息、消费消息并更新订单状态的代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档大纲，当前章节为6.6.1 交互流程，描述支付渠道代理服务查询支付结果后，通过MQ发送“支付结果更新”消息，交易服务监听并更新订单状态。
画面2：展示6.6.2 发送消息部分，代码中定义了发送“支付结果更新”消息的方法，使用rocketMQTemplate.convertAndSend发送。
画面3：展示PayConsumer类中，当查询到支付结果后，调用payProducer.payResultNotice方法发送消息。
画面4：展示PayConsumer类中，当支付状态未知时抛出异常，等待重试。
画面5：展示数据库表结构，包含TRADE_NO、MERCHANT_ID、STORE_ID等字段。
画面6：展示TransactionService类中，使用LambdaUpdateWrapper更新订单状态。
画面7：展示TransactionService类中，使用LambdaUpdateWrapper设置更新条件。
画面8：展示dubbo配置文件，定义了服务分组、端口、注册中心等信息。
画面9：展示PayProducer类中，定义了发送“支付结果更新”消息的常量TOPIC_RESULT。
画面10：展示PayProducer类中，根据支付渠道判断使用哪个接口查询订单状态。
画面11：展示TransactionConsumer类中，接收MQ消息并解析为PaymentResponseDTO。
画面12：展示AlipayClient类中，调用execute方法查询支付结果。
画面13：展示TransactionConsumer类中，根据支付状态更新订单状态。
画面14：展示TransactionConsumer类中，根据支付状态更新订单状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
6.6.1 交互流程
支付渠道代理服务查询到支付结果，将支付结果更新消息发送给交易服务，实现订单状态更新，流程如下：
1、支付渠道代理服务查询到支付结果
2、向MQ发送“支付结果更新”消息
3、交易服务监听“支付结果更新”消息队列
4、交易服务接收到“支付结果更新”消息，更新订单状态

画面2：
private static final String TOPIC_RESULT = "TP_PAYMENT_RESULT";
/**
 * 发送支付结果消息
 * @param result
 */
public void payResultNotice(PaymentResponseDTO result){
 rocketMQTemplate.convertAndSend(TOPIC_RESULT,result);
}

画面3：
//如果查询到订单状态为未知，抛出异常，等待重试
if(responseDTO == null || TradeStatus.UNKNOWN.equals(responseDTO.getTradeState()) || TradeStatus.USERPAYING.equals(responseDTO.getTradeState())){
 throw new RuntimeException("支付状态未知，等待重试");
}
//如果重试的次数达到一次数量，不要重试查询，将消息记录到数据库，由单独的程序人工进行处理
//将订单状态，再次发到mq
payProducer.payResultNotice(responseDTO);

画面4：
//如果查询到订单状态为未知，抛出异常，等待重试
if(responseDTO == null || TradeStatus.UNKNOWN.equals(responseDTO.getTradeState()) || TradeStatus.USERPAYING.equals(responseDTO.getTradeState())){
 throw new RuntimeException("支付状态未知，等待重试");
}
//如果重试的次数达到一次数量，不要重试查询，将消息记录到数据库，由单独的程序人工进行处理
//将订单状态，再次发到mq
payProducer.payResultNotice(responseDTO);

画面5：
Field Type Comment
ID bigint(20) NOT NULL 主键
TRADE_NO varchar(50) NOT NULL 订单号
MERCHANT_ID bigint(20) NOT NULL 商户ID
STORE_ID bigint(20) NOT NULL 店铺ID
APP_ID varchar(50) NOT NULL 应用ID
PAY_CHANNEL varchar(50) NOT NULL 支付渠道
PAY_CHANNEL_MCH_ID varchar(50) NULL 支付渠道商户ID
PAY_CHANNEL_MCH_APP_ID varchar(50) NULL 支付渠道商户应用ID
CHANNEL varchar(50) NULL 渠道
OUT_TRADE_NO varchar(50) NULL 交易流水号
GOODS_ID varchar(50) NULL 商品ID
GOODS_NAME varchar(255) NULL 商品名称
GOODS_PRICE decimal(10,2) NULL 商品价格
GOODS_NUM int(11) NULL 商品数量
GOODS_TOTAL decimal(10,2) NULL 商品总价
GOODS_TYPE varchar(50) NULL 商品类型
GOODS_ATTR varchar(255) NULL 商品属性
GOODS_DESC varchar(255) NULL 商品描述
GOODS_IMAGE varchar(255) NULL 商品图片
GOODS_URL varchar(255) NULL 商品链接
GOODS_URL_TYPE varchar(50) NULL 商品链接类型
GOODS_URL_NAME varchar(255) NULL 商品链接名称
GOODS_URL_DESC varchar(255) NULL 商品链接描述
GOODS_URL_IMAGE varchar(255) NULL 商品链接图片
GOODS_URL_PRICE decimal(10,2) NULL 商品链接价格
GOODS_URL_NUM int(11) NULL 商品链接数量
GOODS_URL_TOTAL decimal(10,2) NULL 商品链接总价
GOODS_URL_TYPE_NAME varchar(50) NULL 商品链接类型名称
GOODS_URL_TYPE_DESC varchar(255) NULL 商品链接类型描述
GOODS_URL_TYPE_IMAGE varchar(255) NULL 商品链接类型图片
GOODS_URL_TYPE_PRICE decimal(10,2) NULL 商品链接类型价格
GOODS_URL_TYPE_NUM int(11) NULL 商品链接类型数量
GOODS_URL_TYPE_TOTAL decimal(10,2) NULL 商品链接类型总价
GOODS_URL_TYPE_NAME_DESC varchar(255) NULL 商品链接类型名称描述
GOODS_URL_TYPE_NAME_IMAGE varchar(255) NULL 商品链接类型名称图片
GOODS_URL_TYPE_NAME_PRICE decimal(10,2) NULL 商品链接类型名称价格
GOODS_URL_TYPE_NAME_NUM int(11) NULL 商品链接类型名称数量
GOODS_URL_TYPE_NAME_TOTAL decimal(10,2) NULL 商品链接类型名称总价
GOODS_URL_TYPE_NAME_DESC_IMAGE varchar(255) NULL 商品链接类型名称描述图片
GOODS_URL_TYPE_NAME_DESC_PRICE decimal(10,2) NULL 商品链接类型名称描述价格
GOODS_URL_TYPE_NAME_DESC_NUM int(11) NULL 商品链接类型名称描述数量
GOODS_URL_TYPE_NAME_DESC_TOTAL decimal(10,2) NULL 商品链接类型名称描述总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE decimal(10,2) NULL 商品链接类型名称描述图片价格
GOODS_URL_TYPE_NAME_DESC_IMAGE_NUM int(11) NULL 商品链接类型名称描述图片数量
GOODS_URL_TYPE_NAME_DESC_IMAGE_TOTAL decimal(10,2) NULL 商品链接类型名称描述图片总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM int(11) NULL 商品链接类型名称描述图片价格数量
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_TOTAL decimal(10,2) NULL 商品链接类型名称描述图片价格总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL decimal(10,2) NULL 商品链接类型名称描述图片价格数量总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC varchar(255) NULL 商品链接类型名称描述图片价格数量总价描述
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE varchar(255) NULL 商品链接类型名称描述图片价格数量总价描述图片
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE decimal(10,2) NULL 商品链接类型名称描述图片价格数量总价描述图片价格
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM int(11) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL decimal(10,2) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC varchar(255) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE varchar(255) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述图片
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE decimal(10,2) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述图片价格
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM int(11) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述图片价格数量
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL decimal(10,2) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述图片价格数量总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC varchar(255) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述图片价格数量总价描述
GOODS_URL_TYPE
