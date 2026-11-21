# 24.完善个人信息之图片上传（阿里云OSS服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\24.完善个人信息之图片上传（阿里云OSS服务）_【海量资源尽在 666java.com】.mp4
- 时长 7分31秒（音频 451s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下完善个人信息的一个功能那么就是用户呢在首次登录的时候呢需要去完善个人的信息包括他的性别呢名称呢还有生日呢成日城市啊头像等等那么其中的这个头像这个数据呢是需要做图片上传的那么我们这里呢采用这个阿里云的OSS作为我们的这个图片的服务器
[00:24] 那么并且呢需要对人脸做识别然后非人像的数据图片是不能够上传的所以接下来呢我们先来把这个图片的上传我们先搞定之后呢我们再去做人脸识别那么接下来呢我们来看一下如何使用这个阿里云的OSS那么
[00:44] 当然了我们想要使用这个阿里云的OSS服务那么你必须在阿里云平台去购买这个服务那么购买这个服务的这个操作步骤那我这里就不再去讲它了因为是一个比较简单的一个操作那么接下来我们就去讲怎么去使用它那么首先呢我们来导入这个依赖那么我们导入这个阿里云的OSS的这个依赖那么我们就去在这个位置吧找到我们的这个SSO
[01:13] 然后呢我们往下面这样一丢啊把这个依赖导入进来导入进来之后呢我们需要写一些配置那么我们需要在我们的这个resource这个下面创建一个阿里云的啊这样的一个public文件然后呢把下面这几个内容呢就拷贝过来那么要注意了这几个呢都是关于阿里云的一些相关的一些这个参数的参数啊那么大家需要根据你购买的阿里云的这样的一个服务
[01:44] 然后从中能够找到这样的一些参数那么大家把它填过来就可以了然后在这个位置里有一个就是我们这个叫bucketer name这个其实就是相当于是我们所存储的图片库一样这样的一个名字那么大家需要去自己创建这样的一个库那么我在这的名字叫做itcast这个探花
[02:07] 然后呢我下面的这个呢是我访问我的一些静态或者说我上传的图片的一些这个URL的前缀啊就是整个URL前面的一部分啊那么就是这个呃他这个节点呢选择是在上海的这样的一个节点啊好嘞好那么有了这个数据之后呢那么下面我们就能够去编写一些这个相关的代码了那么我们需要把我们的这个刚刚所写的一些配置
[02:35] 然后去写一个阿里云的这样的一个config并且完成一个OSS client的初始化通过这几个三个参数来完成一个初始化那么接下来我们把它来拷贝一下那么去写到config这个下面来那么是不是就已经有了这样的一个配置了OK好嘞那么可以看到在我们阿里云config中是不是要读取我们class pass下面的配置文件
[03:04] 然后呢我们在这儿去指定它的一个前缀就是二里云它就会自动去做一个识别能够识别到这个里面的一些这个参数好嘞好那么这个搞定之后啊那么接下来呢我们需要写一个我们这个picture的upload的这样的一个Service啊那么这个Service呢就不去编写了也是一个常规的一个这样的一个逻辑啊那么我们就来去把它去直接拷贝到我们这个Service里面来
[03:34] 好那么这个Service呢需要一些其他额外的一些这个对象那么把这个对象呢也来拷贝一下那还有一个叫做pix upload result放到这哎看他OK了吗还有报错那么把这个datetime就是我们的joda里面的他啊那么这个哎这个里面好像是我们是不是没有导包呢joda没有导包那我们来需要导一下
[04:06] 没有那我们就来导一下吧那么导的这叫做jodtime好这样的话呢就OK了那么我们在这个里面呢把它导入进来就没有问题了好那么下面呢我们就可以来测试一下这样吧我们还是把这Controller我们写完之后呢我们就直接做一个测试啊那么把这个Controller也拷贝过来然后呢就丢到这那直接去做一个上传就可以了
[04:35] 好那么接下来呢我们把我们这个服务呢重新启动一下啊然后呢我们去测试一下我们这个呃上传看有没有问题好那么目前我们这个服务呢就已经跑起来了那么在这个位置呢我去打一个钝点然后呢我们在这个里面来打个钝点啊好那么接下来我们可以来测试一下那么我们可以看到他的这个呃就是路径啊就是pixel upload那么我们就把它往这一丢
[05:05] 然后呢发起的是post请求然后呢这个类型呢是要选择啊在这然后呢这个文件啊我们要去选择文件名字呢就叫fail填到这然后呢我们去选择一个选择一个文件就可以了那么我们在资料中啊找到我们这个测试图片啊比如说我们就用它来做一个测试然后呢走嗯他说这个呃我们来看一下啊
[05:35] 他说这个发送这个可能是我这个工具这个问题是在这个位置我们扫了一个斜杠扫了一个斜杠导致那么我们来点击走好请求来了然后我们进入然后往下面走走走我们可以看一下这个大致的可以看一下这个逻辑那么就是我们对后缀做一个校验文件后缀做校验然后我们获取他的名字获取他的名字然后我们去通过这个OSS client去做一个上传
[06:05] 上传到阿里云的服务器那么上传成功返回返回OK然后呢我们可以来通过一下走好那么我们可以看到返回的这个地址呢就是有这样的一个地址了那么我们尝试的去打开看一下OK是不是就刚刚我们的所看到的这张图片呢对吧那么我们其实也可以登录到阿里云呢来看一下啊那么我来找一下吧阿里云然后呢我们去登录一下
[06:35] 那么登录然后呢我这边使用这个一个淘宝账号去做一个登录啊点击这个登录然后呢我们进入之后呢找到找到这个OSS服务那么我们找到一个控制台吧然后呢控制台中呢有一个叫做OSS对象的存储那么可以看到啊然后在这个位置探花这个位置然后呢我们可以
[07:05] 找到这个文件的管理那么可以看到这个是在8月份2号然后上传一张这张图片这个图片就是我们刚刚所上传的这张图片那么这样的话我们是不是已经就把它上传到这个阿里云了OK好那么测试就是这样最后是这样的一个结果OK好那么关于这个图片的上传就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中实现图片上传功能的完整流程，包括配置阿里云 OSS、编写服务层代码、调试并测试上传接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 UserController 中的 loginVerification 方法，用于处理登录验证，从请求体中获取手机号和验证码，并调用 userService.login 方法。
画面 2: 在 IDEA 中右键点击 pom.xml 文件，弹出菜单，显示了项目依赖的 Maven 依赖项，包括 RocketMQ-spring-boot-starter、RocketMQ-client、jjwt 和 aliyun-oss-sdk。
画面 3: 在 Typora 编辑器中打开 day01 项目搭建及登录个人资料.md 文档，显示了 4.1.3 PicUploadService 的内容，其中包含 AliyunConfig 配置类的代码。
画面 4: 继续在 Typora 中显示 PicUploadService 的代码，主要展示文件上传失败时的处理逻辑，包括设置错误状态并返回。
画面 5: 在 IDEA 中展示 PicUploadService 类的结构，包含 @Service 注解、@Autowired 注解的 OSSClient 和 AliyunConfig 字段，以及 upload 方法。
画面 6: 在 IDEA 中展示 pom.xml 文件，显示了项目依赖的 Maven 依赖项，包括 RocketMQ-client、jjwt 和 aliyun-oss-sdk。
画面 7: 在 IDEA 中展示 PicUploadService 类的代码，主要展示文件上传的 try-catch 块，用于处理上传失败的情况。
画面 8: 在 IDEA 中展示 PicUploadService 类的代码，主要展示文件上传的 try-catch 块，用于处理上传失败的情况。
画面 9: 在 Advanced REST Client 中配置上传图片的请求，选择文件 1.jpg，设置 Content-Type 为 multipart/form-data。
画面 10: 在 IDEA 中展示 PicUploadService 类的代码，主要展示文件上传的 try-catch 块，用于处理上传失败的情况。
画面 11: 在 IDEA 中展示 PicUploadService 类的代码，主要展示文件上传成功后的处理逻辑，包括设置状态为 "done"、设置 URL 和 ID。
画面 12: 浏览器中显示阿里云登录页面。
画面 13: 浏览器中显示空白页面。
画面 14: 在 Typora 中显示上传成功后的 JSON 响应数据，包含 url 和 response 字段，以及一个显示上传图片的预览。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@PostMapping("loginVerification")
public ResponseEntity<Object> login(@RequestBody Map<String,String> param) {
    String mobile = param.get("phone");
    String code = param.get("verificationCode");
    String token = this.userService.login(mobile, code);
    if(StringUtils.isNotEmpty(token)) {
        String[] ss = StringUtils.split(token, separatorChar: '|');
    }
}
```

画面 2:
```xml
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-spring-boot-starter</artifactId>
    <version>2.0.0</version>
</dependency>
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-client</artifactId>
    <version>4.3.2</version>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.9.1</version>
</dependency>
<dependency>
    <groupId>com.aliyun.oss</groupId>
    <artifactId>aliyun-oss-sdk</artifactId>
    <version>2.8.3</version>
</dependency>
```

画面 3:
```java
import com.aliyun.oss.OSSClient;
import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource("classpath:aliyun.properties")
@ConfigurationProperties(prefix = "aliyun")
@Data
public class AliyunConfig {
    private String endpoint;
    private String accessKeyId;
    private String accessKeySecret;
    private String bucketName;
    private String urlPrefix;

    @Bean
    public OSSClient ossClient() {
        return new OSSClient(endpoint, accessKeyId, accessKeySecret);
    }
}
```

画面 4:
```java
if (!isLegal) {
    fileUploadResult.setStatus("error");
    return fileUploadResult;
}
// 文件拆解
String fileName = uploadFile.getOriginalFilename();
String filePath = getFilePath(fileName);
// 上传阿里云
try {
    // 目录结构：images/2018/12/29/xxxx.jpg
    ossClient.putObject(aliyunConfig.getBucketName(), filePath, new ByteArrayInputStream(uploadFile.getBytes()));
} catch (Exception e) {
    e.printStackTrace();
    fileUploadResult.setStatus("error");
    return fileUploadResult;
}
```

画面 5:
```java
package com.tanhua.sso.Service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PicUploadService {
    // 允许上传的格式
    private static final String[] IMAGE_TYPE = new String[]{"bmp", "jpg", "jpeg", "gif", "png"};
    @Autowired
    private OSSClient ossClient;
    @Autowired
    private AliyunConfig aliyunConfig;
    public PicUploadResult upload(MultipartFile uploadFile) {
        PicUploadResult fileUploadResult = new PicUploadResult();
        // 图片做校验，对后缀名
        boolean isLegal = false;
    }
}
```

画面 6:
```xml
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.9.1</version>
</dependency>
<dependency>
    <groupId>com.aliyun.oss</groupId>
    <artifactId>aliyun-oss-sdk</artifactId>
    <version>2.8.3</version>
</dependency>
```

画面 7:
```java
// 文件拆解
String fileName = uploadFile.getOriginalFilename();
String filePath = getFilePath(fileName);
// 上传阿里云
try {
    // 目录结构：images/2018/12/29/xxxx.jpg
    ossClient.putObject(aliyunConfig.getBucketName(), filePath, new ByteArrayInputStream(uploadFile.getBytes()));
} catch (Exception e) {
    e.printStackTrace();
    fileUploadResult.setStatus("error");
    return fileUploadResult;
}
```

画面 8:
```java
// 图片做校验，对后缀名
boolean isLegal = false;
for (String type : IMAGE_TYPE) {
    if (StringUtils.endsWithIgnoreCase(uploadFile.getOriginalFilename(), type)) {
        isLegal = true;
        break;
    }
}
if (!isLegal) {
    fileUploadResult.setStatus("error");
    return fileUploadResult;
}
```

画面 9:
```text
Add new file field
file 1.jpg
Content-Type: multipart/form-data
```

画面 10:
```java
// 图片做校验，对后缀名
boolean isLegal = false;
for (String type : IMAGE_TYPE) {
    if (StringUtils.endsWithIgnoreCase(uploadFile.getOriginalFilename(), type)) {
        isLegal = true;
        break;
    }
}
if (!isLegal) {
    fileUploadResult.setStatus("error");
    return fileUploadResult;
}
```

画面 11:
```java
// 上传成功
fileUploadResult.setStatus("done");
fileUploadResult.setName(this.aliyunConfig.getUrlPrefix() + filePath);
fileUploadResult.setId(String.valueOf(System.currentTimeMillis()));
return fileUploadResult;
```

画面 12:
```text
https://account.aliyun.com/login/qc_login.htm?spm=20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20171220.20

