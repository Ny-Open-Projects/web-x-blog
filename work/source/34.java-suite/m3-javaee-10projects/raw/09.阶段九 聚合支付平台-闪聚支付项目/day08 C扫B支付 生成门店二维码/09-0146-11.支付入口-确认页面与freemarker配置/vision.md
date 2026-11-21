# 画面线理解：11.支付入口-确认页面与freemarker配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\11.支付入口-确认页面与freemarker配置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:48, 01:17, 01:46, 02:14, 02:44, 03:08, 03:37, 03:57, 04:15, 04:33, 05:09, 05:47, 06:23, 06:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:53:34

1) 这一组画面整体在讲什么（一句话）：
实现一个基于 Spring Boot 和 Freemarker 的支付确认页面，并通过 Nacos 配置中心进行配置管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示支付服务的交互流程图，包括用户、商户、聚合支付平台、交易服务、支付渠道代理服务和第三方支付。流程步骤为：顾客扫描二维码请求交易服务支付入口；交易服务解析请求生成支付确认页面；交易服务向服务响应支付确认页面。
画面 2: 说明从资料->代码拷贝 pay.html、pay_error.html 到交易服务工程下的 resources/templates 目录。
画面 3: 展示 IDE 中的项目结构，重点是 pom.xml 文件中的 spring-boot-starter-freemarker 依赖。
画面 4: 展示 pay.html 页面中的 JavaScript 代码，用于处理表单提交，其中 action 路径为 /wxjsapi/。
画面 5: 展示 pay.html 页面中的 HTML 代码，包含表单元素如 input、span 等，用于用户输入商品名称、订单描述、总金额等。
画面 6: 展示 Nacos 配置中心的界面，准备创建新的配置。
画面 7: 在 Nacos 中创建配置，Data ID 为 spring-boot-freemarker.yaml，Group 为 COMMON_GROUP，配置格式为 YAML。
画面 8: 在 Nacos 中编辑配置，内容为 spring.freemarker 相关配置，包括 charset、request-context-attribute、content-type、suffix、enabled、resources 和 add-mappings。
画面 9: 展示 IDE 中的 application.yml 文件，配置了 server.port 为 8088，server.context-path 为 /test-freemarker，以及 nacos 的地址和 namespace。
画面 10: 展示 IDE 中的 application.yml 文件，配置了多个 Spring Boot 配置文件，如 spring-boot-http.yaml、spring-boot-mybatis-plus.yaml、spring-boot-freemarker.yaml 等，group 均为 COMMON_GROUP。
画面 11: 展示 IDE 中的项目结构，重点是 controller 包下的 PayController。
画面 12: 在 Nacos 中编辑配置，内容为 resources 和 mvn 相关配置，包括 add-mappings 和 throw-exception-if-no-handler-found。
画面 13: 展示 pay.html 页面中的 HTML 代码，包含 meta 标签和 JavaScript 代码，用于处理支付请求。
画面 14: 展示 PayController 的 Java 代码，定义了支付入口接口，使用 @RequestMapping 注解，路径为 /pay-entry/{ticket}。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
1. 从资料->代码拷贝pay.html、pay_error.html到交易服务工程下。
```
画面 3:
```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-freemarker</artifactId>
</dependency>
```
画面 4:
```
function IsValidPay() {
    var totalAmount = document.getElementById('totalAmount').value;
    if (totalAmount == "") {
        alert("付款金额不能为空");
        return;
    }
    var action = "";
    if (RequestParameters['openId']??) {
        action = "${rc.contextPath}/wxjsapi/";
    } else {
        action = "${rc.contextPath}/createAllPayOrder/";
    }
    document.getElementById('form').action = action;
    document.getElementById('form').submit();
    return false;
}
```
画面 5:
```
<p class="name">{$RequestParameters.subject}</p>
<div class="form-container">
    <form id="form" action="" method="post">
        <input type="hidden" name="appId" value="{$RequestParam.appId}">
        <input type="hidden" name="openId" value="{$RequestParam.openId}">
        <input type="hidden" name="channel" value="{$RequestParam.channel}">
        <input type="hidden" name="outTradeNo" value="{$RequestParam.outTradeNo}">
        <p>商品名称：<span><input type="text" name="subject" value="{$RequestParam.subject}"></span></p>
        <p>订单描述：<span><input type="text" name="body" value="{$RequestParam.body}"></span></p>
        <p>总金额：<span><input type="text" name="totalAmount" value="{$RequestParam.totalAmount}"></span></p>
        <p><input type="submit" value="立即支付"></p>
    </form>
</div>
```
画面 7:
```
spring:
  freemarker:
    charset: UTF-8
    request-context-attribute: rc
    content-type: text/html
    suffix: .html
    enabled: true
    resources:
      add-mappings: false #关闭工程中默认的资源处理
```
画面 8:
```
spring:
  freemarker:
    charset: UTF-8
    request-context-attribute: rc
    content-type: text/html
    suffix: .html
    enabled: true
    resources:
      add-mappings: false #关闭工程中默认的资源处理
    throw-exception-if-no-handler-found: true #出现错误时直接抛出异常
```
画面 9:
```
server:
  port: 8088 #服务端口
  servlet:
    context-path: /test-freemarker #指定服务点
spring:
  application:
    name: test-freemarker #指定服务名
  freemarker:
    request-context-attribute: rc
    expose-request-attribute: true
    expose-session-attribute: true
    charset: UTF-8
    content-type: text/html
  nacos:
    server:
      address: 127.0.0.1:8848
    discovery:
      server-addr: ${nacos.server.addr}
      namespace: ${nacos.namespace}
      cluster-name: DEFAULT
```
画面 10:
```
refresh: true
data-id: spring-boot-http.yaml # spring boot http配置
group: COMMON_GROUP # 通用配置组

refresh: true
data-id: spring-boot-mybatis-plus.yaml # spring boot mybatis-plus配置
group: COMMON_GROUP # 通用配置组

refresh: true
data-id: spring-boot-freemarker.yaml # spring boot freemarker配置
group: COMMON_GROUP # 通用配置组
```
画面 11:
```
file-extension: yaml
namespace: 5eec3c1-4f05-40c-964a-c844f342a04
ext-config:
  refresh: true
  data-id: spring-boot-http.yaml # spring boot http配置
  group: SHANJUPAY_GROUP # 聚合支付服务组

  refresh: true
  data-id: spring-boot-starter-druid.yaml # spring boot druid配置
  group: SHANJUPAY_GROUP # 通用配置组

  refresh: true
  data-id: spring-boot-mybatis-plus.yaml # spring boot mybatis-plus配置
  group: SHANJUPAY_GROUP # 通用配置组

  refresh: true
  data-id: spring-boot-freemarker.yaml # spring boot freemarker配置
  group: SHANJUPAY_GROUP # 通用配置组

  refresh: true
  data-id: spring-boot-redis.yaml # spring boot redis配置
  group: SHANJUPAY_GROUP # 通用配置组
```
画面 12:
```
resources:
  add-mappings: false #关闭工程中默认的资源处理
mvn:
  throw-exception-if-no-handler-found: true #出现错误时直接抛出异常
```
画面 13:
```
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Cache-Control" content="no-cache">
<meta http-equiv="Expires" content="0">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>向左滑动</title>
<script>
function onBridgeReady() {
    WeixinJSBridge.invoke(
        'getBrandWCPayRequest', {
            "appId": "${appId}",
            "timeStamp": "${timeStamp}",
            "nonceStr": "${nonceStr}",
            "package": "${package}",
            "signType": "MD5",
            "paySign": "${paySign}"
        },
        function(res) {
            if (res.err_msg == "get_brand_wcpay_request:ok") {
                alert("支付成功");
            } else {
                alert("支付失败");
            }
        }
    );
}
</script>
```
画面 14:
```
@S144j
@Controller
public class PayController {
    /**
     * 支付入口
     * @param ticket
     * @param type
     * @param request
     * @return
     */
    @RequestMapping(value = "/pay-entry/{ticket}") String ticket,HttpServletRequest
