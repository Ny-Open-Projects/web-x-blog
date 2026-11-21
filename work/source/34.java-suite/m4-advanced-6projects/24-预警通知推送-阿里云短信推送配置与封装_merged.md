# 24-预警通知推送-阿里云短信推送配置与封装 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们开始讲解学习阿里云短信推送的配置

以及在项目当中的集成使用

短信它不同于邮件

运营商监管比较严格

所以阿里云对短信的使用管理也是非常严苛的

必须要有相应的签名和模板

如果是采用公司的身份就比较容易申请

阿里云的短信是不提供免费的使用额度

首先咱们去查看阿里云短信的后台管理配置

在左上角产品和服务里面

选择短信服务

短信配置来讲也比较简单

点击国内消息

在这里要完成签名管理和模板管理的配置

这些模板信息都是必须要求通过审核之后才能够正常使用

咱们点击添加模板

可以看到这里面的具体配置信息

如果是具备了企业资质

这里可以使用的模板类型就相对比较多一些

整个审核还是比较严格的

申请的时候还需要提供业务使用场景的说明

好这个呢是模板的管理配置

然后呢是签名的管理

这里的签名会跟随短信一起发送

比如咱们接收到的银行通知

不同银行的通知会签署不同银行的名称

咱们可以看一下添加签名所需要的信息

这个呢是签名的名称

这个呢要符合相应的规范

这里是适用的场景

如果是选取验证码

那么模板里面是验证码类型的

它就会附加相应的签名

下面是签名的来源

然后是证明文件信息

这一块如果是公司或者企业的资质

申请起来会相对比较快一些

好这个呢是签名的管理

好那咱们回到讲义当中

接下来我们去实现短信发送服务API的封装

咱们将代码copy到工程当中做讲解

在service下面创建一个新的实现类

名称叫sms生长

将代码粘连进来

修正相应的错误

导入对应的包

这个是在阿里云下面的

好那咱们来看一下它的具体实现

这里是定义的常量配置信息

按默认的内容设置就可以

下面是短信通知发送的具体实现

这里会去组装一个common request的对象

然后会将相应的属性设置进去

这里要填写相应的区域

然后是接受者的电话号码信息

下面是短信的签名信息

然后是短信的模板编号

这个对应的就是咱们在后台里面设置的签名和模板信息

每个签名都会有个签名的名称

每个签名都会有个签名的名称

每个签名都会有个签名的名称

每个签名都会有个签名的名称

每个签名都会有个签名的名称

模板管理下面会有相应的模板扣的

这些需要配置在代码当中

然后下面是模板参数内容的替换处理

因为咱们并没有验证通过的短信模板

在这里是做一个举例讲解

比如说有一个快递通知的模板

这里会有三个变量

那么就需要将模板里面涉及到的所有变量信息

组装为一个map

然后将组装的所有变量信息

放置在模板参数下面

接下来就是通过阿里云的客户端

进行短信通知的发送

处理成功会设置相应的状态码

如果是失败的时候会出现

Serve一个Service或者是Cland一个Service

好 这个就是阿里云短信API的封装

那咱们回到讲义当中

这里要注意一下

短信的发送结果和邮件推送方式是不一样的

短信发送如果出现了失败

短信发送如果出现了失败

会返回具体的错误码和原因

这个可以通过来Support对象里面的Get Data

去获取详情

这里提供了一个响应成功的示例

那如果短信发送错误呢

这个code会返回相应的错误码

message会返回相应的提示消息

好 接着咱们要在调度服务工程里面

增加相应的配置信息

将这些信息做一个copy

回到工程当中

在调度服务下面

找到工程中

在工程配置

咱们就添加到最下面

这些是阿里云通信服务的配置内容

这里面的配置属性和抽象类里面的定义属性是一致的

咱们可以看到

这里有区域信息

访问的key

授权密钥

邮箱账号

短信模板

签名等等

咱们回到工程配置里面

那在这里

首先是配置服务区域

CN是代表中国

CN是代表中国

杭州是杭州市

然后是XSKey

访问的权限信息

这个是secret的授权密钥

下面是发送的邮箱账号

短信的模板编码

以及短信的签名名称

这个在后台管理里面可以看到

每个模板都会提供相应的编号

签名呢

会有个名称

好

回到工程当中

好

这些就是阿里云通信服务的配置

这些

都是必要的信息

大家不要配置错误

接下来咱们还要去实现自动化配置内

通过配置内会注入相应的属性信息

以及初始化阿里云推送服务的调用客户端

咱们加代码做一个copy

回到工程当中

在咱们的start send的模块下面

在这里去添加一个自动化的配置内

Auto stock

Sender configuration

将代码粘贴进来

修正相应的错误

咱们要导入对应的包

这个是在Spring framework下面

咱们来看一下它的实现

这里有个条件化注写

它的条件是根据工程配置当中是否配置了相应的属性

接着会将阿里云的通信配置信息注入进来

然后会将阿里云的通信配置信息注入进来

然后会将阿里云的通信配置信息注入进来

然后会将阿里云的通信配置信息注入进来

然后会将阿里云的通信配置信息注入进来

然后会将阿里云的通信配置信息注入进来

然后会去创建一个邮件发送的实现类

邮件发送的代码咱们之前已经做了实现

它会放入到并容器当中

编译咱们项目服务的使用

下面会创建一个短信发送的实现类

会初始化一个客户端

将它加入到Spring的容器管理当中

好

接下来咱们还去增加Mate INF的配置文件

去指向相应的配置类

右键创建一个新的文件

名称叫Spring factories

这里增加相应的配置

Spring framework boot autoconfigure

Enable autoconfiguration进行换行

这里要指向配置类的路径

将它copy下

粘贴进来

好

那整体配置就已经完成

咱们回到讲义当中

这一讲咱们实现了阿里云短信推送配置

以及在项目当中的集成封装

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为一个技术实战教程，主要讲解如何在 Spring Boot 项目中集成阿里云短信服务。讲师首先介绍了阿里云短信服务的背景和配置要求（如必须有签名和模板），然后通过演示在阿里云控制台创建短信模板，接着在项目中编写 Java 代码调用阿里云 API 发送短信，并最终通过 Spring Boot 的 `@Configuration` 注解和 `@Value` 注解，将阿里云的配置信息（如 AccessKey、Secret、模板ID等）从配置文件中注入到 Java 类中，实现短信服务的自动化配置和调用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程引入，展示课程大纲，定位到第 3.6 节“阿里云短信推送配置与集成”。
*   **00:15 - 00:30**: 讲解阿里云短信服务的背景，强调其监管严格，必须配置签名和模板，且无免费额度。
*   **00:30 - 00:45**: 演示如何进入阿里云短信服务管理后台。
*   **00:45 - 01:00**: 在阿里云控制台创建短信模板，展示模板名称、模板CODE和变量占位符的配置。
*   **01:00 - 01:15**: 回到项目代码，展示 `SmsSender` 类中 `sendMessage` 方法的实现，重点讲解如何构造 `CommonRequest` 对象并设置参数，如 `RegionId`、`PhoneNumbers`、`SignName` 和 `TemplateCode`。
*   **01:15 - 01:30**: 讲解模板变量的使用方式，例如 `$time` 和 `$price`，并展示如何通过 `Map<String, String>` 传递这些变量。
*   **01:30 - 01:45**: 展示短信发送成功后的响应数据结构，包括 `Message`、`RequestId`、`BizId` 和 `Code` 等字段。
*   **01:45 - 02:00**: 讲解如何在 Spring Boot 项目中配置阿里云短信服务，展示 `bootstrap-dev.yml` 配置文件中的 `aliyun.sender` 配置项。
*   **02:00 - 02:15**: 创建 `AutoStockSenderConfiguration` 配置类，使用 `@Value` 注解从配置文件中注入 `regionId` 和 `accessKey`。
*   **02:15 - 02:30**: 在 `AutoStockSenderConfiguration` 类中编写 `@Bean` 方法，创建并初始化 `SmsSender` 实例，并将配置信息注入其中。
*   **02:30 - 02:45**: 在 `META-INF/spring.factories` 文件中配置 `AutoStockSenderConfiguration`，使其能被 Spring Boot 自动加载。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3.6 阿里云短信推送配置与集成”。
    *   **关键文字**: “短信不同于邮件，运营商监管比较严格，所以阿里云对短信使用管理也是非常严苛，必须要有签名和模板，没有免费试用额度。”
    *   **关键文字**: “短信需要通过模板才能发送，模板可以内置变量，多个变量需要通过JSON方式传递，这里做了一个举例，申请下来的模板，可采用此方式配置使用。”
    *   **关键文字**: “短信的发送结果与邮件不同，出现失败，会返回具体错误码和原因。通过 response.getData() 获取，示例：”

*   **代码关键内容**:
    *   **`SmsSender.java` 中的 `sendMessage` 方法**:
        ```java
        @Override
        public SenderResult sendMessage(SenderMessage notifyMessage) {
            CommonRequest request = new CommonRequest();
            request.setMethod(MethodType.POST);
            request.setDomain(DOMAIN);
            request.setVersion(VERSION);
            request.setAction(ACTION_SEND_SMS);
            request.putQueryParameter(name: "RegionId", getRegionId());
            request.putQueryParameter(name: "PhoneNumbers", notifyMessage.getReceiver());
            request.putQueryParameter(name: "SignName", getSmsSignName());
            request.putQueryParameter(name: "TemplateCode", getSmsTemplateCode());
            // 模板变量示例：$name, $time, $price
            Map<String, String> params = new HashMap<>();
            params.put("name", "用户");
            params.put("time", "10分钟");
            params.put("price", "100元");
            // ... (后续代码用于发送请求并处理响应)
        }
        ```
    *   **`bootstrap-dev.yml` 配置文件**:
        ```yaml
        # 阿里云通信服务配置
        aliyun:
          sender:
            # 服务区域
            regionId: cn-hangzhou
            # 访问key
            accessKey: LTAIapcN...XAlA
            # 发送邮箱账号
            mailAccount: mirson.ho@mail.mirson.cn
            # 短信模板编码
            smsTemplateCode: SMS_173342473
            # 短信签名名称
            smsSignName: 传智汇提醒
        ```
    *   **`AutoStockSenderConfiguration.java` 配置类**:
        ```java
        @Configuration
        @EnableAutoConfiguration
        public class AutoStockSenderConfiguration {
            @Value("${aliyun.sender.regionId}")
            private String regionId;
            @Value("${aliyun.sender.accessKey}")
            private String accessKey;
            // ... (后续代码用于创建并初始化 SmsSender 实例)
        }
        ```
    *   **`META-INF/spring.factories` 文件内容**:
        ```properties
        org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
        com.icast.bulls.stock.sender.AutoStockSenderConfiguration
        ```

---

### 4) 关键场景与演示描述

*   **场景一：阿里云控制台配置** (00:30 - 00:45)
    *   讲师在浏览器中打开阿里云短信服务管理后台。
    *   通过导航菜单进入“短信模板”管理页面。
    *   演示如何创建一个新模板，设置模板名称、模板CODE，并配置变量占位符（如 `$name`、`$time`、`$price`）。

*   **场景二：项目代码实现** (01:00 - 01:30)
    *   讲师在 IntelliJ IDEA 中打开项目，定位到 `SmsSender.java` 文件。
    *   详细讲解 `sendMessage` 方法中如何使用 `CommonRequest` 对象构造 HTTP 请求。
    *   展示如何通过 `putQueryParameter` 方法设置请求参数，如 `RegionId`、`PhoneNumbers`、`SignName` 和 `TemplateCode`。
    *   展示如何使用 `Map<String, String>` 对象传递模板变量。

*   **场景三：Spring Boot 配置** (01:45 - 02:30)
    *   讲师打开 `bootstrap-dev.yml` 文件，展示如何在配置文件中定义阿里云短信服务的配置项。
    *   讲师创建 `AutoStockSenderConfiguration` 配置类，并使用 `@Value` 注解将配置文件中的值注入到类的私有属性中。
    *   在配置类中编写 `@Bean` 方法，创建 `SmsSender` 实例，并将注入的配置信息传递给该实例。
    *   讲师在 `META-INF/spring.factories` 文件中添加配置类的全限定名，以便 Spring Boot 自动加载该配置。

---

以上是根据视频画面进行的结构化分析，旨在帮助理解课程内容和实现细节。
