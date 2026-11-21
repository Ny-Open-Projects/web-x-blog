# 10.商户资质申请-上传证件-接口定义

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\10.商户资质申请-上传证件-接口定义【海量资源尽在 666java.com】.mp4
- 时长 9分46秒（音频 586s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们就来实现商户平台应用来提供证件上传的接口根据我们前面说的交互流程前端呢需要上传证件信息到商户平台应用商户平台应用呢远程请求亲友云来上传证件照好那下面我们来看这个接口如何定义呢这个接口应该是要商户管理平台的这个应用这个服务
[00:30] 就是我们说的application这个工程好那也就是说在control了当中啊我们是不是需要去写一个接口在这那么这个接口各位我们可以思考一下我一会就写一个叫上传文件对吧而这个上传文件里面呢它是不是要去调用七牛云的接口来上传文件呀所以这时候我们就需要想一般来说也有逻辑的地方呢我们都会把它
[00:59] 放在一个独立的什么Service当中好所以我们先在我们看到的这个Service这儿定义一个file Service那到这儿呢我要说一下其实各位看这个application这个应用啊这里边定的Service包括前边我们定义的发送验证码这个Service呢我们都不是对外暴露一个double服务
[01:22] 只是用于给商户平台自己去干嘛去本地调用看见了吗和我们前边这个商户服务里面写的Service是完全不一样的商户服务里面写的Service各位你都看见了它都是要对外暴露什么double服务的接口供商户平台应用以及其他为服务去使用所以它这个double服务的接口我们你看我们是不是都用一个叫double给我们提供一个Service注解
[01:51] 而商户平台应用里边我们这里边写的发送验证码的Service以及文件上传的Service都是仅供谁呀仅供我们说的商户平台应用自己的这个程序去使用的所以它的Service注解我们看到它是使用了什么Spring它给我们提供了一个什么Service注解好那么在这个里头呢我们来看在这儿呢我们就会写一个接口这是个interface
[02:21] interface好那么这个接口呢我们说要提供一个叫上传文件前面呢我们其实已经测试了这个上传文件是不是当初在common的这个工程当中啊我们是不是当初建了一个叫七牛云youtube这是不是当初我们测试上传文件的这个东西啊那好那也就是说我们看看怎么样把它这堆代码
[02:48] 对吧我们要把它提取到哪里提取到这个接口当中当前我们只是定义接口一会我们再实现也就是说一会Service的方法就是这一堆代码但是我们要把有一些参数给它抽出来你比如说key看见了吗还有bucket这些我觉得都要抽出来那么这里面我们来看如何抽取所以这里面我们要定义我们的接口的参数
[03:19] 首先呢我们知道你要上传文件你是不是需要给我一个什么文件的一个字节素组呀我们原来测试过根据字节素组来上传文件对不对那么那这个文件的字节素组你给我了之后呢你是不是还要给我一个文件名对那有时候老是不对呀你刚才不是说还要把这些什么key给抽取出来你看啊我这么设计各位看这是不是一个工具类这个工具类是不是在common当中
[03:49] 那一会儿呢我准备在这提供一个什么上传文件的工具方法这工具方法我们准备把谁抽取出来比如说这个什么什么key啊密钥呀还有bucket呀对吧甚至还有我们说的这个filename呀对吧就是这个key嘛file的这个文件的名称嘛所以这些我都会在工具内给它抽出来
[04:19] 明白吗而各位注意而我们刚才说的这个file Service那我只会定义一个方法里边提供一个什么两个参数啊注意我们打开讲义看一下啊一个是字节输出一个是file name将来这个什么这个file Service的方法它呢会调用工具类懂吧我给你写一下啊
[04:48] 首先我们这里边要定义一个什么一个接口这个接口它的参数我刚才是不是分析过了upload是不是这些参数然后呢注意再看啊那它的返回值呢它的返回值返回啥那最终你是不是得把这个文件的这个地址给我返回这是不是就是它的返回值对所以这里边呢我们来看它的参数是什么
[05:20] 这叫上传文件然后呢这个叫文件的字结束组这个叫文件名文件名刚才我们说了我们是不是使用UUID的方法对吧返回的是文件名文件名这写错了叫文件名有时候老师这两文件名有啥区别这个文件名应该说确切的说是叫文件的访问路径这个是一个什么
[05:51] 绝对的URL地址对吧哎那我的意思是啥呢以后呢我们是不是要写实现类啊对吧我在这写实现类嘛然后上面是不是写一个Service注解呀对然后呢这里边你要实现刚才我们说的这个什么fileservice的接口吧对我的意思是在这我要让它调用common下边的工具类懂这意思了吧哎我在这调用common下边的工具类好那所以说
[06:23] 一会呢就让他在这里调用工具类那还有这只是一个Service的接口对吧那我们刚才说了在control的那儿你是不是要调用一个干嘛定义一个接口来调用刚才我们写的file Service理解吗所以这里面呢我们要把刚才定义的一个file Service这个给他注进去然后呢在这儿呢我们就定义一个上传什么上传证件
[06:53] 造这样一个接口这个接口是给前端调用的对吧所以这个接口呢我们来看一下啊前端呢它只会给你上传一个什么文件嘛然后呢最终你是不是给前端返回一个什么文件的访问地址嘛然后这里面呢Spring MVC来上传文件我们是不是之前学过是不是有一个叫Multipart File对吧然后呢
[07:20] 我们就可以在这个里头调用刚才我们写的file Service来上传文件懂我意思了吧一会我们再实现但是你这个整体结构你得知道啊好那上面呢我们是不是可以给他一个底色这叫上传证件照对吧然后呢你上传了吗这是不是要用post的呀在这个url得指定没错吧然后呢你这个Swagger参数你是不是得
[07:50] 说一下这就是我们说的API Param然后呢给它一个参数说明这叫这应该是我们具体的一个上传什么啊证件照证件照是吧好那现在呢我们就拿到了这个什么这个具体的这个MultipartFile然后呢就可以调用File Service一会实现的时候我们再说啊那我们先把这个接口给它完善了好还有一个
[08:22] 这里边要注意就是我们去上传的时候我们之前学过Sprite MVC我们是不是要指定清楚这个参数的名称这一步不能少我们和讲义保持一致它叫filefile的话将来我们去上传文件的时候这个参数的名字就叫file你这样的ABC将来上传文件的那个名字内幕就是ABC一定记得一会我给大家演示这个测试
[08:49] 好到这我们的接口就定义好了我再给大家捋一遍啊呃这个交互流程上面说的前端要上传证件照到商户平台应用这个他要暴露一个http的接口我们这个接口是不是在这没错吧然后呢这个接口呢他会调用我们商户平台应用下边本地的一个Service的这个一个bin然后呢进行文件的上传
[09:15] 因为我们为什么定义Service不在这个Controller里面直接写我刚才说过你进行文件上传的时候难免有一些业务逻辑的判断所以这里边我们就让什么让Controller来调用我们本地的这个file Service注意这是本地调用不是远程调用而这个file Service里边调用common下面的工具类最终来访问清流云完成文件的上传这就是我们的一个什么接口的定义咱们是不是就写完了
[09:45] 好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在商户平台应用中实现上传证件照片到七牛云的接口开发，包括定义接口、实现服务层和控制器层代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档目录，当前定位在“3.3.1.1 接口定义”，介绍接口功能：前端携带证件信息请求商户平台应用，商户平台请求七牛云上传图片，七牛云返回图片地址给前端。
画面2：在IDE中打开MerchantController，展示一个测试接口，用于演示如何接收参数。
画面3：在IDE中选中FileService接口文件，准备编写服务层代码。
画面4：在IDE中为FileService接口添加@Service注解，准备实现文件上传功能。
画面5：在IDE中打开QiniuUtils工具类，展示用于测试上传的代码，包括配置信息和文件上传逻辑。
画面6：展示文档中FileService接口的定义，包含上传文件的方法签名。
画面7：在IDE中展示QiniuUtils工具类中用于生成随机文件名的代码。
画面8：在IDE中展示FileService接口中上传文件的方法定义，包含异常处理。
画面9：在IDE中展示@Service注解的可用选项，准备为FileService添加注解。
画面10：在IDE中展示@Autowired注解的可用选项，准备为MerchantController注入服务。
画面11：在IDE中展示MerchantController中使用@RequestBody注解接收上传的文件。
画面12：在IDE中展示MerchantController中使用@ApiOperation注解定义上传证件照的接口。
画面13：在IDE中展示MerchantController中使用@ApiOperation注解定义测试接口。
画面14：展示系统交互流程图，说明前端、商户平台应用和七牛云之间的交互流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2代码：
```java
@ApiOperation("测试")
@GetMapping(path = "/hello")
public String hello() { return "hello"; }

@ApiOperation("测试")
@ApiOperation(value = "姓名", required = true, dataType = "string")
@PathVariable(value = "name")
public String hi(String name) { return "hi,"+name; }
```

画面3代码：
```java
package com.shanjupay.merchant.Service;
// @author Administrator
// @version 1.0
// @Service
public class FileService {
```

画面4代码：
```java
@Service (org.springframework.stereotype)
```

画面5代码：
```java
//测试文件上传
private static void testUpload() {
//约定一个带地区 Region 对象的配置类，指定存储区域，和存储空间向选择的区域一致
Configuration cfg = new Configuration(Region.huanan());
//并也设置上传过程
UploadManager uploadManager = new UploadManager(cfg);
//生成上传凭证，然后准备上传
String accessKey = "vG3rn6ZU9J_KCJ8OV-76A38XbpgCk66tKDOf_";
String secretKey = "p04h8a1151UXAb0K3OpZmPaGusJ_9Lb6gJus";
String bucket = "shanjupay-ri";
//默认不指定文件名的情况下，以文件内容的hash值作为文件名
String key = UUID.randomUUID().toString() + ".png";
FileInputStream fileInputStream = null;
try {
String filePath = "F:\\develop\\shanjupay\\1.png";
fileInputStream = new FileInputStream(filePath);
//得到本地文件的字节数组
byte[] bytes = IOUtils.toByteArray(fileInputStream);
//上传文件
uploadManager.putBytes(bucket, key, bytes);
}
```

画面6代码：
```java
import org.springframework.web.multipart.MultipartFile;

/**
 * 文件服务
 */
public interface FileService {
    /**
     * 上传文件
     * @param bytes 文件字节
     * @param filename 文件名称
     * @return 文件下载路径
     * @throws BatchUpdateException
     */
    public String upload(byte[] bytes,String filename) throws BatchUpdateException;
}
```

画面7代码：
```java
//测试文件上传
private static void testUpload() {
//约定一个带地区 Region 对象的配置类，指定存储区域，和存储空间向选择的区域一致
Configuration cfg = new Configuration(Region.huanan());
//并也设置上传过程
UploadManager uploadManager = new UploadManager(cfg);
//生成上传凭证，然后准备上传
String accessKey = "vG3rn6ZU9J_KCJ8OV-76A38XbpgCk66tKDOf_";
String secretKey = "p04h8a1151UXAb0K3OpZmPaGusJ_9Lb6gJus";
String bucket = "shanjupay-ri";
//默认不指定文件名的情况下，以文件内容的hash值作为文件名
String key = UUID.randomUUID().toString() + ".png";
FileInputStream fileInputStream = null;
try {
String filePath = "F:\\develop\\shanjupay\\1.png";
fileInputStream = new FileInputStream(filePath);
//得到本地文件的字节数组
byte[] bytes = IOUtils.toByteArray(fileInputStream);
//上传文件
uploadManager.putBytes(bucket, key, bytes);
}
```

画面8代码：
```java
import rx.internal.operators.BackpressureUtils;
// @author Administrator
// @version 1.0
// @Service
public interface FileService {
    public upload(byte[] bytes,String fileKey) throws bulk
```

画面9代码：
```java
@Service (org.springframework.stereotype)
```

画面10代码：
```java
@Autowired
//注入本地的Bean
@Service saasService
```

画面11代码：
```java
//使用MapStruct转换对象
MerchantDTO merchantDTO = MerchantRegisterConvert.INSTANCE.vo2dto(merchantVO);
merchantService.createMerchant(merchantDTO);
return merchantRegisterVO;
```

画面12代码：
```java
//上传证件
@ApiOperation("上传证件照")
@PostMapping(value = "/upload")
public String upload(@ApiParam(value = "证件照",required = true) @RequestParam MultipartFile multipartFile) {
//调用fileService上传文件
return null;
}
```

画面13代码：
```java
//上传证件照
@ApiOperation("上传证件照")
@PostMapping(value = "/upload")
public String upload(@ApiParam(value = "证件照",required = true) @RequestParam MultipartFile multipartFile) {
//调用fileService上传文件
return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
标题：3.3.1 商户平台应用证件上传(接口①)
子标题：七牛云
内容：
七牛云是国内一家云服务提供商，本系统与七牛云对接将商户资质照片存储在七牛云。
交互流程如下：
1. 前端上传证件照片，请求商户平台应用。
2. 商户平台应用请求七牛云上传图片。
3. 上传成功返回图片标识给前端。
4. 前端携带证件图片标识和资质申请信息提交到商户平台应用。
5. 请求商户服务保存资质申请。
6. 保存成功返回给前端。
架构图：
- 6. 提交商户资质申请（接口③） → 7. 请求保存资质信息（接口②） → 8. 保存资质申请信息
- 10. 资质申请成功

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

