# 画面线理解：24.完善个人信息之图片上传（阿里云OSS服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\24.完善个人信息之图片上传（阿里云OSS服务）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:07, 01:26, 02:47, 03:25, 03:46, 04:08, 04:29, 04:56, 05:26, 05:52, 06:09, 06:36, 06:57, 07:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:14:08

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中实现图片上传功能的完整流程，包括配置阿里云 OSS、编写服务层代码、调试并测试上传接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 UserController 中的 loginVerification 方法，用于处理登录验证，从请求体中获取手机号和验证码，并调用 userService.login 方法。
画面 2: 在 IDEA 中右键点击 pom.xml 文件，弹出菜单，显示了项目依赖的 Maven 依赖项，包括 rocketmq-spring-boot-starter、rocketmq-client、jjwt 和 aliyun-oss-sdk。
画面 3: 在 Typora 编辑器中打开 day01 项目搭建及登录个人资料.md 文档，显示了 4.1.3 PicUploadService 的内容，其中包含 AliyunConfig 配置类的代码。
画面 4: 继续在 Typora 中显示 PicUploadService 的代码，主要展示文件上传失败时的处理逻辑，包括设置错误状态并返回。
画面 5: 在 IDEA 中展示 PicUploadService 类的结构，包含 @Service 注解、@Autowired 注解的 OSSClient 和 AliyunConfig 字段，以及 upload 方法。
画面 6: 在 IDEA 中展示 pom.xml 文件，显示了项目依赖的 Maven 依赖项，包括 rocketmq-client、jjwt 和 aliyun-oss-sdk。
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
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
    <version>2.0.0</version>
</dependency>
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-client</artifactId>
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
package com.tanhua.sso.service;

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
