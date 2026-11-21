# 画面线理解：06.阿里云OSS存储之图片上传逻辑的编写

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\06.阿里云OSS存储之图片上传逻辑的编写【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:40, 03:05, 04:36, 06:27, 08:17, 09:29, 11:43, 13:13, 14:39, 15:53, 17:19, 18:52, 19:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:52:44

1) 这一组画面整体在讲什么（一句话）：
实现一个图片上传功能，包括前端控制器、服务层逻辑、OSS对象存储配置及文件上传流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PDF文档中“2.4.4、编写PicUploadResult”章节，介绍返回数据结构定义。
画面2：IDE中显示PicUploadService.java文件，定义了@Service注解的PicUploadService类。
画面3：展示Ant Design上传组件的文档，说明上传响应数据结构（file、filelist、event）。
画面4：IDE中显示PicUploadController.java，定义了@RequestMapping("/pic/upload")的控制器方法，调用PicUploadService.upload方法。
画面5：IDE中显示PicUploadService.java，定义了IMAGE_TYPE数组，用于校验上传文件类型。
画面6：IDE中显示PicUploadService.java，继续展示文件类型校验逻辑，若非法则设置状态为“error”并返回。
画面7：展示阿里云OSS控制台，显示名为“itcast-haoke”的Bucket，当前无文件。
画面8：PDF文档中再次出现“2.4.4、编写PicUploadResult”章节内容。
画面9：PDF文档中展示PicUploadService.java中getFilePath方法的实现，用于生成文件路径。
画面10：IDE中显示PicUploadService.java，展示上传成功后设置文件状态、名称、ID的代码。
画面11：IDE中显示DubboApiApplication.java，展示Spring Boot主类，但终端提示“aliyun.properties”文件不存在。
画面12：IDE中显示HouseResourcesServiceImpl.java，展示保存房屋资源的代码，终端显示Java执行命令。
画面13：浏览器空白页，可能用于演示上传后跳转或等待。
画面14：PDF文档中展示“查看OSS中的图片信息”页面，包含一张现代客厅图片，下方有“文件名（Object Name）”和“文件大小”字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Bean
public OSS ossClient() {
    return new OSSClient(endpoint, accessKeyId, accessKeySecret);
}
```

画面2：
```java
package cn.itcast.haoke.dubbo.api.service;
import org.springframework.stereotype.Service;
@Service
public class PicUploadService {
}
```

画面3：
```json
{
  "file": [ "/.../"], 
  "filelist": [ "/.../"], 
  "event": [ "/.../"]
}
```

画面4：
```java
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;
@Controller
@RequestMapping("pic/upload")
public class PicUploadController {
    @Autowired
    private PicUploadService picUploadService;
    @PostMapping
    return this.picUploadService.upload(multipartFile);
}
```

画面5：
```java
private static final String[] IMAGE_TYPE = new String[]{"bmp", "jpg", "jpeg", "gif", "png"};
public PicUploadResult upload(MultipartFile multipartFile) {
    if (StringUtils.endsWithIgnoreCase(uploadFile.getOriginalFilename(), type)) {
        return null;
    }
}
```

画面6：
```java
PicUploadResult fileUploadResult = new PicUploadResult();
//图片做校验，对后缀名
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
return fileUploadResult;
```

画面7：
无代码或配置。

画面8：
无代码或配置。

画面9：
```java
private String getFilePath(String sourceFileName) {
    DateTime dateTime = new DateTime();
    return "images/" + dateTime.toString("yyyy") + "/" + dateTime.toString("dd") + "-" + System.currentTimeMillis() + StringUtils.substringAfterLast(sourceFileName, ".");
}
```

画面10：
```java
// 上传成功
fileUploadResult.setStatus("done");
fileUploadResult.setName(this.aliyunConfig.getUrlPrefix() + filePath);
fileUploadResult.setUid(String.valueOf(System.currentTimeMillis()));
return fileUploadResult;
```

画面11：
```java
package cn.itcast.haoke.dubbo.api;
import ...
@SpringBootApplication
public class DubboApiApplication {
    public static void main(String[] args) { SpringApplication.run(DubboA... }
}
```

画面12：
```java
"C:\Program Files\Java\jdk1.8.0_144\bin\java.exe" ...
```

画面13：
无代码或配置。

画面14：
无代码或配置。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PDF文档标题为“2.4.4、编写PicUploadResult”，副标题“该类用于返回给前端的数据结构定义”。
画面8：PDF文档标题为“2.4.4、编写PicUploadResult”，副标题“该类用于返回给前端的数据结构定义”。
画面14：PDF文档标题为“查看OSS中的图片信息”，下方有“文件名（Object Name）”和“文件大小”字段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
