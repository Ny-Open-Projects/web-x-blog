# 画面线理解：16.Hyperledger fabric入门之术语回顾

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day20-了解区块链以及Hyperledger fabric
- 源文件：03.阶段三 好客租房(生活服务)项目\day20-了解区块链以及Hyperledger fabric\16.Hyperledger fabric入门之术语回顾【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:43, 01:12, 01:42, 01:43, 02:11, 02:12, 02:15, 02:17, 02:18, 02:36, 02:41, 02:42, 02:43, 03:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:56:46

1) 这一组画面整体在讲什么（一句话）：
讲解 Hyperledger Fabric 的核心概念，包括 channel、chaincode、ledger、network、ordering service、world state 和 MSP 等组件及其作用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Typora 编辑器中的 Markdown 文档，标题为“2.7、术语回顾”。
- 内容包括：channel（数据通道，可理解成独立的 Hyperledger Fabric 实例，不同 channel 数据完全隔离，可保证区块链上的数据隐私问题，类似微信群聊）、chaincode（链码，智能合约，chaincode 定义了 business logic，Ledger 的变化只能通过调用 chaincode 来完成）、ledger（账本，记录当前世界状态（world state），链式记录所有历史世界状态，在 Hyperledger 中是具有授权管理的共享账本系统，从底层设计上保证数据一致性、有效性、不可篡改性）、network（由 peer 组成的 network）、ordering service（排序服务）、world state（当前 ledger 中存放的数据，key 和 value 以 version 的形式存在，当前实现有 couchdb 和 leveldb）、MSP（Membership Service Provider，管理 peer 的身份和访问许可，具有相同 MSP 的 peer 才能通信）。

画面 2：
- 画面内容与画面 1 基本一致，光标位置在“在 Hyperledger 中，ledger 是一个具有授权管理的共享账本系统”这一行。

画面 3：
- 画面内容与画面 1 基本一致，光标位置在“在 Hyperledger 中，ledger 是一个具有授权管理的共享账本系统”这一行。

画面 4：
- 画面内容与画面 1 基本一致，光标位置在“在 Hyperledger 中，ledger 是一个具有授权管理的共享账本系统”这一行。

画面 5：
- 画面内容与画面 1 基本一致，光标位置在“在 Hyperledger 中，ledger 是一个具有授权管理的共享账本系统”这一行。

画面 6：
- 展示了架构图，图中包含“orderer”和“verify”两个模块。
- 文本内容包括：SDK 是为客户端提供操作的 API，和实现语言无关；peer（peer0、peer1、peer2 在同一个 channel 中，多个 peer 必须有相同的 MSP 才能进行通信）；提书（客户端通过 SDK 发起提案，如需要修改某一条数据，各个 peer 接收到提案后，进行模拟执行，会产生读写集，内部采用 version 的机制来记录修改后的状态）；背书（各个 peer 将模拟执行后的结果以及签名，发送给 SDK）；更新申请（SDK 收集到一定数量的背书后，将发送正式的更新申请给 orderer）；orderer（对请求的内容以及签名做校验，如果校验完成，没有问题的话，就会发送真正的更新通知给各个 peer，各个 peer 才真正的执行更新，如果请求不合法，也会保存到 block chain，方便后续的审查）。

画面 7：
- 画面内容与画面 6 基本一致，光标位置在“各个 peer 接收到提案后，进行模拟执行，会产生读写集，内部采用 version 的机制来记录修改后的状态”这一行。

画面 8：
- 画面内容与画面 1 基本一致，光标位置在“world state”标题下。

画面 9：
- 画面内容与画面 1 基本一致，光标位置在“3、项目中的应用”标题下。

画面 10：
- 画面内容与画面 1 基本一致，光标位置在“ordering service”下的“排序，验证 transaction，最终提交 invocation，把数据写入 peer 的 ledger”这一行。

画面 11：
- 画面内容与画面 6 基本一致，光标位置在“orderer”下的“对请求的内容以及签名做校验”这一行。

画面 12：
- 画面内容与画面 1 基本一致，光标位置在“channel”下的“数据通道，可以理解成独立的 Hyperledger fabric 的实例”这一行。

画面 13：
- 画面内容与画面 1 基本一致，光标位置在“ordering service”下的“排序，验证 transaction，最终提交 invocation，把数据写入 peer 的 ledger”这一行。

画面 14：
- 画面内容与画面 1 基本一致，光标位置在“MSP”下的“管理 peer 的身份和访问许可”这一行。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
架构图（画面 6 和 画面 11）：
- 一个箭头从上方指向“orderer”模块。
- “orderer”模块下方有一个“verify”模块。
- “orderer”模块内部包含“verify”功能。

表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
