# 画面线理解：12.身份认证-接口定义

- 阶段：10.阶段十 万信金融项目
- 章节：07_万信金融-项目实战/7-4 身份认证功能实战
- 源文件：10.阶段十 万信金融项目\07_万信金融-项目实战\7-4 身份认证功能实战\12.身份认证-接口定义_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:33, 01:24, 01:49, 02:47, 03:17, 03:33, 03:52, 04:34, 05:36, 06:59, 07:35, 08:26, 09:22, 09:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:57:41

1) 这一组画面整体在讲一个用户中心系统如何通过调用百度AI接口实现身份证识别、获取上传凭证、上传身份证照片、保存身份证信息的完整流程。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了系统架构的时序图，包含“端应用/App”、“用户服务”、“文件服务”和“百度AI平台”四个模块，描述了从请求身份证识别到保存文件标识的完整交互流程。
画面2: 展示了PDF文档“1 业务概述”，说明了当前开户流程存在的风险，如冒名、盗用他人身份证等。
画面3: 展示了PDF文档“5.1 第一阶段：识别身份证”，定义了在ConsumerApi接口中定义的imageRecognition方法。
画面4: 与画面3内容相同，再次强调了imageRecognition方法的定义。
画面5: 展示了百度AI开放平台的Java SDK文档首页。
画面6: 展示了百度AI开放平台的“安装OCR Java SDK”页面，列出了SDK的包结构。
画面7: 展示了PDF文档“5.2 第二阶段：获取上传凭证”，其中包含一个@PostMapping注解的imageRecognition方法代码片段。
画面8: 展示了PDF文档“5.2 第二阶段：获取上传凭证”，定义了applyUploadCertificate方法。
画面9: 展示了PDF文档“5.3 第三阶段：上传身份证”，说明了前端如何调用文件服务上传身份证照片。
画面10: 展示了PDF文档“5.4 第四阶段：保存身份证信息”，定义了saveConsumerDetails方法。
画面11: 展示了文件服务的控制台页面，显示了AccessKey和SecretKey。
画面12: 展示了SQLyog数据库管理工具，显示了“file_upload”表的结构。
画面13: 展示了记事本程序，用于编辑ConsumerDetails.java文件。
画面14: 展示了PDF文档“5.4 第四阶段：保存身份证信息”，定义了saveConsumerDetails方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3:
```java
/**
 * 提交身份证图片给百度AI进行识别
 * @param file 上传的文件
 * @param flag 身份证正面、反面front或back
 * @return Map集合 识别成功后把身份证上的姓名和身份证号存到map中返回
 */
RestResponse<Map<String, String>> imageRecognition(MultipartFile file, String flag);
```

画面7:
```java
@Override
@ApiOperation("提交身份证图片给百度AI进行识别")
@PostMapping("/my/imageRecognition")
public RestResponse<Map<String, String>> imageRecognition(
        @RequestParam("file") MultipartFile file,
        String flag) {
    return null;
}
```

画面8:
```java
/**
 * 申请获得上传凭证
 * @return
 */
RestResponse<String> applyUploadCertificate();
```

画面9:
```java
@Override
@ApiOperation("申请获得上传凭证")
@GetMapping("/my/applyUploadCertificate")
public RestResponse<String> applyUploadCertificate() {
    return null;
}
```

画面10:
```java
/**
 * 保存用户详细信息（主要存储身份证文件标识）
 * @param consumerDetailsDTO 时尚用户详情信息
 * @return
 */
RestResponse<String> saveConsumerDetails(ConsumerDetailsDTO consumerDetailsDTO);
```

画面14:
```java
/**
 * 保存用户详细信息（主要存储身份证文件标识）
 * @param consumerDetailsDTO 时尚用户详情信息
 * @return
 */
RestResponse<String> saveConsumerDetails(ConsumerDetailsDTO consumerDetailsDTO);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1: 架构图/流程图，包含四个模块：“端应用/App”、“用户服务”、“文件服务”和“百度AI平台”，描述了从请求身份证识别到保存文件标识的完整交互流程。
画面2: PPT标题“1 业务概述”，表格数据包括“证件类型”、“客户姓名”、“证件号”、“银行卡号”、“手机号”等字段。
画面3: PPT标题“5.1 第一阶段：识别身份证”，表格数据包括“接口描述”和“接口定义如下”。
画面4: PPT标题“5.1 第一阶段：识别身份证”，表格数据包括“接口描述”和“接口定义如下”。
画面7: PPT标题“5.2 第二阶段：获取上传凭证”，表格数据包括“接口描述”和“接口定义如下”。
画面8: PPT标题“5.2 第二阶段：获取上传凭证”，表格数据包括“接口描述”和“接口定义如下”。
画面9: PPT标题“5.3 第三阶段：上传身份证”，表格数据包括“接口描述”和“接口定义如下”。
画面10: PPT标题“5.4 第四阶段：保存身份证信息”，表格数据包括“接口描述”和“接口定义如下”。
画面14: PPT标题“5.4 第四阶段：保存身份证信息”，表格数据包括“接口描述”和“接口定义如下”。

5) 不要评价画面美观，不要输出与课程无关的内容。
