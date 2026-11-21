# 06.阿里云OSS存储之图片上传逻辑的编写

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\06.阿里云OSS存储之图片上传逻辑的编写【海量资源尽在 ubkz.com】.mp4
- 时长 19分57秒（音频 1198s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续啊那么下面呢我们就来编写上传的逻辑啊那么首先呢我们先来编写的Controller啊然后呢我们在这Controller这个包下面呢我们来创建一个类啊就叫pic uploadcontroller然后呢我们给它去写一些这个注解首先呢写的就是Controller这个注解然后呢写一个request mapping
[00:28] 然后呢它的路径呢叫PIC然后呢upload啊然后呢我们下面去一边写一个方法那么这个方法呢我们就要思考一下了那么这个方法的返回值它是什么呢那么现在我们可能还不太确定那么这样咱们先写一个空那么一会儿我们来去修改那么这个方法的名字就叫upload然后呢我们去给它写一个注解
[00:53] 就叫什么呢post mapping因为要发起post请求做上传吧对吧然后呢我们响应就是response body然后呢响应的肯定也是个阶层这么串然后呢在这个参数这个位置的我们写一个request requestpyram这个组结来接收一个什么的fail文件对吧然后呢通过什么接收呢是不是matthewmatthewpartifail是不是通过task来接收我们上传的一个文件的一个对象ok
[01:21] 那么这个接收之后呢他是不是就需要调用一个Service去做一个上传所以呢我们需要在这个Service下面啊来创建一个Service就叫picture然后呢upload然后呢Service好那么把这个Service创建出来然后呢我们给他标记为这是一个Service好然后呢下面我们在Controller中呢把这个Service注入进来private然后呢pic然后呢upload Service把它呢注入进来
[01:50] 那么注入进来之后我们就可以调用它的方法了对吧虽然现在的方法还没有实现我们先来把架子我们先搭好然后下面我们调用this.phuploadservice.upload然后传递一个fail对象那就是把这个multiple的fail对象传递给它然后它的返回值响应是什么我们一会再定
[02:17] 那我们就要去思考一下这个word的位置应该怎么去写这个位置怎么去写啊那么由于我们在我们的前端所使用的是不是按着底线的一个前端所以我们就需要参考一下按着底线它的一个前端所要求的一个响应的一个结构是什么样子的我们来看一下那么这个呢就是按着底线它的一个upload上传组件它的一个这个上传组件的一个这个文档啊那么下面我们来看一下在这个文档中呢它一定
[02:46] 一定要有一个它的一个定义对吧就是你上传结构成功之后的一个数据的一个定义那么其实我们可以看到在这个位置是不是就是它的要求的一个定义那么也就是说我们最终上传完成所返回的这个T这个对象那么一定是符合这样的一个结构这个对象对不对所以接下来我们是不是就可以参考这个结构来编写我们的一个对象
[03:10] 对吧有一个叫什么UID啊Name啊State啊等等好那么我们来把这个对象来拷贝一下啊在我们的讲义中呢咱们有把这个来拷贝一下这个对象的名字叫Pixel upload result啊这样的一个对象好那么把这个对象我们拷过来然后呢我们在这个嗯在这个下面吧创建一个包啊叫什么呢叫VO是不是放我们的一些普通的一些对象那么我们来创建一个类啊就叫这个Pixel upload result
[03:40] 那么这个对象他有哪些这个字段呢其实我们刚才是不是已经看到了对吧这个字段是不是和我们的这个官方所要求这个字段是一样的当然了除了最后一个另一个publish这个是他指的是什么叫下载额外的一些html的属性现在我们不需要这个属性啊他也不是必须的啊所以呢我们就不设置这个属性了那我们给他设置四个属性对吧那么你可以看到是不是对应的有四个属性啊把这四个属性我们拷过来拷贝到我们的一个代码中然后呢再上来看一下
[04:09] 是不是有这样的一个代码然后我们在这个位置是不是要注意给他添加一个什么是不是date注册给他增加一个get和set的方法OK这样的话我们这个对象是不是就搞定了然后我们就可以看到在我们上传的control这个位置这个t是不是就可以改成picture upload是upload result这个对象对吗返回是不是就他然后我们是不是要求这个stories所返回的对象是不是也就是这个对象OK
[04:39] 返回return它就好了然后我们在Service中是不是需要创建一个这个方法对吧那么我们就创建一个这个方法这个方法的返回值是不是也是这个对象ok 好这样的话我们就ok了那么这样的话我们是不是把基本的一个架构是不是就搭建完成那么接下来我们来编写这个Service的具体实现是不是就ok了好 那么下面我们来参考我们这个讲义我们来做一个实现
[05:08] 那么这个Service它是实现了这个OSS客户端的一个API对吧调用这个API去做一个上传这里面有些这个逻辑那么有这个逻辑我们就一点一点来call然后我们边call边做一个讲解那么在我们这个方法中那么首先我们其实对上传的一个文件我们其实先做一个什么呢做一个校验图片做这个校验做什么校验呢是不是对一个后罪名
[05:37] 后罪名是不是做一个教验啊对吧后罪名后罪名后罪名啊后罪名啊这样写后罪名去做一个这个教验啊那么怎么教验呢我们在上面这个位置呢我们来定义定义一个这个
[06:04] 上传的一个格式就是我们允许上传的一个格式有什么叫BMPJPGJPGGIF还有PNG那么这几个是我们允许上传的一个格式所以下面我们先要去对它的一个上传的一个文件的一个后缀名我们做一个校验那么把这个拷过来把这个拷过来然后我们来看一下下面这个位置把它拷一下这个逻辑比较简单的一个逻辑我们就
[06:34] 不重复的去写这个逻辑了好来看一下那么这个逻辑是什么意思呢我们一起来解读一下就是我们是拿到我们这个上传的这个文件它的一个真实的一个名字然后我们去判断对我们上面的这个上传允许上传的格式做一个这样的一个校验就是是不是以这个结尾对吧是不是以这个结尾如果要是的话把它标记为true对吧标记为true那么我们在这有一个标记的一个
[07:03] 标记的一个这个变量然后对它做一个标记如果为chill那代表就是合法如果注意如果在这个位置我们认为它不合法或者说后对面不是我们以我们这个开头那么怎么办呢我们需要给我们的一个这个对象就是我们最终所返回这个对象咱们定义到上面最终所返回的这个对象我们给它设置以它的一个state状态为这个arrow
[07:32] 那么为什么是error呢我们来看一下在官方的这个文档中它这个stace是不是有几个状态我们来看一下一个叫做uploading一个叫做dunk一个叫error一个叫remote那么显然这个error是代表的就是失败是吧dunk就是成功uploading显然就是我们的一个上传中的一个状态那么remote是不是就是做一个删除
[07:53] 已经删除这个状态好那么我们对它做一个标记那么如果不以我们任何一个后缀开头结尾的话那么我们就把它标记为是一个error好那么我们接着继续往下面看那么在这个上传这个逻辑中呢那我们就需要去调用我们的这个阿里云的一个这个SDKOSS的这样的SDK去做一个上传那么怎样咱们把这个代码拷过来把这个代码拷过来之后我们来看一下它这个逻辑
[08:21] 那么在这个里面呢首先它需要一个OSS client对吧这个OSS client呢是不是在前面我们这个API Controller中是不是已经就把它是不是就注入进来了是不是作为一个bin对吧作为一个bin那么所以在这个位置是不是我们就可以把它注入进来定一个private private oss client然后呢来定义一个什么呢OSS client然后我们把它呢就注入进来
[08:51] 好注入进来好那么下面呢我们是不是就有了这个OSS这个client那么有了这个之后呢我们就可以调用阿里云的这个OSS的客户端然后他的API做一个上传那我们来看一下在这个API中他需要有三个参数去做一个上传那么第一个参数呢是我们那个Bugget的一个Name这个Name是不是就需要来找到我们所创建的这个Bugget的名字对吧那么我们需要上传到这个里面来
[09:20] 好重新我来登录一下然后重新登录一下点击授权然后就进入我这个页面然后我们来看一下在这个页面中我们可以看到Bucket name是不是就是他对吧那么我们就需要把他是不是就拷过来
[09:36] 但是大家想一想我们能不能够直接写实到这个位置呢并不能对吧所以我们需要给他写到外部的一个配置文件中然后在这个里面呢我们来拷贝一下拷贝一下我们讲义中的所定义的这个bucket的一个名字那就叫他把他扣过来然后呢Ctrl C然后到这Ctrl V然后呢这个是不是就搞定了对吧他如何去读取到我们的config中呢是不是只需要给他添加一个这个属性是不是就OK了
[10:05] 好 那么下面呢我们进入这个Service中我们调用这个阿里云的阿里云config这个对象但是这个对象呢是不是还没有注入进来所以呢我们来注入一下叫做阿里云config把它呢注入进来然后呢我们在这把它注入然后呢我们调用这个阿里云config拿到它哎OK没有问题那么这是第一个参数我们搞定那么第二个参数呢是叫做fail name
[10:30] 就是说我们上传的把图片上传到我们的阿里云这个里面呢那么它的这个存储的一个目录在哪所以呢我们需要去给它创建一个目录那么我们希望呢它是以这样的一个目录结构去做一个上传目录结构我们大概写一下目录一个结构是这样的一个结构我们以这个年年斜杠月日然后呢下面什么什么点什么jpg
[10:59] 这样去做一个jpg以这样的一个结构做一个上传大家前面的我们来一个images然后是不是说在那个上传那么OK比如说我们来一个比如说2018年的比如说12月然后20号29号随便来写一个然后叉叉叉jpg做这样的一个上传那么我们来看一下我们现在的一个目录目录结构的他现在目前的就会有这样的一个目录结构
[11:28] 是不是有这样的一个结构哎OK201811啊这样的一个结构去做这样的一个上传哎OK好那么我们所以呢我们要去生成一个这样的一个目录对吧生成一个目录那么fail这个pass所以呢我们需要去来看一下这个代码啊来生成这样的一个目录怎么生成呢我们来找一下啊去把这个拿过来吧这个是我们这两个对象啊一个呢是拿到我们的一个
[11:55] 名字然后去getfailpass得到一个failedpass然后下面是我们去写了一个私有的一个这样的一个方法把这个方法靠过来来看一下那么拷贝然后拷贝了我们代码中放到下面来好那么这个方法它其实就是返回我们刚刚所看到的一个这样的一个目录这样的目录结构只是我们在这个方法中把我们文件名做了一个从命名给它写了个名字
[12:24] 当前的一个时间戳加一个随机数生成的这样的一个文件名OK好那么当我们拿到这个文件路径之后那么OK那么这样的话我们就可以传递到我们这个方法中那么也就是说我们上传到我们的OSS中的它的一个文件的一个路径就是这样的路径包含了文件名然后具体的文件的内容是不是就是通过我们传入的一个upload fail拿到它的一个bytes拿到它的一个字节数组
[12:52] 那么做一个这样的一个字节数组的一个上传OK好那么这样的话我们来看一下基本上是不是这个上传逻辑是不是就搞定了对吧到这是不是就完成了上传那么如果一旦出错的话那么我们就把它标记为上传失败那么接下来我们来看一下那么接下来呢我们就需要去将我们的一个上传成功的一个状态以及一个数据是不是做一个返回啊
[13:17] 到这儿是不是就是代表的上传上传是不是成功了上传成功那么它的一个状态就是一个档一个档这样的一个状态然后下面我们给它设置一个内幕这个内幕是什么意思来看一下内幕就是我们上传之后的一个文件名那么我们在这儿给它返回的一个绝对路径访问的一个绝对路径那么这个绝对路径我们来看一下这个绝对路径那么就不能要它了对吧
[13:47] 不能要这个URL这个是我们的一个前对对吧这个我注意一下啊后面这个fail pass他所代表的是不是我们这个路径就是来访问一个咱们来看一下就是说这样的一个路径啊我点一个预览复制他URL那我们来访问一下他呢就是假设是这样的一个路径啊那么我们的这个pass啊我们这个pass我们这个pass fail
[14:17] 它所代表的是不是就是这个路径对吧而前面这个路径呢是不是我们还没有啊所以我们需要把这个路径我们也拷贝一下然后呢我们去做一个配置啊做一个配置那么这个配置呢我们还是到上面去找吧找到我们的前面那个配置项啊配置文件然后呢把它拷过来这是我们前面的一个URL的一个前缀啊然后呢我们把它放到哪里呢放到我们这个这个里面来放到这
[14:44] 放到上然后我们同样把它是不是加入到APA的这个阿里云的一个config这个对象中好嘞那么这样的话我们就可以在这个Service中是不是引用到我们的这个前缀OK好这样的话我们是不是就把这个Service是不是就上传编写逻辑就编写完成了好那么接下来我们是不是就可以开始来测试一下看究竟这个上传是否能够上传成功来我们去run一下就run一下
[15:15] 把我们这个服务呢启动起来我们来做一个测试这个里面这个有点问题把这个先拿掉编译会报错OK这个对象是我们后面用到的对象那么后面我们再说那么我们还是呢到这个里面来让一下走重新再跑一下看效果等待它这个启动OK现在报错了来看一下它说说什么呢
[15:52] 他说这个找不到这个路径路径的配置不对是吧阿里云我们名字写的对吗阿里云来检查一下我们读取的配置文件这个位置看一下可能名字是不是写的有点问题少一个亿少一个亿刚刚这个写的过程中这个拼这个单词拼错了然后呢少一个亿然后呢我们重新来启动一下好这回应该就OK了
[16:31] 其实当我们发现错的时候呢我们去看一下这个文件名就可以了对吧发现诶是拼错了那么这个启动呢会有点问题因为它需要我们后端是不是提供的一个服务对不对那么这样我们先把这个服务呢先给它也启动起来因为它要去查找一个服务把这个服务呢启动起来好知道吧来启动一下我们先把这个服务给它启动起来对吧然后我们再启动我们的这个
[17:02] 服务是吧大家这个他也有点错误调一下这个是我们后面需要实验的方法先把它翻掉好然后呢我们再来尝试的去启动一下我们应该启动前面这个把它启动一下那么我们先把后端这个服务启动起来然后呢我们就来启动我们的这个Tomcat然后呢去测试一下我们上传功能是否OK等待它那个启动
[17:49] 那这样我把这个视频呢先暂停一下然后等它启动起来之后呢我们再去做一个测试好那么现在呢我们就把这两个工程呢都跑起来了跑起来之后呢我们来测试一下啊那么我们使用这个rest这个client一个工具做一个测试然后呢我们来找一下找到这个地址啊这个地址是不对的我们来给它写一个叫做这个pixel upload啊然后呢我们选择这个post请求然后呢我们选择这个fail啊然后
[18:18] 我们来看一下选择一个文件选择一个就这个文件吧选择它然后呢这个是我们上传的一个名字这个名字呢要和我们在Controller中所定义的这个名字呢要保持一致然后就是这个fail这个名字好那么把它贴过来然后呢上传的这个类型呢我们要设置这个multi typemulti part然后呢form data这样的一个类型我们点击一个上传走好那么我们可以看到
[18:43] 在这是不是响应的一个数据是不是我们可以看到是不是已经就上传成功了对吧那我们尝试去访问一下这个URL它是否能够拿到我们刚刚上传那个图片的走好是不是已经看到这个图片了然后呢我们是不是也可以进入这个OSS这个管理的控制台然后呢去查看一下我们是否可以看到我们的一个上传的一个目录是不是有这样的一张图片啊对吧来看一下
[19:08] 你去浏览一下是不是这样的一张图片那么到这里是不是我们就已经完成了一个基于阿里云的OSS的一个图片的一个上传对吧OK好那么我们来看一下这个讲义做一个上传这个是Controller的一个编写这个我们都已经编写完成了那么下面做一个测试是不是通过一个restclient的工具去做这样的一个图片上传的一个模拟做这样的一个测试那么一定要注意的有这么两个点一个是这个名字
[19:37] 一定要和你的Controller中所定义那个参数的名字保持一致还有一个呢就是我们提交的一个类型一定要选这个类型啊别搞错了如果搞错的话那么是上传肯定是不成功的啊好嘞那么关于这个图片的上传的这个逻辑呢它的一个编写呢我们就讲到这里啊OK好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package cn.itcast.haoke.dubbo.api.Service;
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
"C:\Program Files\Java\JDK 8.0_144\bin\java.exe" ...
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

