# 画面线理解：12.商户资质申请-上传证件-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\12.商户资质申请-上传证件-接口实现【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:00, 01:42, 02:28, 03:15, 03:41, 04:48, 05:28, 05:57, 06:22, 07:25, 09:04, 09:57, 10:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:08:46

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成七牛云文件上传功能，包括配置 Nacos 服务、编写服务层和控制器层代码，并在七牛云控制台管理相关配置。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程大纲，当前章节为“2.6.2 完善代码”，子章节“2. FileServiceImpl”中提到“在nacos七牛云上传参数”，并展示了配置项：oss: qiniu: url: "" accessKey: "" secretKey: "" bucket: ""。
画面2: 展示了 Nacos 配置管理界面，用于创建或编辑配置，Data ID 为 merchant-application.yaml，Group 为 SHANJUPAY_GROUP，配置格式为 TEXT。
画面3: 展示了七牛云控制台，显示了存储空间 shanjupay-m1 的信息，包括空间概览、API 请求等，并在“融合 CDN 测试域名”区域显示了测试域名 q2cd31bb.bkt.clouddn.com。
画面4: 与画面3内容相同，为七牛云控制台页面，显示了测试域名 q2cd31bb.bkt.clouddn.com。
画面5: 展示了课程大纲，当前章节为“2.6.2 完善代码”，子章节“2. FileServiceImpl”中提到“在nacos七牛云上传参数”，并展示了配置项：oss: qiniu: url: "" accessKey: "" secretKey: "" bucket: ""。
画面6: 展示了 IDEA 编辑器中的 FileServiceImpl.java 文件，其中定义了上传文件的方法，使用了 @Value 注解注入配置，并调用了 QiniuUtils 的 upload 方法。右侧显示了 Profiles 列表。
画面7: 展示了 Nacos 配置管理界面，配置已编辑完成，Data ID 为 merchant-application.yaml，Group 为 SHANJUPAY_GROUP，配置内容为：server: port: 8080 spring: application: name: merchant-application context-path: / swagger: enable: true oss: url: "http://qzcd31bb.bkt.clouddn.com/"。
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
swagger:
  enable: true
oss:
  url: "http://qzcd31bb.bkt.clouddn.com/"

画面6:
package com.shanju.pay.merchant.service;
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
