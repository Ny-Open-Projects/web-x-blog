# 画面线理解：08.图片存储解决方案之本地文件系统存储实现

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\08.图片存储解决方案之本地文件系统存储实现【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:23, 00:47, 01:19, 01:42, 02:31, 03:21, 03:56, 04:57, 05:33, 06:25, 07:13, 08:04, 08:46, 09:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:53:30

1) 这一组画面整体在讲什么（一句话）：
本课程讲解如何在项目中实现图片上传功能，重点是通过本地文件系统存储，并涉及服务层、控制器层代码修改、文件路径生成逻辑以及Nginx反向代理配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程讲义PDF第1页，标题“1、图片存储解决方案”，内容介绍四种存储方案（直接存服务端、分布式文件系统、NFS、第三方服务），并说明本课程采用第一和第四种方案，第三方服务选用阿里云OSS。
画面2：展示代码片段，是PicUploadService类的upload方法，用于校验文件类型，若非法则返回错误结果。
画面3：展示代码片段，是PicUploadFileSystemService类的upload方法，用于校验文件类型，若非法则返回错误结果。
画面4：展示代码片段，是PicUploadFileSystemService类的upload方法，用于校验文件类型，若非法则返回错误结果。
画面5：展示代码片段，是PicUploadFileSystemService类的upload方法，用于生成文件绝对路径和相对路径，写入文件并返回结果。
画面6：展示代码片段，是PicUploadFileSystemService类的getFilePath方法，用于生成文件夹路径和文件名，包含日期格式化逻辑。
画面7：展示代码片段，是PicUploadFileSystemService类的upload方法，用于写入文件并处理异常。
画面8：展示代码片段，是PicUploadController类的upload方法，使用@Autowired注入PicUploadService。
画面9：展示控制台日志，显示Spring Boot应用启动成功，包括Tomcat启动、Dubbo服务注册、Spring DispatcherServlet初始化等。
画面10：展示课程讲义PDF第3页，标题“3.2、修改Controller中的引用”，列出Controller层需要导入的包。
画面11：展示命令行窗口，执行命令“start nginx.exe”启动Nginx服务。
画面12：展示Switchhosts工具界面，配置了本地hosts文件，将“image.haoke.com”指向“127.0.0.1”。
画面13：展示课程讲义PDF第15页，展示一张图片，图片下方有“image.haoke.com”和“127.0.0.1:8080”字样。
画面14：展示课程讲义PDF第14页，标题“3、本地文件系统存储”，列出PicUploadFileSystemService类的导入包。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2代码：
```java
private static final String[] IMAGE_TYPE = new String[]{"bmp", ".jpg", ".jpeg", ".gif", ".png"};
public PicUploadResult upload(MultipartFile uploadFile) {
    boolean isLegal = false;
    for (String type : IMAGE_TYPE) {
        if (StringUtils.endsWithIgnoreCase(uploadFile.getOriginalFilename(), type)) {
            isLegal = true;
            break;
        }
    }
    if (!isLegal) {
        PicUploadResult fileUploadResult = new PicUploadResult();
        fileUploadResult.setStatus("error");
        return fileUploadResult;
    }
    String fileName = uploadFile.getOriginalFilename();
    String filePath = getFilePath(fileName);
    String picUrl = StringUtils.replace(StringUtils.substringAfter(filePath, separator), "\\", replacement);
    fileUploadResult.setFileName("http://image.haoke.com" + picUrl);
    File newFile = new File(filePath);
    fileUploadResult.setUid(String.valueOf(System.currentTimeMillis()));
    return fileUploadResult;
}
```

画面3代码：
```java
import java.awt.Image;
import java.awt.Image;
import java.io.File;
import java.io.IOException;
import java.util.Date;
@Service
public class PicUploadFileSystemService {
    private static final String[] IMAGE_TYPE = new String[]{"bmp", ".jpg", ".jpeg", ".gif", ".png"};
    public PicUploadResult upload(MultipartFile uploadFile) {
        boolean isLegal = false;
        for (String type : IMAGE_TYPE) {
            if (StringUtils.endsWithIgnoreCase(uploadFile.getOriginalFilename(), type)) {
                isLegal = true;
                break;
            }
        }
    }
}
```

画面4代码：
```java
package cn.itcast.haoke.dubbo.api.service;
import cn.itcast.haoke.dubbo.api.vo.PicUploadResult;
import org.apache.commons.lang3.RandomUtils;
import org.apache.commons.lang3.StringUtils;
import org.joda.time.DateTime;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
@Service
public class PicUploadFileSystemService {
    private static final String[] IMAGE_TYPE = new String[]{"bmp", ".jpg", ".jpeg", ".gif", ".png"};
    public PicUploadResult upload(MultipartFile uploadFile) {
        boolean isLegal = false;
        for (String type : IMAGE_TYPE) {
            if (StringUtils.endsWithIgnoreCase(uploadFile.getOriginalFilename(), type)) {
                isLegal = true;
                break;
            }
        }
    }
}
```

画面5代码：
```java
String picUrl = StringUtils.replace(StringUtils.substringAfter(filePath, separator), "\\", replacement);
fileUploadResult.setFileName("http://image.haoke.com" + picUrl);
File newFile = new File(filePath);
fileUploadResult.setUid(String.valueOf(System.currentTimeMillis()));
return fileUploadResult;
```

画面6代码：
```java
private String getFilePath(String sourceFileName) {
    String baseFolder = "F:\\code\\itcast-haoke\\haoke-upload" + File.separator + "images";
    Date nowDate = new Date();
    String filefolder = baseFolder + File.separator + new DateTime(nowDate).toString(pattern: "yyyy") + File.separator + new DateTime(nowDate).toString(pattern: "MM") + File.separator + new DateTime(nowDate).toString(pattern: "dd");
    File file = new File(filefolder);
    if (!file.isDirectory()) {
        if (file.mkdirs()) {
            // 创建目录成功
        }
    }
    String fileName = new DateTime(nowDate).toString(pattern: "yyyyMMddhhmmssSSS") + RandomUtils.nextInt(1000, 9999) + StringUtils.substringAfterLast(sourceFileName, ".");
    return filefolder + File.separator + fileName;
}
```

画面7代码：
```java
try {
    uploadFile.transferTo(newFile);
} catch (IOException e) {
    e.printStackTrace();
}
fileUploadResult.setStatus("error");
return fileUploadResult;
```

画面8代码：
```java
@RequestMapping("pic/upload")
@Controller
public class PicUploadController {
    @Autowired
    private PicUploadService picUploadService;
    @Autowired
    private PicUploadFileSystemService picUploadService;
    @PostMapping
}
```

画面10代码：
```java
package cn.itcast.haoke.dubbo.api.controller;
import cn.itcast.haoke.dubbo.api.service.PicUploadFileSystemService;
import cn.itcast.haoke.dubbo.api.vo.PicUploadResult;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.lang3.RandomUtils;
import org.apache.commons.lang3.StringUtils;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
```

画面14代码：
```java
import cn.itcast.haoke.dubbo.api.vo.PicUploadResult;
import org.apache.commons.lang3.RandomUtils;
import org.apache.commons.lang3.StringUtils;
import org.joda.time.DateTime;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import java.awt.Image;
import java.awt.Image;
import java.io.File;
import java.io.IOException;
import java.util.Date;
@Service
public class PicUploadFileSystemService {
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“1、图片存储解决方案”，内容包括四种存储方案及其优缺点。
画面10：PPT标题“3.2、修改Controller中的引用”，列出Controller层需要导入的包。
画面14：PPT标题“3、本地文件系统存储”，列出PicUploadFileSystemService类的导入包。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
