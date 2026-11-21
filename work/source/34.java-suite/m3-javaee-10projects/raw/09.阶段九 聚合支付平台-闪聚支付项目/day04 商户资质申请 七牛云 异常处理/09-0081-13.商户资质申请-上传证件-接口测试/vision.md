# 画面线理解：13.商户资质申请-上传证件-接口测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\13.商户资质申请-上传证件-接口测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:10, 00:23, 00:28, 01:10, 01:18, 01:30, 01:35, 01:57, 02:03, 02:18, 02:29, 02:41, 02:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:09:17

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现文件上传功能，并通过 Postman 测试接口，最终将文件上传至七牛云对象存储。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Postman 中配置上传接口，URL 为 http://localhost:57010/merchant/upload，Body 格式为 form-data，已选择文件 basic-architecture.png。
画面 2: 在 IntelliJ IDEA 中查看 MerchantController.java 代码，其中定义了 @PostMapping("/upload") 方法用于处理文件上传。
画面 3: 在 IntelliJ IDEA 中查看 MerchantController.java 代码，光标位于 @PostMapping("/upload") 方法的注解上。
画面 4: 在 IntelliJ IDEA 中查看 MerchantController.java 代码，光标位于 @PostMapping("/upload") 方法的注解上。
画面 5: 在 Postman 中切换到 Authorization 标签页，选择 "Inherit auth from parent"。
画面 6: 在 IntelliJ IDEA 中查看 MerchantController.java 代码，光标位于 @PostMapping("/upload") 方法的注解上。
画面 7: 在 IntelliJ IDEA 中查看 MerchantController.java 代码，光标位于 @PostMapping("/upload") 方法的注解上。
画面 8: 在 Postman 中切换到 Body 标签页，准备添加上传文件的 form-data。
画面 9: 在 Windows 文件资源管理器中选择要上传的文件 basic-architecture.png。
画面 10: 在 IntelliJ IDEA 中查看 MerchantController.java 代码，光标位于 return fileService.upload(multipartFile.getBytes(), fileName); 这行代码上。
画面 11: 在 IntelliJ IDEA 中查看 MerchantController.java 代码，光标位于 @PostMapping("/upload") 方法的注解上。
画面 12: 在浏览器中打开七牛云对象存储的网页，显示上传的文件链接。
画面 13: 在浏览器中打开七牛云对象存储的网页，显示上传的文件链接。
画面 14: 在 Postman 中显示上传成功，响应状态为 200，返回的文件 URL 为 http://qcedf31bb.bkt.clouddn.com/1F0B45e-w779-492e-91db-66a4e990f001.png。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
//上传证件照
@ApiOperation("上传证件照")
@PostMapping("/upload")
public String upload(@ApiParam(value = "证件照", required = true) @RequestParam("file") MultipartFile file) {
    //调用fileService上传文件
    //生成的文件名写成filename，要保证它的唯一
    //文件存储路径
    String originalFilename = multipartFile.getOriginalFilename();
    //扩展名
    String suffix = originalFilename.substring(originalFilename.lastIndexOf(".") + 1);
    //文件名
    String fileName = UUID.randomUUID().toString() + suffix;
    //读取文件内容
    byte[] bytes = file.getBytes();
    //调用fileService上传文件
    return fileService.upload(bytes, fileName);
}
```

画面 10:
```java
//上传证件照
@ApiOperation("上传证件照")
@PostMapping("/upload")
public String upload(@ApiParam(value = "证件照", required = true) @RequestParam("file") MultipartFile multipartFile) {
    //调用fileService上传文件
    //生成的文件名写成filename，要保证它的唯一
    //文件存储路径
    String originalFilename = multipartFile.getOriginalFilename();
    //扩展名
    String suffix = originalFilename.substring(originalFilename.lastIndexOf(".") + 1);
    //文件名
    String fileName = UUID.randomUUID().toString() + suffix;
    //读取文件内容
    byte[] bytes = multipartFile.getBytes();
    //调用fileService上传文件
    return fileService.upload(bytes, fileName);
}
```

画面 11:
```java
//上传证件照
@ApiOperation("上传证件照")
@PostMapping("/upload")
public String upload(@ApiParam(value = "证件照", required = true) @RequestParam("file") MultipartFile multipartFile) {
    //调用fileService上传文件
    //生成的文件名写成filename，要保证它的唯一
    //文件存储路径
    String originalFilename = multipartFile.getOriginalFilename();
    //扩展名
    String suffix = originalFilename.substring(originalFilename.lastIndexOf(".") + 1);
    //文件名
    String fileName = UUID.randomUUID().toString() + suffix;
    //读取文件内容
    byte[] bytes = multipartFile.getBytes();
    //调用fileService上传文件
    return fileService.upload(bytes, fileName);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“3.3.1.3 接口测试”，子标题为“证件上传”。
画面 14: PPT 标题为“3.3.1.3 接口测试”，子标题为“证件上传”，并显示“2、上传成功，登录七牛云查询图片是否上传成功”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
