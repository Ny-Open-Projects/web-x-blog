# 08.图片存储解决方案之本地文件系统存储实现

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\08.图片存储解决方案之本地文件系统存储实现【海量资源尽在 ubkz.com】.mp4
- 时长 9分18秒（音频 559s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来我们继续那么在前面我们是不是已经实现了我们使用第三方的这种存储的服务将我们的图片上传到了阿里云的OSS服务中
[00:11] 那么接下来我们就需要去做的是第一种解决方案直接将我们的图片保存到我们的磁盘那么也就是我现在的本地硬盘上面对吧那么这种方案其实相对而言是比较简单的那么我们快速的去把这个方案去实现一下那么其实我们要去实现的就是这个Service那么咱们把这个Service拷过来这样吧我这样来拷从这开始拷一直拷到下面来我们去做一个讲解
[00:41] 然后呢一直靠到这然后看一下啊呃这样靠的可能内容有点多不大好靠那这样咱们还是呃一点一点点靠吧靠到这里然后呢呃这样的话啊不行啊那这样我们先来创建一个这个文件吧把这个文件我们先创建好把这个类我们创建出来在下面这个位置呢创建一个这个Service啊把这个Service创建好这个叫system啊fail system就是我们本地本地的文件系统
[01:11] 好那么我们把下面内容我们拷过来首先给他添加一个Service的注解添加一个Service注解然后添加完成之后我们去拷贝下面的实现这个实现的内容跟我们在前面的实现的差不多只是在上传逻辑上面会有一些不一样就是这个是直接保存到我们的硬盘而在前面那个是将我们的数据文件保存到阿里云上面
[01:40] 就是这样的一个不同其他的都是大同小异差不多好那么拷贝进来之后那么我们就把这个里面的一些这个错误去解决一下这个date呢把这个包呢导入进来好这样的话就搞定了把这个注释呢给它往后面去放一下大概呢我们来整理一下这个格式啊好那么这样的话呢还有还缺了一个吧这个点set一下好这样的话是不是就OK了
[02:13] 对吧OK那么这个是写入文件这个逻辑还是缺点逻辑的写入写入文件下面缺逻辑在这缺少这个写入逻辑的这个上面那么我们去把它靠一下就在这里贴过来好这样的话这个逻辑就全了好那么我们大概的来读一下这个代码吧好那么我们可以看到
[02:43] 这个代码其实跟我们这个注释就不要了然后把这个也拿掉吧然后呢这个是教验啊OK好那么这个逻辑其实跟我们刚刚写这个逻辑呢差不多啊差不多那么这个是教验图片的一个后缀然后呢去生成一个图片的一个绝对的引用地址那么要注意的是我们这个引用地址呢是在我们的这个盘F盘下面呢会有一个这个后刻这个upload的一个目录
[03:12] 去做我们的一个存储那么我们来打开一下这个目录OK打开这个目录在这有这样的一个目录好那么里面所存的这个目录结构跟我们前面所说这个目录结构也是一样的也是以这个年月日这样的一个存储的一个结构去做一个存储好那么唯一可能不同的一点就是在这个位置就是在这个位置
[03:36] 在前面我们的阿里云实现是我们将文件上传到阿里云的服务器对吧那么在这个位置实现是直接通过IO的形式去将我们的文件去写到我们本地的一个文件系统中OK就这样的一个区别其他的没有什么太大的区别对吧好那么我们来看一下在这个里面我们访问的一个前缀就是玉米前缀我们通过一个imager点什么的浩克
[04:05] 点com这样的域名去做一个访问但是这个域名我们现在肯定访问不了因为我们需要有一个Nginx的服务器的一个映射包括我们本地host的一个映射一会我们再说我们先来去测试一下这个Service好用吗那么我们进入到我们上传的Controller中那么咱们是不是可以把这个给它注掉对吧把这个注掉然后我们再去注入一个我们刚刚写的一个本地文件系统的一个
[04:34] 上传的一个Service对吧然后把这个Service去注入进来就叫什么就叫他名字属性名我们给他设置为是一样的然后把它注入进来好那么这样的话我们就使用了我们本地的文件系统而上面这个是使用的阿里云的OSS好那么现在我们就可以把我们的服务去重新去启动一下然后重启
[05:03] 那么重启之后呢我们来测试一下它是否能够把我们的图片去成功的上传写到我们指定的一个目录中呢我们来看一下好那么等待它的一个启动启动之后我们来做一个测试那么我们先准备这个测试啊那么在这个里面呢依然是还是这个地址不变对吧然后呢我们下面去图片上传我们重新选择另外一张图片吧那比如说选择这张图啊4.gpg这张图
[05:31] 然后我们点击这个提交就可以了来看一下有没有启动起来呢还没有要稍微等一下等一下它可以启动因为它要去拿到我们那个double的一个服务OK好那么现在已经启动起来了点击这个发送走好嘞那么可以看到是不是也上传成功了那么这个时候它返回了一个访问图片的一个路径
[05:53] 变成了img.hawk.com对不对就不是那个阿里云的那个地址那么这个地址显然现在是不是不能够访问对那么所以我们就需要先来检查一下在我们这个目录中它有没有去生成这样的一个目录是吧21然后这个里面是不是有这样的一张图片OK这个图片是不是已经成功的去写入到我们的服务器的一个操作这个硬盘中对不对那么我们接下来要解决的问题就是通过这个域名去做一个这个访问
[06:23] 好那么下面我们来看一下我们的讲义那么在讲义中的这个Service这个Controller这个跟我们刚刚写的呢是一样的做一个测试没有任何问题那么下面呢我们来搭建一个Nginx进行做一个图片做一个访问啊那么Nginx呢我相信大家呢应该是比较熟悉了啊所以说我们就不做过多的一个讲解那我们来看一下最终我们的一个部署那么这个Nginx在我们的资料中呢也有大家可以去找一下啊那么都会拿到
[06:52] 然后我们在config下面配置一个Nginx的config然后下面我们来指定一个img-hawk.com是不是指向到我们去上传图片这个位置然后我们是不是就可以去做一个访问了ok那么其实我们只是做了第一步先启动Nginx对吧通过star的Nginx命令去做一个启动那么我Nginx已经启动起来了来看一下我这个有没有没有的话就启动一下
[07:18] 可以看到在这个位置我是不是已经启动了这个Nginx所以我就不做一个启动了大家可以通过这样的一个命令去做一个启动那么我相信大家已经比较熟悉这个Nginx了然后下面我们去修改一下本机的host那么我们本机的host是在这个位置是在我们的我看一下我在这有那么我的一个host去修改host这样的工具在
[07:45] 这个资料中也给大家提供了那么我们在这给他设置一个image的好客点com然后去指向了我的本地点击这个应用然后我是可以通过域名去做一个访问了那么我相信大家在这个位置关于host的一个设置以及unjacked设置大家已经很熟悉了这个就不是我们课程中要去详细讲的一些内容了所以我们就
[08:13] 快速的去做这样的一个使用那我们来测试一下这个图片它是否能够正常的去做一个访问呢我们到这个位置来走可以看到这个图片依然是不是可以做一个正常的访问当然了我们这个里面显然是不是就没有水印这个功能了那么如果想要去做这个水印功能的话那么就需要我们自己做一个代码的一个编写功能这个实现哎OK好那么这个呢其实就是我们所说的这个第二种这种
[08:42] 解决方案的方式就是我们保存到我们本地的一个文件系统那么其实就是我们前面所说的第一种解决方案对吧那么目前我们是不是已经实现了第一种解决方案以及我们的第四种解决方案对不对ok
[08:59] 好那么这两种解决方案都是可以去做一个解决的都可以去完成一个图片的上传那么其实我们接下来是不是就需要去整合我们的前端去做一个图片上传功能的一个实现OK好那么关于我们本地文件系统的这种层组的解决方案我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面11：展示命令行窗口，执行命令“start Nginx.exe”启动Nginx服务。
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
package cn.itcast.haoke.dubbo.api.Service;
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
package cn.itcast.haoke.dubbo.api.Controller;
import cn.itcast.haoke.dubbo.api.Service.PicUploadFileSystemService;
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

