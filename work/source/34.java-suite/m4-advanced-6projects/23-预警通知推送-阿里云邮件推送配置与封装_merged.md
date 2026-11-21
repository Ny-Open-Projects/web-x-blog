# 23-预警通知推送-阿里云邮件推送配置与封装 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面咱们开始学习阿里云邮件推送配置与集成封装使用

阿里云是国内最大的云服务提供商

它能够提供比较稳定可靠的短信和邮件推送服务

很多公司也介入阿里云去采用它的推送服务

在这里咱们来学习如何采用阿里云推送的服务

去实现预警通知的发送功能

阿里云的短信发送

它需要设定相应的模板

但是模板审核来讲

要求是非常严格的

需要相关的资质和证明

因为大家知道短信骚扰比较严重

所以运营商对这一块的监管是非常严格的

这里咱们就不能通过短信去发送具体的预警通知内容

但是咱们仍然会去讲解

如何去进行短信的集成和对接配置

掌握阿里云短信对接之后

大家将来如果在参加工作的时候

通过公司的名义

去申请短信

这样就比较容易

这里咱们可以采用阿里云的邮件发送

作为揭露的演示

在下面的章节

咱们会做相应的讲解和验证

因为阿里云邮件

它每天是可以免费发送200封

大家也可以自行去注册阿里云的免费账号

做实际的应用测试

阿里云对短信发送这块

就没有提供免费的额度

因为短信发送

运营商是要收取一定费用的费用

好

在这里咱们就来演示一下

如何去配置阿里云的邮件发送功能

咱们可以通过浏览器

登录阿里云的控制后台

通过左上角的导航

在产品和服务里面

选择邮件推送

在这里就可以进入阿里云邮件推送的管理后台

整个配置来讲比较简单

只需要做两个步骤

第一个步骤

去实现发信预备

第二个步骤

去配置相应的发信地址

好咱们首先看一下发信预名

这里我已经配置了一些预名

绿色是代表可用的

如果是在阿里云上面申请的预名

那么配置和验证起来就比较快

要配置新的预名点击新建预名

在这里输入相应的预名的名称

然后点击确定

如果是阿里云上面的预名

确定完成之后会显示出

会提示相应的授权

也就是在这里

会有一个提示界面

点击同意授权就可以

好咱们回到管理后台

发信预名配置完成之后

接下来就是配置发信地址

这个发信地址就是邮件显示的发信人

要配置一个新的发信地址

点击新建发信地址

然后在这里选择咱们上面所配置的发信预名

下面呢就输入相应的账号名字

名称

然后是发信类型的选择

可以是批量邮件也可以是触发邮件

这里的类型选择触发邮件就可以

如果需要批量发送可以选择批量邮件

好那咱们回到响应当中

阿里云的邮件后台配置就已经完成

接着的话呢可以在项目当中去集成阿里云的推送服务

咱们将依赖引入工程当中

回到工程代码

在buzztalk start的工程下面

找到生的模块

在POM文件下面咱们增加对应的依赖

让它导入生效

注意版本号不要配置错误

好接着回到讲义当中

下面咱们要去封装邮件发送服务的API接口

首先是定义一个抽象类阿里云生的

咱们将代码引入工程当中

将抽象类阿里云生的放到Base目录下面

6-6 java class

阿里云生的

将代码引入进来

咱们可以看到该抽象类提供了一些公用的信息

比如说区域

访问的key

授权密钥邮箱账号等等

这些是阿里云推送服务的必要配置信息

下面提供了一个初始化方法

初始化完成之后才能进行消息的推送

接下来咱们回到讲义当中

下面咱们去实现邮件发送的API

咱们放到工程当中来做讲解

在service包下面创建一个新的实现类

mail sender

将代码粘连进来

将错误进行修正

导入相应的依赖

好那咱们来看一下具体的实现

邮件发送的实现类

它继承了阿里云生的抽象类

实现了预警通知

发送的接口

预警通知发送有两个接口

一个是同步的方式去发送消息

另外一个是异步的方式去发送相应的消息

咱们来看一下如何去实现邮件的发送

这里定义了一个single sendmail request

单个邮件的请求发送对象

下面send result是记录发送的结果

这里是设置发件人的信息

Adjust type默认设置为1

下面是tag name

tag name是设置邮件的主题

然后是reply to address

这个设置响应

然后是发送人的邮件地址

这里的邮件地址可以给多个收件人去发送邮件

他们之间要采用逗号进行分开

但是如果是大批量的发送邮件

建议要将single sendmail request对象更换为batch sendmail request的对象

下面是设置邮件的主题

然后是设置邮件的内容

这个是支持html的格式

下面是通过阿里云的client进行邮件的发送

如果邮件发送失败

在这里就会跳到异常的处理

这里主要有两类异常

一类是服务端的异常

另外一类就是客户端的异常

这里会将相应的错误信息做一个记录

便于咱们的追踪和排查

好

这就是阿里云邮件推送功能的实现

那咱们回到讲习当中

这一讲咱们讲解了阿里云邮件推送的配置

以及在项目当中的集成和封装

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析：

---

### 1) 视频摘要

本视频课程主要讲解如何在 Java 项目中集成阿里云的邮件推送服务。讲师首先介绍了阿里云邮件服务的基本情况和免费额度，然后演示了如何在阿里云控制台配置发信域名。接着，课程重点转向了代码层面，指导观众如何在项目的 `pom.xml` 文件中添加阿里云通信 SDK 的依赖，定义抽象的邮件发送服务接口 `AliyunSender`，并实现具体的邮件发送类 `MailSender`。整个过程旨在为后续的在线预警通知功能提供一个可复用的邮件发送服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开始，讲师在 Typora 文档中展示本节内容“3.5 阿里云邮件推送配置与集成封装”，并介绍阿里云作为国内主流云服务商，其邮件服务是实现预警通知功能的演示载体。
*   **00:05 - 00:15**: 讲师在 Typora 中切换到“3. 阿里云推送服务集成”章节，开始讲解如何在项目中添加依赖。
*   **00:15 - 00:25**: 讲师切换到 IntelliJ IDEA，展示 `pom.xml` 文件，并在其中添加阿里云通信 SDK 的依赖项。
*   **00:25 - 00:35**: 讲师在 IDE 中展示 `AliyunSender` 抽象类的代码，定义了 `regionId` 和 `accessKey` 等核心属性。
*   **00:35 - 00:45**: 讲师展示 `AliyunSender` 类中的 `initClient()` 方法，用于初始化阿里云的 `IClientProfile` 和 `DefaultAcsClient` 客户端。
*   **00:45 - 00:55**: 讲师展示 `MailSender` 类的 `sendMessage()` 方法，演示如何构建 `SingleSendMailRequest` 对象并调用阿里云 API 发送邮件。
*   **00:55 - 01:05**: 讲师在 Typora 中切换到“5. 邮件发送实现类”章节，展示 `MailSender` 类的完整实现，它继承自 `AliyunSender` 并实现了 `IwarnNotifySender` 接口。
*   **01:05 - 01:15**: 讲师在 IDE 中展示 `MailSender` 类的 `sendSyncMessage()` 方法，该方法调用 `sendMessage()` 方法来发送邮件。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.5 阿里云邮件推送配置与集成封装”。
    *   **关键文字**: “阿里云是国内最大的云服务提供商，能提供比较稳定可靠的短信与邮件推送服务，较多公司都接入采用其服务。”
    *   **关键文字**: “阿里云邮件，每天可以免费发送200封，大家可以注册阿里云账号，作实际应用测试。”
    *   **章节列表**: 包含了从“3.1 定义接口数据结构”到“3.8 用户注册邮件通知功能实现”的完整目录。

*   **代码内容**:
    *   **Maven 依赖 (pom.xml)**:
        ```xml
        <!-- 阿里云通信组件依赖 -->
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.1.0</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-dm</artifactId>
            <version>3.1.0</version>
        </dependency>
        ```
    *   **抽象类 `AliyunSender`**:
        ```java
        @Data
        public abstract class AliyunSender {
            /**
             * 区域信息
             */
            private String regionId;
            /**
             * 访问key
             */
            private String accessKey;
            protected IClientProfile profile;
            public void initClient() {
                this.profile = DefaultProfile.getProfile(getRegionId(), getAccessKey(), getSecret());
                this.client = new DefaultAcsClient(profile);
            }
        }
        ```
    *   **实现类 `MailSender`**:
        ```java
        @Log4j2
        public class MailSender extends AliyunSender implements IwarnNotifySender {
            @Override
            public SenderResult sendSyncMessage(SenderMessage senderMessage) {
                return sendMessage(senderMessage);
            }
            @Override
            public async SenderResult sendMessage(SenderMessage senderMessage) {
                SingleSendMailRequest request = new SingleSendMailRequest();
                SenderResult result = new SenderResult();
                result.setId(senderMessage.getId());
                try {
                    request.setAccountName(getMailAccount());
                    request.setFromAlias("mirson.ho");
                    request.setAddressType(1);
                    request.setTagType(1);
                    request.setReplyToAddress(true);
                    request.setToAddress(senderMessage.getReceiver());
                    request.setSubject(senderMessage.getSubject());
                    request.setHtmlBody(senderMessage.getNotifyContent());
                    SingleSendMailResponse httpResponse = client.getAcsResponse(request);
                    result.setSendStatus(GlobalConstants.STATUS_OK);
                    return result;
                } catch (ServerException e) {
                    log.error("errorCode: " + e.getErrorCode() + ", errorMsg: " + e.getMessage(), e);
                    result.setSendStatus(GlobalConstants.STATUS_ERROR);
                    result.setMemo(e.getMessage());
                    return result;
                } catch (ClientException e) {
                    log.error("errorCode: " + e.getErrorCode() + ", errorMsg: " + e.getMessage(), e);
                    result.setSendStatus(GlobalConstants.STATUS_ERROR);
                    result.setMemo(e.getMessage());
                    return result;
                }
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：阿里云控制台配置** (00:05 - 00:15)
    *   讲师在浏览器中打开阿里云邮件推送控制台。
    *   在“发信地址”页面，点击“新建发信地址”按钮，演示如何创建一个新的发信地址，如 `mirson.ho@mirson.cn`。
    *   讲师强调了配置发信域名的重要性，并展示了阿里云邮件服务的免费额度。

*   **场景二：IDEA 中添加依赖** (00:15 - 00:25)
    *   讲师在 IntelliJ IDEA 中打开项目 `bulls-stock-starter-sender`。
    *   在 `pom.xml` 文件中，将阿里云通信 SDK 的依赖项添加到 `<dependencies>` 标签内。
    *   讲师特别指出，如果使用短信功能，需要使用 `aliyun-java-sdk-core` 的最新版本 4.1.0。

*   **场景三：定义抽象类** (00:25 - 00:35)
    *   讲师在 IDE 中创建并展示 `AliyunSender` 抽象类。
    *   该类定义了 `regionId` 和 `accessKey` 等属性，并包含 `initClient()` 方法，用于初始化阿里云客户端。

*   **场景四：实现邮件发送功能** (00:35 - 00:55)
    *   讲师在 IDE 中展示 `MailSender` 类的实现。
    *   该类继承自 `AliyunSender`，并实现了 `IwarnNotifySender` 接口。
    *   讲师演示了 `sendMessage()` 方法，该方法构建 `SingleSendMailRequest` 对象，设置收件人、主题、内容等参数，并调用阿里云 API 发送邮件。
    *   讲师还展示了异常处理逻辑，用于捕获并记录发送失败的错误信息。

*   **场景五：整合与测试** (00:55 - 01:05)
    *   讲师在 Typora 中展示 `MailSender` 类的完整实现。
    *   该类通过 `sendSyncMessage()` 方法调用 `sendMessage()` 方法，为后续的预警通知功能提供了邮件发送能力。

---
