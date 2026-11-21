# 画面线理解：20.RocketMQ的Producer详解之分布式事务消息（回查的演示）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\20.RocketMQ的Producer详解之分布式事务消息（回查的演示）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:08, 00:09, 00:12, 00:16, 00:17, 00:19, 00:26, 00:38, 00:40, 00:50, 00:53, 01:12, 01:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:06:39

1) 这一组画面整体在讲什么（一句话）：
演示 RocketMQ 事务消息中 TransactionListenerImpl 类的 checkLocalTransaction 和 executeLocalTransaction 方法的代码逻辑与状态回查机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 代码：`@Override public LocalTransactionState checkLocalTransaction(MessageExt msg) { System.out.println("状态回查 ---> " + msg.getTransactionId() + " " + STATE_MAP.get(msg.getTransactionId())); return STATE_MAP.get(msg.getTransactionId()); }`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 2:
- 代码：`// 二次提交确认 return LocalTransactionState.UNKNOWN; catch (Exception e) { e.printStackTrace(); } STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.ROLLBACK_MESSAGE); // 回滚 return LocalTransactionState.ROLLBACK_MESSAGE;`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 3:
- 代码：`@Override public LocalTransactionState executeLocalTransaction(Message msg, Object arg) { try { System.out.println("用户A账户减500元。"); Thread.sleep(millis: 500); // 模拟调用服务 System.out.println(1/0); System.out.println("用户B账户加500元。"); Thread.sleep(millis: 800); STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.COMMIT_MESSAGE); // 二次提交确认 return LocalTransactionState.UNKNOWN; } catch (Exception e) { e.printStackTrace(); } STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.ROLLBACK_MESSAGE); // 回滚 return LocalTransactionState.ROLLBACK_MESSAGE; }`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 4:
- 代码：`// 二次提交确认 return LocalTransactionState.UNKNOWN; catch (Exception e) { e.printStackTrace(); } STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.ROLLBACK_MESSAGE); // 回滚 return LocalTransactionState.ROLLBACK_MESSAGE;`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 5:
- 代码：`STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.COMMIT_MESSAGE); // 二次提交确认 return LocalTransactionState.UNKNOWN; catch (Exception e) { e.printStackTrace(); } STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.ROLLBACK_MESSAGE); // 回滚 return LocalTransactionState.ROLLBACK_MESSAGE;`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 6:
- 代码：`try { System.out.println("用户A账户减500元。"); Thread.sleep(millis: 500); // 模拟调用服务 System.out.println(1/0); System.out.println("用户B账户加500元。"); Thread.sleep(millis: 800); STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.COMMIT_MESSAGE); // 二次提交确认 return LocalTransactionState.UNKNOWN; } catch (Exception e) { e.printStackTrace(); } STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.ROLLBACK_MESSAGE); // 回滚 return LocalTransactionState.ROLLBACK_MESSAGE;`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 7:
- 代码：`// System.out.println(1/0); System.out.println("用户B账户加500元。"); Thread.sleep(millis: 800); STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.COMMIT_MESSAGE); // 二次提交确认 return LocalTransactionState.UNKNOWN; catch (Exception e) { e.printStackTrace(); } STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.ROLLBACK_MESSAGE); // 回滚 return LocalTransactionState.ROLLBACK_MESSAGE;`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 8:
- 代码：`// 二次提交确认 return LocalTransactionState.UNKNOWN; catch (Exception e) { e.printStackTrace(); } STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.ROLLBACK_MESSAGE); // 回滚 return LocalTransactionState.ROLLBACK_MESSAGE;`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 9:
- 代码：`// 二次提交确认 return LocalTransactionState.UNKNOWN; catch (Exception e) { e.printStackTrace(); } STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.ROLLBACK_MESSAGE); // 回滚 return LocalTransactionState.ROLLBACK_MESSAGE;`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 10:
- 代码：`e.printStackTrace(); STATE_MAP.put(msg.getTransactionId(), LocalTransactionState.ROLLBACK_MESSAGE); // 回滚 return LocalTransactionState.ROLLBACK_MESSAGE; }`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 11:
- 代码：`@Override public LocalTransactionState checkLocalTransaction(MessageExt msg) { System.out.println("状态回查 ---> " + msg.getTransactionId() + " " + STATE_MAP.get(msg.getTransactionId())); return STATE_MAP.get(msg.getTransactionId()); }`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 12:
- 代码：`@Override public LocalTransactionState checkLocalTransaction(MessageExt msg) { System.out.println("状态回查 ---> " + msg.getTransactionId() + " " + STATE_MAP.get(msg.getTransactionId())); return STATE_MAP.get(msg.getTransactionId()); }`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 13:
- 代码：`@Override public LocalTransactionState checkLocalTransaction(MessageExt msg) { System.out.println("状态回查 ---> " + msg.getTransactionId() + " " + STATE_MAP.get(msg.getTransactionId())); return STATE_MAP.get(msg.getTransactionId()); }`
- 终端输出：`用户A账户减500元。 用户B账户加500元。 状态回查 ---> AC1037B419D818B4AAC2615A6866K0000 COMMIT_MESSAGE`

画面 14:
- 代码：`@Override public LocalTransactionState checkLocalTransaction(MessageExt msg) { System.out.println("状态回查 ---> " + msg.getTransactionId() + " " + STATE_MAP.get(msg.getTransactionId())); return STATE_MAP.get(msg.getTransactionId()); }`
- 终端输出：`用户A给用户B转账500元`
