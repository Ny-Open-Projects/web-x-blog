# 画面线理解：day11-2-用户投标-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-2-用户投标-功能实现1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 02:18, 03:00, 07:21, 08:12, 09:04, 10:27, 13:15, 14:38, 15:43, 16:38, 17:10, 17:50, 18:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:30:45

1) 这一组画面整体在讲如何在微服务架构中实现投标功能，包括定义数据模型、编写服务接口与实现、调用存管系统查询用户余额，以及通过 Apollo 配置中心管理相关配置。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了“用户投标业务流程图”，图中包含“浏览器APP”、“交易中心”、“用户服务”、“存管代理服务”、“存管系统”五个模块，通过编号步骤描述了从用户发起投标到存管系统更新账户余额的完整流程。
画面 2: 展示了 IDE 中的 `TenderDTO.java` 文件，定义了投标数据传输对象，包含 `id` 字段和注解 `@JsonSerialize(using = ToStringSerializer.class)`。
画面 3: 展示了 PPT 文档，标题为“2.3.2.1 功能实现”，内容包括在 `ProjectService` 接口中新增 `createTender` 方法，以及在 `ProjectServiceImpl` 中实现该方法的两个前置条件：A. 检查 Apollo 上是否配置最小投标金额（`mini.investment.amount 100.0`）；B. 实现查询账户余额功能，需在 `ConsumerAPI` 接口中新增查询当前余额的方法。
画面 4: 展示了 `ProjectServiceImpl.java` 文件中 `createTender` 方法的实现，其中包含一个私有方法 `getProjectRemainingAmount`，用于计算项目剩余金额。
画面 5: 展示了 `BalanceDetailsDTO.java` 文件，定义了用户余额信息的数据传输对象，包含 `consumerId`、`userNo`、`changeType`、`freezeAmount`、`balance`、`applyTime` 等字段。
画面 6: 展示了 `ConsumerController.java` 文件，其中包含 `getBorrower` 和 `getBalance` 方法的定义，以及一个测试方法 `testResources`。
画面 7: 展示了 `ConsumerController.java` 文件中 `getBalance` 方法的实现，方法签名是 `getBalance(String userNo)`。
画面 8: 展示了 `ConsumerController.java` 文件中 `getBalanceFromDepository` 方法的实现，使用 `OkHttpClient` 发起 HTTP 请求获取用户余额。
画面 9: 展示了 `ConsumerController.java` 文件中 `getBalanceFromDepository` 方法的实现，使用 `RestTemplate` 发起 HTTP 请求获取用户余额。
画面 10: 展示了 `ConsumerController.java` 文件中 `getBalanceFromDepository` 方法的实现，使用 `RestTemplate` 发起 HTTP 请求获取用户余额。
画面 11: 展示了 Apollo 配置中心的界面，显示了 `consumer-service` 项目下的多个配置项，包括 `swagger.enable`、`spring.mvc.throw-exception-if-no-handler-found`、`micro_service.spring-boot-http`、`micro_service.spring-eureka`、`micro_service.spring-hystrix`、`micro_service.spring-ribbon` 等。
画面 12: 展示了 Apollo 配置中心的界面，显示了 `consumer-service` 项目下的多个配置项，包括 `swagger.enable`、`spring.mvc.throw-exception-if-no-handler-found`、`micro_service.spring-boot-http`、`micro_service.spring-eureka`、`micro_service.spring-hystrix`、`micro_service.spring-ribbon` 等。
画面 13: 展示了 `ConsumerController.java` 文件中 `hello` 方法的实现，使用 `@Autowired` 注入 `ConsumerService`，并定义了一个测试接口 `@GetMapping("/hello")`。
画面 14: 展示了 PPT 文档，内容为“2.1 前置条件判断准备工作（投标金额是否大于最小投标金额、账户余额是否足够）”，并列出 A、B、C 三个子项，其中 C 项是“在 ConsumerController 类中实现该方法”，并显示了 `getBalance` 方法的注解和签名。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 2:
```java
package cn.ictast.waningzp.api.transaction.model;

import ...

/**
 * 投标信息
 */
public class TenderDTO {
    @JsonSerialize(using = ToStringSerializer.class)
    private Long id;
    // 按标用户标识
}
```

画面 3:
```text
1.在ProjectService接口中新增createTender方法：
/**
 * 用户投标
 * @param projectInvestDTO
 * @return
 */
TenderDTO createTender(ProjectInvestDTO projectInvestDTO);

2.在ProjectServiceImpl类中实现该方法，由于业务非常复杂，我们拆分成若干部分逐一实现
2.1 前置条件判断准备工作（投标金额是否大于最小投标金额、账户余额是否足够）
A：检查Apollo上是否配置最小投标金额
    mini.investment.amount 100.0
B：实现查询账户余额功能，在ConsumerAPI接口中新增查询当前余额的方法：
    /**
     * 获取当前登录用户余额信息
     * @param userNo 用户编码
     * @return
     */
    RestResponse<BalanceDetailsDTO> getBalance(String userNo);
```

画面 4:
```java
@Override
public TenderDTO createTender(ProjectInvestDTO projectInvestDTO) {

}

/**
 * 获取标的剩余可投标额度
 * @param project
 * @return
 */
private BigDecimal getProjectRemainingAmount(Project project) {
    List<BigDecimal> decimalList = tenderMapper.selectAmountInvested(project.getId());
    BigDecimal amountInvested = new BigDecimal("0.0");
    for (BigDecimal d : decimalList) {
        amountInvested = amountInvested.add(d);
    }
    return amountInvested;
}
```

画面 5:
```java
public class BalanceDetailsDTO implements Serializable {
    private static final long serialVersionUID = 1L;
    @ApiModelProperty(value = "用户标识")
    private Long consumerId;
    @ApiModelProperty(value = "用户编码，生成唯一，用户在存管系统标识")
    private String userNo;
    @ApiModelProperty(value = "账户变动类型 1.增加、2.减少、3.冻结、4.解冻")
    private Integer changeType;
    @ApiModelProperty(value = "冻结金额")
    private BigDecimal freezeAmount;
    @ApiModelProperty(value = "可用余额")
    private BigDecimal balance;
    @ApiModelProperty(value = "应用编码")
    private String applyCode;
}
```

画面 6:
```java
@ApiOperation("获取借款人用户信息")
@ApiImplicitParam(name = "id", value = "用户标识", required = true, dataType = "Long", paramType = "path")
@GetMapping("/my/borrowers/{id}")
public RestResponse<BorrowerDTO> getBorrower(@PathVariable Long id) {
    return RestResponse.success(consumerService.getBorrower(id));
}

@Override
@ApiOperation("获取用户可用余额")
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
@GetMapping("/1/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(String userNo) {
    return null;
}

@ApiOperation("过网关保护资源，进行认证拦截测试")
@ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "String")
@GetMapping(value = "/m/consumers/test")
public RestResponse<String> testResources(String jsonToken) {
    return RestResponse.success(EncryptUtil.decodeUTF8StringBase64(jsonToken));
}
```

画面 7:
```java
@ApiOperation("获取用户可用余额")
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
@GetMapping("/1/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(String userNo) {
    return null;
}
```

画面 8:
```java
private RestResponse<BalanceDetailsDTO> getBalanceFromDepository(String userNo) {
    String url = depositorURL + "/balance-details/" + userNo;
    BalanceDetailsDTO balanceDetailsDTO = new BalanceDetailsDTO();
    Request request = new Request.Builder().url(url).build();
    try (Response response = okHttpClient.newCall(request).execute()) {
        if (response.isSuccessful()) {
            String responseBody = response.body().string();
            balanceDetailsDTO = JSON.parseObject(responseBody, BalanceDetailsDTO.class);
            return RestResponse.success(balanceDetailsDTO);
        }
    } catch (IOException e) {
        log.warn("调用存管系统获取余额失败", url, e);
        return RestResponse.fail("获取失败");
    }
    return RestResponse.fail("获取失败");
}
```

画面 9:
```java
private RestResponse<BalanceDetailsDTO> getBalanceFromDepository(String userNo) {
    String url = depositorURL + "/balance-details/" + userNo;
    BalanceDetailsDTO balanceDetailsDTO = new BalanceDetailsDTO();
    Request request = new Request.Builder().url(url).build();
    try (Response response = restTemplate.getForEntity(url, BalanceDetailsDTO.class).getBody()) {
        if (response != null) {
            String responseBody = response.getBody().toString();
            balanceDetailsDTO = JSON.parseObject(responseBody, BalanceDetailsDTO.class);
            return RestResponse.success(balanceDetailsDTO);
        }
    } catch (IOException e) {
        log.warn("调用存管系统获取余额失败", url, e);
