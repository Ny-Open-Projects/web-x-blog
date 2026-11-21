# 画面线理解：10.商户资质申请-上传证件-接口定义

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\10.商户资质申请-上传证件-接口定义【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:56, 01:27, 02:05, 02:47, 03:16, 04:14, 05:06, 06:02, 06:43, 07:30, 08:21, 09:06, 09:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:07:11

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
package com.shanjupay.merchant.service;
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
