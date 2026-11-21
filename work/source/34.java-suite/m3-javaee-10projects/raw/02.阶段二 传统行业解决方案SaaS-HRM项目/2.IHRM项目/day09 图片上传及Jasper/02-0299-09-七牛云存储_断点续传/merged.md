# 09-七牛云存储：断点续传

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\09-七牛云存储：断点续传_【海量资源尽在 ubkz.com】.mp4
- 时长 6分10秒（音频 371s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那对于七牛云存储而言除了可以上传一张图片保存到人家的存储空间之外其实呢还可以对一些其他的文件进行上传那比如说呢我可以上传一个歌或者上传一部电影或者一个小说等等都可以那如果说上传的是一个比较大的一个文件的话那这个时候呢可能就会有一个问题比如说传统上传的时候你上传了一半断网了那你再上传又要从头上传没错吧
[00:31] 那青牛云呢它很好的支持了一个比较牛的这么一个方式叫做什么呢断点续传也就是说如果说传到中途的时候你断网了或者造成网络波动了或者中间上传失败了那如果下次再去传的话它就从中间上次传到什么地方接着继续往后传就是一个断点续传的一个功能所以接下来呢续传所以接下来呢我们就来看一下青牛云它这个断点
[01:04] 哎续传功能当了对于这个功能呢嗯也是去参照一下对我们他为我们提供好的sdk好了这边有一个叫做断点续传的这么一个功能那我们要做的事情呢其实也是比较简单的直接ctrl c把中间这段代码拿过来接着写方法public will id好了testupload我叫02了
[01:34] OK那中间这段代码呢各位会发现和我们之前写的这个代码基本上都是大同小异的基本上都差不多所以呢我们看一下这个里面的代码这个里面应该如何去做起来就可以了首先呢这边构造对象接着呢上传凭证等等这些内容都是一模一样的Ctrl C我做一个替换Ctrl V好了那这回呢我上传的一个文件是什么注意在我今天的资料当中
[02:02] 给各位准备了一个20多兆的这么一个TIT的一个Excel文档好了那我这回就上传这个Excel文档其实就可以了OK那好了接下来这个Excel文档呢你也可以给它指定一个名称当然这边又说了如果不指定K它是用这个文件的哈希值做文件名的这个其实无所谓我就叫做叫叫叫Test Excel就是上传一张这个Excel的一个文件就是一个模拟一个大文件上传
[02:39] 中间用到了断点续传这么一个功能OK那这些的内容都比较简单基本上都比较简单其中这边呢有一项要跟各位来聊的和我们刚才普通文件上传不一样的点是这边借助一个叫做Fill Recorder那这个Fill Recorder什么意思其实就是可以设置一个断点续传进度的一个目录那我们都知道对于断点续传而言断点续传而言大家都知道它的一个含义就是可以支持中间间断的一个传递
[03:12] 比如说第一次上传的时候出现网络波动那第二次再传上次传到什么地方咱们继续沿着上次的轨迹继续传递其实就可以了所以这边呢需要对你以传递的内容做一个记录那记录到什么地方其实记录就是到记录到我本机的一个目录当中了OK这个目录呢当然呢我们也可以自己随意去指定而这个目录呢这边呢也跟各位简单的说一下
[03:44] 这边呢就不用system.get.env了我们叫get property获取一下我当前的这个临时目录好了获取到临时目录之后根据临时目录里面去记录一下我上传的一个进度就这么个意思那接下来底下呢都是一个大同小异的这么一个过程当然了我们可以关注一下SOT可以关注一下这个临时目录好了那这个代码呢就不过多的和各位做讲解了我们可以开始上传来看一下效果
[04:18] 来各位这边开始启动好了我上传上传上传注意我把它断开断开那注意这边打印出了我临时目录所在的路径Ctrl Ccall到这边Ctrl V好了这个就是我们的临时目录当然了现在这个临时目录什么都没有啊我们继续让它上传这个由于文件比较大我们来看一下有没有各位会发现
[04:48] 已经出现了这么一个临时目录的一个文件夹并且呢我这边还是在进行上传还是在进行上传那注意我把它断开把它断开那各位你会发现这个文件里面其实已经有了一些数据了啊各位可以看到这里面指令了就是说当前你上传的这个文件叫什么你上传到了什么位置那一共有多长一共有多少大的大小我们已经上传到了多少等等等等
[05:17] 这个就不再跟各位讲一句说了因为断点细传就是通过一个文件记录下以传递的一个内容其实就可以了OK那接下来我再去进行传递他其实还是访问这个目录去看一下我当前的这个文件上传到什么程度我继续往后面去传递其实就可以了OK那这边我再回来继续去走那他其实就是沿着我们之前文件记录的这个进度继续进行上传了由于这个文件比较大呢我这边就不把它全部都上传了我就开始停掉了
[05:49] OK那其实呢对于青牛云存储来说我们以后要用到的其实就是这两个功能第一个功能对一些小的图片直接上传上去就可以了如果是一个比较大的这么一个文件的话我们也可以使用它提供的这种断点续传的功能来做

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Java SDK 将本地文件上传至七牛云对象存储服务，并展示相关代码实现和测试过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 显示 IntelliJ IDEA 编辑器界面，代码文件为 `QiniuDemo.java`。
- 代码中定义了测试方法 `testUpload01()`，用于上传文件。
- 代码中包含七牛云的访问密钥、密钥、存储空间名和本地文件路径。
- 代码中使用了 `Configuration`、`UploadManager`、`Auth` 等类进行初始化和上传操作。
- 代码中使用了 `DefaultPutRet` 类解析上传成功后的响应。

画面2：
- 显示 IntelliJ IDEA 编辑器界面，代码文件为 `QiniuDemo.java`。
- 代码中定义了测试方法 `testUpload01()`，用于上传文件。
- 代码中包含七牛云的访问密钥、密钥、存储空间名和本地文件路径。
- 代码中使用了 `Configuration`、`UploadManager`、`Auth` 等类进行初始化和上传操作。
- 代码中使用了 `DefaultPutRet` 类解析上传成功后的响应。

画面3：
- 显示七牛云开发者中心的网页界面。
- 页面显示了 Java SDK 的上传凭证生成示例代码。
- 代码中包含 `accessKey`、`secretKey`、`bucket` 和 `key` 等变量。
- 代码中使用了 `Auth` 类生成上传凭证。

画面4：
- 显示 IntelliJ IDEA 编辑器界面，代码文件为 `QiniuDemo.java`。
- 代码中显示了 `@Test` 注解和 `@Before` 注解。
- 代码中显示了 `@After` 注解。
- 代码中显示了 `@org.junit.Test` 注解。

画面5：
- 显示 IntelliJ IDEA 编辑器界面，代码文件为 `QiniuDemo.java`。
- 代码中定义了测试方法 `testUpload02()`，用于上传文件。
- 代码中包含七牛云的访问密钥、密钥、存储空间名和本地文件路径。
- 代码中使用了 `Configuration`、`UploadManager`、`Auth` 等类进行初始化和上传操作。
- 代码中使用了 `DefaultPutRet` 类解析上传成功后的响应。

画面6：
- 显示 Windows 文件资源管理器界面。
- 文件夹路径为 `C:\Users\ThinkPad\Desktop\ihrm\day9\资源\`。
- 文件夹中包含 `001.png`、`002.png`、`dataurl.txt` 和 `test.xlsx` 等文件。

画面7：
- 显示 IntelliJ IDEA 编辑器界面，代码文件为 `QiniuDemo.java`。
- 代码中定义了测试方法 `testUpload02()`，用于上传文件。
- 代码中包含七牛云的访问密钥、密钥、存储空间名和本地文件路径。
- 代码中使用了 `Configuration`、`UploadManager`、`Auth` 等类进行初始化和上传操作。
- 代码中使用了 `DefaultPutRet` 类解析上传成功后的响应。

画面8：
- 显示 IntelliJ IDEA 编辑器界面，代码文件为 `QiniuDemo.java`。
- 代码中定义了测试方法 `testUpload02()`，用于上传文件。
- 代码中包含七牛云的访问密钥、密钥、存储空间名和本地文件路径。
- 代码中使用了 `Configuration`、`UploadManager`、`Auth` 等类进行初始化和上传操作。
- 代码中使用了 `DefaultPutRet` 类解析上传成功后的响应。

画面9：
- 显示 IntelliJ IDEA 编辑器界面，代码文件为 `QiniuDemo.java`。
- 代码中定义了测试方法 `testUpload02()`，用于上传文件。
- 代码中包含七牛云的访问密钥、密钥、存储空间名和本地文件路径。
- 代码中使用了 `Configuration`、`UploadManager`、`Auth` 等类进行初始化和上传操作。
- 代码中使用了 `DefaultPutRet` 类解析上传成功后的响应。

画面10：
- 显示 IntelliJ IDEA 编辑器界面，代码文件为 `QiniuDemo.java`。
- 代码中定义了测试方法 `testUpload02()`，用于上传文件。
- 代码中包含七牛云的访问密钥、密钥、存储空间名和本地文件路径。
- 代码中使用了 `Configuration`、`UploadManager`、`Auth` 等类进行初始化和上传操作。
- 代码中使用了 `DefaultPutRet` 类解析上传成功后的响应。

画面11：
- 显示 Windows 文件资源管理器界面。
- 文件夹路径为 `C:\Users\ThinkPad\AppData\Local\Temp\ihrm-bucket`。
- 文件夹中包含一个名为 `7a4990f295ac085922f7c30830e9a6a710c1aad1f` 的文件。

画面12：
- 显示 Windows 文件资源管理器界面。
- 文件夹路径为 `C:\Users\ThinkPad\AppData\Local\Temp\ihrm-bucket`。
- 文件夹中包含一个名为 `7a4990f295ac085922f7c30830e9a6a710c1aad1f` 的文件。
- 窗口底部显示了两个并排的窗口，分别是 IntelliJ IDEA 和文件资源管理器。

画面13：
- 显示 IntelliJ IDEA 编辑器界面，代码文件为 `QiniuDemo.java`。
- 代码中定义了测试方法 `testUpload02()`，用于上传文件。
- 代码中包含七牛云的访问密钥、密钥、存储空间名和本地文件路径。
- 代码中使用了 `Configuration`、`UploadManager`、`Auth` 等类进行初始化和上传操作。
- 代码中使用了 `DefaultPutRet` 类解析上传成功后的响应。

画面14：
- 显示 IntelliJ IDEA 编辑器界面，代码文件为 `QiniuDemo.java`。
- 代码中定义了测试方法 `testUpload02()`，用于上传文件。
- 代码中包含七牛云的访问密钥、密钥、存储空间名和本地文件路径。
- 代码中使用了 `Configuration`、`UploadManager`、`Auth` 等类进行初始化和上传操作。
- 代码中使用了 `DefaultPutRet` 类解析上传成功后的响应。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
public class QiniuDemo {
    /**
     * 将图片上传到七牛云服务
     * 1.获取七牛图片信息（用户id-key）
     * 2.访问图片
     * 存储空间分发的，http://pbkivgfrm.bkt.clouddn.com
     * 上传文件名
     * 更换图片之后，访问的时候，再请求链接加上时间戳
     */
    @Test
    public void testUpload01() {
        //指定一个非绑定Zone对象的配置类
        Configuration cfg = new Configuration(Zone.zone0());
        //上传管理器
        UploadManager uploadManager = new UploadManager(cfg);
        //生成上传凭证，然后准备上传
        String accessKey = "COuDRAV7JLsurrIvQSI_pEDCeHwDyGfJEmvw";
        String secretKey = "3RupTjB53xgQ0sUf4mxBHKJ5JR2n6AMQyS5l";
        String bucket = "ihrm-bucket";
        //上传文件路径
        String localFilePath = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\001.png";
        //文件名
        String key = "test01.png";
        //生成上传凭证
        Auth auth = Auth.create(accessKey, secretKey);
        String upToken = auth.uploadToken(bucket);
        //上传文件
        try {
            Response response = uploadManager.put(localFilePath, key, upToken);
            //解析上传成功的结果
            DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
            System.out.println(putRet.key);
            System.out.println(putRet.hash);
        } catch (QiniuException ex) {
            Response r = ex.response;
            System.err.println(r.bodyString());
        }
    }
}
```

画面2：
```java
public class QiniuDemo {
    /**
     * 将图片上传到七牛云服务
     * 1.获取七牛图片信息（用户id-key）
     * 2.访问图片
     * 存储空间分发的，http://pbkivgfrm.bkt.clouddn.com
     *

