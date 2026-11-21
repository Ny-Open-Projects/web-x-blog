# 52-文件服务课程-文件服务开发（接口开发_根据 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好

那么刚才呢

咱们把这个file.biz啊

整个这个代码呢

都已经开发完成了

咱们最终呢

是调用了我们这个ziputils啊

就是我们提前提供好的这个工具类

对吧

它给我们提供了这么一个方法

用于文件下载

好

那么我们呢

就是把它需要的这些参数呢

在我们这个方法里边

是不是一个一个给它封装好

重点呢

我们是需要封装这么一个map

对吧

就是这个filemap

而这个filemap里边封装的是什么东西呢

放的就是我们的这个key呢

是我们要下载的这个文件

它的原始文件名

而且它的value呢

对应的就是这个url地址

但是呢

为了防止这种重名的情况

对吧

所以说呢

我们需要把这个原始文件名呢

可能需要进行一个处理

进行一个什么处理呢

其实就是啊

如果文件名出现重复

我们在后边是不是给它通过这种

加上这种123

对吧

下标的这种形式啊

把这些重复的文件名给它区分开

给它区分开

好

然后接下来呢

我们可以来大概读一下

咱们提供的这个工具类啊

它是具体如何来完成文件下载的

那么就是这个方法

咱们把这个filemap

还有总的要下载的文件大小

以及我们要下载的这个文件名称

对吧

还有request response对象呢

都传进来了

大家可以看到啊

这个地方呢

进行文件下载了

它其实最根本的是基于我们的这个

http url connection

对吧

因为呢

我们不管你使用的是本地存储策略

还是远程的

发自的dfs

或者是阿里云存储

最终呢

我们都可以通过一个url地址

来访问到这个文件

对吧

所以说呢

我们就可以通过一个url connection

然后呢

访问到我们那个url地址

这样的话呢

就可以读取到我们这个流对象

对吧

有了这个流对象呢

我就可以来进行文件下载了

好

大家可以看一下

我们这个地方的response

对吧

set content type

对吧

表示呢

我们往客户端写的是我们这种二进制流

然后呢

这是我们的文件下载

文件要下载的文件名

对吧

下载的这个文件名呢

有人说这个地方

你这不是已经设置好了吗

直接给它复制

是不是就可以了

但是呢

因为我们客户端呢

有可能是通过浏览器来进行下载

那这个时候呢

如果我们这个下载的文件是中文的话呢

就会出现乱码这种情况

所以说呢

它这个地方呢

又针对不同的浏览器啊

是不是来做了一个转码

对吧

通过这个base64啊

来进行了一个转码

然后呢

最终达到的效果就是什么呢

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

就是

里边

或者有一些特殊字符呢

需要进行一个替换

哎

要进行一个替换

所以你看到啊

这一大堆代码

对吧

其实都是在来确定什么呢

确定我们这个最终下载的文件名

里边有一些中文的

或者一些特殊字符的

需要来进行这个替换的

好

那么

到这的话呢

我们就把这个download的file name

是不是给处理好了

对吧

就已经给处理好了

处理好之后呢

我们可以通过response set header

对吧

然后设置一个想用头信息

content disposition

表示这是一个附件形式下载

对吧

下载的文件名

把它追加到后边就可以了

然后呢

再往下的话呢

咱们是不是就需要来

通过我们的传过来的response对象

来获得一个output stream

因为我们是不是要向我们的客户端

来写入我们的这个流

对吧

然后呢

实现文件下载

但是这个下载的时候呢

我们前面也提到了

可能是下载一个文件

也可能是多个文件打包下载

所以说我们在这个地方呢

是不是做了一个判断

if什么呢

我们这个传过来的map

它的size呢

等于1

那么在什么情况下

它会等于1呢

那肯定就是下载的只有一个文件

对吧

只有一个文件

那么这种情况呢

是比较简单的

那这个时候呢

我们是不是就可以啊

直接把咱们这个

把这个map呢

给它

entry

对吧

便利一下

然后呢

拿到它的URL地址

然后呢

拿到这个URL地址之后呢

我们就可以get connection

get connection呢

其实是在下边封装的一个方法

对吧

其实就是new了一个URL

然后呢

open connection

对吧

最终呢

把那个connect到

这样的话呢

我们就连接上这个地址

然后呢

拿到这个connection之后啊

咱们回到这边来

拿到connection之后

我们是不是就可以通过connection

来get input stream

通过这个输入流

对吧

来读取远程的那个文件

信息

当然了

它这个地方呢

因为都是细节处理啊

所以又封装了这么一个方法

叫做download file

这个方法

然后呢

把我们那个输入流

是不是传过去

然后呢

把我们刚才得到的这个输出流

是不是也传过去

具体在这个方法里边

你看咱们是不是就是从输入流来读

对吧

read

然后呢

通过输出流是不是来写

write

最终一个一个把它写回到我们这个客户端

那就可以了

这是我们这个下载

然后呢

回到这边来

咱们继续来看啊

ZIP

Utils

这里边比较多啊

咱们还是从这边来借

好

你看

刚才呢

我们说的是比较简单的这种情况

也就是说啊

我们要下载的是一个文件

对吧

是一个文件

那么

我们就可以拿到它这个URL地址

然后呢

直接去下载就可以了

那么如果说if不成立

这就说明什么呢

说明我们这个filemap

它的size应该是大于1

也就是说

我们同时要下载的可能是多个文件

那么呢

我们就需要把这多个文件呢

把它这个下载下来

然后呢

打到一个压缩包里边

然后呢

我们把这个压缩包

这个文件

然后下载到这个客户端

对吧

所以接下来呢

我们就需要啊

执行下边这一段代码

对吧

下边这一段代码

然后呢

它这个地方呢

是需要把我们

刚才这个out啊

也就是这个输出流

把它进行一个包装

包装成一个什么呢

ZIP

output stream

因为我们要下载的是一个什么呢

是一个压缩包

对吧

所以需要使用这种啊

流

然后呢

我们再把这个什么呢

ZOS啊

ZOS是什么呢

是我们就是创建出来的这个输出流

对吧

然后呢

把它转成一个带有缓冲功能的

这么一个流

一会儿呢

我们直接使用的

其实是这个BOS

这个流对象

这个输出流

然后接下来呢

我们这里边是不是要下载多个文件呢

下载多个文件呢

肯定需要便利了

对不对

然后呢

把我们这个filename

就是entry嘛

getfilename

geturl

这是咱们map里面封装的

这些对吧

一次一次

一个一个给它封装过来

然后呢

getconnection

来下载

那么

把它这个connection得到之后啊

这样就连接到我们远程那个文件了

对不对

对

然后呢

通过这个connection

getinputstream

这样就得到远程的

这个文件的输入流了

比如说我们现在啊

是在便利第一次对吧

那么

它就可以拿到这个文件了

它对应的输入流

然后呢

把这个流呢

通过通过这个输入流呢

来读

然后呢

再通过我们这个输出流对吧

zos呢

来写

来写

因为它是个压缩文件对不对

所以说呢

我们应该是

把这些流呢

全都压到这个里边去

全都压到这个里边去啊

就是new了一个zipentry

对吧

zipentry

然后呢

一个一个在这边写

当我们最终这个for晕环

全都便利完了

对吧

全都便利完了

那么整个啊

它这里边是全都写完了

相当于它是通过for晕环

每一次呢

是便利出来

其中要写的呢

是这个

下载的一个文件

然后呢

把它这个压到我们

对应的这个输出流

对象里面去

对吧

这不是put next entry吗

好

然后呢

一个一个来写就可以了

最终呢

flush一下

当然如果出异常呢

就泡这种异常

就可以了

这些呢

都是一些细节的处理啊

所以说呢

我们是把它封装到

我们这个工具类里面来了

而在我们这个filebiz这边呢

相当于是一些

对象格式的一些处理

对吧

把我们这些

传过来的对象

然后呢

进行一个数据库查询

然后进行过滤

然后进行对象的封装

转换

最终呢

转换成他想要的

这些参数

然后呢

我们

然后传给这个工具类

由这个工具类呢

去实现具体的

这些下载的细节处理

好

这是咱们

来大概读一下

我们这个工具类里面

文件下载的这个方法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程聚焦于一个Java Web项目中文件下载与打包功能的实现。讲师通过 IntelliJ IDEA 开发环境，逐行讲解了 `ZipUtils.zipFilesByInputStream` 方法的核心代码。该方法的主要功能是：接收一个包含文件名与URL映射的 `Map`，将这些文件从网络或本地路径读取并打包成一个ZIP文件供用户下载。课程重点讲解了如何处理文件名重复、文件名安全编码、以及如何使用 `HttpURLConnection` 和 `ZipOutputStream` 进行网络文件读取和流式写入。整个过程体现了Java中流式处理、异常处理和资源管理的最佳实践。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，讲师介绍本节将讲解文件打包下载功能。
*   **00:05 - 00:15**: 讲解 `fileMap` 的初始化和 `duplicateFile` 的作用，用于处理文件名重复。
*   **00:15 - 00:30**: 详细分析 `fileDOList.stream().filter(...).forEach(...)` 代码块，说明如何遍历文件列表并处理每个文件。
*   **00:30 - 00:45**: 讲解 `buildNewFileName` 方法的逻辑，用于为重复文件名生成新名称。
*   **00:45 - 01:00**: 讲解 `response.setContentType` 和 `downloadFileName` 的设置，特别是对文件名进行URL编码以避免特殊字符问题。
*   **01:00 - 01:15**: 讲解 `response.setHeader("Content-Disposition", "attachment;filename=" + downloadFileName);`，设置HTTP响应头以触发浏览器下载。
*   **01:15 - 01:30**: 讲解 `downloadFile` 方法，用于从输入流读取数据并写入输出流。
*   **01:30 - 01:45**: 讲解 `getConnetion` 方法，用于创建 `HttpURLConnection` 对象。
*   **01:45 - 02:00**: 讲解 `zipFilesByInputStream` 方法的主逻辑，包括创建 `ZipOutputStream` 和 `BufferedOutputStream`。
*   **02:00 - 02:15**: 讲解如何遍历 `fileMap`，为每个文件创建 `ZipEntry` 并读取数据写入ZIP流。
*   **02:15 - 02:30**: 讲解 `finally` 块，确保 `HttpURLConnection`、`BufferedInputStream` 和 `ZipOutputStream` 等资源被正确关闭。
*   **02:30 - 02:45**: 讲解 `catch` 块，处理在打包过程中可能出现的异常。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 1 (文件名去重与重命名)**：
    ```java
    Map<String, Integer> duplicateFile = new HashMap<>(fileDOList.size());
    fileDOList.stream().filter(file -> file != null && file.getDataType().eq(DataType.DIR) && StringUtils.isNotBlank(file.getUrl())).forEach(file -> {
        String submittedFileName = file.getSubmittedFileName();
        if (fileMap.containsKey(submittedFileName)) {
            // 将重复的文件名次数加1处理
            duplicateFile.put(submittedFileName, duplicateFile.get(submittedFileName) + 1);
        } else {
            duplicateFile.put(submittedFileName, 1);
        }
        submittedFileName = buildNewFileName(submittedFileName, duplicateFile.get(submittedFileName));
        fileMap.put(submittedFileName, file.getUrl());
    });
    ```

*   **关键代码片段 2 (文件名安全编码)**：
    ```java
    response.setContentType("application/octet-stream; charset=utf-8");
    String downloadFileName = "";
    String agent = request.getHeader("USER-AGENT");
    if (agent != null && agent.toLowerCase().indexOf(AGENT_FIREFOX) > 0) {
        downloadFileName = "=PUTF-8?B" + (new String(Base64.encodeBase64(extName.getBytes("UTF-8"))));
    } else {
        // 这些字符不能被替换，因为系统允许文件名有这些字符
        downloadFileName = URLEncoder.encode(extName, "UTF-8")
            .replaceAll("%20", " ")
            .replaceAll("%29", "\\)")
            .replaceAll("%3B", StrPool.SEMICOLON)
            .replaceAll("%40", StrPool.AT)
            .replaceAll("%23", "\\#")
            .replaceAll("%26", StrPool.PLUS)
            .replaceAll("%25", StrPool.PERCENT)
            .replaceAll("%21", StrPool.EXCLAMATION_MARK)
            .replaceAll("%5E", StrPool.HAT)
            .replaceAll("%24", StrPool.TILDA)
            .replaceAll("%60", StrPool.BACKTICK)
            .replaceAll("%5B", StrPool.LEFT_SQ_BRACKET)
            .replaceAll("%5D", StrPool.RIGHT_SQ_BRACKET)
            .replaceAll("%5C", StrPool.SLASH)
            .replaceAll("%3F", StrPool.LEFT_BRACE)
            .replaceAll("%7D", StrPool.RIGHT_BRACE)
            .replaceAll("%7C", StrPool.PIPE)
            .replaceAll("%3A", StrPool.COLON)
            .replaceAll("%22", StrPool.SINGLE_QUOTE)
            .replaceAll("%3B", StrPool.SEMICOLON)
            .replaceAll("%3F", StrPool.QUESTION_MARK)
            .replaceAll("%3D", StrPool.EQUALS)
            .replaceAll("%27", StrPool.APOSTROPHE);
    }
    ```

*   **关键代码片段 3 (文件下载与打包核心逻辑)**：
    ```java
    public static void zipFilesByInputStream(Map<String, String> fileMap, Long fileSize, String extName, HttpServletRequest request, HttpServletResponse response) throws Exception {
        response.setContentType("application/octet-stream; charset=utf-8");
        String downloadFileName = "";
        String agent = request.getHeader("USER-AGENT");
        if (agent != null && agent.toLowerCase().indexOf(AGENT_FIREFOX) > 0) {
            downloadFileName = "=PUTF-8?B" + (new String(Base64.encodeBase64(extName.getBytes("UTF-8"))));
        } else {
            // ... (安全编码逻辑)
        }
        response.setHeader("Content-Disposition", "attachment;filename=" + downloadFileName);
        if (fileSize != null && fileSize > 0) {
            response.setHeader("Content-Length", String.valueOf(fileSize));
        }
        ServletOutputStream out = response.getOutputStream();
        if (fileMap.size() == 0) {
            String url = null;
            // ... (处理空文件映射)
        }
        try (ZipOutputStream zos = new ZipOutputStream(out); BufferedOutputStream bos = new BufferedOutputStream(zos)) {
            for (Map.Entry<String, String> entry : fileMap.entrySet()) {
                String fileName = entry.getKey();
                String url = entry.getValue();
                BufferedInputStream bis = null;
                try {
                    HttpURLConnection connection = getConnection(url);
                    bis = new BufferedInputStream(connection.getInputStream());
                    zos.putNextEntry(new ZipEntry(fileName));
                    int len;
                    byte[] buf = new byte[10 * 1024];
                    while ((len = bis.read(buf, 0, buf.length)) != -1) {
                        bos.write(buf, 0, len);
                    }
                    bos.flush();
                } catch (Exception e) {
                    log.warn("打包下载多个文件异常, fileName=" + fileName + ", url=" + url, e);
                } finally {
                    if (connection != null) {
                        connection.disconnect();
                    }
                    if (bis != null) {
                        bis.close();
                    }
                }
            }
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 文件名去重处理** (00:15-00:30)
    讲师在IDEA中高亮显示了 `fileMap` 和 `duplicateFile` 的初始化代码。他解释了 `fileDOList.stream().filter(...).forEach(...)` 的作用，即遍历所有文件，检查其文件名是否已存在于 `fileMap` 中。如果存在，则在 `duplicateFile` 中记录其重复次数；如果不存在，则将其加入 `fileMap` 并设置重复次数为1。最后，通过 `buildNewFileName` 方法为重复文件生成新名称，确保下载时文件名唯一。

*   **场景 2: 文件名安全编码** (00:45-01:00)
    讲师展示了 `response.setContentType` 和 `downloadFileName` 的设置。他特别强调了对文件名进行URL编码的重要性，以防止特殊字符（如空格、引号、斜杠等）导致下载失败。他详细演示了 `URLEncoder.encode` 方法，并展示了如何使用 `replaceAll` 方法将各种特殊字符替换为安全的编码形式（如 `%20` 代表空格，`%2F` 代表斜杠），并特别指出某些字符
