# 26-预警通知推送-用户注册邮件通知功能 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来这一讲咱们在用户注册功能里面增加邮件通知功能的实现

之前咱们讲解了实现了用户注册寄开户的功能

但当时由于没有实现阿里云的揭露

所以没有完成邮件发送功能

那现在已经实现

我们需要重新去增加注册邮件通知的功能

将下面的方法做一个copy

回到工程当中

定位到stock user service

这个是在用户服务下面

咱们在下面增加对应邮件发送的实现

这里需要引入发送服务组件

那咱们将调度任务里面的home依赖增加进去

把它放到stock user里面

加在最下面

让它导入生效

回到stock user service

接下来咱们还要

注入邮件发送的接口

private

没有sender

添加outwide注解

添加注释

这个是邮件发送的服务接口

咱们来看一下邮件发送方法的实现

这里组装了sender message

邮件发送的消息

设置了邮件主题

接收者的信息

这个ID采用当前服务的纳秒级别的时间

这个ID采用当前服务的纳秒级别的时间

作为唯一的标识

下面是邮件通知的具体内容

接下来就通过邮件发送接口

去实现邮件的内容发送

这里注意一下

它是采用异步方式进行的发送

这里增加了R3的注解

好咱们回到刚才的service

接下来咱们去用户注册接口

增加邮件功能的发送

在这里咱们添加相应的代码

调用sender

再来是邮件发送接口

这里我们可以看到

我们可以看到

email message方法

传递chad user.io

好这样就实现了

用户注册的时候增加邮件通知的发送

接下来咱们回到讲义当中

这里我们是采用异步的方式去发送邮件信息

需要增加现成词的配置

这里咱们将代码引入工程当中

在configure 下面

我们创建一个新的配置类

名称叫task

是qt

名称叫task

configuration

将配置类的代码引入进来

检查修正相应的错误

导入splint framework下面的包

导入executor

这个是在JDK下面的

好现成词的配置咱们之前已经做过讲解

这里就不再赘述

咱们再回到讲义当中

接下来要在工程配置文件里面

增加现成词以及阿里云的通信配置信息

将以下配置信息

做一个copy

回到工程当中

找到stock user用户服务的工程配置文件

在最下面增加相应的配置

好咱们来看一下

这一部分是现成词的配置信息

下面是阿里云的通信服务配置

这些都是必要的配置属性

好回到讲义当中

在这里咱们就完成了用户注册接口

邮件通知功能的实现

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“ bulls-stock-user ”的 Spring Boot 项目的技术实现课程。讲师正在讲解如何为用户注册功能增加邮件通知功能。核心内容包括：
- 在 `StockUserServiceImpl` 服务类中，实现一个 `sendEmailMessage` 方法，用于发送注册成功邮件。
- 使用 `SenderMessage` 对象构建邮件内容，包括主题、接收者邮箱、发送时间、邮件正文等。
- 通过 `mailSender.send(message)` 方法调用邮件发送服务。
- 课程还涉及了项目结构、配置文件（如 `bootstrap-dev.yml`）以及线程池配置（`TaskExecutorConfiguration`）等背景知识，为邮件通知功能的集成提供上下文。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的播放时间点，以下章节是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:05**: 课程引入，展示 PPT 页面，标题为“3.8 用户注册邮件通知功能实现”，并说明当前任务是为用户注册功能增加邮件通知。
- **00:05 - 00:15**: 展示项目结构，重点在 `StockUserServiceImpl.java` 文件，讲师准备在其中添加邮件发送功能。
- **00:15 - 00:30**: 在 `StockUserServiceImpl.java` 中编写 `sendEmailMessage` 方法，定义 `SenderMessage` 对象并设置其属性。
- **00:30 - 00:45**: 为 `sendEmailMessage` 方法添加注释，并设置邮件正文内容，包含用户名和邮箱。
- **00:45 - 00:55**: 调用 `mailSender.send(messages)` 发送邮件，并添加日志记录。
- **00:55 - 01:05**: 展示 `bootstrap-dev.yml` 配置文件，其中包含阿里云短信服务的配置信息（`smsTemplateCode` 和 `smsSignName`）。
- **01:05 - 01:15**: 展示 `TaskExecutorConfiguration.java` 文件，讲解线程池配置，包括核心线程数、最大线程数、队列容量等。
- **01:15 - 01:25**: 展示 `bootstrap-dev.yml` 文件中的线程池配置和阿里云通信服务配置，与 PPT 内容对应。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

- **PPT 内容**:
  - **标题**: “3.8 用户注册邮件通知功能实现”
  - **说明**: “之前我们讲解实现了用户即刻开户功能，当时并没有实现阿里云的邮件发送，现在已经实现，我们需要重新增加注册邮件通知功能。”
  - **代码示例**: 在 PPT 中展示了 `sendEmailMessage` 方法的伪代码，用于说明邮件发送的逻辑。

- **代码关键内容**:
  - **`StockUserServiceImpl.java` 中的 `sendEmailMessage` 方法**:
    ```java
    private void sendEmailMessage(TradeUserVo tradeUser) {
        SenderMessage messages = new SenderMessage();
        messages.setSubject("智牛股注册成功通知");
        messages.setReceiver(tradeUser.getEmail());
        messages.setId(System.nanoTime());
        messages.setUpdateTime(new Date());
        messages.setNotifyContent("您的帐号注册成功！用户名：" + tradeUser.getName() + "，帐号：" + tradeUser.getEmail());
        Log.info("send regist email: " + messages);
        mailSender.sendMessage(messages);
    }
    ```
  - **`bootstrap-dev.yml` 配置文件**:
    ```yaml
    # 线程池配置
    task:
      executor:
        corePoolSize: 5
        maxPoolSize: 10
        queueCapacity: 500
        keepAliveSeconds: 60

    # 阿里云通信服务配置
    aliyun:
      sender:
        regionId: cn-hangzhou
        accessKey: LTAIapcNcBUBR8w
        secret: LzgImYlRVuE4OkjQ6eemdeXAlA
        mailAccount: mirson.ho@mail.mirson.cn
        smsTemplateCode: SMS_17334273
        smsSignName: 传智汇提
    ```

- **图表/配置文件**:
  - **项目结构图**: 展示了 `bulls-stock-user` 项目在 IntelliJ IDEA 中的目录结构，包括 `src/main/java`、`src/main/resources` 等。
  - **配置文件**: `bootstrap-dev.yml` 文件，用于配置线程池和阿里云通信服务。

---

### 4) 关键场景与演示描述

- **场景一：邮件通知功能实现**
  - 讲师在 `StockUserServiceImpl.java` 文件中，编写 `sendEmailMessage` 方法。
  - 通过 `SenderMessage` 对象设置邮件主题、接收者、发送时间、正文内容。
  - 调用 `mailSender.sendMessage(messages)` 发送邮件，并添加日志记录。

- **场景二：配置文件管理**
  - 讲师展示 `bootstrap-dev.yml` 文件，其中包含线程池配置和阿里云通信服务配置。
  - 重点讲解 `task.executor` 和 `aliyun.sender` 的配置项，如核心线程数、最大线程数、队列容量、阿里云的 `accessKey`、`secret`、`mailAccount` 等。

- **场景三：线程池配置**
  - 讲师展示 `TaskExecutorConfiguration.java` 文件，讲解线程池的配置。
  - 通过 `@Value` 注解注入配置值，并使用 `ThreadPoolTaskExecutor` 创建线程池。
  - 设置线程池的核心线程数、最大线程数、队列容量、保持时间等参数。

- **场景四：项目结构与依赖管理**
  - 讲师展示项目结构，包括 `src/main/java`、`src/main/resources` 等目录。
  - 通过 `pom.xml` 文件管理项目依赖，如 `spring-boot-starter-mail`、`aliyun-java-sdk-sms` 等。

- **场景五：代码调试与测试**
  - 讲师在 `StockUserServiceImpl.java` 中调用 `sendEmailMessage` 方法，并返回新创建的用户对象。
  - 通过 `Log.info` 记录日志，用于调试和测试邮件发送功能。

---

以上是根据视频画面进行的结构化技术课程分析。
