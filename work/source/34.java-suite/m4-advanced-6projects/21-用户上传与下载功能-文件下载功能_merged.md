# 21-用户上传与下载功能-文件下载功能 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接下来呢

咱们去实现文件的下载功能

这样呢

咱们也就实现了用户资料的上传和下载的完整功能

那我们来看一下文件下载呢

具体要去怎么实现呢

首先我们DO数据层呢

要增加对应的接口

然后service层呢

要封装一个根据文件ID查找文件对象的接口

拿到这个文件对象之后呢

controller层就能将文件输出给客户端

完成了文件的下载

这里要注意一下呢

为了便于演示

request mapping当中呢

是增加了get方法的支持

之前呢

我们上传只支持post

这样呢

咱们在浏览机当中就能便于测试和验证

然后呢

我们在参数当中做了一个not blank的自动化教验

需要去增加呢

约束性异常的检查

要检查呢

这个头部

它是否有validate这个注解

这样呢

not blank

它才能够生效

最后呢

再来检查拦截器当中

对约束性异常的处理

之前呢

咱们做了对应的实现

对不对

好

这个呢

就是文件下载的整体实现流程

那咱们呢

就来从代码上做个具体实现

首先呢

是要在数据层当中去实现一个

根据文件ID获取用户对象的接口

这个呢

咱们检查一下

在iChat user file

DUO当中

我们查询一下

这个呢

已经做了实现

对不对

好

拿到

用户文件对象之后呢

就要在service层当中呢

去实现文件的获取

那么我们再stock user file

service当中呢

给它做一个实现

这个呢

比较简单

咱们呢

就将代码直接扩比过来

好

这个呢

就是根据文件ID

然后获取文件对象

我们把它呢

抽象到接口当中

probe members

好

再往下面呢

就是control层的实现

control层呢

我们就来做

一个代码的编写

那么呢

先copy下

方法的头部信息

在咱们的

control层结果当中

lock user control

放在最下面

好

在这里呢

我们是加了一个教验

对不对

这个是约束性的检查

我们将它导入进来

那我们注意了

既然你要采用约束性检查

最上面呢

一定要加validata的注解

好

那么我们可以看到

它传递的参数呢

是file ID

它所支持的

请求类型呢

既可以支持get

又可以支持post

那咱们呢

就对文件下载

做个具体实现

我们要定一个呢

文件的输出流

output stream

这个就叫os

默认为no

然后呢

再给它定一个文件的缓冲数据流

buffed input stream

BAS

默认值呢

也为no

这个呢

是文件缓冲数据流

那我们来看一下

如何去实现它的

下载处理呢

最后呢

我们要加一个cache异常的补货

copy一下

这个呢

是组件的异常

我们的一个session

我们将它的日子呢

错误日子输出

get message

然后呢

做个封装处理

API

respond result

get add code

将add code呢

传递进去

打回对象呢

我们在上面定义一下

统一打回对象

API

respond result

这个呢

默认为no

再回到呢

刚才的异常处理

这里面呢

我们也将错误异常的打印出来

然后呢

给它一个封装

打印用csl的方法

将错误信息呢

打回出去

最后呢

不要忘记了

要关闭文件流

关闭文件流

以免这个句柄产生泄露

先要判断它是否会通

如果是不允许呢

就进行关闭处理

这里也加上异常的补货

将错误日子呢

通过日子输出

那我们就来看一下具体该怎么去实现

我们整理下它的实现步骤

首先第一步呢

要去获取

attp

server letter

response

输出返回对象

它会将数据呢

输出给客户端

那么呢

我们可以

从代码当中直接将它拨比到这里

这个呢

就是response对象的获取

它呢

是从request contact上些文章中呢

获取

而且buse

然后呢

再去获取具体的response对象

好

拿到response对象之后呢

我们再来看一下

要去呢

获取用户的文件信息

咱们再写下下面的步骤

第三个步骤呢

咱们就要从save服务器上面呢

去获取文件流

之前呢咱们save服的呢

工庄的对应的接口

那么第四个步骤呢

要去设置文件的输出类型

你到底返回给客户端的是一个zip文件

还是说text还是图片对不对

这个时候呢

我们要给他context type的设置

有问题

好

接着的话呢

就要去设置呢

文件下载的名称

最后呢

就是输出文件流完成了整个系列

最后呢

就是输出文件流完成了整个系列

最后呢

就是输出文件流完成了整个系列

完成下载处理

这个就是整体步骤

那么我们呢

注意做实现

share user file

从stock user file service上中呢

去获取文件对象

传进了file id

下面呢

就是获取他的imput stream

这个通过save的接口来获取

接口呢

我们将他注入进来

加上注解

这个时候呢

咱们就可以通过

save的接口来获取

来获取imput stream

传递的是file id

文件id标识

接着的话呢

咱们从数据文件类型来做一个判断

如果这个文件类型他为空呢

就是未知的文件类型

那么我们就让他强行下载

怎么去实现强行下载呢

我们给他一个固定的标识

叫application

pause download

这样呢

他就能够实现强行下载

就是防止浏览器直接打开

长置

下载

文件

好

那如果是故意空呢

我们就将他原来的类型呢

返回给客户端

shade

use file

接到file type

接下来呢

咱们就设置本件的下载名称

sponse

add header

通过context

dispotion

他的值呢

就是attach

attachment

file name

这点我们拼接一下

shade user

这个file

这个filename

将他的文件名称呢

设置进来

再往下面呢

就来实现他

文件的输出流处理

定义一个byte直接输出

长度呢

1024

然后呢

我们将他

设置下

es

创建一个buffer的stream

buffer input stream

将imput stream包装一下

os呢

从response当中来获取

getoutput stream

getoutput stream

这个话呢

我们给他一个

i变量

这个是读取呢

他当前的

长度

也就是说

将这个

将imput stream里面的内容呢

读取到buffer的直接输出当中

这个imput stream呢

就是咱们从save服务器当中

获取的文件流

我们要做一个循环处理

如果i不等于-1呢

说明他仍然存有数据

那么将这个数据呢

输出给buffer

然后呢

0到i

i呢

就要等于bs.read

bufferbuffer

这个意思呢

就是通过咱们的response

output stream的对象呢

将字节输入当中

读取的内容呢

输出给客户端

那么输出完成之后呢

又要重新进行一次读取

这样的话呢

i的值就会产生变化

直到呢

i等于-1的情况

那么整个文件流呢

就读取输出完成

最后呢

不要忘了

将这个输出流呢

brush清空刷新下

因为咱们是实现了文件下载

这里呢不需要任何跳转

也不需要渲染任何页面

直接返回到

这个呢

就是对文件下载的功能流程处理

这里我们可以看到有个异常对不对

是因为呢

我们没有couple to compare的

组件异常

我们在这个service当中呢

加上对应的处理

这里要加一个交易判断

就是你必须要呢

能够找到对应的文件信息

对不对

如果文件信息都没找到呢

那接下来这些逻辑

文件的下载呢

就没法处理

这个user file

我们做一个微风判断

if now等于

缺的user file

我们就给它抛出一个异常

给它一个错误码

就是说用户文件呢

没有找到

然后呢

Shared user file

这个呢

我们讲异常抛出来

Service confirmed exception

抛出完成之后呢

将接口给它做个修改

好

这样来就没有报错了

咱们再回到Ctrl的层当中

我们加上去

Return result

这个呢

就是对用户文件下载的

整体功能的处理

我们在把注射加上

根据文件ID

去下载用户文件信息

最后咱们再从讲义当中

做个梳理和回复

这个约束性异常

已经做了实现

这里就不再追溯

咱们来看一下

整个的流程

通过service方法

获取到用户的文件信息

如果是没有找到

就会抛出对应的异常

然后根据文件ID

我们会从save服务器当中

去获取对应的文件流

然后输出给客户端

不用再通过临时文件方式进行输出

来提升它的处理效率

这也就是说

咱们为什么在save当中

去封装了一个文件流的方法

对不对

好

然后我们要去设置

它的响应类型

以及文件名称

便于浏览器和客户端

去正确识别处理

通过流式的缓冲下载处理

如果网络带宽

服务器内存配置比较高

可以将缓存适当的扩大

我们这里设置的是多少呢

是1024

对不对

那么可以根据自己的需要

适当调大一点

当然的话

也并不是说调得越大越好

适当的话

一般配置个4K左右就可以了

最后不要忘记去关闭流式操作对象

所以流式操作

都要养成一个良好的操作习惯

使用完毕之后

要及时释放对应的资源

不关闭流

会产生什么样的问题呢

它不会导致内存泄露

但是它会产生系统资源的泄露

也就是File Descript FD文件描述

虽然

Findalize这个方法

有调用Close来释放FD

但是执行的时间点

是存在不确定性的

这点大家要注意一下

因为它存在不确定性

对不对

我并不知道

它是不是有周期

有规律的进行回收

那么在高并发的场景下面

是极容易出现问题了

可能的话

你一瞬间

很多流量请求都过来了

那么导致你的内存压力过大

就会导致整个服务资源耗尽

甚至可能产生崩溃的现象

好

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个 Spring Boot 项目中“用户资料上传与下载功能”的实现教程，具体聚焦于**文件下载功能**的开发与验证。讲师通过在 IntelliJ IDEA 中演示代码，讲解了如何在 Controller 层实现文件下载接口，如何在 Service 层通过文件 ID 获取文件对象，并最终从 Ceph 分布式存储系统直接读取文件内容并响应给客户端。视频还强调了关键的编程实践，如使用 `BufferedInputStream` 和 `HttpServletResponse` 进行流式传输，并提醒开发者务必关闭流以避免系统资源泄露（file descriptor）。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，讲师在 Typora 文档中定位到“3.7 文件下载功能”章节，介绍本节目标是实现根据文件 ID 下载文件的功能。
*   **00:00:05 - 00:00:15**：讲师展示 `ITradeUserFileDao` 接口的代码，定义了根据 `fileId` 获取 `TradeUserFile` 对象的方法。
*   **00:00:15 - 00:00:25**：讲师切换到 IntelliJ IDEA，展示 `StockUserFileServiceImpl` 类中 `getTradeUserFile` 方法的实现，该方法通过 DAO 层获取文件对象。
*   **00:00:25 - 00:00:35**：讲师在 `StockUserController` 中编写 `@RequestMapping` 注解的 `downloadFile` 方法，用于处理下载请求。
*   **00:00:35 - 00:00:45**：讲师在 `downloadFile` 方法中创建 `HttpServletResponse` 对象，并初始化 `BufferedInputStream`。
*   **00:00:45 - 00:00:55**：讲师演示如何设置响应头，包括 `Content-Type` 和 `Content-Disposition`，以便浏览器正确识别和处理文件。
*   **00:00:55 - 00:01:05**：讲师展示如何从 Ceph 获取文件字节流，并使用 `response.getOutputStream()` 将字节流写入响应体。
*   **00:01:05 - 00:01:15**：讲师强调了关闭流的重要性，并指出不关闭流会导致系统资源泄露（file descriptor），虽然 `finalize` 方法会调用 `close`，但在高并发场景下执行时间不确定，极易出问题。
*   **00:01:15 - 00:01:25**：讲师切换回 Typora 文档，进入“3.8 文件下载功能验证”章节，准备进行功能测试。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文档内容**：
    *   **章节标题**：`3.7 文件下载功能`，`3.8 文件下载功能验证`。
    *   **关键要点**：
        1.  通过 Service 方法获取用户文件信息，如果未找到，抛出异常。
        2.  根据文件 ID，从 Ceph 服务器获取文件流，直接输出至客户端，提升处理效率，上百兆的大文件不要采用此方式。
        3.  设置响应类型与文件名称，便于浏览器及客户端正确识别处理。
        4.  通过流式缓冲下载处理，如果网络带宽高，服务器内配置比较高，可以将缓冲扩大。
        5.  最后，不要忘记关闭流操作对象，所有流式操作，都要养成良好操作习惯，使用完毕及时释放资源。
        6.  不关闭流不会产生内存泄露，但会产生系统资源泄露（file descriptor）；虽然 `finalize` 方法有调用 `close` 来释放 fd，但是执行时间点是存在不确定性的，在高并发场景下，极易出现问题。

*   **代码关键内容**：

    *   **DAO 层接口 (`ITradeUserFileDao`)**：
        ```java
        /**
         * 根据文件ID获取对象
         * @param userId
         * @param bizType
         * @return
         */
        TradeUserFile getByFileId(@Param("fileId") Long fileId);
        ```

    *   **Service 层实现 (`StockUserFileServiceImpl`)**：
        ```java
        @Override
        public TradeUserFile getTradeUserFile(String fileId) {
            TradeUserFile tradeUserFile = tradeUserFileDao.getByFileId(Long.valueOf(fileId));
            if (null == tradeUserFile) {
                throw new RuntimeException("文件不存在");
            }
            return tradeUserFile;
        }
        ```

    *   **Controller 层实现 (`StockUserController`)**：
        ```java
        @RequestMapping(value = "/downloadFile", method = {RequestMethod.GET, RequestMethod.POST})
        public ApiRespResult downloadFile(@NotBlank(message = "文件ID不能为空！") String filed) {
            HttpServletResponse response = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes().getResponse();
            // 1. 获取文件对象
            TradeUserFile tradeUserFile = stockUserFileService.getTradeUserFile(filed);
            // 2. 设置响应头
            response.setContentType(tradeUserFile.getFileType());
            response.addHeader("Content-Disposition", "attachment;filename=" + tradeUserFile.getFileName());
            // 3. 从 Ceph 获取文件流
            InputStream inputStream = tradeUserFile.getInputStream();
            // 4. 创建缓冲流
            BufferedInputStream bis = new BufferedInputStream(inputStream);
            // 5. 写入响应体
            OutputStream outputStream = response.getOutputStream();
            byte[] buffer = new byte[1024];
            int length;
            while ((length = bis.read(buffer)) != -1) {
                outputStream.write(buffer, 0, length);
            }
            // 6. 关闭流
            bis.close();
            outputStream.close();
            return ApiRespResult.success();
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：功能流程设计** (00:00:00-00:00:15)
    *   讲师在 Typora 文档中导航至“3.7 文件下载功能”章节，明确本节目标。
    *   展示了 `ITradeUserFileDao` 接口的代码，说明了数据访问层需要提供根据文件 ID 查询文件对象的方法。

*   **场景二：Service 层实现** (00:00:15-00:00:35)
    *   讲师在 IntelliJ IDEA 中打开 `StockUserFileServiceImpl` 类。
    *   通过 `tradeUserFileDao.getByFileId(Long.valueOf(fileId))` 方法获取文件对象。
    *   使用 `if (null == tradeUserFile)` 判断文件是否存在，若不存在则抛出异常。

*   **场景三：Controller 层实现** (00:00:35-00:01:15)
    *   讲师在 `StockUserController` 中编写 `downloadFile` 方法。
    *   通过 `@RequestMapping` 注解定义了下载接口的路径和方法。
    *   使用 `HttpServletResponse` 对象设置响应头，包括 `Content-Type` 和 `Content-Disposition`。
    *   通过 `BufferedInputStream` 和 `OutputStream` 实现文件流的读取和写入。
    *   在代码中添加了 `bis.close()` 和 `outputStream.close()` 语句，演示了关闭流的操作。

*   **场景四：关键知识点强调** (00:01:15-00:01:25)
    *   讲师切换回 Typora 文档，进入“3.8 文件下载功能验证”章节。
    *   重点强调了流式操作中关闭流的重要性，以及不关闭流会导致系统资源泄露（file descriptor）的问题。
    *   提醒观众在高并发场景下，`finalize` 方法的不确定性可能导致资源泄露，因此必须显式关闭流。
