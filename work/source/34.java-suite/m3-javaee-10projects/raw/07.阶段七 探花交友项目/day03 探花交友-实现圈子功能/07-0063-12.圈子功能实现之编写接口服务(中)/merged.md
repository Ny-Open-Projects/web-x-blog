# 12.圈子功能实现之编写接口服务（中）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\12.圈子功能实现之编写接口服务（中）_【海量资源尽在 666java.com】.mp4
- 时长 9分25秒（音频 566s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 这个呢其实就是我们在我们去发布什么呢发布我们的一个动态啊然后呢下面我们来去做一个实现那么首先呢其实我们需要根据这个token呢去做一个用户的一个查询那么如果查询不到呢就说明了我们已经登录状态呢已经就失效了对吧那我们先来把这个代码先来整理一下那么就是因为这个参数太多了然后整个这个太长了看起来不是
[00:27] 很方便那么我们把它简单去调一下然后呢在上面这个位置我们就直接来注入谁呢叫做user Service把这个user Service注入进来那么注入进来之后呢我们就通过它呢去做一个查询那么就是这个user Service.query user by token那么就这个token这个传入进去那我们来看一下这个user对象那么我们需要对它呢去做一个判断
[00:55] 那么如果我们这个空等于是一个等于谁呢等于我们这个U的话那么就代表着什么呢我们这个是登录状态已经失效了那么就返回False就可以了那么如果没有失效的话那我们就可以去做一个调用了对吧就可以去做一个保存了那么下面呢我们需要去我们定义一个什么呢我们Publish这样的一个对象我们去New一个Publish对象
[01:25] 然后呢我们去给它填充一些这个属性那么UID呢我们去填充一个叫做U的点GetID对吧然后呢我们还需要去Set一个Text就是我们的文本的这个内容那就是它了然后呢下面呢我们还需要给它Set谁呢我们这个Location的Name那么就是我们这个Location就是我们这个地理位置的名称
[01:51] 然后呢我们再继续设置它的一个经纬度对吧那么我们把它设置进来嗯在哪在这儿那么我们把这个经纬度呢给它去填充过来然后呢做一个这样的一个填充那么下面呢还会有一些谁呢我们再来看一下有没有那么这个C type其实我们不需要去传递了对吧然后还有还有谁呢creator
[02:17] 也不需要ID也不需要这个Midius就是我们的图片那么这个我们呢暂时也不做处理因为后面我们再去做一个处理啊然后呢这个呢是我们的一个NoteClist和Clist这个我们也不做填充了那么基本上呢是不是就OK了对吧那么接下来呢我们是不是就在我们先写了照啊那么这个我们是ToDo对吧就是我们关于这图片还没处理然后呢下面我们是不是就可以去注入我们的一个对象
[02:45] 那么这个对象呢就叫什么呢就叫这个圈子对吧圈子API这个对象那么我们需要去做一个这个引用了对吧引用那么我们使用的是阿里的这个double下面的一个他对吧然后呢我们需要设置一个什么呢worth是1.1.0.0做一个引用拿到这个对象那么拿到这个对象之后呢下面呢我们在这个位置就可以调用this.这个圈子API
[03:14] 然后呢作为一个C5 Publish把这个Publish给它那么这样的话呢我们是不是就OK了对吧然后呢它的返回值是不是也是个布尔值那我们就直接把它丢到这个Return这个位置是不是就好了丢到这儿来哎这样就OK了那么接下来呢我们就把这个图片呢来处理一下那么图片呢我们其实可以看到我们的这个API呢它呢是可以上传什么呢是不是多张这个图片的那我们需要去
[03:43] 把我们的图片上传这个逻辑呢也拷贝过来然后呢我们去做一个图片的一个上传那么下面呢我们就从我们的这个就是之前的这个我们的这个SSO里面啊我们去把图片上传的一些相关的逻辑呢我们拷贝过来那么是在这里对吧首先呢其实我们是需要这个OSS Client对吧那么我们需要呢在我们的这个工程中啊去把这个OSS Client我们去导入进来
[04:13] 那么其实是在这里对吧那么我们就把它就拷过来拷贝到哪里呢我们这个server这个里面来然后丢到下面的这个位置好这样我们就直接把代码拷贝过来然后需要什么我们来拷贝什么就好了这也是我们之前所整理的逻辑那么我们把picture upload的Service去做一个拷贝拷贝到我们这个server下面有一个Service那么我们把它丢到这个里面来
[04:41] 这个呢是我们的核心的一个代码逻辑对吧那么来看一下这个里面肯定会报一些错误啊那么首先呢是这个就是我们的OSS Client它需要做一个初始化那么之前呢我们在这个位置是不是有一个阿里云Config那么我们就把它也丢到我们这个里面来对吧叫阿里云Config那么这个里面呢显然呢也会有些问题就是那么我们缺少我们这个配置文件有一个叫阿里云的Properties文件
[05:09] 那么这个呢我们同样的也来做一个拷贝那我们就把这个拷贝过来吧放到我们的这个下面来那么这个呢我们就不做修改了跟我们之前的是一样的OK那么这样的话呢这个阿里云的config这个呢就搞定了然后呢他呢是不是就这个呢就搞定了然后呢这个呢我们把这个包呢给他导入进来就OK
[05:33] 那么它还需要一些这个VO对象就是我们的一些什么这个pixel upload result这样的一个对象那我们也是通过前面的SSO呢去做一个拷贝那么就是它了然后呢我们把它拷贝到这个VO里面来拷贝到这然后呢我们就把这个包呢去导入进来导入了吗我们来看一下啊这个呢就把它导入进来
[05:57] OK这样的话呢是不是就OK了那么还缺少一个datetime对象那么这个呢我们就需要把我们那个什么joda是不是就拷贝过来啊把它呢拷贝一下然后呢再到我们的这个里面来对吧好那么这样的话呢这个是不是就搞定了看一下哎等待它的一个导入没有问题好嘞那么我们来看一下上面还有错误这个呢就拿掉
[06:25] OK这样的话呢是不是就OK了没有问题了然后呢我们就可以在我们的这个Service中啊去把它引入进来了那么就是在是不是在这个位置对吧那么在这个位置呢我们去把我们的这个picture upload Service呢去引入进来然后呢去做一个注入那么然后呢下面在这个位置就需要去做一个我们的图片上传了
[06:54] 上传那么怎么做呢我们肯定是需要做一个迭代然后呢去做一个这个上传那么我们来看一下如何去做一个上传呢是不是就调用啊我们的这个picture upload Service一个upload这样的一个方法那么它呢就会有返回一个对象那么这个对象呢是一个result或者说就叫upload啊应该叫upload result对象
[07:22] 然后呢我们来看一下那么在upload result对象中呢会有一个name这样的一个属性那么它其实就是我们的一个这个url就是我们图片的一个绝对路径我们来看一下那么其实可以看到是在这个位置是我们做了一个set这样的一个操作对吧OK好那么我们就来看一下那么我们找到刚刚的我们这个Service在这
[07:49] 那么这个呢我们是不是应该去拿一个集合去做一个接收那我们就定一个集合吧定一个这个集合死去那么就叫谁呢就叫这个image urls等于什么呢等于new一个arraylist然后呢我们通过它呢就去做一个什么呢点end这样的一个操作
[08:15] 那么这样的话呢我们是就把这个URL是不是就写到啊写到我们这个里面来了对吧然后呢在下面呢我们就需要就可以做一个set这个操作了比如说set一个medius然后呢它呢接收的是一个这个URL这个list那么这样的话呢我们是不是就搞定了对吧这样来搞定了OK
[08:37] 好那么也就是说我们到目前为止呢我们这个发布动态这个逻辑呢是不是都已经就写完了那么接下来呢我们是不是就可以把我们这种服务呢就跑起来我们来做一个测试了对吧OK好那么关于我们的这个服务的一个这个编写那我们来看讲义吧跟我们写的是不是也是基本上是一样的对吧然后呢那么写完之后呢我们一会儿就做一个测试那么刚刚呢我们是不是也是去
[09:04] 把一些关于图片的一些上传的一些这个内容都拷贝过来了所需要的依赖还有这个上传的这个代码对吧然后呢还有一些二里云的configure配置啊里面的对象啊OK那么接下来呢我们就可以做测试了好那么关于我们这个接口服务的一个编写呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package com.tanhua.server.Service;
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
package com.tanhua.server.Service;

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
package com.tanhua.server.Service;

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

