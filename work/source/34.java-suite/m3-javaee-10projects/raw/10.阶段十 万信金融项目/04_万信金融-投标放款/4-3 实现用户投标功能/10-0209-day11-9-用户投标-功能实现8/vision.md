# 画面线理解：day11-9-用户投标-功能实现8

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-9-用户投标-功能实现8_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 02:05, 03:33, 05:24, 06:48, 08:23, 10:25, 12:18, 14:08, 15:50, 17:19, 18:28, 19:16, 20:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:36:24

1) 这一组画面整体在讲什么（一句话）：
演示一个投标项目中，前端发起投标请求后，后端服务如何进行金额校验、用户身份校验、项目状态校验，并最终在数据库中创建投标记录的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 `ProjectServiceImpl.java` 中的 `createTender` 方法，包含三个校验步骤：
  1. 判断投标金额是否大于最小投标金额：
     ```java
     BigDecimal amount = new BigDecimal(projectInvestDTO.getAmount());
     BigDecimal miniInvestmentAmount = configService.getMiniInvestmentAmount();
     if (amount.compareTo(miniInvestmentAmount) < 0) {
         throw new BusinessException(TransactionErrorCode.E_150109);
     }
     ```
  2. 判断用户账户余额是否足够：
     ```java
     LoginUser user = SecurityUtil.getUser();
     RestResponse<ConsumerDTO> restResponse = consumerApiAgent.getOurConsumer(user.getMobile());
     RestResponse<BalanceDetailDTO> balanceDetailRestResponse = consumerApiAgent.getBalance(restResponse.getResult().getUserId());
     if (amount.compareTo(balanceDetailRestResponse.getResult().getBalance()) > 0) {
         throw new BusinessException(TransactionErrorCode.E_150112);
     }
     ```
  3. 判断标的状态是否为“招标中”：
     ```java
     Project project = getProjectById(projectInvestDTO.getProjectId());
     if (project.getProjectStatus().equalsIgnoreCase(ProjectCode.FULL.getCode())) {
         throw new BusinessException(TransactionErrorCode.E_150114);
     }
     ```

画面2：
- 展示了 `TransactionController.java` 中的两个接口：
  1. 查询项目下的投标信息：
     ```java
     @Override
     @GetMapping("/tenders/projects/{id}")
     public RestResponse<List<TenderOverviewDTO>> queryTendersByProjectId(@PathVariable Long id) {
         return RestResponse.success(projectService.queryTendersByProjectId(id));
     }
     ```
  2. 创建投标：
     ```java
     @PostMapping("/my/tenders")
     public RestResponse<TenderDTO> createTender(@RequestBody ProjectInvestDTO projectInvestDTO) {
         TenderDTO tenderDTO = projectService.createTender(projectInvestDTO);
         return RestResponse.success(tenderDTO);
     }
     ```

画面3：
- 展示了一个流程图，描述了用户投标的完整流程，涉及“P2P平台”、“交易中心”、“商户服务”、“存管代理服务”和“存管系统”五个角色，通过箭头表示交互顺序。

画面4：
- 展示了 `ProjectServiceImpl.java` 中的 `createTender` 方法的后续部分，包括创建投标对象和返回结果。

画面5：
- 展示了 Postman 中的请求，用于获取用户登录的 access_token，请求地址为 `http://localhost:3301/user/auth/token`，返回的 JSON 数据包含 access_token、refresh_token、expires_in、code、msg 和 jti 字段。

画面6：
- 展示了 `TransactionController.java` 中的 `createTender` 方法，与画面2中的内容一致。

画面7：
- 屏幕空白，无有效信息。

画面8：
- 展示了 `ProjectServiceImpl.java` 中的 `createTender` 方法，其中 `if (amount.compareTo(miniInvestmentAmount) < 0)` 这一行被高亮，表示该条件判断。

画面9：
- 展示了 `ProjectServiceImpl.java` 中的 `createTender` 方法，其中 `if (amount.compareTo(miniInvestmentAmount) < 0)` 这一行被高亮，表示该条件判断。

画面10：
- 展示了 SQLyog 中的数据库表结构，表名为 `p2p_transaction_1`，包含 `project_0` 和 `tender_0` 等数据表。

画面11：
- 展示了 `ProjectServiceImpl.java` 中的 `createTender` 方法，其中 `if (amount.compareTo(remainingAmount) > 0)` 这一行被高亮，表示该条件判断。

画面12：
- 展示了 `TransactionErrorCode.java` 中的 `E_150110` 错误码定义：
  ```java
  E_150110("本次投标金额超出标的剩余未投资金额"),
  ```

画面13：
- 展示了 SQLyog 中的数据库表结构，表名为 `p2p_transaction_0`，包含 `tender_0` 数据表。

画面14：
- 展示了 `ProjectServiceImpl.java` 中的 `createTender` 方法，其中 `if (amount.compareTo(miniInvestmentAmount) < 0)` 这一行被高亮，表示该条件判断。
