# 12.支付入口-确认页面测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\12.支付入口-确认页面测试【海量资源尽在 666java.com】.mp4
- 时长 7分23秒（音频 444s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下面呢我们就来写一个Controller然后呢咱们让他请求这个支付入口然后呢最终跳转到这个缺点页面好那么还是在交易服务这里边我们在Controller这啊Controller然后呢我们写一个Controller这个Controller呢就是交易服务啊支付支付相关的一个什么接口那支付相关的接口这里边呢
[00:26] 我们还是用Controller注解因为它可能会存在就是返回页面的一个情况因为我们说这个支付入口就是返回支付确认页面所以你必须用Controller注解不要用res的Controller好那么这呢我们就开始写这个方法嘛这个支付入口然后这是它的url这是它url然后呢这里边呢我们就可以来写一个方法先写一个方法方法的名字叫返回值就是stream
[00:54] 那么在这里边呢我们要传哪些数据呢支付入口肯定我们最方便的就是从request的里边就可以拿所有的东西就是请求参数嘛然后当然当然这个支付入口在前边我们其实已经配置过这个支付入口大家还有印象吗在交易服务这边我们来看其实当初我们配置的就是支付入口你看它的地址是它对吧
[01:23] 叫做这个什么呀叫做payintrade那么我们配置这个支付入口各位你别忘了它后边还有一堆参数的有印象吗当初我们生成二维码的这个地址后边还带了一个ticket是不是啊所以所以我们说在什么呀我们在这个参数当中应该还有一个参数并且这个参数是通过什么pass路径
[01:53] 传进来的懂吧就是Ticket所以这个不要少好这样的话我们这个接口就定好了当然URL那我们可以看到Netcast里边这个就是我们的URL没错吧然后呢这里边我们就可以你看比如Request Mapping然后呢你看后边后边是不是就是一个什么Ticket就是传的餐当初我们生成这个支付入口的URL
[02:24] 大家应该还有印象吧这就是这弄错了这大口号就行了搞定了吗这就是我们的支付入口懂吧这个Ticket大家还记得这个Ticket的格式吗这是我们说的传入的这个数据吗大家回忆一下当初我们生成这个支付入口的URL这个Ticket的格式是不是就是base64编码的呀对不对这个格式是对什么呀
[02:55] 对Jason的这个数据进行的一个什么贝斯六四编嘛所以一会儿呢你在这个里头要解析Tag的时候你要注意嗯你要先知道这个格式啊好那后面那我要啊这个响应也就是我返回一个什么确认页面是不是就返回这个页面看见吗就是这个配对吧那这个确认页面怎么返回呢因为页面当中你看
[03:23] 是不是要显示一些这个模型数据啊那你肯定不能用read direct因为这我们学过Spring MVC嘛read direct是不是就是从定向我们应该用什么转发forward懂吧然后冒号那么刚才我们是不是建了一个叫做视图control也就是说我们请求这个地址呢就可以直接定向到转发到这个视图所以
[03:52] 我们在control2这直接让它forward这个地址大家看懂了吗这就是我们的什么入口页面那么这个页面这个方法我们搞定了之后呀我们是不是就可以来测试了但测试的时候你别忘了啊注意啊我们说原来我们测试生成这个什么支付入口的URL的时候我们当初测试还有印象吗我们是走的网关地址对不对
[04:19] 我们是走的网关地址并不是这个交易服务的这个什么叫56050大家有印象吗所以我们这里边要配置一个东西注意我们要在网关上边配一个东西配可以转发到交易服务所以我们要进到我们的网关配置虽然网关不是我们开发的但是我们也知道它的一些信息比如这里头各位凡是以这个Gang Machine打头的它就转到商户的服务对吧
[04:48] 那其实你可以参考这个配置呢我们让他干嘛对我们让他去转发到我们说的这个交易服务那这个配置方法很简单你复制他的这个服务名然后呢在网关的这个配置文件啊就是这个什么gateway然后呢在这把这个服务名改了然后呢所有以什么呀以杠transaction打头的都要转发到我们说的
[05:19] 交易服务这样的话注意这样的话一会我们测试去请求这个地址我们就可以走网关它就可以转发到这个地址大家懂这意思吧好那这个网关的端口是不是就56010啊好了那下面呢我就开始重启了啊那么重启哪些啊那么你刚才我建议这些我们都重启一下网关重启一下然后呢交易服务也重启一下
[05:47] 交易服务肯定我们新增了一些方法重启一下然后我们把这个重启完了之后注意那我接下来要怎么做我是不是就要来访问网关的56010的端口然后URL后边是不是要跟怎么样看我的讲义要个transaction而我们走网关它遇到这个杠transaction它是不是就转发到交易服务了就这样一种方式好就这个地址
[06:14] 那下面呢我们来看它是不是可以转发到这个什么页面呢这是我们最终想要的一个结果因为现在就是当用户一扫二维码它就定向到支付入口那入口呢就转发到一个具体的订单确认页面那我们在这儿吧后边你随便填点东西行吧好大家可以看一下那就到了当然现在各位你看到的这是我用浏览器去浏览嘛
[06:41] 正式的话是用手机浏览对吧那Chrome浏览器呢我们可以切成手机的这种浏览方式你看对吧大概是这样一个效果但是现在页面没有数据嘛因为你现在这个Controller这儿是不是还没有准备数据对这是准备着确认页面所需要的数据我们现在是不是还没有写呀到这为止我们是不是就实现了支付确认页面的一个什么显示对吧我们就在Controller当中写了一个
[07:11] 支付入口的方法然后呢让它转发到确认页面然后后边呢我们就开始在里边呢去准备数据好那么支付确认页面的测试呢咱们就完成了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现支付功能，包括前端页面、后端控制器、Nacos 配置中心的配置以及与微信支付的对接。

2) 按时间顺序列出每张画面的要点：
画面 1:
- IDE 中打开项目 shanjupay-transaction-Service。
- 编辑器中显示 JavaScript 代码，用于生成微信支付所需的参数，包括 appid、timestamp、nonceStr、package、signType、paySign。
- 项目结构中可见 bootstrap.yml、log12.xml、pay.html、pay_error.html。
- 控制台显示服务启动成功。

画面 2:
- IDE 中显示 PayController.java 文件，光标位于类定义处。
- 项目结构中可见 controllers、entity、Mapper、Service 等包。

画面 3:
- Nacos 配置管理页面，显示多个配置文件，如 spring-boot-starter-dubbo.yaml、merchant-Service.yaml、transaction-Service.yaml。
- Group 为 SHANJUPAY_GROUP 的配置文件。

画面 4:
- Nacos 配置编辑页面，编辑的是 transaction-Service.yaml。
- 配置内容：
  ```
  druid:
    url: jdbc:mysql://127.0.0.1:3306/shanjupay_transaction?useUnicode=true&characterEncoding=utf-8
    serverName: localhost
    username: root
    password: mysql
  mybatis-plus:
    typeAliasesPackage: com.shanjupay.transaction.entity
    mapperLocations: classpath:/shanjupay/*/Mapper/*.xml
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
- Nacos 配置编辑页面，编辑的是 merchant-Service.yaml。
- 配置内容：
  ```
  routes:
    - operation-application:
        path: /operation/**
        stripPrefix: false
        merchant-application:
          path: /merchant/**
          stripPrefix: false
        uaa-Service:
          path: /uaa/**
          stripPrefix: false
        transaction-Service:
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

