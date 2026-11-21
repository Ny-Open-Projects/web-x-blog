# 画面线理解：12.支付入口-确认页面测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\12.支付入口-确认页面测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:50, 01:15, 02:08, 03:09, 03:42, 04:27, 05:03, 05:29, 05:49, 06:04, 06:31, 06:47, 07:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:54:07

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现支付功能，包括前端页面、后端控制器、Nacos 配置中心的配置以及与微信支付的对接。

2) 按时间顺序列出每张画面的要点：
画面 1:
- IDE 中打开项目 shanjupay-transaction-service。
- 编辑器中显示 JavaScript 代码，用于生成微信支付所需的参数，包括 appid、timestamp、nonceStr、package、signType、paySign。
- 项目结构中可见 bootstrap.yml、log12.xml、pay.html、pay_error.html。
- 控制台显示服务启动成功。

画面 2:
- IDE 中显示 PayController.java 文件，光标位于类定义处。
- 项目结构中可见 controllers、entity、mapper、service 等包。

画面 3:
- Nacos 配置管理页面，显示多个配置文件，如 spring-boot-starter-dubbo.yaml、merchant-service.yaml、transaction-service.yaml。
- Group 为 SHANJUPAY_GROUP 的配置文件。

画面 4:
- Nacos 配置编辑页面，编辑的是 transaction-service.yaml。
- 配置内容：
  ```
  druid:
    url: jdbc:mysql://127.0.0.1:3306/shanjupay_transaction?useUnicode=true&characterEncoding=utf-8
    serverName: localhost
    username: root
    password: mysql
  mybatis-plus:
    typeAliasesPackage: com.shanjupay.transaction.entity
    mapperLocations: classpath:/shanjupay/*/mapper/*.xml
  shanjupay:
    payurl: "http://127.0.0.1:56010/transaction/pay-entry"
  ```

画面 5:
- IDE 中 PayController.java 文件，光标位于 return 语句处。
- 代码提示中显示 Return、ReturnNode 等类。

画面 6:
- IDE 中显示项目结构，左侧为项目目录，右侧为 PayController.java 文件。
- 代码中显示 @RequestMapping("/pay-entry/{ticket}")。

画面 7:
- PPT 页面，标题为“5. 定义支付入口接口”，内容为：
  ```
  @Slf4j
  @Controller
  public class PayController {
      /**
       * 支付入口
       * @param ticket
       * @param type
       * @param request
       * @return
       */
      @RequestMapping(value = "/pay-entry/{ticket}")
      public String payEntry(@PathVariable("ticket") String ticket, HttpServletRequest request) {
          return "forward:/pay-page";
      }
  }
  ```

画面 8:
- Nacos 配置编辑页面，编辑的是 merchant-service.yaml。
- 配置内容：
  ```
  routes:
    - operation-application:
        path: /operation/**
        stripPrefix: false
        merchant-application:
          path: /merchant/**
          stripPrefix: false
        uaa-service:
          path: /uaa/**
          stripPrefix: false
        transaction-service:
          path: /transaction/**
          stripPrefix: false
  ```

画面 9:
- IDE 中 PayController.java 文件，光标位于 return 语句处。
- 控制台显示服务启动成功。

画面 10:
- IDE 中 PayController.java 文件，光标位于 return 语句处。
- 控制台显示服务启动成功。
- Terminal 中显示 Java.exe 路径。

画面 11:
- PPT 页面，标题为“2) 用chrome浏览器访问（用于机视模式）二维的统一入口地址。”
- 地址：http://127.0.0.1:56010/transaction/pay-entry/...
- 注意：由于没有数据，订单信息均为空。
- 页面显示蓝色背景，下方有“商品名称”和“订单金额”输入框。

画面 12:
- 浏览器页面，显示微信支付文档。
- 接口地址：https://api.mch.weixin.qq.com/pay/unifiedorder
- 请求参数表：
  | 字段名 | 参数名 | 必填 | 类型 | 示例值 | 描述 |
  |--------|--------|------|------|--------|------|
  | 公众号ID | appid | 是 | String(32) | wxdc678efh567hg/876 | 微信支付分配的公众账号ID（企业号可不填） |

画面 13:
- 浏览器页面，显示支付页面。
- 页面包含“商品名称”和“订单金额”输入框，以及“立即支付”按钮。
- 右侧显示 HTML 代码和样式。

画面 14:
- PPT 页面，标题为“4.3.1 支付确认页面”。
- 内容：
  1. 从资料代码拷贝 pay.html、pay_error.html 到交易服务工程下。
  2. 在交易服务接口实现工程的 pom.xml 中引入依赖：
     ```
     <!-- freemarker依赖 -->
     <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-freemarker</artifactId>
     </dependency>
     ```
  3. 在 Nacos 中配置 spring-boot-freemarker.yaml，Group: COMMON_GROUP。
     ```
     # freemarker基本配置
     spring:
     ```
