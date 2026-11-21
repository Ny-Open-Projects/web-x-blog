# 13.商户资质申请-上传证件-接口测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\13.商户资质申请-上传证件-接口测试【海量资源尽在 666java.com】.mp4
- 时长 2分51秒（音频 172s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们就来测试一下上传证件的这个接口好刚才我们完成了接口的实现那这里边我们来看一下Controller它的接口是upload对不对哎然后post好那这里边呢我们是不是需要把我们的平台应用这个给它重启一下嗯那这里边呢它暂时没有用到商户服务所以商户服务呢你可以不用去起只起一个商户平台应用的这个工程啊起来之后呢我们打开post闷
[00:29] 这里边呢我们来看啊当前我们正在进行的是不是商户注册当中然后我们是不是要做一个叫做资质申请的一个上传证件对不对所以这里面我们新建一个request好然后这里面呢我们叫商户的一个什么资质申请然后资质申请这里面呢干嘛呀资质申请之前他是不是需要去上传证件照啊好然后呢你
[00:59] 保存到这个什么上户注册的这个概念当中然后这个是post对吧好那现在呢我们需要做一个什么事啊你是不是需要去把这个URL给他写上去这个URL呢我们刚才看到了他这个control了是不是就是upload呀对吧好那么你把它放进去注意现在关键的问题来了怎么来上传文件呢
[01:24] 这个Controller它要求的参数是file并且是一个multiple是不是就需要我们本地选这个文件往上上传没错吧所以这里边呢看好我们找到body然后呢这里边我们怎么做选择file然后这里边这个名字一定是file这个名称一定是和你Controller指定的request param这个名称是一致的这如果是abc那么你这也是abc理解吧
[01:53] 好然后这里面我们是不是要选择文件呀这个选择文件的时候就选择我们桌面上面的这个一点偏记可以吧好那这时候我们要上传上传的话首先是不是执行到这里呀然后呢执行Service好对不对现在看走现在就进来了进来之后我们看文件的名称对住了吧没错吧好让它继续前进然后我们是不是就可以让它上传最终成功
[02:22] 这个是不是就是我们的一个什么文件的一个访问的绝对路径这时候其实你可以打开浏览器来访问一下它是可以的没问题吧这时候其实你打开你的七牛云的空间内容管理其实这个文件都已经传上去了你看它的末尾是60第1对不对60第1所以这就是我们说的文件上传的测试好我们就测试完成了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

