# 22-文件服务课程-文件服务开发（文件处理策略 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好

那么刚才呢

咱们这个文件上传这个方法

前面这段都已经写完了

还差最后这一点

最后这一点要完成的是什么呢

就是需要把我们这个文件对象

它的一些属性

比如说URL地址

对吧

还有filename

还有这个绝对的磁盘路径

把这些属性给它设置好

用于什么呢

保存到数据库

这个前面咱们都已经说过了

所以接下来我们要做的呢

就是需要来设置这三个属性

那么设置哪个file对象呢

你看咱们这个地方

其实已经传进来了

是谁传给它的呢

咱们来捋一下这个思路啊

其实是在我们这个抽象类里边

对不对

抽象类里边

我们是不是有一个upload方法

然后咱们在这个地方

是不是构造了一个file对象

然后呢

接下来在这个地方

是不是调用upload

upload file这个方法

然后呢

把这个file对象

是不是给我们传进去

给我们传进去

所以最终呢

它就upload file呢

这样的话就找到了我们

这个方法对不对

这是我们具体的

这个实现的方法

然后在这个地方

所以它把这个file

已经给我们传进来了

那么我们要做的就是什么呢

在这来file.set

分别set这三个

一个是url

对吧

具体什么值

一会我们再去说

然后呢

还有一个set什么呢

filename

文件名

然后还有一个什么

file.set

这个relative path

对吧

这三个

但是现在这个filename呢

这个比较好说

filename我们是不是

都已经生成了

前面已经生成了

所以直接设置进去就可以

好

然后呢

这个磁盘的这个绝对路径呢

这个呢

也比较简单

对吧

relative path

这个的话

我们前面是不是都已经

有了

好

所以说把这个

给它设置好

然后呢

剩下的就是这个什么呢

url地址

对吧

那么这个url地址的话呢

就需要我们去拼一下了

咱们可以先来看一下

最终拼成的

应该是一个什么样的效果

啊

那么这个url地址呢

它其实是一个http的访问地址

也就是http

然后后边是什么呢

可能是ip地址

然后呢

再后是不是端口号

然后再往后呢

再往后的话呢

对应的就是我们的这个

具体的这个路径了

比如说是

2020对吧

然后呢

杠什么呢

05

然后杠

叉叉叉点什么呢

这个doc

好

大概是这么一个路径

好

大概是这么一个路径

所以说呢

我们现在呢

就需要把这一段呢

给它拼起来

但是这段拼的话呢

我们其实都是可以获取到的啊

比如说前面这一段

实际上是什么呢

是我们在这个配置文件里面

配置的这个

local下边是不是有一个叫做

uri prefix

对吧

其实对应的就是这一段

对应的就是这一段

所以说呢

我们前面这一段就有了

然后呢

再往后呢

再往后其实还有一层啊

我刚才其实少写了一层

应该是什么呢

应该是我们这个bucket name

对吧

对应的应该是这么一个目录

好

所以这个框架的话呢

我们是不是也能获得

就是从我们这个配置文件

这个地方来获取

从这个地方来获取

这样的话呢

我假设获取到的就是它

然后再往后呢

是不是就是我们这个日期目录

日期目录呢

我们也知道

前面是不是已经生成了

对吧

已经生成了

就是这个相对路径

然后呢

动态的给它拼接进来就可以

再往后呢

再往后呢

是不是就是我们产生的这个这个

UID产生的这个动态的文件名

对不对

唯一的文件名

所以最终呢

我们这个URL地址啊

应该就是这么一个构成

类似于这样的一个构成

好

只不过这个地方呢

我们需要一点一点去拼去啊

那么对于这种细节呢

我们也就不再去课上去拼了

咱们直接从我们讲义上考过来

大家可以看到

就是为了这个设置

我们这个URL地址呢

我们写了这么一大堆代码

咱们可以看到

我们可以来看一下

好

你看

这个都是怎么怎么做到的呢

首先是new一个string builder

是不是进行字符串的一个拼接

对吧

字符串的一个拼接

首先呢

先取的是get UI prefix

而这个方法是在哪呢

其实是在我们这个附类里边

咱们可以按着control点进来

大家可以看到

在这个地方

而它取的是什么呢

它取的其实就是properties.get UI prefix

是不是对应的

就是我刚才提到的

这段

对吧

按照这个属性值来取

最终取到的应该就是这段

好

当然了

我们这个地方呢

是做了一个判断

对吧

如果它不为空就取它

如果它为空的话呢

就取这个

那么对于咱们当前这个配置

咱们肯定作为local的时候呢

一定要配置这个

所以说呢

它肯定取到的就是这个潜坠了

好

那么这就这段就搞定了

然后接下来又append的

是不是追加

追加一个什么呢

这其实是一个斜线啊

追加的是我们这个

就是这么一个斜线

这是在这个工具类里面

给我们定义的一个常量

你看吧

它其实就是一个斜线

好

然后呢

再往后拼是不是就是我提到的这一段

而这一段的话呢

就是我们这个bucket name

所以我们通过properties.get bucket name

就可以得到配置文件里面

配置的这个值了

然后再往后是不是又是斜线

所以又来个斜线

然后再往后呢

是不是就是我们日期目录

日期目录就是这一段

好

然后呢

我们再往后拼

拼完日期目录之后呢

再来一个斜线对吧

最后呢

再把我们这个文件名拼上

最后to3

所以这个写起来呢

确实是比较繁琐

整体来说呢

就是有这么多字符串拼接到一块

形成了一个完整的URL地址

大家可以看到我们这个URL地址呢

拼完之后呢

又做了一个replace对吧

就是防止什么呢

防止主要就是防止我们这个日期目录这一块呢

因为不同的操作系统呢

它可能这个斜线取得不对对吧

为了以防万一

所以说呢

我们在这个地方呢

统一啊都给它

如果有这种反斜线的情况呢

统一都给它改成正斜线

因为我们线外啊

这是URL地址

注意这不是磁盘路径对不对

URL代表的是我们的这个访问地址

它一定都是这种正斜线

所以说如果说这个路径里面存在反斜线

我们需要给它正过来对吧

那么通过replace呢

给它替换一下就可以了

保证我们最终呢

拼成的是一个合法的URL地址

好

那么拼完了之后呢

咱们把这个URL给它复给它

就可以了

好

那么最终呢

我们是不是就可以把这个file来

返回一下了

好

实际上这个地方呢

我们其实当前这个方法啊

你看我们现在定义的是

返回一个file对象对吧

其实呢

不返回也是可以的

因为我们传进来这个参数呢

传进来之后呢

咱们直接改它就可以了

然后在上一层它的这个负类

也就是抽象类里面呢

其实直接

就可以使用它了

你看它在这是不是直接返回这个file了

所以说为了跟咱们的讲义保持一致啊

因为我们讲义上呢

并没有去使用返回值

好

所以说我们在这个地方呢

也跟讲义保持一致

改成void

当然你直接改这一个地方肯定不够

还需要什么呢

在我们这个抽象类里面

咱们定义的抽象方法

在这改成void

好

这样的话呢

我们就不需要这个返回值了

好

你看这边也就没有问题了

那么我们直接啊

改这个file

然后呢给它设置值

这个return呢就不需要了

好

那么到这儿的话呢

咱们整个这个service里边

也就是我们这个local service impr里边

咱们这个文件上传的这个方法呢

就已经搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频课程聚焦于一个基于 Spring Boot 的文件服务开发项目，核心内容是实现一个本地文件存储策略（`LocalFileStrategy`）。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何构建一个抽象的文件上传接口 `AbstractFileStrategy`，并实现其具体的本地存储子类 `LocalServiceImpl`。课程详细讲解了文件上传的核心逻辑，包括：生成唯一文件名、构建目标文件路径、将文件字节写入磁盘、以及为文件对象设置 URL 和相对路径等元数据，以便后续在业务层或前端使用。同时，视频也展示了如何通过 Nacos 配置中心管理文件服务的存储路径和端点等配置，以及如何处理文件上传失败的异常情况。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供明确的时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:30**：课程开场与项目背景介绍。讲师展示了项目结构和核心模块，包括 `AbstractFileStrategy` 接口和 `LocalServiceImpl` 实现类。
*   **00:30 - 01:00**：讲解 `LocalServiceImpl` 类中的 `upload` 方法。重点演示了如何获取原始文件名、校验文件后缀、创建 `File` 对象并设置其属性。
*   **01:00 - 01:30**：深入讲解文件路径的构建逻辑。讲师展示了如何使用 `Paths.get()` 和 `DateTimeFormatter` 来生成目标文件的绝对路径和相对路径。
*   **01:30 - 02:00**：演示文件写入磁盘的过程。讲师使用 `FileUtils.writeByteArrayToFile` 方法将上传的文件字节写入到指定的 `File` 对象中。
*   **02:00 - 02:30**：讲解文件元数据的设置。讲师演示了如何使用 `file.setUrl()`、`file.setFilename()` 和 `file.setRelativePath()` 方法，为文件对象设置 URL、文件名和相对路径。
*   **02:30 - 03:00**：处理 Windows 环境下的路径分隔符问题。讲师使用 `StrUtil.replace` 方法将 `\` 替换为 `/`，以确保 URL 的兼容性。
*   **03:00 - 03:30**：讲解文件上传失败的异常处理。讲师展示了如何在 `try-catch` 块中捕获异常并抛出自定义的 `BizException`。
*   **03:30 - 04:00**：演示文件删除功能。讲师展示了 `delete` 方法的实现，该方法接收一个 `FileDeleteDO` 对象作为参数。
*   **04:00 - 04:30**：讲解 `AbstractFileStrategy` 接口的抽象方法 `uploadFile`。讲师说明了该方法的签名和用途。
*   **04:30 - 05:00**：讲解 `LocalServiceImpl` 中的 `uploadFile` 方法。讲师展示了如何通过 `properties` 对象获取配置信息，并调用 `buildClient()` 方法。
*   **05:00 - 05:30**：讲解 `buildClient()` 方法。讲师展示了如何从 `FileServerProperties` 中获取端点、存储桶名称和 URI 前缀等配置。
*   **05:30 - 06:00**：课程总结。讲师回顾了本地文件存储策略的核心实现，并强调了配置管理的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **文件服务开发结构图**：展示了项目目录结构，包括 `AbstractFileStrategy`、`LocalServiceImpl`、`FastDfsServiceImpl`、`AliServiceImpl` 等模块。
    *   **文件上传核心逻辑**：在 PPT 中列出了文件上传的关键步骤，包括生成文件名、构建路径、写入文件、设置元数据。
    *   **Nacos 配置详情**：展示了 `pd-file-server.yml` 配置文件的内容，其中包含了 `file` 配置块，定义了存储类型、端点、存储路径等。

*   **代码关键内容**：

    *   **文件上传方法 `upload` (在 `LocalServiceImpl` 中)**：
        ```java
        @Override
        public File upload(MultipartFile multipartFile) {
            try {
                // 获取上传文件的原始文件名
                String originalFilename = multipartFile.getOriginalFilename();
                if (originalFilename.contains(FILE_SPLIT)) {
                    throw BizException.wrap(ExceptionCode.BASE_VALID_PARAM, "上传文件名称缺少后缀");
                }

                // 封装一个File对象
                File file = File.builder()
                    .isDelete(false) // 文件是否被删除
                    .size(multipartFile.getSize()) // 文件大小
                    .contextType(multipartFile.getContentType()) // 文件类型
                    .dataTuna(FileDataTunaUtil.getTuna(multipartFile.getContentType())) // 数据类型
                    .build();

                // 构建目标文件路径
                String absolutePath = Paths.get(endpoint, bucketName, relativePath).toString();
                java.io.File outFile = new java.io.File(Paths.get(absolutePath, fileName).toString());

                // 向目标文件写入数据
                FileUtils.writeByteArrayToFile(outFile, multipartFile.getBytes());

                // 设置文件对象的属性
                file.setUrl(url); // URL
                file.setFilename(fileName); // 文件名
                file.setRelativePath(relativePath); // 相对路径

                return file;
            } catch (Exception e) {
                log.error("e = {}", e);
                throw BizException.wrap(ExceptionCode.BASE_VALID_PARAM, "文件上传失败");
            }
        }
        ```

    *   **文件路径构建逻辑**：
        ```java
        String url = new StringBuilder(getUriPrefix())
            .append(StrPool.SLASH)
            .append(properties.getBucketName())
            .append(StrPool.SLASH)
            .append(relativePath)
            .append(StrPool.SLASH)
            .append(fileName)
            .toString();
        ```

    *   **Windows 路径分隔符处理**：
        ```java
        url = StrUtil.replace(url, searchStr: "\\", StrPool.SLASH);
        url = StrUtil.replace(url, searchStr: "\\", StrPool.SLASH);
        ```

    *   **Nacos 配置文件 (`pd-file-server.yml`) 关键内容**：
        ```yaml
        file:
          type: FAST_DFS # LOCAL_ALL_MINIO_FAST_DFS
          uriPrefix: http://172.17.115.8188 # 存储类型为FAST_DFS时使用
          bucket-name: oss-file-service
          endpoint: D:/uploadFiles
        ```

    *   **抽象接口 `AbstractFileStrategy`**：
        ```java
        public abstract File uploadFile(File file, MultipartFile multipartFile) throws Exception;
        ```

---

### 4) 关键场景与演示描述

*   **场景一：文件上传核心逻辑演示 (00:30 - 02:30)**：
    讲师在 IntelliJ IDEA 中逐步演示了 `LocalServiceImpl` 的 `upload` 方法。他首先获取了上传文件的原始名称并进行后缀校验，然后创建了一个 `File` 对象并设置了其基本属性。接着，他通过 `Paths.get()` 方法构建了目标文件的绝对路径，并使用 `FileUtils.writeByteArrayToFile` 将文件字节写入磁盘。最后，他调用 `file.setUrl()`、`file.setFilename()` 和 `file.setRelativePath()` 方法，为文件对象设置了 URL、文件名和相对路径，以便后续使用。

*   **场景二：Windows 路径分隔符处理演示 (02:30 - 03:00)**：
    讲师在代码中展示了如何处理 Windows 环境下的路径分隔符问题。他使用 `StrUtil.replace` 方法，将 URL 中的反斜杠 `\` 替换为正斜杠 `/`，以确保 URL 在不同操作系统下的兼容性。他强调了这一处理步骤的重要性，以避免因路径分隔符不一致而导致的 URL 错误。

*   **场景三：Nacos 配置中心演示 (03:00 - 03:30)**：
    讲师切换到 Nacos 配置管理界面，展示了 `pd-file-server.yml` 配置文件的内容。他重点讲解了 `file` 配置块中的 `type`、`uriPrefix`、`bucket-name` 和 `endpoint` 等关键属性。他解释了这些配置如何影响文件服务的存储策略和访问路径，并强调了使用 Nacos 进行配置管理的好处，如动态更新和集中管理。

*   **场景四：异常处理演示 (03:30 - 04:00)**：
    讲师在 `upload` 方法中添加了 `try-catch` 块，用于捕获上传过程中可能出现的异常。他演示
