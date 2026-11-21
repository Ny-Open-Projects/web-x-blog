# 12.商户资质申请-上传证件-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\12.商户资质申请-上传证件-接口实现【海量资源尽在 666java.com】.mp4
- 时长 10分35秒（音频 635s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来我们继续来编写啊商户平台应用证件上传的接口实现刚才我们完成了工具类的编写下面呢我们就准备让Service来调用这个工具类那个工具类呢这里边大家可以看到有很多的参数好那么我们把这个参数呢先把它罗列到这儿好那现在呢各位来看一下这是几个密钥包括bucket这个文件的字节这是不是在这儿啊然后文件名称都在这儿
[00:30] 所以其实前边这几个参数我们是需要去配置的那怎么配置呢我们一般来说这种配置信息我们是不是都统一写在了Necros上面对吧所以这里边我们来看讲义我们在讲义呢把这个配一下七牛的一个什么URL包括两个密钥包括bucket我们都在我们的Necros进行配置好那么Necros配置的话我们就需要找到你配置的地方
[00:53] 在配置列表然后点到我们的Lab Space然后找到我们三户平台应用的配置文件然后点开编辑在这是这样吗你搞清楚你是哪个配置文件你现在弄的是Merchant-ApplicationApplication是不是指的是我们三户平台应用的对不对那你这个Service是哪是不是就是三户平台应用对你要搞清楚你要是搞不清楚配置文件的话你配了你是读取不到的
[01:25] 一定要注意是吧好那现在我们是不是把它配上去了配上去之后呢这里边这些地址我们是不是要补齐啊好补齐地址的话我们是不是就需要打开我们的亲友对吧然后这里边呢我们来看一下啊这里边我们配的是他的一个什么给我们的一个融合CDN的一个域名啊这个域名就是我们访问文件的一个域名好我们找到没错吧好然后呢拿到这个域名之后呢还有就是什么呀他的
[01:57] 它的key对吧它的key那这个key呢我们要去哪找呀原来我是不是给大家说过密钥从密钥管理当中来配置嗯然后呢还是复制啊还是复制然后呢继续再复制好这个key呢大家一定要自己去清邮局注册然后呢刚开始临时空间是不要钱的啊你自己注册因为这个key呢稍后呢我这边可能就删除了然后呢再复制它的bucket嗯
[02:28] 然后继续你把它贴到这到这这个配置咱们是搞定了搞定之后发布好到这这个配置信息就OK了OK了之后呢有时候老师那怎么拿到嘞那是不是就是我们之前说过用viral注解来拿呀viral注解拿的话需要怎么做是不是需要找到你Necros里面刚才配置的这个配置文件的这个配置信息的keyoss.cnew.url就这么拿
[02:59] 所以现在你要拿的是七牛的URL对吧所以这是七牛的URL对吧然后呢它是刚才我们看到它的key是oss.七牛.URL是不是就这么拿对打开讲义啊这块代码呢就比较简单所以我就给大家复制过去然后呢这个代码就是读取刚才你在Necros里边配置的这些参数OK吧好那么配置好了之后呢
[03:27] 那现在你的目的是不要调用它这个工具类啊那你就一个一个的给它传进去就行了这是从配置文件拿到的对吧然后呢还有配置文件拿到的还有一个就是bucket这也是配置文件拿到的好再有这是它直接传进来的参数再有filename各位这个工具类咱们是不是就搞定了看见了吗好然后继续这儿
[03:54] 如果上传成功的话那你是不是要返回一个文件的一个访问地址而这个访问地址一定记着啊是绝对路径什么是绝对路径绝对路径就是前边七牛的URL要加上你这个文件的名称懂我意思吧你加上文件的名称的话这里边你要怎么做啊你最终要组成的一定是这么一个地址
[04:25] 看见了吗一定是他对不对所以这里边呢我们要注意一点的就是你配置的这个信息最终是和他正好拼装而成你明白吧那怎么拼装而成的你比如说举个例子你看这他后边你要加一个杠然后咱们的文件名称正好往后边一累加是不是就正好拼装成了懂我意思吧所以这个URL后边你看这是一个地址吧这个地址
[04:54] 哎加上哎刚才我们上传文件的这个名称回车是不是就正好啊所以这样的话我们就知道了注意啊把刚才那块我们改变了之后就发布一下然后再回到代码然后这呢是不是就可以加上我们的这个file name了你告诉我这样是不是返回去的是不是就是一个完整的一个路径对吧当然话又说回来了我们说了吗轻牛
[05:23] 这个云如果上传成功它你会返回一个绝对路径那如果没有成功呢也就是这一句它报错了工具类报错了那怎么弄那我建议你补一个异常吧然后呢我们之前学过异常处理咱们这里头是不是就可以抛出我们自己定义的一个异常而自己定义的异常这里边呢我们当初是不是有一个叫异常代码的一个类这边你看是不是就可以我们指定叫上传错误是不是上传文件错误
[05:53] 看懂了吗这就是我们的Service是不是就搞定了好那Service搞定了之后呢接下来我们要做什么呀是不是就是Controller来调用我们的这个servicecontroller调用Service是首先把Service给它注进去然后在这儿我们是不是就可以来调用怎么调用你看是不是有一个叫做upload然后这里边又有两个参数一个是什么文件的字节一个是文件名称
[06:24] 对不对那这个文件的字节的宿主我们是不是就可以直接通过multipartfile来拿到呀可以拿到吧看然后还有一个还有一个是啥还有一个就是我们说的文件名了对不对这个时候文件名的话我们就需要干嘛去构造生成创建一个什么生成一个文件名称这个文件名称一定记着要
[06:53] 保证它的什么唯一对不对因为你这里边我们说让你来谁调用这个Service工具类谁来控制这个文件名那你要保证它唯一好那保证唯一怎么做你上传的文件首先我们是不是也可以采用我们说的这个UUID的方法是不是那关键有一点要注意你上传的有PNG有GPG等等各种拓展名的文件你首先要拿到什么拿到它的拓展名
[07:23] 你明白吗对你要拿到它的扩展名好那拿到扩展名之后呢拿到扩展名之后你就可以组成一个完整的名称但是你先取扩展名扩展名怎么取扩展名你要拿到你必须拿到什么文件的原始名称那文件的原始名称怎么拿这就是文件原始名称那你要想拿扩展名的话你是不是就需要怎么弄你就比如说
[07:54] 看好你就比如说这个文件这是文件的原始名称你拿扩展名是不是一点分割的来取出后边这堆你懂我意思吧所以各位现在我们要拿这个扩展名的话你就需要从原始文件当中来拿对吧拿那么注意看咱们说这个扩展名应该是这么做首先你要拿到这个位置
[08:24] 对吧拿到了这个位置的话那么你就需要来-1啥意思各位这一句大家理解吗这是不是就找到点的位置懂吗找到点的位置我再-1是不是就从点前边开始来取数据这是不是就拿到扩展名对吧拿到了扩展名我现在要做的事是不是要组成一个文件名那这个文件名就是我们可以用我们的什么UUID
[08:54] 然后加这个扩展名你告诉我这行不行这种文件名组织的方法各位是不是大家能够理解最后我们是不是就把这个文件名给它放进去这个上传是不是就完工了那么这个上传完工了之后呢注意看啊注意看啊点它是不是返回了一个地址对吧而你这里边是不是也要返回一个地址就control了是不是也要返回地址所以return直接返回大家理解了吗
[09:25] 这就是我们说的整个的上传的一个过程咱们这个代码实现部分是不是就完工了好我再把代码的思路给大家捋一下注意听Ctrl 这里边会解析出扩展名然后原始文件名称目的只有一个拿到文件名称这个文件名称由调用方来控制生成一个 UUID就是不重复的一个文件名称然后把它传给我们的Service Upload 方法然后Service Upload 方法
[09:54] 从9house里边拿到这一堆key以及青雄军URL包括bucket然后准备开始执行上传动作上传的话调用我们的工具类这工具类是不是我们封装好的工具类让它来调最终上传成功之后Service会把完整的文件下载路径给Controller返回而Controller就会返回给前端前端将来再次请求自治申请的时候就把这个信息最终会请求到我们商务平台应用商务平台应用
[10:22] 就保存到我们的什么数据库当中大家这个过程理解了吧也就是将来在这儿呢就是一个绝对路径了嗯好那么这个呢就是我们整个接口的实现

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成七牛云文件上传功能，包括配置 Nacos 服务、编写服务层和控制器层代码，并在七牛云控制台管理相关配置。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程大纲，当前章节为“2.6.2 完善代码”，子章节“2. FileServiceImpl”中提到“在Nacos七牛云上传参数”，并展示了配置项：oss: qiniu: url: "" accessKey: "" secretKey: "" bucket: ""。
画面2: 展示了 Nacos 配置管理界面，用于创建或编辑配置，Data ID 为 merchant-application.yaml，Group 为 SHANJUPAY_GROUP，配置格式为 TEXT。
画面3: 展示了七牛云控制台，显示了存储空间 shanjupay-m1 的信息，包括空间概览、API 请求等，并在“融合 CDN 测试域名”区域显示了测试域名 q2cd31bb.bkt.clouddn.com。
画面4: 与画面3内容相同，为七牛云控制台页面，显示了测试域名 q2cd31bb.bkt.clouddn.com。
画面5: 展示了课程大纲，当前章节为“2.6.2 完善代码”，子章节“2. FileServiceImpl”中提到“在Nacos七牛云上传参数”，并展示了配置项：oss: qiniu: url: "" accessKey: "" secretKey: "" bucket: ""。
画面6: 展示了 IDEA 编辑器中的 FileServiceImpl.java 文件，其中定义了上传文件的方法，使用了 @Value 注解注入配置，并调用了 QiniuUtils 的 upload 方法。右侧显示了 Profiles 列表。
画面7: 展示了 Nacos 配置管理界面，配置已编辑完成，Data ID 为 merchant-application.yaml，Group 为 SHANJUPAY_GROUP，配置内容为：server: port: 8080 spring: application: name: merchant-application context-path: / Swagger: enable: true oss: url: "http://qzcd31bb.bkt.clouddn.com/"。
画面8: 展示了 IDEA 编辑器中的 FileServiceImpl.java 文件，其中定义了上传文件的方法，使用了 @Value 注解注入配置，并调用了 QiniuUtils 的 upload 方法。右侧显示了 Profiles 列表。
画面9: 展示了 IDEA 编辑器中的 FileServiceImpl.java 文件，其中定义了上传文件的方法，使用了 @Value 注解注入配置，并调用了 QiniuUtils 的 upload 方法。右侧显示了 Profiles 列表。
画面10: 展示了 IDEA 编辑器中的 MerchantController.java 文件，其中定义了上传文件的接口，使用了 @PostMapping 注解，并调用了 fileService.upload 方法。
画面11: 展示了 IDEA 编辑器中的 MerchantController.java 文件，其中定义了上传文件的接口，使用了 @PostMapping 注解，并调用了 fileService.upload 方法。
画面12: 展示了课程大纲，当前章节为“3. MerchantController”，并展示了 MerchantController.java 文件中的代码，其中定义了上传文件的接口，使用了 @PostMapping 注解，并调用了 fileService.upload 方法。
画面13: 展示了 IDEA 编辑器中的 FileServiceImpl.java 文件，其中定义了上传文件的方法，使用了 @Value 注解注入配置，并调用了 QiniuUtils 的 upload 方法。右侧显示了 Profiles 列表。
画面14: 展示了课程大纲，当前章节为“3. MerchantController”，并展示了 MerchantController.java 文件中的代码，其中定义了上传文件的接口，使用了 @PostMapping 注解，并调用了 fileService.upload 方法。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1:
oss:
  qiniu:
    url: ""
    accessKey: ""
    secretKey: ""
    bucket: ""

画面2:
Data ID: merchant-application.yaml
Group: SHANJUPAY_GROUP
配置格式: TEXT

画面7:
server:
  port: 8080
spring:
  application:
    name: merchant-application
  context-path: /
Swagger:
  enable: true
oss:
  url: "http://qzcd31bb.bkt.clouddn.com/"

画面6:
package com.shanju.pay.merchant.Service;
import com.shanju.pay.common.domain.BusinessException;
import com.shanju.pay.common.domain.CommonErrorCode;
import com.shanju.pay.common.util.QiniuUtils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class FileServiceImpl implements FileService {

    @Value("${oss.qiniu.url}")
    private String qiniuUrl;

    @Value("${oss.qiniu.accessKey}")
    private String accessKey;

    @Value("${oss.qiniu.secretKey}")
    private String secretKey;

    @Value("${oss.qiniu.bucket}")
    private String bucket;

    //上传文件
    @Override
    public String upload(byte[] bytes, String fileName) throws BusinessException {
        //调用七牛云的上传接口
        return QiniuUtils.upload(qiniuUrl, accessKey, secretKey, bucket, bytes, fileName);
    }
}

画面10:
//上传证件
@PostMapping("/upload")
public String upload(@ApiParam(value = "上传的文件", required = true) @RequestParam("file") MultipartFile file) {
    //调用fileService上传文件
    //生成的文件名具有唯一性，确保文件唯一
    String originalFilename = file.getOriginalFilename();
    String suffix = originalFilename.substring(originalFilename.lastIndexOf(".")+1);
    String fileName = UUID.randomUUID().toString() + suffix;
    //上传文件，返回文件下载url
    String fileUrl = fileService.upload(file.getBytes(), fileName);
    return fileUrl;
}

画面12:
@AutoWired
private FileService fileService;

@PostMapping("/upload")
public String upload(@ApiParam(value = "上传的文件", required = true) @RequestParam("file") MultipartFile file) {
    //原始文件名称
    String originalFilename = file.getOriginalFilename();
    //文件后缀
    String suffix = originalFilename.substring(originalFilename.lastIndexOf(".")+1);
    //文件名称
    String fileName = UUID.randomUUID().toString() + suffix;
    //上传文件，返回文件下载url
    String fileUrl = fileService.upload(file.getBytes(), fileName);
    return fileUrl;
}

画面13:
@Service
public class FileServiceImpl implements FileService {

    @Value("${oss.qiniu.url}")
    private String qiniuUrl;

    @Value("${oss.qiniu.accessKey}")
    private String accessKey;

    @Value("${oss.qiniu.secretKey}")
    private String secretKey;

    @Value("${oss.qiniu.bucket}")
    private String bucket;

    //上传文件
    @Override
    public String upload(byte[] bytes, String fileName) throws BusinessException {
        //调用七牛云的上传接口
        return QiniuUtils.upload(qiniuUrl, accessKey, secretKey, bucket, bytes, fileName);
    }
}

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

