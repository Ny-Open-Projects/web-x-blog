# 画面线理解：08.商户资质申请-七牛云-上传测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\08.商户资质申请-七牛云-上传测试【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:24, 01:48, 02:49, 04:04, 04:44, 05:38, 07:19, 09:18, 10:57, 12:00, 13:05, 14:00, 15:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:05:42

1) 这一组画面整体在讲如何使用 Java SDK 将文件上传到七牛云对象存储。

2) 按时间顺序列出每张画面的要点：
画面1：展示七牛云开发者中心文档，介绍 Java SDK 的功能，包括生成上传凭证、直接上传、管理中间件、处理文件、CDN刷新等功能。
画面2：展示七牛云开发者中心的 Java SDK 安装页面，提供 Gradle 和 Maven 的依赖配置。
画面3：展示 Java 代码中导入的七牛云相关包，包括 Configuration、Response、UploadManager 等。
画面4：展示七牛云开发者中心的 Java SDK 文档，提供生成上传凭证的代码示例。
画面5：展示七牛云开发者中心的 Java SDK 文档，说明如何配置 AccessKey、SecretKey 和 bucket，以及调用 SDK 上传文件。
画面6：展示 IDE 中的 Java 代码，定义了上传文件的变量和上传方法。
画面7：展示 IDE 中的 Java 代码，已填写 AccessKey、SecretKey 和 bucket 的值。
画面8：展示 IDE 中的 Java 代码，修改了上传文件的路径和文件名。
画面9：展示 IDE 中的 Java 代码，修改了上传文件的路径和文件名，并添加了文件输入流。
画面10：展示 IDE 中的 Java 代码，添加了异常处理。
画面11：展示 IDE 中的调试界面，显示了上传文件的 key 值。
画面12：展示 IDE 中的 Java 代码，添加了注释和版本信息。
画面13：展示七牛云控制台，显示了上传的文件列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```gradle
compile 'com.qiniu.qiniu-java-sdk:7.2.21'
```
```maven
<dependency>
    <groupId>com.qiniu</groupId>
    <artifactId>qiniu-java-sdk</artifactId>
    <version>7.2.21</version>
</dependency>
```
画面4：
```java
String accessKey = "access key";
String secretKey = "secret key";
String bucket = "bucket name";
Auth auth = Auth.create(accessKey, secretKey);
String uploadToken = auth.uploadToken(bucket);
```
画面5：
```java
public static String accesskey = "";
public static String secretKey = "";
public static String bucket = "";
```
画面6：
```java
String accessKey = "your access key";
String secretKey = "your secret key";
String bucket = "your bucket name";
String key = null;
byte[] uploadBytes = "hello qiniu cloud".getBytes(charset: "utf-8");
Auth auth = Auth.create(accessKey, secretKey);
String uploadToken = auth.uploadToken(bucket);
```
画面7：
```java
String accessKey = "vGShrn6ZU91_KCJEsOW-76A3RzEbgCkM6tktDOD_";
String secretKey = "p04hR8a1151UAXOK3cpnZaPnA6uS1_SLbegaJus";
String bucket = "shanjupy-al";
String key = null;
```
画面8：
```java
String filePath = "F:\\develop\\shanjupy\\1.png";
```
画面9：
```java
FileInputStream fileInputStream = new FileInputStream(new File(filePath));
byte[] bytes = IOUtils.toByteArray(fileInputStream);
```
画面10：
```java
try {
    Response r = uploadManager.put(uploadBytes, key, uploadToken);
    System.out.println(r.bodyString());
} catch (QiniuException ex) {
    System.err.println(ex.toString());
}
```
画面11：
```java
String key = UUID.randomUUID().toString();
```
画面12：
```java
/**
 * 测试文件上传
 * @author Administrator
 * @version 1.0
 */
public class QiniuUtils {
    // 其他参数配置
    Configuration cfg = new Configuration(Region.region0());
    UploadManager uploadManager = new UploadManager(cfg);
    // 生成上传凭证，然后上传
    String accessKey = "vGShrn6ZU91_KCJEsOW-76A3RzEbgCkM6tktDOD_";
    String secretKey = "p04hR8a1151UAXOK3cpnZaPnA6uS1_SLbegaJus";
    String bucket = "shanjupy-al";
    // 默认不指定key的情况下，以文件内容的hash值作为文件名
    String key = UUID.randomUUID().toString();
    FileInputStream fileInputStream = null;
    try {
        // 读取本地文件的字节数据
        String filePath = "F:\\develop\\shanjupy\\1.png";
        fileInputStream = new FileInputStream(new File(filePath));
        // 将文件内容转为字节数组
        byte[] bytes = IOUtils.toByteArray(fileInputStream);
        // 生成上传凭证，然后上传
        Auth auth = Auth.create(accessKey, secretKey);
        // 上传凭证
        String uploadToken = auth.uploadToken(bucket);
        // 上传文件
        Response response = uploadManager.put(bytes, key, uploadToken);
        // 解析上传结果
        DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
        System.out.println(putRet.key);
        System.out.println(putRet.hash);
    } catch (IOException ex) {
        // ignore
    } catch (QiniuException ex) {
        System.err.println(ex.toString());
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3.1 Java SDK简介”，内容包括 Java SDK 的功能。
画面5：PPT标题为“3. 将七云的AccessKey/SecretKey和存储空间配置到代码中”，内容包括配置 AccessKey、SecretKey 和 bucket。
画面13：七牛云控制台显示了上传的文件列表，包括文件名、文件类型、存储类型、文件大小、最后更新时间。

5) 不要评价画面美观，不要输出与课程无关的内容。
