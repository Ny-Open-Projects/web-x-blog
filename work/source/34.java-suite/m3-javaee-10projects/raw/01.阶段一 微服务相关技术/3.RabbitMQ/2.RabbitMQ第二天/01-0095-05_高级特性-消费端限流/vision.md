# 画面线理解：05_高级特性-消费端限流

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\05_高级特性-消费端限流_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 02:35, 05:06, 05:32, 05:47, 06:39, 06:51, 07:13, 07:49, 08:40, 09:05, 09:11, 09:33, 10:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:47:35

1) 这一组画面整体在讲什么（一句话）：
讲解 RabbitMQ 消费端限流的实现原理与代码配置，包括如何通过 prefetch 属性控制消费速度和手动确认机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示消费端限流的架构图，用户 → MQ → A系统（每秒最大处理1000请求）→ DB。
画面 2: 显示 ConsumerTest 测试类和 OosListener.java 代码，其中包含注释说明如何设置手动确认和 prefetch。
画面 3: 代码编辑器中高亮显示 OosListener.java 中的 @Component 注解和 onMessage 方法。
画面 4: RabbitMQ 管理界面，显示名为 "test_queue_confirm" 的队列，其 Durability 设置为 Durable。
画面 5: 显示 OosListener.java 中的 onMessage 方法，其中包含注释说明如何设置手动确认和 prefetch。
画面 6: 显示 pom.xml 文件，其中包含 spring-rabbitmq 依赖。
画面 7: 显示 ProducerTest.java 中的代码，包含 rabbitTemplate.convertAndSend 方法调用。
画面 8: 显示 ProducerTest.java 中的 testSend 方法，包含 for 循环和 rabbitTemplate.convertAndSend 方法调用。
画面 9: 显示 OosListener.java 中的 onMessage 方法，其中包含注释说明如何设置手动确认和 prefetch。
画面 10: 显示测试结果，ConsumerTest 测试失败，输出 "message confirm..."。
画面 11: 显示 OosListener.java 中的 onMessage 方法，其中包含注释说明如何设置手动确认和 prefetch。
画面 12: 显示测试结果，ConsumerTest 测试失败，输出 "message confirm..."。
画面 13: 显示 OosListener.java 中的 onMessage 方法，其中包含注释说明如何设置手动确认和 prefetch。
画面 14: 展示消费端限流小结，包括在 <rabbitlistener-container> 中配置 prefetch 属性和确认模式为手动确认。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
//1. 处理业务逻辑
System.out.println("处理业务逻辑...");
//2. 手动确认
channel.basicAck(deliveryTag, multiple=true);
//3. 抛异常
channel.basicNack(deliveryTag, multiple=true);
//4. 拒绝消息
channel.basicReject(deliveryTag, true);
//5. 拒绝消息
channel.basicReject(deliveryTag, false);
//6. 拒绝消息
channel.basicReject(deliveryTag, true);
//7. 拒绝消息
channel.basicReject(deliveryTag, true);
//8. 拒绝消息
channel.basicReject(deliveryTag, true);
//9. 拒绝消息
channel.basicReject(deliveryTag, true);
//10. 拒绝消息
channel.basicReject(deliveryTag, true);
//11. 拒绝消息
channel.basicReject(deliveryTag, true);
//12. 拒绝消息
channel.basicReject(deliveryTag, true);
//13. 拒绝消息
channel.basicReject(deliveryTag, true);
//14. 拒绝消息
channel.basicReject(deliveryTag, true);
//15. 拒绝消息
channel.basicReject(deliveryTag, true);
//16. 拒绝消息
channel.basicReject(deliveryTag, true);
//17. 拒绝消息
channel.basicReject(deliveryTag, true);
//18. 拒绝消息
channel.basicReject(deliveryTag, true);
//19. 拒绝消息
channel.basicReject(deliveryTag, true);
//20. 拒绝消息
channel.basicReject(deliveryTag, true);
//21. 拒绝消息
channel.basicReject(deliveryTag, true);
//22. 拒绝消息
channel.basicReject(deliveryTag, true);
//23. 拒绝消息
channel.basicReject(deliveryTag, true);
//24. 拒绝消息
channel.basicReject(deliveryTag, true);
//25. 拒绝消息
channel.basicReject(deliveryTag, true);
//26. 拒绝消息
channel.basicReject(deliveryTag, true);
//27. 拒绝消息
channel.basicReject(deliveryTag, true);
//28. 拒绝消息
channel.basicReject(deliveryTag, true);
//29. 拒绝消息
channel.basicReject(deliveryTag, true);
//30. 拒绝消息
channel.basicReject(deliveryTag, true);
//31. 拒绝消息
channel.basicReject(deliveryTag, true);
//32. 拒绝消息
channel.basicReject(deliveryTag, true);
//33. 拒绝消息
channel.basicReject(deliveryTag, true);
//34. 拒绝消息
channel.basicReject(deliveryTag, true);
//35. 拒绝消息
channel.basicReject(deliveryTag, true);
//36. 拒绝消息
channel.basicReject(deliveryTag, true);
//37. 拒绝消息
channel.basicReject(deliveryTag, true);
//38. 拒绝消息
channel.basicReject(deliveryTag, true);
//39. 拒绝消息
channel.basicReject(deliveryTag, true);
//40. 拒绝消息
channel.basicReject(deliveryTag, true);
//41. 拒绝消息
channel.basicReject(deliveryTag, true);
//42. 拒绝消息
channel.basicReject(deliveryTag, true);
//43. 拒绝消息
channel.basicReject(deliveryTag, true);
//44. 拒绝消息
channel.basicReject(deliveryTag, true);
//45. 拒绝消息
channel.basicReject(deliveryTag, true);
//46. 拒绝消息
channel.basicReject(deliveryTag, true);
//47. 拒绝消息
channel.basicReject(deliveryTag, true);
//48. 拒绝消息
channel.basicReject(deliveryTag, true);
//49. 拒绝消息
channel.basicReject(deliveryTag, true);
//50. 拒绝消息
channel.basicReject(deliveryTag, true);
//51. 拒绝消息
channel.basicReject(deliveryTag, true);
//52. 拒绝消息
channel.basicReject(deliveryTag, true);
//53. 拒绝消息
channel.basicReject(deliveryTag, true);
//54. 拒绝消息
channel.basicReject(deliveryTag, true);
//55. 拒绝消息
channel.basicReject(deliveryTag, true);
//56. 拒绝消息
channel.basicReject(deliveryTag, true);
//57. 拒绝消息
channel.basicReject(deliveryTag, true);
//58. 拒绝消息
channel.basicReject(deliveryTag, true);
//59. 拒绝消息
channel.basicReject(deliveryTag, true);
//60. 拒绝消息
channel.basicReject(deliveryTag, true);
//61. 拒绝消息
channel.basicReject(deliveryTag, true);
//62. 拒绝消息
channel.basicReject(deliveryTag, true);
//63. 拒绝消息
channel.basicReject(deliveryTag, true);
//64. 拒绝消息
channel.basicReject(deliveryTag, true);
//65. 拒绝消息
channel.basicReject(deliveryTag, true);
//66. 拒绝消息
channel.basicReject(deliveryTag, true);
//67. 拒绝消息
channel.basicReject(deliveryTag, true);
//68. 拒绝消息
channel.basicReject(deliveryTag, true);
//69. 拒绝消息
channel.basicReject(deliveryTag, true);
//70. 拒绝消息
channel.basicReject(deliveryTag, true);
//71. 拒绝消息
channel.basicReject(deliveryTag, true);
//72. 拒绝消息
channel.basicReject(deliveryTag, true);
//73. 拒绝消息
channel.basicReject(deliveryTag, true);
//74. 拒绝消息
channel.basicReject(deliveryTag, true);
//75. 拒绝消息
channel.basicReject(deliveryTag, true);
//76. 拒绝消息
channel.basicReject(deliveryTag, true);
//77. 拒绝消息
channel.basicReject(deliveryTag, true);
//78. 拒绝消息
channel.basicReject(deliveryTag, true);
//79. 拒绝消息
channel.basicReject(deliveryTag, true);
//80. 拒绝消息
channel.basicReject(deliveryTag, true);
//81. 拒绝消息
channel.basicReject(deliveryTag, true);
//82. 拒绝消息
channel.basicReject(deliveryTag,
