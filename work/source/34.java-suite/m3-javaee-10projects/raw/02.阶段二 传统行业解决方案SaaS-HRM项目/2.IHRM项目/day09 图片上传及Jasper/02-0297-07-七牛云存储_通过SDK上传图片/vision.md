# 画面线理解：07-七牛云存储：通过SDK上传图片

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\07-七牛云存储：通过SDK上传图片_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:38, 01:56, 02:31, 03:03, 03:58, 04:53, 05:46, 06:10, 07:18, 07:57, 08:41, 09:23, 10:34, 11:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:25:44

1) 这一组画面整体在讲如何使用七牛云对象存储服务，通过 Java SDK 实现图片上传功能。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示七牛云对象存储控制台，展示名为 "ihrm-bucket" 的存储空间及其 CDN 域名信息。
画面 2: 显示七牛云开发者中心的 Java SDK 页面，提供通过 Gradle 和 Maven 安装 SDK 的方式，并展示对应的依赖配置。
画面 3: 在 IntelliJ IDEA 中，选择创建新项目，准备使用 Maven。
画面 4: 在 IntelliJ IDEA 中，创建新模块，设置 GroupId、ArtifactId 和 Version。
画面 5: 显示 IntelliJ IDEA 中新创建的模块 "qiniu-demo" 的项目结构，包含 pom.xml 文件。
画面 6: 在 IntelliJ IDEA 中，打开并编辑 Java 类 "QiniuDemo"，准备编写上传代码。
画面 7: 显示七牛云开发者中心的 Java SDK 页面，展示 Java SDK 的使用示例代码。
画面 8: 在 IntelliJ IDEA 中，为 "QiniuDemo" 类导入 "Configuration" 类。
画面 9: 显示 "Configuration.class" 的源码，展示其内部的配置参数。
画面 10: 在 IntelliJ IDEA 中，编写 Java 代码，初始化配置并创建上传管理器。
画面 11: 在 IntelliJ IDEA 中，为 "accessKey" 和 "secretKey" 赋予具体的值。
画面 12: 在 IntelliJ IDEA 中，为 "localFilePath" 赋予 Windows 系统下的具体文件路径。
画面 13: 在 IntelliJ IDEA 中，为 "key" 赋予 "test"，并完成上传代码的编写。
画面 14: 显示七牛云对象存储控制台的“内容管理”页面，显示已上传的文件 "test"，并确认其存在。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```gradle
compile 'com.qiniu.qiniu-java-sdk:7.2.1'
```
```maven
<dependency>
    <groupId>com.qiniu</groupId>
    <artifactId>qiniu-java-sdk</artifactId>
    <version>7.2.1</version>
</dependency>
```
画面 6:
```java
package cn.itcast.qiniu;
import org.junit.Test;
public class QiniuDemo {
    @Test
    public void testUpload01() {
        //图片上传到七牛云服务
        //1.创建一个配置对象
        Configuration cfg = new Configuration(Zone.zone0());
        //2.创建上传管理器
        UploadManager uploadManager = new UploadManager(cfg);
        //3.生成上传凭证，然后准备上传
        String accessKey = "your access key";
        String secretKey = "your secret key";
        String bucket = "your bucket name";
        //4.默认不指定key的情况下，以文件内容的hash值作为文件名
        String key = null;
        Auth auth = Auth.create(accessKey, secretKey);
        String upToken = auth.uploadToken(bucket);
        try {
            Response response = uploadManager.put(localFilePath, key, upToken);
            DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
            System.out.println(putRet.key);
            System.out.println(putRet.hash);
        } catch (QiniuException ex) {
            Response r = ex.response;
            System.err.println(r.toString());
        } catch (Exception ex2) {
            System.err.println(ex2.toString());
        }
    }
}
```
画面 7:
```java
// 1.创建一个配置对象
Configuration cfg = new Configuration(Zone.zone0());
// 2.创建上传管理器
UploadManager uploadManager = new UploadManager(cfg);
// 3.生成上传凭证，然后准备上传
String accessKey = "your access key";
String secretKey = "your secret key";
String bucket = "your bucket name";
// 4.默认不指定key的情况下，以文件内容的hash值作为文件名
String key = null;
Auth auth = Auth.create(accessKey, secretKey);
String upToken = auth.uploadToken(bucket);
try {
    Response response = uploadManager.put(localFilePath, key, upToken);
    DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
    System.out.println(putRet.key);
    System.out.println(putRet.hash);
} catch (QiniuException ex) {
    Response r = ex.response;
    System.err.println(r.toString());
} catch (Exception ex2) {
    System.err.println(ex2.toString());
}
```
画面 8:
```java
import com.qiniu.storage.Configuration;
import com.qiniu.storage.UploadManager;
import com.qiniu.util.Auth;
```
画面 9:
```java
package com.qiniu.storage;
import java.util.*;
public final class Configuration implements Cloneable {
    public Zone zone;
    public boolean unrollHttpsDomains = true;
    public int putThreshold = 4194304;
    public int connectTimeout = 10;
    public int writeTimeout = 0;
    public int readTimeout = 30;
    public int dispatcherMaxRequests = 64;
    public int dispatcherMaxRequestsPerHost = 16;
    public int connectionPoolMaxIdleCount = 32;
    public int connectionPoolMaxIdleMinutes = 5;
    public int retryBox = 5;
    public Dns dns;
    public boolean usedNmsFirst;
    public ProxyConfiguration proxy;
    public static String defaultRsHost = "rs.qiniu.com";
    public static String defaultApiHost = "api.qiniu.com";
    public static String defaultUcHost = "uc.qiniu.me";
    public Configuration() {
    }
}
```
画面 10:
```java
//1.创建一个配置对象
Configuration cfg = new Configuration(Zone.zone0());
//2.创建上传管理器
UploadManager uploadManager = new UploadManager(cfg);
//3.生成上传凭证，然后准备上传
String accessKey = "your access key";
String secretKey = "your secret key";
String bucket = "your bucket name";
//4.默认不指定key的情况下，以文件内容的hash值作为文件名
String key = null;
Auth auth = Auth.create(accessKey, secretKey);
String upToken = auth.uploadToken(bucket);
try {
    Response response = uploadManager.put(localFilePath, key, upToken);
    DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
    System.out.println(putRet.key);
    System.out.println(putRet.hash);
} catch (QiniuException ex) {
    Response r = ex.response;
    System.err.println(r.toString());
} catch (Exception ex2) {
    System.err.println(ex2.toString());
}
```
画面 11:
```java
String accessKey = "COUdRVA7JLsuRzIvQ51_pDceHDv3yGfFEmvvw";
String secretKey = "30Kp7J853gXQpSlF4rmd4mK0C5T12a6uNQy7s51r";
String bucket = "ihrm-bucket";
```
画面 12:
```java
String localFilePath = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\源码\\资源\\1001.png";
```
画面 13:
```java
String key = "test";
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
