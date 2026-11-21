# 画面线理解：day03-11-用户中心保存信息-搭建MP环境

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-11-用户中心保存信息-搭建MP环境_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:58, 01:19, 01:34, 01:48, 02:33, 03:11, 03:49, 04:04, 04:20, 04:54, 06:14, 07:00, 07:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:34:49

1) 这一组画面整体在讲什么（一句话）：
演示如何在微服务架构中，通过 Apollo 配置中心为消费者服务（consumer-service）配置数据库连接信息，并展示相关代码和配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了在万向2p-api 工程中定义 ConsumerApi 接口，其中包含 register 方法。
- 代码：public interface ConsumerApi { /* 用户注册 */ @param consumerRegisterDTO @return } RestResponse register(ConsumerRegisterDTO consumerRegisterDTO);
- 同时展示了在 ConsumerController 中实现 register 方法的代码：
@ApiOperation("用户注册") @ApiImplicitParam(name = "consumerRegisterDTO", value = "用户注册", required = true, dataType = "AccountRegisterDTO", paramType = "body") @PostMapping(value = "/consumers") public RestResponse register(@RequestBody ConsumerRegisterDTO consumerRegisterDTO) {

画面 2：
- 展示了在万向2p-account-service 工程中定义 checkMobile 方法。
- 代码：
RestResponse<Integer> checkMobile(String mobile, String key, String code);
@ApiOperation("校验手机号和验证码") @ApiImplicitParams({@ApiImplicitParam(name = "mobile", value = "手机号", required = true, dataType = "String"), @ApiImplicitParam(name = "code", value = "验证码", required = true, dataType = "String")}) @GetMapping("/mobiles/{mobile}/key/{key}/code/{code}") @Override public RestResponse<Integer> checkMobile(@PathVariable String mobile, @PathVariable String key, @PathVariable String code) {

画面 3：
- 展示了万向2p-consumer-service 的 pom.xml 文件内容，其中包含多个依赖项。
- 代码：
<dependency> <groupId>com.baidou</groupId> <artifactId>mybatis-plus-boot-starter</artifactId> </dependency> <dependency> <groupId>org.mybatis</groupId> <artifactId>mybatis-typehandlers-jsr310</artifactId> </dependency> <dependency> <groupId>com.alibaba</groupId> <artifactId>druid-spring-boot-starter</artifactId> </dependency> <dependency> <groupId>mysql</groupId> <artifactId>mysql-connector-java</artifactId> </dependency> </dependencies>

画面 4：
- 展示了万向2p-consumer-service 的 pom.xml 文件内容，其中包含 Spring Cloud 的依赖。
- 代码：
<dependency> <groupId>org.springframework.cloud</groupId> <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId> </dependency> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-test</artifactId> <scope>test</scope> </dependency>

画面 5：
- 展示了万向2p-consumer-service 的 pom.xml 文件内容，其中包含 MyBatis Plus 和 Druid 的依赖。
- 代码：
<dependency> <groupId>com.baidou</groupId> <artifactId>mybatis-plus-boot-starter</artifactId> </dependency> <dependency> <groupId>org.mybatis</groupId> <artifactId>mybatis-typehandlers-jsr310</artifactId> </dependency> <dependency> <groupId>com.alibaba</groupId> <artifactId>druid-spring-boot-starter</artifactId> </dependency> <dependency> <groupId>mysql</groupId> <artifactId>mysql-connector-java</artifactId> </dependency> </dependencies>

画面 6：
- 展示了 Apollo 配置中心的登录页面，地址为 localhost:8070/config.html#/?appId=consumer-service。
- 页面为空白，等待加载。

画面 7：
- 展示了 Apollo 配置中心的界面，当前选中的是 account-service 项目。
- 页面显示了多个配置项，如 micro_service.spring-boot-http、micro_service.spring-eureka 等。

画面 8：
- 展示了 Apollo 配置中心中 consumer-service 项目的配置页面。
- 页面显示了多个配置项，如 mybatis-plus.mapper-locations、mybatis-plus.typeAliasesPackage 等。

画面 9：
- 展示了 Apollo 配置中心中 consumer-service 项目的配置页面。
- 页面显示了 micro_service.mybatis-plus 配置项下的数据库连接信息。
- 代码：
spring.datasource.url jdbc:mysql://localhost:3306/pz_consumer?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=UTC
spring.datasource.driver-class-name com.mysql.cj.jdbc.Driver
spring.datasource.username root
spring.datasource.password 123456

画面 10：
- 展示了 Apollo 配置中心的界面，当前选中的是 consumer-service 项目。
- 页面显示了多个配置项，如 micro_service.spring-boot-http、micro_service.spring-eureka 等。

画面 11：
- 展示了万向2p-consumer-service 项目的结构，其中包含了 ConsumerService 类。
- 代码：
package cn.itecast.wanxing2p.consumer; @SpringBootApplication @EnableDiscoveryClient @EnableFeignClients(basePackages = "cn.itecast.wanxing2p.consumer.agent") public class ConsumerService { public static void main(String[] args) { SpringApplication.run(ConsumerService.class, args); } }

画面 12：
- 展示了 SQLyog Professional 64 的界面，用于数据库操作。
- 页面为空白，等待输入。

画面 13：
- 展示了万向2p-api 工程中 Consumer 实体类的代码。
- 代码：
private String userNo; /* 用户编号，生成唯一，用户在容器系统标识 */ private String mobile; /* 平台预留手机号 */ private String userType; /* 用户类型，个人or企业，预留 */ private String role; /* 用户角色，借款人or投资人 */

画面 14：
- 展示了万向2p-consumer-service 项目的 Consumer 实体类代码。
- 代码：
/* 用户编号，生成唯一，用户在容器系统标识 */ private String userNo; /* 平台预留手机号 */ private String mobile; /* 用户类型，个人or企业，预留 */ private String userType; /* 用户角色，借款人or投资人 */ private String role; /* @TableField("USER_NO") */ /* @TableField("MOBILE") */ /* @TableField("USER_TYPE") */ /* @TableField("ROLE") */

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
public interface ConsumerApi { /* 用户注册 */ @param consumerRegisterDTO @return } RestResponse register(ConsumerRegisterDTO consumerRegisterDTO);
@ApiOperation("用户注册") @ApiImplicitParam(name = "consumerRegisterDTO", value = "用户注册", required = true, dataType = "AccountRegisterDTO", paramType = "body") @PostMapping(value = "/consumers") public RestResponse register(@RequestBody ConsumerRegisterDTO consumerRegisterDTO) {

画面 2：
RestResponse<Integer> checkMobile(String mobile, String key, String code);
@ApiOperation("校验手机号和验证码") @ApiImplicitParams({@ApiImplicitParam(name = "mobile", value = "手机号", required = true, dataType = "String"), @ApiImplicitParam(name = "code", value = "验证码", required = true, dataType = "String")}) @GetMapping("/mobiles/{mobile}/key/{key}/code/{code}") @Override public RestResponse<Integer> checkMobile(@PathVariable String mobile, @PathVariable String key, @PathVariable String code) {

画面 3：
<dependency> <groupId>com.baidou</groupId> <artifactId>mybatis-plus-boot-starter</artifactId> </dependency> <dependency> <groupId>org.mybatis</groupId> <artifactId>mybatis-typehandlers-jsr310</artifactId> </dependency> <dependency> <groupId>com.alibaba</groupId> <artifactId>druid-spring-boot-starter</artifactId> </dependency> <dependency> <groupId>mysql</groupId> <artifactId>mysql-connector-java</artifactId> </dependency> </dependencies>

画面 4：
<dependency> <groupId>org.springframework.cloud</groupId> <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId> </dependency> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-test</artifactId> <scope>test</scope> </dependency>

画面 5：
<dependency> <groupId>com.baidou</groupId> <artifactId>mybatis-plus-boot-starter</artifactId> </dependency> <dependency> <groupId>org.mybatis</groupId> <artifactId>mybatis-typehandlers-jsr310</artifactId> </dependency> <dependency> <groupId>com.alibaba</groupId> <artifactId>druid-spring-boot-starter</artifactId> </dependency> <dependency> <groupId>mysql</groupId> <artifactId>mysql-connector-java</artifactId> </dependency> </dependencies>

画面 6：
无代码或配置。

画面 7：
无代码或配置。

画面 8：
无代码或配置。

画面 9：
spring.datasource.url jdbc:mysql://localhost:3306/pz_consumer?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=UTC
spring.datasource.driver-class-name com.mysql.cj.jdbc.Driver
spring.datasource.username root
spring
