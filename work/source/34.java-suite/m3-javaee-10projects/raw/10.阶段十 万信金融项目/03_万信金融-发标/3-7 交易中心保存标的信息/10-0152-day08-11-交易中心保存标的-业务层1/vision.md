# 画面线理解：day08-11-交易中心保存标的-业务层1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-11-交易中心保存标的-业务层1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:30, 01:30, 02:26, 02:58, 03:58, 05:21, 06:18, 07:56, 08:50, 10:24, 11:14, 11:56, 12:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:50:23

1) 这一组画面整体在讲什么（一句话）：
演示如何在交易系统中创建项目服务接口、实现类，并关联用户中心的消费者注册功能，涉及 MyBatis 映射文件、Service 层接口与实现、实体类及 Controller 层的 API 接口定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了在 MyBatis 的 Mapper 文件中定义了 ProjectMapper.xml 的结构。
- 代码内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="cn.itcast.wanxingzp.transaction.mapper.ProjectMapper">
  </mapper>
  ```

画面 2：
- 展示了在 Service 包中新建的 ProjectService 接口，定义了 createProject 方法。
- 代码内容：
  ```java
  /**
   * 交易中心service接口
   */
  public interface ProjectService {
      /**
       * 创建标的
       * @param project
       * @return ProjectDTO
       */
      ProjectDTO createProject(ProjectDTO project);
  }
  ```

画面 3：
- 展示了在 IDEA 中打开的 ProjectServiceImpl.java 文件，准备编写实现类。
- 项目结构显示了 service 包下的 ProjectService 接口和 ProjectServiceImpl 类。

画面 4：
- 展示了在 ProjectDTO 类中设置用户 ID、生成项目编号、设置状态等业务逻辑。
- 代码内容：
  ```java
  projectDTO.setUserId(consumer.getResultSet().getUserId());
  projectDTO.setProjectNo(CodeUtil.getNo(CodePrefixCode.CODE_PROJECT_PREFIX));
  projectDTO.setProjectStatus(ProjectCode.COLLECTING.getCode());
  projectDTO.setStatus(StatusCode.STATUS_OUT.getCode());
  projectDTO.setCreateDate(LocalDateTime.now());
  projectDTO.setRepaymentWay(RepaymentWay.FIXED_REPAYMENT.getCode());
  ```

画面 5：
- 展示了 Project 实体类中定义了 ID、CONSUMER_ID、USER_NO、PROJECT_NO 等字段。
- 代码内容：
  ```java
  @TableId("ID")
  private Long id;
  @TableField("CONSUMER_ID")
  private Long consumerId;
  @TableField("USER_NO")
  private String userNo;
  @TableField("PROJECT_NO")
  private String projectNo;
  ```

画面 6：
- 展示了 Project 实体类中定义了 USER_NO 字段的注解和类型。

画面 7：
- 展示了 ConsumerAPI 接口，定义了注册和创建消费者的方法。
- 代码内容：
  ```java
  public interface ConsumerAPI {
      /**
       * 用户注册，操作用户信息
       * @param consumerRegisterDTO
       * @return
       */
      RestResponse register(ConsumerRegisterDTO consumerRegisterDTO);
      /**
       * 生成开户请求数据
       * @param consumerRequest 开户信息
       * @return
       */
      RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);
  }
  ```

画面 8：
- 展示了 ConsumerController 类，定义了 hello 和 hi 两个测试接口。
- 代码内容：
  ```java
  @RestController("用户服务的Controller", tags = "Consumer", description = "用户服务API")
  public class ConsumerController implements ConsumerAPI {
      @Autowired
      private ConsumerService consumerService;
      @ApiOperation("测试Hello")
      @RequestMapping(path = "/hello")
      public String hello() { return "hello"; }
      @ApiOperation("测试Hi")
      @ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
      public String hi(String name) { return "hi,"+name; }
  }
  ```

画面 9：
- 展示了 SecurityUtil 类，用于获取当前登录用户。
- 代码内容：
  ```java
  public static LoginUser getUser() {
      ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
      if (servletRequestAttributes != null) {
          HttpServletRequest request = servletRequestAttributes.getRequest();
          Object jwt = request.getAttribute("jsonToken");
          if (jwt instanceof LoginUser) {
              return (LoginUser) jwt;
          }
      }
      return new LoginUser();
  }
  ```

画面 10：
- 展示了 ConsumerService 类中定义了 register 和 createConsumer 方法。
- 代码内容：
  ```java
  void register(ConsumerRegisterDTO consumerRegisterDTO);
  RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);
  ```

画面 11：
- 展示了 ConsumerController 类中定义了获取当前消费者信息的接口。
- 代码内容：
  ```java
  @ApiOperation("获取登录用户信息")
  @RequestMapping("/currConsumer")
  public RestResponse<ConsumerDTO> getCurrConsumer() {
      ConsumerDTO consumerDTO = consumerService.getCurrConsumer(SecurityUtil.getUser().getMobile());
      return RestResponse.success(consumerDTO);
  }
  ```

画面 12：
- 展示了 ConsumerController 类中定义了测试接口。
- 代码内容：
  ```java
  @ApiOperation("过网关保护资源，进行认证测试")
  @ApiImplicitParams({
      @ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "String")
  })
  @RequestMapping(value = "/m/consumers/test")
  public RestResponse<String> testResources(String jsonToken) {
  }
  ```

画面 13：
- 展示了 ConsumerApiAgent 类，用于代理 ConsumerController 的接口。
- 代码内容：
  ```java
  @ApiOperation("生成开户请求数据")
  @PostMapping("/consumers")
  public RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest) {
      return consumerService.createConsumer(consumerRequest);
  }
  ```

画面 14：
- 展示了 Project 实体类中定义了 USER_NO 字段的注解和类型。
