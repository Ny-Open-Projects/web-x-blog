# 25-预警通知推送-调度服务增加阿里云发送功能 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们在调度服务里面

去增加阿里云的发送功能

这里咱们需要修改发送预警通知数据的接口

那回到工程当中

定位到相应的实现类

Account

Settingserviceimplement

首先咱们去注入短信和邮件的实现接口

Private

I want notify send

这个是短信服务

添加我的外的注解

接下来咱们再注入邮件服务接口

这个名称不要写错了

它会根据属性名称去注入相应的实现类

如果名称写错了是无法正常注入

接着咱们去修改预警通知的发送接口

在下面咱们去增加阿里云的发送功能

首先增加短信通知

制造判断处理

将类型修改为短信方式

将注释做个调整

阿里云短信通知

更改为短信的发送接口

接下来咱们再去增加邮件的发送

修改判断类型

改成email

发送方式改成mail sender

这里要注意一下通知呢

都是采用同步的方式进行发送

因为下面要进行消息的反写处理

如果采用异步的方式

如果消息发送失败

下面的更新呢还会正常执行

所以要采用同步方式发送

发送如果出现异常

下面代码就无法正常执行

好咱们回到讲义当中

这一讲咱们在调度服务里面

增加了阿里云的发送功能

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易预警通知系统的开发教学，重点讲解如何在服务层 `AccountWarnSettingServiceImpl` 中实现对不同通知类型的分发逻辑。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何根据通知类型（如邮件、短信、阿里云推送等）调用不同的发送器（`MailSender`, `SmsSender`, `WarnNotifySender`），并处理发送结果。核心内容是实现一个“策略模式”或“分发器模式”，将具体的发送逻辑解耦，便于后续扩展和维护。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频中的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: 课程概览与当前章节介绍。讲师在 Typora 文档中展示了本节标题“3.7 调度任务增加阿里云发送功能”，并介绍了本节目标：修改服务层以支持新的发送方式。
*   **00:05 - 00:15**: 展示项目结构。讲师在 IDEA 中展示了项目 `bulls-stock-starter-sender` 的完整目录结构，包括 `src/main/java` 下的各个服务实现类，如 `AccountWarnSettingServiceImpl`。
*   **00:15 - 00:30**: 定位并查看核心服务类。讲师将光标定位到 `AccountWarnSettingServiceImpl.java` 文件，并展示了其类成员变量，包括 `@Autowired` 注入的 `WarnNotifySender appSender`。
*   **00:30 - 00:45**: 展示核心方法 `sendWarnNotifyMessage`。讲师滚动到方法体，展示了其核心逻辑：获取通知列表，然后通过 `parallelStream().forEach` 并行处理每个通知。
*   **00:45 - 01:00**: 重点讲解条件分支。讲师聚焦于 `if` 语句块，解释如何根据 `notifyMessage.getNotifyType()` 的值来决定调用哪个发送器。
*   **01:00 - 01:15**: 演示添加阿里云短信发送逻辑。讲师在 `else if` 分支中添加了针对阿里云短信的判断条件 `ACCOUNT_WARN_NOTIFY_TYPE_SMS`，并调用 `smsSender.sendSyncMessage(...)`。
*   **01:15 - 01:30**: 演示添加阿里云邮件发送逻辑。讲师在 `else if` 分支中添加了针对阿里云邮件的判断条件 `ACCOUNT_WARN_NOTIFY_TYPE_EMAIL`，并调用 `mailSender.sendSyncMessage(...)`。
*   **01:30 - 01:45**: 演示添加阿里云推送通知逻辑。讲师在 `else` 分支中添加了针对阿里云推送的判断条件 `ACCOUNT_WARN_NOTIFY_TYPE_PUSH`，并调用 `appSender.sendSyncMessage(...)`。
*   **01:45 - 02:00**: 总结与收尾。讲师展示了最终的代码结构，强调了通过 `appSender` 实现了对不同通知类型的统一处理。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `3.7 调度任务增加阿里云发送功能`。
    *   **代码注释**: 代码中包含详细的中文注释，如 `// 发送预警通知数据`、`// 邮件通知类型`、`// 短信通知类型`、`// 站内通知`、`// 阿里云邮件通知`、`// 阿里云短信通知`、`// 阿里云推送通知`。
    *   **常量定义**: `GlobalConstants.ACCOUNT_WARN_NOTIFY_TYPE_EMAIL`、`GlobalConstants.ACCOUNT_WARN_NOTIFY_TYPE_SMS`、`GlobalConstants.ACCOUNT_WARN_NOTIFY_TYPE_PUSH`。

*   **代码关键内容**:
    *   **核心方法**: `public void sendWarnNotifyMessage()`
    *   **数据获取**: `List<AccountWarnNotifyMessage> accountWarnNotifyMessages = accountWarnNotifyMessageDao.get(...)`
    *   **并行处理**: `accountWarnNotifyMessages.parallelStream().forEach(...)`
    *   **发送逻辑**:
        ```java
        if (GlobalConstants.ACCOUNT_WARN_NOTIFY_TYPE_EMAIL.equals(notifyMessage.getNotifyType())) {
            result = mailSender.sendSyncMessage(getSenderMessage(notifyMessage));
        } else if (GlobalConstants.ACCOUNT_WARN_NOTIFY_TYPE_SMS.equals(notifyMessage.getNotifyType())) {
            result = smsSender.sendSyncMessage(getSenderMessage(notifyMessage));
        } else if (GlobalConstants.ACCOUNT_WARN_NOTIFY_TYPE_PUSH.equals(notifyMessage.getNotifyType())) {
            result = appSender.sendSyncMessage(getSenderMessage(notifyMessage));
        } else {
            log.warn("no support notify type, pls check!");
            notifyMessage.setMemo("no support type!");
        }
        ```
    *   **结果更新**: `accountWarnNotifyMessageDao.updateNotifyDataSendStatus(result);`

---

### 4) 关键场景与演示描述

*   **场景一：项目结构导航 (00:05-00:15)**
    *   **描述**: 讲师在 IDEA 中使用搜索功能，快速定位到 `AccountWarnSettingServiceImpl` 类。他通过滚动和缩放，向观众展示了项目中与通知相关的所有 Java 文件，强调了这是一个模块化的项目结构。

*   **场景二：核心方法逻辑演示 (00:30-01:00)**
    *   **描述**: 讲师将光标移动到 `sendWarnNotifyMessage` 方法的开始处，通过滚动和放大，向观众展示了方法的注释和整体结构。他重点讲解了 `parallelStream().forEach` 的作用，即并行处理通知列表，以提高发送效率。

*   **场景三：条件分支添加 (01:00-01:45)**
    *   **描述**: 讲师在 `if` 语句块中，依次添加了三个 `else if` 分支。他通过鼠标点击和键盘输入，演示了如何为每种通知类型（邮件、短信、推送）添加对应的判断条件和发送逻辑。他特别强调了 `appSender` 的作用，即它是一个通用的发送器，可以处理所有类型的通知。

*   **场景四：最终代码结构展示 (01:45-02:00)**
    *   **描述**: 讲师将光标移动到方法末尾，展示了最终的代码结构。他通过高亮和缩进，向观众展示了代码的清晰性和可读性。他总结道，通过这种方式，系统可以轻松地支持新的通知类型，而无需修改核心逻辑。

---

以上是根据视频画面进行的结构化分析。希望对您有所帮助。
