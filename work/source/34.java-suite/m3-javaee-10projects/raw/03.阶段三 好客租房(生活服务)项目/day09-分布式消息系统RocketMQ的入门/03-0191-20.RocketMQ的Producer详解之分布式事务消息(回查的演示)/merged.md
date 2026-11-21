# 20.RocketMQ的Producer详解之分布式事务消息（回查的演示）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\20.RocketMQ的Producer详解之分布式事务消息（回查的演示）【海量资源尽在 ubkz.com】.mp4
- 时长 1分37秒（音频 97s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 为了给大家演示完整性我们把回查这个逻辑给大家去演示一下因为可能会要稍微花一点点时间所以大家看一下这个效果就好了那么我是怎么玩的呢就是我是在我的实践中那么如果注意这个执行都是正常的情况下我返回的是一个不是commit是一个unknown这个状态返回这个状态
[00:26] 然后呢我在下面这个回查这个里面打印一句话就是一个状态的回查然后他的一个事务的ID然后以及他的一个状态的一个情况那么我我把它打印出来那么如果如果我返回的这个unknown然后呢服务端是不是就肯定会做一个回查的这个动作那么我们来看他有没有做一个执行的来看一下控制下这个输出啊那么当我的这个生产者发打印这两句话之后呢呃被其实这个还没有啊这个都等了等了一会儿才会去
[00:56] 看到这个消息的内容的然后在我的消费者这一端他并没有一个消息但是等到我打印一个状态回查的时候那么我这个消息这个是YD就他这个这样的改递然后我们做一个comment就拿到他的一个状态就是一个commit的状态然后你返回了这个commit的一个状态然后我这个消费者这一端就拿到了这个消息那么如果在这一端我拿到的是一个rollback这个状态的话那么他一定是不是也拿不到这个消息
[01:24] OK这就是关于这个回查的一个测试啊那么OK这个呢就让大家这个学习呢这个更加完整一点OK那么关于这个回查的一个演示呢我们就演示到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

