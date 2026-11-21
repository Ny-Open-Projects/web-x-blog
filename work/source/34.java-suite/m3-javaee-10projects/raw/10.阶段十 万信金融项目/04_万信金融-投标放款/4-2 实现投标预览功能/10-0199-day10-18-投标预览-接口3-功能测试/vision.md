# 画面线理解：day10-18-投标预览-接口3-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-18-投标预览-接口3-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:37, 00:42, 00:50, 01:02, 01:14, 01:25, 01:31, 01:52, 02:31, 02:35, 02:40, 03:01, 03:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:28:14

1) 这一组画面整体在讲什么（一句话）：
演示一个用户服务模块的代码实现、API 接口测试以及其在 P2P 平台业务流程中的角色。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示了 IntelliJ IDEA 中的项目结构，左侧是 `wanning2p` 项目下的 `wanning2p-consumer-service` 模块。
- 右侧是 `ConsumerService` 类的代码，包含 `BeanUtils.copyProperties` 方法调用和 `getById` 方法。
- 代码片段：
  ```java
  BeanUtils.copyProperties(consumerDTO, borrowerDTO);
  Map<String, String> cardInfo = IDCardUtil.getlInfo(borrowerDTO.getlDNumber());
  borrowerDTO.setAge(new Integer(cardInfo.get("age")));
  borrowerDTO.setBirthday(cardInfo.get("birthday"));
  borrowerDTO.setGender(cardInfo.get("gender"));
  return borrowerDTO;
  private ConsumerDTO getById(Long id) {
      Consumer entity = getBvById(id);
      if (entity == null) {
          log.info("id为[{}]的用户信息不存在", id);
          throw new BusinessException(ConsumerErrorCode.E_140101);
      }
      return convertConsumerEntityToDTO(entity);
  }
  ```

画面 2：
- 显示了 IntelliJ IDEA 中的项目结构，聚焦在 `wanning2p-consumer-service` 模块。
- 底部控制台显示了日志信息，包含 `NettyCleanSelector` 和 `SH4loggerFactory` 的信息。

画面 3：
- 与画面 2 类似，显示了 IntelliJ IDEA 的项目结构和控制台日志。

画面 4：
- 与画面 2、3 类似，显示了 IntelliJ IDEA 的项目结构和控制台日志。

画面 5：
- 显示了 Swagger UI 页面，标题为“万信金融P2P平台-用户服务API文档”。
- 页面显示了 API 列表，包括 `/consumers`、`/hello`、`/h1`、`/balances/{userNo}`、`/currConsumer/{mobile}` 等。

画面 6：
- 显示了 Swagger UI 页面，聚焦在 `/consumers` 接口。

画面 7：
- 显示了 Swagger UI 页面，聚焦在 GET `/my/borrowers/{id}` 接口，参数为 `id`，类型为 `Integer (64)`。

画面 8：
- 显示了 DBeaver 数据库客户端，连接到 `p2p_transaction` 数据库。
- 查询结果表 `t_user` 中显示了用户数据，包括 `CONSUMER_ID`、`USER_NO`、`PROJECT_ID` 等字段。

画面 9：
- 显示了 DBeaver 数据库客户端，连接到 `p2p_transaction` 数据库。
- 查询结果表 `project` 中显示了项目数据。

画面 10：
- 与画面 7 类似，显示了 Swagger UI 页面，聚焦在 GET `/my/borrowers/{id}` 接口。

画面 11：
- 显示了 Windows 桌面，多个窗口同时打开，包括 DBeaver、Swagger UI、WPS 文档、IntelliJ IDEA 等。
- 窗口标题显示了“万信金融-用户服务API文档”、“ApolloPortal”、“adminService”、“configService”等。

画面 12：
- 显示了 Swagger UI 页面，聚焦在 GET `/my/borrowers/{id}` 接口。
- 在参数输入框中输入了 `27`。
- 在响应区域显示了对应的 curl 命令和请求 URL。

画面 13：
- 显示了一个 P2P 平台的借款页面截图。
- 页面显示了借款信息，包括年利率 10%、期限 12 个月、总额 29,100 元。
- 页面底部有一个“授权出借”按钮。

画面 14：
- 显示了一个业务流程图。
- 流程图从左到右依次为：`浏览器/APP` → `交易中心` → `用户服务` → `存管通道服务` → `存管系统`。
- 流程图中的步骤包括：获取借款人信息、保存借款人信息、通过银行生成签名、保存交易信息、创建投标信息、更新交易状态等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上述要点中完整抄录）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- PPT 标题：无明确标题，但画面 13 和 14 显示了 P2P 平台的借款页面和业务流程图。
- 架构图/流程图结构：
  - 画面 14 的流程图：
    - `浏览器/APP` → `交易中心`（步骤 1.1-1.4）
    - `交易中心` → `用户服务`（步骤 1.5-1.6）
    - `用户服务` → `存管通道服务`（步骤 2.1-2.2）
    - `存管通道服务` → `存管系统`（步骤 2.5-2.6）
    - `存管系统` → `存管通道服务`（步骤 2.7-2.8）
    - `存管通道服务` → `用户服务`（步骤 2.9-2.10）
- 表格数据：
  - 画面 8：`t_user` 表数据，包含 `CONSUMER_ID`、`USER_NO`、`PROJECT_ID` 等字段。
  - 画面 9：`project` 表数据，包含 `PROJECT_ID`、`PROJECT_NAME`、`PROJECT_STATUS` 等字段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
