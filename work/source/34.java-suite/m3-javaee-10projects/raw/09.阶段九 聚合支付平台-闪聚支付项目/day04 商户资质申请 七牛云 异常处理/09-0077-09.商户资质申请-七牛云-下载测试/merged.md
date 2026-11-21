# 09.商户资质申请-七牛云-下载测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\09.商户资质申请-七牛云-下载测试【海量资源尽在 666java.com】.mp4
- 时长 3分39秒（音频 220s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 有上传就有下载对不对下载怎么下载其实下载刚才我都已经给你测试过了怎么说你上传成功之后各位这儿你是不是就可以复制外链这是不是就是下载对于公共的存储空间你这时候呢给这个地址发给谁是不是都可以访问呢这就是一种下载但是有的老人呢对于私有存储空间呢对于私有存储空间的话你要想下载那好这时候你就用他的这个
[00:30] API了也就是在他的什么给我们提供的这个SDK上面你往下再翻他有一个专门下载文件的一块代码看见吗对这一块代码就是生成一个什么一个下载地址你也可以测试一下来看一下我们get一个什么download的URL然后呢看一下我们把它复制进去这个方式各位跟刚才的这个
[01:02] 方式呢都差不多我们需要做的是什么呀其实我们就需要导入包然后呢我们就把key这些key要拿过来对不对你先看它的代码吧key肯定是需要的看见了吗然后呢还有啥呀还有就是你的这个bucket的名字好这里边我们让它抛个一层那bucket这个名字怎么拿到的bucket的名字这不是它吗
[01:31] 但是它有一个域名你需要呀啥域名还有印象吗如果你访问我们存储空间的文件它前面是不是有一个域名你看看嘛对不对这个域名你得在这写好但这个域名呢我们后边也可以申请作为我们就是使用我们公司公司自己的名字默认你可以使用bucket的他给我们分的名字懂吧好这是我们说的文件的名称是不是那文件的名称刚才我都
[02:02] 咱们都拿到这个文件的名称了吧这个文件的名称刚才控制台是不是都打出来了就是它吧对吧这个文件的名称一定是要和什么和你刚才上传上去的这个什么内容管理里边前边的这个文件的名称保持一致就它懂吧好也就是说白了你拿到了一个文件的key就这个这个名称啊你需要来生成一个下载路径对
[02:29] 你按照这个过程呢它的API就可以来生成一个下载路径当然对于公共的存储空间不需要这一步对于私有的存储空间我们就需要这一步大家理解我的意思吧好现在呢我们弄完了之后你就可以来测试一下那我看一下啊有时候老师你这个是你这个是个公共的存储空间难道我们也可以这么玩吗当然可以啊因为它的API都是一样的嘛所以我给你测试一下即使我是公共
[02:58] 存储空间我也可以把我的文件呢生成他给我们的一个什么下载路径这个路径就是他生成了一个经过认真处理的一个什么临时的一个下载路径他可以仍然下载我们说的这个文件大家懂吧这里面最关键的啊大家主要是掌握上传文件的整个测试过程
[03:16] 对下载文件的这里边我们知道通常我们使用的都是公共存储空间的对于一些私有存储空间的文件呢可能我们公司就自己搭建服务器来上传了当然你也可以用它的私有空间我们只要生成什么按照它的方式生成一个下载路径也可以好那到这儿清又云的SDK的上传文件测试和下载咱们就讲完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用七牛云 Java SDK 实现文件的上传与下载功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Java 代码，用于上传文件并解析返回结果，包含 try-catch 块处理异常。
画面2：在七牛云控制台的“对象存储”页面，显示已上传的文件列表，其中文件“283d041b-2a49-4a04-8409-516043804870.png”被选中。
画面3：在七牛云控制台的“对象存储”页面，展示“shanju-pay-m1”空间的详情，包括域名和文件列表。
画面4：在七牛云开发者中心的“Java SDK”页面，展示用于生成下载链接的 Java 代码示例。
画面5：在 IntelliJ IDEA 编辑器中，展示 `QiniuUtils.java` 文件，其中包含 `getDownloadUrl()` 方法的代码，用于生成下载链接。
画面6：在 IntelliJ IDEA 编辑器中，展示 `getDownloadUrl()` 方法的代码，光标位于 `String encodeFileName = URLEncoder.encode(fileName, "utf-8").replace(target, replacement);` 这一行。
画面7：在 IntelliJ IDEA 编辑器中，展示 `getDownloadUrl()` 方法的代码，光标位于 `String publicUrl = String.format("%s/%s", domainOfBucket, encodeFileName);` 这一行。
画面8：在浏览器中，显示七牛云对象存储的宣传页面，包含“立即使用”和“产品价格”按钮。
画面9：在 IntelliJ IDEA 编辑器中，展示 `getDownloadUrl()` 方法的代码，光标位于 `String encodeFileName = URLEncoder.encode(fileName, "utf-8").replace(target, replacement);` 这一行，同时控制台显示连接和断开信息。
画面10：在 IntelliJ IDEA 编辑器中，展示 `getDownloadUrl()` 方法的代码，光标位于 `String encodeFileName = URLEncoder.encode(fileName, "utf-8").replace(target, replacement);` 这一行，同时控制台显示连接和断开信息。
画面11：在 IntelliJ IDEA 编辑器中，展示 `getDownloadUrl()` 方法的代码，光标位于 `String encodeFileName = URLEncoder.encode(fileName, "utf-8").replace(target, replacement);` 这一行，同时控制台显示连接和断开信息。
画面12：在七牛云控制台的“对象存储”页面，显示已上传的文件列表，其中文件“283d041b-2a49-4a04-8409-516043804870.png”被选中。
画面13：在 IntelliJ IDEA 编辑器中，展示 PPT 页面“3.1 Java SDK简介”，内容包括 Java SDK 的功能介绍和官方文档链接。
画面14：在 IntelliJ IDEA 编辑器中，展示 PPT 页面“3 上传文件测试”，内容包括 Java SDK 的功能介绍。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
try {
    Response response = uploadManager.put(uploadBytes, key, upToken);
    //解析上传成功的結果
    DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
    System.out.println(putRet.key);
    System.out.println(putRet.hash);
} catch (QiniuException ex) {
    Response r = ex.response;
    System.err.println(r.toString());
    try {
        System.err.println(r.bodyString());
    } catch (QiniuException ex2) {
        //ignore
    }
} catch (IOException ex) {
    //ignore
}
```

画面4：
```java
String fileKey = "公司/存档/qiniu.jpg";
String domainOfBucket = "http://devtools.qiniu.com";
String encodeFileName = URLEncoder.encode(fileKey, "utf-8").replace(target, replacement);
String publicUrl = String.format("%s/%s", domainOfBucket, encodeFileName);
String accessKey = "your access key";
String secretKey = "your secret key";
Auth auth = Auth.create(accessKey, secretKey);
long expireInSeconds = 3600; //1小时，可以自定义有效时间
String finalUrl = auth.privateDownloadUrl(publicUrl, expireInSeconds);
System.out.println(finalUrl);
```

画面5：
```java
private static void getDownloadUrl() throws UnsupportedEncodingException {
    String fileKey = "公司/存档/qiniu.jpg";
    String domainOfBucket = "http://devtools.qiniu.com";
    String encodeFileName = URLEncoder.encode(fileKey, "utf-8").replace(target, replacement);
    String publicUrl = String.format("%s/%s", domainOfBucket, encodeFileName);
    String accessKey = "your access key";
    String secretKey = "your secret key";
    Auth auth = Auth.create(accessKey, secretKey);
    long expireInSeconds = 3600; //1小时，可以自定义有效时间
    String finalUrl = auth.privateDownloadUrl(publicUrl, expireInSeconds);
    System.out.println(finalUrl);
}
```

画面7：
```java
private static void getDownloadUrl() throws UnsupportedEncodingException {
    String fileKey = "公司/存档/qiniu.jpg";
    String domainOfBucket = "http://devtools.qiniu.com";
    String encodeFileName = URLEncoder.encode(fileKey, "utf-8").replace(target, replacement);
    String publicUrl = String.format("%s/%s", domainOfBucket, encodeFileName);
    String accessKey = "your access key";
    String secretKey = "your secret key";
    Auth auth = Auth.create(accessKey, secretKey);
    long expireInSeconds = 3600; //1小时，可以自定义有效时间
    String finalUrl = auth.privateDownloadUrl(publicUrl, expireInSeconds);
    System.out.println(finalUrl);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面13：
标题：3.1 Java SDK简介
内容：
- 使用此 SDK 构建您的网络应用程序，能让您以非常便捷地方式将数据安全地存储到七牛云上。无论您的网络应用是一个网站程序，还是包括从云端（服务端程序）到终端（手持设备应用）的架构服务或应用，通过七牛云及其 SDK，都能让您应用程序的终端用户高速上传和下载，同时也让您的服务端更加轻盈。
- Java SDK 属于七牛服务端SDK之一，主要有如下功能：
  1. 提供生成客户端上传所需上传凭证的功能
  2. 提供文件从服务端直接上传七牛的功能
  3. 提供对七牛空间中文件进行管理的功能
  4. 提供对七牛空间中文件进行处理的功能
  5. 提供七牛CDN相关的刷新，预取，目志功能
- 详细内容参考官网：https://developer.qiniu.com/kodo/sdk/1239/java

画面14：
标题：3 上传文件测试
内容：
- 官方提供了java SDK方便开发。
- 3.1 Java SDK简介
  - 使用此 SDK 构建您的网络应用程序，能让您以非常便捷地方式将数据安全地存储到七牛云上。无论您的网络应用是一个网站程序，还是包括从云端（服务端程序）到终端（手持设备应用）的架构服务或应用，通过七牛云及其 SDK，都能让您应用程序的终端用户高速上传和下载，同时也让您的服务端更加轻盈。
  - Java SDK 属于七牛服务端SDK之一，主要有如下功能：
    1. 提供生成客户端上传所需上传凭证的功能
    2. 提供文件从服务端直接上传七牛的功能
    3. 提供对七牛空间中文件进行管理的功能
    4. 提供对七牛空间中文件进行处理的功能
    5. 提供七牛CDN相关的刷新，预取，目志功能

5) 无

