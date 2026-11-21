# 画面线理解：12.圈子功能实现之编写接口服务（中）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\12.圈子功能实现之编写接口服务（中）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:57, 01:42, 02:18, 03:01, 04:00, 04:36, 05:09, 05:50, 06:27, 07:06, 07:53, 08:45, 09:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:41:18

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现动态发布功能，包括服务层代码编写、阿里云 OSS 文件上传、以及与第三方 API 的集成。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 MovementsService.java 文件，定义了 saveMovements 方法，接收 textContent、location、longitude、latitude、multipartFile、token 参数，返回 Boolean 类型。
画面 2: 在 saveMovements 方法中，光标位于 return null; 语句前，IDE 显示了“Expression expected”错误提示。
画面 3: 在 saveMovements 方法中，光标位于 return null; 语句前，IDE 显示了“Expression expected”错误提示。
画面 4: 在 saveMovements 方法中，光标位于 return null; 语句前，IDE 显示了“Expression expected”错误提示。
画面 5: 在 MovementsService.java 文件中，添加了 @Autowired 注解的 userService 和 @Reference 注解的 quanZiApi 字段。
画面 6: 在 MovementsService.java 文件中，展示了 saveMovements 方法的实现，包括获取用户、创建 Publish 对象并设置属性、调用 quanZiApi.savePublish 方法。
画面 7: 展示了项目的 Maven 依赖配置，包括 mysql-connector-java、commons-codec、commons-io、aliyun-sdk-oss 等依赖。
画面 8: 展示了 AliyunConfig.java 文件，其中定义了 @Configuration、@PropertySource 注解，并声明了 endpoint、accessKeyId、accessKeySecret、bucketName、urlPrefix 等私有属性。
画面 9: 展示了 PicUploadService.java 文件，其中定义了 upload 方法，用于处理文件上传，包含对文件类型的判断和非法文件的处理。
画面 10: 展示了 QuanzApiImpl.java 文件，其中定义了 save 方法，用于保存时间线数据到 MongoDB。
画面 11: 在 MovementsService.java 文件中，光标位于 saveMovements 方法中，准备调用 picUploadService.upload 方法。
画面 12: 在 MovementsService.java 文件中，展示了调用 picUploadService.upload 方法并获取文件名的代码。
画面 13: 在 MovementsService.java 文件中，展示了将获取到的文件名添加到 imageUrls 列表中，并设置 publish.setMedias(imageUrls)。
画面 14: 展示了 Typora 编辑器中的 day03 四子.md 文件，其中定义了 PicUploadResult 类，并展示了测试接口的请求页面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.tanhua.server.service;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

@Service
public class MovementsService {

    /**
     * @param textContent
     * @param location
     * @param longitude
     * @param latitude
     * @param multipartFile
     * @param token
     * @return
     */
    public Boolean saveMovements(String textContent, String location, String longitude, String latitude, MultipartFile[] multipartFile, String token) {
        return null;
    }
}
```

画面 2:
```java
public Boolean saveMovements(String textContent, String location, String longitude, String latitude, MultipartFile[] multipartFile, String token) {
    if (null == token) {
        return false;
    }
    Publish publish = new Publish();
    publish.setUserId(user.getId());
    publish.setText(textContent);
    publish.setLocationName(location);
    publish.setLatitude(latitude);
    publish.setLongitude(longitude);
    return this.quanZiApi.savePublish(publish);
}
```

画面 3:
```java
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
<dependency>
    <groupId>commons-codec</groupId>
    <artifactId>commons-codec</artifactId>
</dependency>
<dependency>
    <groupId>commons-io</groupId>
    <artifactId>commons-io</artifactId>
    <version>2.6</version>
</dependency>
<dependency>
    <groupId>com.aliyun.oss</groupId>
    <artifactId>aliyun-sdk-oss</artifactId>
    <version>2.8.3</version>
</dependency>
```

画面 4:
```java
@Configuration
@PropertySource("classpath:aliyun_properties")
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

画面 5:
```java
package com.tanhua.server.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MovementsService {

    @Autowired
    private UserService userService;

    @Reference(version = "1.0")
    private QuanZiApi quanZiApi;

    /**
     * @param textContent
     * @param location
     * @param longitude
     * @param latitude
     * @param multipartFile
     * @param token
     * @return
     */
    public Boolean saveMovements(String textContent, String location, String longitude, String latitude, MultipartFile[] multipartFile, String token) {
        User user = this.userService.queryUserByToken(token);
        if (null == user) {
            return false;
        }
        Publish publish = new Publish();
        publish.setUserId(user.getId());
        publish.setText(textContent);
        publish.setLocationName(location);
        publish.setLatitude(latitude);
        publish.setLongitude(longitude);
        // todo 图片
        return this.quanZiApi.savePublish(publish);
    }
}
```

画面 6:
```java
public class PicUploadService {
    private OSSClient ossclient;
    private AliyunConfig aliyunConfig;

    public PicUploadResult upload(MultipartFile uploadFile) {
        PicUploadResult result = new PicUploadResult();
        // 图片校验，对后缀名
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
        // 上传文件
        String fileName = UUID.randomUUID().toString() + "_" + uploadFile.getOriginalFilename();
        String url = ossclient.putObject(aliyunConfig.getBucketName(), fileName, uploadFile.getInputStream());
        result.setUrl(url);
        result.setName(fileName);
        result.setStatus("success");
        return result;
    }
}
```

画面 7:
```java
package com.tanhua.server.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MovementsService {

    @Autowired
    private UserService userService;

    @Reference(version = "1.0")
    private QuanZiApi quanZiApi;

    /**
     * @param textContent
     * @param location
     * @param longitude
     * @param latitude
     * @param multipartFile
     * @param token
     * @return
     */
    public Boolean saveMovements(String textContent, String location, String longitude, String latitude, MultipartFile[] multipartFile, String token) {
        User user = this.userService.queryUserByToken(token);
        if (null == user) {
            return false;
        }
        Publish publish = new Publish();
        publish.setUserId(user.getId());
        publish.setText(textContent);
        publish.setLocationName(location);
        publish.setLatitude(latitude);
        publish.setLongitude(longitude);
        // todo 图片
        return this.quanZiApi.savePublish(publish);
    }
}
```

画面 8:
```java
@Configuration
@PropertySource("classpath:aliyun_properties")
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

画面 9:
```java
public class PicUploadService {
    private OSSClient ossclient;
    private AliyunConfig aliyunConfig;

    public PicUploadResult upload(MultipartFile uploadFile) {
        PicUploadResult result = new PicUploadResult();
        // 图片校验，对后缀名
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
        // 上传文件
        String fileName = UUID.randomUUID().toString() + "_" + uploadFile.getOriginalFilename();
        String url = ossclient.putObject(aliyunConfig.getBucketName(), fileName, uploadFile.getInputStream());
        result.setUrl(url);
        result.setName(fileName);
        result.setStatus("success");
        return result;
    }
}
```

画面 10:
```
