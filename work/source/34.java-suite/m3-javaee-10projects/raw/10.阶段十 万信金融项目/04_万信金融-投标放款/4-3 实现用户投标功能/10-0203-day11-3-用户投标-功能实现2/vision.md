# 画面线理解：day11-3-用户投标-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-3-用户投标-功能实现2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:26, 01:43, 02:15, 02:28, 02:41, 02:44, 02:56, 03:27, 04:05, 04:11, 04:18, 04:39, 05:08, 05:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:31:38

1) 这一组画面整体在讲什么（一句话）：
在万向金融项目中，实现ConsumerAPI接口的“获取用户可用余额”功能，涉及在ConsumerController中定义方法、在ConsumerAgent中暴露远程调用接口、以及在ConsumerService中调用底层数据访问层。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了课程PPT内容，标题为“2.1 预案：用户中心接口改造”。
- 内容A：检查Apollo是否配置最小投资金额，显示配置项：min.investment.amount = 100.0。
- 内容B：实现查询用户余额功能，在ConsumerAPI接口中新增查询当前余额的方法，代码片段：
  ```java
  /**
   * 获取当前登录用户余额信息
   * @param userNo 用户编码
   * @return
   */
  RestResponse<BalanceDetailsDTO> getBalance(String userNo);
  ```
- 内容C：在ConsumerController类中实现该方法，代码片段：
  ```java
  @Override
  @ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
  @GetMapping("/balances/{userNo}")
  public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
  }
  ```

画面2：
- 展示了ConsumerAPI接口中新增的getBalance方法的实现代码，代码片段：
  ```java
  String url = depositoryURL + "/balance-details/" + userNo;
  BalanceDetailsDTO balanceDetailsDTO = new Request.Builder()
      .url(url)
      .build()
      .execute()
      .body().string();
  if (response.isSuccessful()) {
      balanceDetailsDTO = JSON.parseObject(response.body().string(), BalanceDetailsDTO.class);
      return RestResponse.success(balanceDetailsDTO);
  } else {
      log.warn("调用存管系统失败", url, e);
      return RestResponse.validFail("获取失败");
  }
  ```

画面3：
- 展示了IDEA中ConsumerAPI接口的代码，其中包含获取用户信息和获取用户余额的方法。

画面4：
- 展示了IDEA中ConsumerAPI接口的代码，其中包含获取用户信息和获取用户余额的方法，鼠标选中了获取用户余额的方法。

画面5：
- 展示了IDEA中项目结构，选中了ConsumerAPI接口。

画面6：
- 展示了ConsumerController类中定义的获取用户信息、获取借款人信息、获取用户可用余额的方法。

画面7：
- 展示了ConsumerController类中定义的获取用户可用余额的方法，代码片段：
  ```java
  @Override
  @ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
  @GetMapping("/balances/{userNo}")
  public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
      return getBalanceFromDepository(userNo);
  }
  ```

画面8：
- 展示了课程PPT内容，标题为“2.1 预案：用户中心接口改造”。
- 内容D：在ConsumerApiAgent接口中新增getBalance方法，供交易中心远程调用查询当前余额，代码片段：
  ```java
  @GetMapping("/consumer/1/balances/{userNo}")
  public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo)
  ```
- 内容E：考虑到前端也需要获取账户余额，所以在ConsumerAPI接口中新增供前端调用的查询当前余额的方法，代码片段：
  ```java
  /**
   * 获取当前登录用户余额信息
   * @param userNo 用户编码
   * @return
   */
  RestResponse<BalanceDetailsDTO> getBalance();
  ```
- 内容F：在ConsumerController类中实现该方法，代码片段：
  ```java
  /**
   * 获取当前登录用户余额信息
   * @param userNo 用户编码
   * @return
   */
  RestResponse<BalanceDetailsDTO> getBalance();
  ```

画面9：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  return RestResponse.success(consumerService.getBalanceFromDepository(userNo));
  ```

画面10：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  @Override
  @ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
  @GetMapping("/balances/{userNo}")
  public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
      return getBalanceFromDepository(userNo);
  }
  ```

画面11：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  public RestResponse<BalanceDetailsDTO> getBalance() {
      return getBalanceFromDepository(consumerDTO.getUserNo());
  }
  ```

画面12：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  public RestResponse<BalanceDetailsDTO> getBalance() {
      return getBalanceFromDepository(consumerDTO.getUserNo());
  }
  ```

画面13：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  public RestResponse<BalanceDetailsDTO> getBalance() {
      return getBalanceFromDepository(consumerDTO.getUserNo());
  }
  ```

画面14：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  public RestResponse<BalanceDetailsDTO> getBalance() {
      return getBalanceFromDepository(consumerDTO.getUserNo());
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 获取当前登录用户余额信息
 * @param userNo 用户编码
 * @return
 */
RestResponse<BalanceDetailsDTO> getBalance(String userNo);
```

画面2：
```java
String url = depositoryURL + "/balance-details/" + userNo;
BalanceDetailsDTO balanceDetailsDTO = new Request.Builder()
    .url(url)
    .build()
    .execute()
    .body().string();
if (response.isSuccessful()) {
    balanceDetailsDTO = JSON.parseObject(response.body().string(), BalanceDetailsDTO.class);
    return RestResponse.success(balanceDetailsDTO);
} else {
    log.warn("调用存管系统失败", url, e);
    return RestResponse.validFail("获取失败");
}
```

画面6：
```java
@Override
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
@GetMapping("/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
    return getBalanceFromDepository(userNo);
}
```

画面8：
```java
/**
 * 获取当前登录用户余额信息
 * @param userNo 用户编码
 * @return
 */
RestResponse<BalanceDetailsDTO> getBalance();
```

画面9：
```java
return RestResponse.success(consumerService.getBalanceFromDepository(userNo));
```

画面10：
```java
@Override
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
@GetMapping("/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
    return getBalanceFromDepository(userNo);
}
```

画面11：
```java
public RestResponse<BalanceDetailsDTO> getBalance() {
    return getBalanceFromDepository(consumerDTO.getUserNo());
}
```

画面12：
```java
public RestResponse<BalanceDetailsDTO> getBalance() {
    return getBalanceFromDepository(consumerDTO.getUserNo());
}
```

画面13：
```java
public RestResponse<BalanceDetailsDTO> getBalance() {
    return getBalanceFromDepository(consumerDTO.getUserNo());
}
```

画面14：
```java
public RestResponse<BalanceDetailsDTO> getBalance() {
    return getBalanceFromDepository(consumerDTO.getUserNo());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
- PPT标题：2.1 预案：用户中心接口改造
- 内容A：检查Apollo是否配置最小投资金额，显示配置项：min.investment.amount = 100.0。
- 内容B：实现查询用户余额功能，在ConsumerAPI接口中新增查询当前余额的方法。
- 内容C：在ConsumerController类中实现该方法。

画面8：
- PPT标题：2.1 预案：用户中心接口改造
- 内容D：在ConsumerApiAgent接口中新增getBalance方法，供交易中心远程调用查询当前余额。
- 内容E：考虑到前端也需要获取账户余额，所以在ConsumerAPI接口中新增供前端调用的查询当前余额的方法。
- 内容F：在ConsumerController类中实现该方法。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
