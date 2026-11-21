# day11-17-满标放款-定义接口3

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-4 满标放款需求分析和接口定义
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-4 满标放款需求分析和接口定义\day11-17-满标放款-定义接口3_【海量资源尽在 666java.com】.mp4
- 时长 3分41秒（音频 221s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接口二定义好之后咱接下来就该接口三了在接口三这个地方大家一定要注意其实这个时候已经实现了什么放款就接口二这块其实已经把放款给实现了你看这边银行那边是不是都已经花不自禁了对不对所以说到接口三的时候其实是放款这个核心的业务已经执行完了接口三接下来要干啥事王冼然说了一旦放款其实立即又进入了什么还款阶段是不是
[00:28] 所以说呢借口三呢主要就是来更改这个什么呀数据的状态啊给它改成什么呀对还款中啊所以你看又是交易中心对发起请求到哪从下代理服务啊这边还是生成签名保存交易记录啊然后修改标底的这个状态为什么还款中当然呢这个银行那边是不是也要同步做修改是不是然后这边还要更新交易记录数据状态为同步改成以同步等等等等然后交易中心这边收到结果之后是不是要把
[00:57] 这个标题状态也要改成什么还款中啊所以说这是接口三吧它主要实现的这个功能图当中呢也展示的非常清晰那接下来的话把这个接口三来定义一下那这个是不是还是这个存款代理服务这一块是不是啊存款代理服务那咱看看讲义吧那我们需要在存款代理服务这个接口当中再新增一个方法叫modifyprojectstatus修改标题的状态啊修改成什么呀还款中
[01:24] 那咱再新增这么一个方法过来还是这个谁啊不是他了啊是这个depositoryargent API这个接口再新增这么一个方法呃这里边呢我们需要一个modify project的stator DTO这么一个类啊我们找一下给他考过来是他吧我们看看他应该是考到API对吧API Translation里面API的Translation
[01:58] 这里边转过来转过来之后这边应该会自动倒包那接下来看看这个主要是看参数啊说呢修改标底的状态那这里边自然是比较封装跟状态相关的一些数据对吧具体都封装了啥呢咱是不是就去里边熟悉一下就行那这里边有请求留任号标底号还有这个什么呀更新标底的状态我们应该给的值就是那个什么呀缓缓中对不对这下边是一个这个什么呀一个测试代码
[02:29] 那至于这些东西的话咱就是具体用到时候再说这咱大概先熟一下这是我们又新增了一个方法啊修改这个标题状态那这个方法定义好之后呢我们既然还是回到这个Controller里边把这个方法呢给它生成一下在这对吧然后呢我们测好讲义把一些注解呢给它补充完善一下还是Swagger MVC啊这些注解然后呢这个地方是不是还有一个request body
[03:11] 好咱看一下吧这个地方啊大家需要注意的是不是还是L开头的那看图因为接口三这一块是不是还是微服之间的一个一个呃请求对不对是还是交易中心去远程请求谁啊从来代理服务所以说呢这个是给微服务后端进行调用所以说这是L开头然后呢参数这一块你要注意加上request body这个注解就行其他的我们就不再过多说了吧这是第几个接口啊对第三个接口这一块我们也就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在万向金融项目中，通过定义和实现 `ModifyProjectStatusDTO` 数据传输对象，并在 `DepositoryAgentController` 中对接口 `modifyProjectStatus` 进行实现，同时展示其在业务逻辑中的调用和签名处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了IDE中 `DepositoryAgentApi.java` 文件的内容，其中定义了 `modifyProjectStatus` 接口。
- 代码内容：
  ```java
  /**
   * 修改标的的状态
   * @param modifyProjectStatusDTO
   * @return
   */
  RestResponse<String> modifyProjectStatus(ModifyProjectStatusDTO modifyProjectStatusDTO);
  ```
- 同时展示了 `DepositoryAgentController.java` 文件中对 `modifyProjectStatus` 方法的实现，代码为：
  ```java
  @Override
  @ApiOperation(value = "修改标的的状态", value = "修改标的的状态DTO",
      required = true, dataType = "ModifyProjectStatusDTO",
      paramType = "body")
  @PostMapping("/modify-project-status")
  public RestResponse<String> modifyProjectStatus(
      @RequestBody ModifyProjectStatusDTO modifyProjectStatusDTO) {
      return null;
  }
  ```

画面2：
- 展示了IDE中 `DepositoryAgentApi.java` 文件的内容，其中定义了 `createTender` 接口。
- 代码内容：
  ```java
  /**
   * 用户投标
   * @param projectInvestDTO
   * @return
   */
  RestResponse(TenderDTO) createTender(ProjectInvestDTO projectInvestDTO);
  ```
- 同时展示了 `DepositoryAgentApi.java` 文件中定义的 `loanApprovalStatus` 方法。
- 代码内容：
  ```java
  /**
   * 审核标的的满标放款
   * @param id 标的id
   * @param approveStatus 审核状态
   * @param commission 平台佣金
   * @return
   */
  RestResponse(String) loanApprovalStatus(Long id, String approveStatus, String commission);
  ```

画面3：
- 展示了IDE中 `DepositoryAgentApi.java` 文件的内容，其中定义了 `confirmLoan` 接口。
- 代码内容：
  ```java
  /**
   * 审核标的的满标放款
   * @param loanRequest
   * @return
   */
  RestResponse(String) confirmLoan(LoanRequest loanRequest),
  ```
- 同时展示了 `DepositoryAgentApi.java` 文件中定义的 `modifyProjectStatus` 方法。
- 代码内容：
  ```java
  /**
   * 修改标的的状态
   * @param modifyProjectStatusDTO
   * @return
   */
  RestResponse(String) modifyProjectStatus(ModifyProjectStatusDTO modifyProjectStatusDTO);
  ```

画面4：
- 展示了文件资源管理器中 `ModifyProjectStatusDTO.java` 文件的属性信息。
- 文件信息：
  - 文件名：ModifyProjectStatusDTO.java
  - 修改日期：2019/9/2 9:27
  - 大小：2.23 KB
  - 全部日期：2019/9/28 10:14

画面5：
- 展示了IDE中 `DepositoryAgentApi.java` 文件的内容，其中定义了 `modifyProjectStatus` 接口。
- 代码内容：
  ```java
  /**
   * 修改标的的状态
   * @param modifyProjectStatusDTO
   * @return
   */
  RestResponse(String) modifyProjectStatus(ModifyProjectStatusDTO modifyProjectStatusDTO);
  ```

画面6：
- 展示了IDE中 `ModifyProjectStatusDTO.java` 文件的内容，其中定义了 `ModifyProjectStatusDTO` 类。
- 代码内容：
  ```java
  @Data
  public class ModifyProjectStatusDTO {
      /**
       * 请求流水号
       */
      private String requestNo;
      /**
       * 标的号
       */
      private String projectNo;
      /**
       * 更标的的状态
       */
      private String projectStatus;
      /**
       * 业务实体id
       */
      private Long id;
      public static void main(String[] args) throws UnsupportedEncodingException {
  }
  ```

画面7：
- 展示了IDE中 `ModifyProjectStatusDTO.java` 文件的内容，其中定义了 `ModifyProjectStatusDTO` 类。
- 代码内容：
  ```java
  @Data
  public class ModifyProjectStatusDTO {
      /**
       * 请求流水号
       */
      private String requestNo;
      /**
       * 标的号
       */
      private String projectNo;
      /**
       * 更标的的状态
       */
      private String projectStatus;
      /**
       * 业务实体id
       */
      private Long id;
      public static void main(String[] args) throws UnsupportedEncodingException {
  }
  ```

画面8：
- 展示了IDE中 `ModifyProjectStatusDTO.java` 文件的内容，其中定义了 `ModifyProjectStatusDTO` 类。
- 代码内容：
  ```java
  @Data
  public class ModifyProjectStatusDTO {
      /**
       * 请求流水号
       */
      private String requestNo;
      /**
       * 标的号
       */
      private String projectNo;
      /**
       * 更标的的状态
       */
      private String projectStatus;
      /**
       * 业务实体id
       */
      private Long id;
      public static void main(String[] args) throws UnsupportedEncodingException {
  }
  ```

画面9：
- 展示了IDE中 `DepositoryAgentApi.java` 文件的内容，其中定义了 `modifyProjectStatus` 接口。
- 代码内容：
  ```java
  /**
   * 修改标的的状态
   * @param modifyProjectStatusDTO
   * @return
   */
  RestResponse(String) modifyProjectStatus(ModifyProjectStatusDTO modifyProjectStatusDTO);
  ```

画面10：
- 展示了IDE中 `DepositoryAgentController.java` 文件的内容，其中定义了 `confirmLoan` 接口。
- 代码内容：
  ```java
  @ApiOperation(value = "审核标的的满标放款", value = "标的的满标放款信息", required = true, dataType = "LoanRequest", paramType = "body")
  @PostMapping("/confirm-loan")
  public RestResponse<String> confirmLoan(@RequestBody LoanRequest loanRequest) {
      return null;
  }
  ```
- 同时展示了 `DepositoryAgentController.java` 文件中定义的 `getRestResponse` 方法。
- 代码内容：
  ```java
  private RestResponse<String> getRestResponse(DepositoryBaseResponse depositoryResponse) {
      final RestResponse<String> restResponse = new RestResponse<>();
      return restResponse;
  }
  ```

画面11：
- 展示了PPT页面，标题为“3.2.1.4 还款服务启动还款接口（接口④）”。
- 内容：
  1. 接口描述
  1) 接受交易中心的还款信息

画面12：
- 展示了PPT页面，标题为“3.2.1.4 还款服务启动还款接口（接口④）”。
- 内容：
  1. 接口描述
  1) 接受交易中心的还款信息

画面13：
- 展示了多个窗口的截图，包括：
  - 一个名为“流程图”的PPT页面，包含“交易中心”、“存管系统”、“清算系统”、“清算中心”等节点。
  - 一个名为“万向金融-还款服务v1.0.pdf”的PDF文件。
  - 一个名为“55log Professional 64 - localhost:8080”的日志窗口。
  - 一个名为“流程图”的PPT页面，包含“交易中心”、“存管系统”、“清算系统”、“清算中心”等节点。

画面14：
- 展示了“流程图”PPT页面，包含“交易中心”、“存管系统”、“清算系统”、“清算中心”等节点。
- 流程图内容：
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  - 交易中心 -> 存管系统 -> 清算系统 -> 清算中心
  -

