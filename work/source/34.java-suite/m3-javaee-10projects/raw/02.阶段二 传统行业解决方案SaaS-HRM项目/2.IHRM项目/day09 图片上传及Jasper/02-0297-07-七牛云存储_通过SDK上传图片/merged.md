# 07-七牛云存储：通过SDK上传图片

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\07-七牛云存储：通过SDK上传图片_【海量资源尽在 ubkz.com】.mp4
- 时长 11分38秒（音频 699s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那青牛云开发的这些基础准备工作我们都已经做好那接下来我们就可以写一些简单的案例来玩一下把一张图片存到青牛云里面接着我们把它获取到来看一下如何去做那其实呢对于咱们自己去玩一个入门案例来说最好的老师是什么并不是我其实可以参照一下人家给我们提供的一些文档
[00:30] 对着文档我们去编写自己的代码这样一来更加快速一点好了呢接下来呢我们的文档可以回到浏览器找到我们的青牛云那在这边呢其中各位来找到右上角呢这边有一个文档中心里面已经涵盖了所有青牛云提供的服务的一些内容文档好了我们打开它简单的来看一下底下
[00:54] 我们关注的是提供的对象存储的这个服务所以去找到对象存储相关的文档那各位来看他的文档呢还是比较多的比较多的我们重点的关注的不是说他这个文档究竟是怎么介绍快速入门是什么等等我们重点关注的是往下拖一般来说呢他都会提供这么一个SDK的这么一种机制
[01:17] SDK什么意思其实就是人家把基本的访问人家这边他的一些接口都给我们准备好并且会给我们准备一些势力的一些代码所以呢我们可以快速的通过人家准备的SDK势力的代码去构建我们自己的服务OK这边的点击进来找到相应的语言版本我们用的是Java所以找到Java SDK好了这样一来点进来之后呢这边有对他自己的介绍
[01:46] 那我们通过Java这个SDK呢它属于青牛服务端SDK之一它提供了如下这么多的功能那对于我们而言咱们直接这个我就过掉了不再看了那接下来我们直接关注的就是如何快速的能够搭建一个环境并且呢能够把一张图片存到青牛云这边好了那如何去做呢首先我们自己要搭建环境的时候
[02:11] 是不是要导入相应的坐标那这个坐标或者这个jar 包其实就是七牛云为我们准备的SDK那这边呢有很多种方式我们使用Maven的形式所以直接想都不要想创建一个工程把Maven坐标拷过来好了在这边呢我去创建一个新的工程打开ideanew一个project好了我个人习惯呢去创建一个空的project好了把它叫做就叫做七牛-test
[02:42] 好了我把它放到哪个目录下呢就放到我们HRM这个目录下了Ctrl C Ctrl VFinish好了这个工程我们创建好了之后呢接着在里面去创建一个新的模块那这个模块呢我就叫做奇牛demo了当然是一个maven模块cn.itcast好了叫做奇牛demoOK这边呢点击Finish那工程创建好了那接下来呢我需要引入坐标
[03:18] 那我们的坐标在哪呢其实刚才我们看过人甲的文档已经为我们准备好了所以直接想都不要想直接Ctrl C拿过来Ctrl A当然了我一会要做测试呢可能还要JUnit相关支持所以我也搞一个JUnit过来好了随便选一版本那这样一来我这个基本的依赖咱们都已经添加进来了那添加进来了之后我们可以看一下那其中在这边已经为我们准备了一个叫做com.7牛
[03:50] 这么一个包这个里面是人家提供的SDK里面由我们去访问金牛云所离不开的一些方法OK好了那接下来呢我们开始在这边去创建一个测试类着手去完成把一张图片上传到人家这边好了写一个测试类zin.itcast金牛.我就叫做金牛金牛叫这个叫demo吧
[04:25] OK那这个测试类我们写好了那接下来我们要完成的第一个测试就是一个将图片上传到奇牛云服务那要想将图片上传到奇牛云服务其实呢也比较简单我们可以写一个test网吧testpublicvidtestupload比如说就叫01了那里面这个代码如何去写呢其实我们
[05:02] 这个代码呢咱们从头到尾去写这个不太现实为什么呢是因为这个SDK是通过七牛云帮助我们封装好的所以七牛云那边应该会给我们准备一些它的一些帮助的一些内容那我们这回再去回到我们的文档帮助的这边打开浏览器好了各位咱们继续往下去看继续往下去看那在这边呢
[05:28] 它支持文件上传支持很多种类那我们现在做的是不是客户端因为我们现在是Java服务端所以我们关注的是Java服务器这边的一个叫做直传那Java服务器直传咱们重点关注到就是一个文件上传的这么一个案例demo这边那各位会发现它已经把基本的这些代码已经都给我们准备好了
[05:54] 那我们只需要把这端代码想都不要想直接Ctrl Ccall到我们的事例工程这边做一个简单的修改其实就可以了好了那这边call过来之后呢我们需要引入一下基本的jar 包提牛云的别选错OK把这个代码呢做一个简单的格式化处理快一些那接下来呢我们想跟各位来聊的就是说啊第一句话就是构造了一个代由指定
[06:24] 总对象的一个配置类那这个呢我需要跟各位解释一下那这个配置类是我们进行文件上传的一个基础配置类里面需要指定你的你上传文件的服务器地区那我们刚才创建的一个服务器是把它放到一个华东或者华北还有这个还有异想啊那不管是你创建到哪儿那我们都需要告诉他那如何去告诉他呢其实就是借助这么一个参数好了华东代表的是零
[06:57] 好了华北12然后呢NA0 AS0等等那按照你自己的需求按照你自己创建的自己创建的存储空间自己去选择就可以了那我们要做的事情我就叫0了因为我们刚才创建的就是华东OK那这样一来第一个我们搞定了当然了除了这个配置之外呢还有一些其他的配置这边呢有他自己的一个原码那其实这个原码里面呢咱们可以简单的做一个猜测
[07:27] 那比如说呢这边有写的一个超时时间或者读的超时时间等等当然了这些我们用默认值其实就可以了那除了这个参数之外接着这边这边有一个叫做upload managerupload manager那对于这个upload manager它其实是我们的上传管理器OK当然了上传管理器也是通过一个CFG对象创建出来的那好了接下来我们重点关注的内容来了我们重点关注的内容
[07:56] 一共有这么三项首先第一项Access Key那Access Key各位应该还有印象我们创建好了存储空间之后是不是从通过我个人中心里面拿到了Access Key拿到了Secret Key当然了还有我自己的我们叫做存储空间的名称所以这些我们刚才已经准备到这边了那一个一个的Ctrl CCopy过来即可一个第二个好了接着第三个
[08:28] 所以对于我们要写这个代码考量各位的并不是代码而是考量的各位会不会填空那这三个空我已经填好了那接下来就是说我们要想上传一张图片上传到青牛云那这边呢我可以准备一张我自己的图片那我自己图片呢在今天的这个资料当中呢其实也给各位准备了一张基础的一个资源这边有一个001或者002比如说我就想上传001
[08:58] 好了我把这个001这个路径拷过来001.pngOK那这样一来我这个图片路径这是图片路径也已经准备好了那接下来呢我们就开始去关注如何进行上传如何进行上传那这边呢想跟各位说一下这边有个叫做死君key那这个死君key代表的什么含义不用他的了我跟各位简单的说一下这个key代表的是
[09:34] 存入到存储空间的空间的文件名所以呢对于这个Key指的是别看我上面上传的叫001但是上传到人家七牛人那边他会把这个图片给你改一个名字那这个名字从哪来是你自己通过Key传递过来的那所以这边呢我可以给他传递一个名称比如说呢就叫做泰斯特就是泰斯特可以了
[10:05] OK那接下来注意底下就是人家做身份认证的一些内容好了身份认证的这些我们不再关注了都是一样的那接下来呢就是可以进行一个叫做上传的一个操作上传那上传好了之后得到他的一个上传的一个返回结果那接下来我们可以一起运行一下这个TES的案例来看一下能不能把一张图片上传过去OK走
[10:45] 这边在编译啊稍微有点慢各位耐心等待一下好了已经开始执行了各位来看其实已经执行成功了那执行成功了之后我们已经上传了一张图片叫001PNG那是否传到奇牛云了呢那我们回到浏览器找到奇牛云那我现在上传到的是IHRMAN BOOKEROK刷新一把
[11:10] 那注意这里面呢有一个内容管理找到内容管理各位你会看到我上传了一张文件这个名称叫做泰斯特这边呢点击小眼睛我们可以做一个预览这个这个它这浏览器不太不太方便啊其实各位已经能够看到了没错吧就是这一张图啊这个浏览器不太好不太好弄啊OK我们已经摆张图片其实已经上传上去了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

