# 画面线理解：day15-17-还款短信提醒-还款提醒功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-7 实现还款短信提醒功能
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-7 实现还款短信提醒功能\day15-17-还款短信提醒-还款提醒功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:23, 01:07, 01:52, 03:55, 04:41, 05:27, 06:41, 07:32, 08:04, 09:21, 10:34, 10:54, 11:38, 12:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:40:41

1) 这一组画面整体在讲如何在还款服务中通过调用用户服务获取借款人手机号，并发送还款提醒短信。

2) 按时间顺序列出每张画面的要点：
画面1:
- 在ConsumerAPI中新增一个方法，用于根据用户id获取用户信息。
- 代码：
  ```java
  /**
   * 获取借款人用户信息-供微服务调用
   * @param id 用户标识
   * @return
   */
  RestResponse<BorrowerDTO> getBorrowerMobile(Long id);
  ```
- 在ConsumerController类中实现该方法：
  ```java
  @Override
  @ApiImplicitParam(name = "id", value = "借款人id", required = true,
          dataType = "Long", paramType = "path")
  @GetMapping("/l/borrowers/{id}")
  public RestResponse<BorrowerDTO> getBorrowerMobile(@PathVariable Long id) {
      return RestResponse.success(consumerService.getBorrower(id));
  }
  ```
- 在还款微服务中创建Feign代理：
  ```java
  @FeignClient(value = "consumer-service")
  ```

画面2:
- 在RepaymentServiceImpl中，调用`depositoryAgentApiAgent.confirmRepayment`方法确认还款。
- 代码：
  ```java
  public void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
      RestResponse<String> repaymentResponse = depositoryAgentApiAgent.confirmRepayment(repaymentRequest);
      if (!repaymentResponse.get(Result).equals(DepositoryReturnCode.RETURN_CODE_00000.getCode())) {
          throw new RuntimeException("还款失败");
      }
  }
  ```

画面3:
- 在RepaymentService接口中定义方法：
  ```java
  /**
   * 查询借款人相关信息，并调用发送短信后接口进行还款提醒
   * @param date
   */
  void sendRepaymentNotify(String date);
  ```

画面4:
- 在RepaymentServiceImpl中，执行还款逻辑。
- 代码：
  ```java
  public void executesRepayment(String date, int shardingCount, int shardingItem) {
      // 查询到期的还款计划
      List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date, shardingCount, shardingItem);
      // 逐笔还款
      for (RepaymentPlan repaymentPlan : repaymentPlanList) {
          // 逐笔还款
          repaymentPlan.setRepaymentStatus(RepaymentStatus.SUCCESS);
          repaymentPlan.setRepaymentDate(LocalDateTime.now());
          repaymentPlan.setRepaymentCode(RepaymentCode.CODE_REQUEST_PREFIX + UUID.randomUUID().toString().replace("-", ""));
          repaymentPlan.setRepaymentDetailMapper.insert(repaymentPlan);
      }
  }
  ```

画面5:
- 在PlanMapper中定义查询到期还款计划的SQL。
- 代码：
  ```java
  @Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(should_repayment_date, '%Y-%m-%d') = #{date} AND repayment_status = '0'")
  List<RepaymentPlan> selectDueRepayment(String date);
  ```

画面6:
- 在RepaymentServiceImpl中，根据还款计划生成还款明细。
- 代码：
  ```java
  // 保存还款明细
  planList.forEach(plan -> {
      saveReceivablePlan(plan, tenderDTO.receipt());
  });
  ```

画面7:
- 在RepaymentServiceImpl中，调用`selectDueRepayment`方法查询到期还款计划。
- 代码：
  ```java
  List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date);
  ```

画面8:
- 在RepaymentServiceImpl中，保存还款明细。
- 代码：
  ```java
  public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {
      if (repaymentDetail == null) {
          repaymentDetail = new RepaymentDetail();
      }
      repaymentDetail.setRepaymentPlan(repaymentPlan);
      repaymentDetailMapper.insert(repaymentDetail);
      return repaymentDetail;
  }
  ```

画面9:
- 在RepaymentServiceImpl中，发送还款通知。
- 代码：
  ```java
  public void sendRepaymentNotify(String date) {
      List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date);
      repaymentPlanList.forEach(repaymentPlan -> {
          // 查询借款人信息
          RestResponse<BorrowerDTO> consumerResponse = consumerApiAgent.getBorrowerMobile(repaymentPlan.getConsumerId());
          // 得到借款人的手机号
          String mobile = consumerResponse.getResult().getMobile();
          // 发送还款短信
          smsService.sendRepaymentNotify(mobile, date, repaymentPlan.getAmount());
      });
  }
  ```

画面10:
- 在RepaymentServiceImpl中，调用`consumerApiAgent.getBorrowerMobile`方法获取借款人手机号。
- 代码：
  ```java
  RestResponse<BorrowerDTO> consumerResponse = consumerApiAgent.getBorrowerMobile(repaymentPlan.getConsumerId());
  ```

画面11:
- PPT标题：8.2.2 还款服务还款提醒接口。
- 内容：调用腾讯云发送短信。

画面12:
- 在RepaymentServiceImpl中，获取借款人手机号。
- 代码：
  ```java
  String mobile = consumerResponse.getResult().getMobile();
  ```

画面13:
- 在RepaymentServiceImpl中，调用`smsService.sendRepaymentNotify`方法发送短信。
- 代码：
  ```java
  smsService.sendRepaymentNotify(mobile, date, repaymentPlan.getAmount());
  ```

画面14:
- PPT标题：8.3.2 还款服务发送短信接口。
- 内容：创建`ICloudSmsServiceImpl`实现发送短信功能。
