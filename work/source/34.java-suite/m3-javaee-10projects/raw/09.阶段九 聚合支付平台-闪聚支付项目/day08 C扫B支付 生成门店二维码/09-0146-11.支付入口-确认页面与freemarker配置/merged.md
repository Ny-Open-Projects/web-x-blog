# 11.支付入口-确认页面与freemarker配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\11.支付入口-确认页面与freemarker配置【海量资源尽在 666java.com】.mp4
- 时长 6分51秒（音频 412s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来开发交易服务的支付入口当用户扫描门店的二维码然后呢就会请求到我们的交易服务那交易服务呢就会去获取一些数据因为我们知道当初我们生成二维码的时候呢它是二维码
[00:21] 这个URL会携带一些数据的对吧交易服务会获取这些数据然后呢最终准备一些数据呢啊响应给用户那响应回去呢会响应一个确认页面对吧这个支付入口最终得到的是一个什么订单的确认页面里面会显示啊这个订单的标题啊内容啊包括金额等等啊这儿有一个确认支付对所以这个确认页面就是支付入口最终
[00:51] 所显示的一个画面注意这里边看一下我有没有啊看一下看就这页面看到吗有点丑对吧因为是没有数据啊那再回来我们说交易服务的支付入口呢是二维码的地址那它最终会响应一个订单的确认页面那你想呀订单确认页面当中有一些信息那就需要交易服务在这去准备好对吧好那么首先呢我们要做一件事呢就是要把确认页面呢
[01:20] 把它写一下这个确认页面呢就是我们采用的是FreeMark模板引擎技术呢去编写的这里边呢我们可以把页面直接拿到我们的什么交易服务当中那么注意看啊页面的内容呢不要求大家一点一点的去写但是呢里边的内容是要求大家呢去能够会这个认的好看好把它放进去好那么放进去之后呢大家看
[01:52] 这个就是我们说的定单的确认页面像商家付款对吧里边有一些信息你看这些标签其实我们都学习过对吧这是free market的这个什么dollar符号里边是不是就是模型数据这个模型数据是不是就取的内置对象的数据是吧包括很多的这些还有什么free market的这个衣服标签对吧衣服指令好回头呢我们再
[02:21] 去准备数据的时候我们再来详细的看这个页面现在这个页面呢是不是我就考进来了并且这个timeplace是不是free market默认的一个什么这个地址对吧好光考进去页面还不行因为我们要最终请求交易服务嘛请求交易服务是要使用free market的嘛所以交易服务里边要添加free market的什么这个依赖大家可以看一下如果没有我们添一下如果有了就不用添了
[02:50] 是不是有了有了就不用添了好然后继续往下走因为我们知道FreeMark它是需要一些配置的凡是我们项目当中用到FreeMark的都要进行配置那么我们使用Necros所以我们这里边用一个单独给FreeMark建一个配置这应该是我们常用的一个方法叫Common Group通用的那将来谁用它是又引入这个配置文件就行了
[03:21] 好那具体的配置内容我们在当初研究free marker的时候呢其实这个内容我们都知道对吧我就不再多说然后呢去把它发布无效的前面有个小空格好然后找配置已存在报杂错然后再看一下那里头有free marker吗我们看一下已经有了是吧已经有了有了之后呢我们来看一下这是不是就是配置信息都OK了吧
[04:01] 好那么接下来我们继续那你刚才建了一个Fremark的配置文件咱们现在要在交易服务当中用Fremark很显然我们是需要在交易服务的这个Bootstrap这个YML里边再把这个配置文件把它引进去你看现在我们是不是引了很多的这个配置文件了大家看到吗这就是一个Fremark的配置文件我们就引上来了好了那么基本上这个配置就快结束了
[04:27] 还有一点就是说将来我们统一入口就是支付入口我们会把请求最终转发到页面上边所以在转发页面的时候我们这里边用webmvc的configure我们来配置一个Controller这个Controller你看这个Controller这是一个url它对应的视图就是页面的一个名称就是我们将来请求这个Controller就可以来定向到这个页面
[04:53] 所以我们呢来把它配置一下因为这个过程呢其实很少去用也就是在我们的什么因为我们用Spring Boot嘛用Spring Boot的话你们通常我们是在Controller里面去写的对吧但也有少量情况我们是需要干嘛是需要去配置一些比如说我们的一些这个
[05:15] 设置好的Controller的那这个配置这个过程呢其实我就直接考过去了然后大家理解啥意思就行了因为这个呢就是一劳永逸的事我们不用去去写这个代码那看好这个就是url它呢就对应什么对应这个配好这就是我们建了一个什么四图的一个Controller将来请求这个地址就得到这个拿到这个页面了好那我们看这个配.html它的扩展名是不是html
[05:44] 扩展名是html那各位我们在配置free marker的时候注意这里边一定是.html大家看到了吗千万不要乱写啊因为早期我们在测试这个其他功能的时候你看这里边是不是我们写的一个叫ftl是吧因为你现在已经引入进来了就这个free marker的配置并且我们的后缀是指定为.html的大家看到了吗所以啊所以啊就是这个.ftl这
[06:13] 我建议你呢你就可以把它改成html懂吧原来的文件你可以保留啊好那这样的话我们整个free marker的这个配置包括我们的支付确认页面咱们是不是都在我们的项目当中就准备就绪了吧那接下来我们是不是就要编写一个Controller就是我们支付入口的Controller然后呢来这个去写一些逻辑
[06:43] 好那交易服务支付入口这块for remarker配置以及确认页面我们就完工好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面 9: 展示 IDE 中的 application.yml 文件，配置了 server.port 为 8088，server.context-path 为 /test-freemarker，以及 Nacos 的地址和 namespace。
画面 10: 展示 IDE 中的 application.yml 文件，配置了多个 Spring Boot 配置文件，如 spring-boot-http.yaml、spring-boot-mybatis-plus.yaml、spring-boot-freemarker.yaml 等，group 均为 COMMON_GROUP。
画面 11: 展示 IDE 中的项目结构，重点是 Controller 包下的 PayController。
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
  Nacos:
    server:
      address: 127.0.0.1:8848
    discovery:
      server-addr: ${Nacos.server.addr}
      namespace: ${Nacos.namespace}
      cluster-name: DEFAULT
```
画面 10:
```
refresh: true
data-id: spring-boot-http.yaml # Spring Boot http配置
group: COMMON_GROUP # 通用配置组

refresh: true
data-id: spring-boot-mybatis-plus.yaml # Spring Boot mybatis-plus配置
group: COMMON_GROUP # 通用配置组

refresh: true
data-id: spring-boot-freemarker.yaml # Spring Boot freemarker配置
group: COMMON_GROUP # 通用配置组
```
画面 11:
```
file-extension: yaml
namespace: 5eec3c1-4f05-40c-964a-c844f342a04
ext-config:
  refresh: true
  data-id: spring-boot-http.yaml # Spring Boot http配置
  group: SHANJUPAY_GROUP # 聚合支付服务组

  refresh: true
  data-id: spring-boot-starter-druid.yaml # Spring Boot druid配置
  group: SHANJUPAY_GROUP # 通用配置组

  refresh: true
  data-id: spring-boot-mybatis-plus.yaml # Spring Boot mybatis-plus配置
  group: SHANJUPAY_GROUP # 通用配置组

  refresh: true
  data-id: spring-boot-freemarker.yaml # Spring Boot freemarker配置
  group: SHANJUPAY_GROUP # 通用配置组

  refresh: true
  data-id: spring-boot-redis.yaml # Spring Boot redis配置
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

