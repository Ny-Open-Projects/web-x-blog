# 10-七牛云存储：实现员工头像保存

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\10-七牛云存储：实现员工头像保存_【海量资源尽在 ubkz.com】.mp4
- 时长 8分32秒（音频 512s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那基本的七牛云的一个入门操作呢咱们都已经掌握了那接下来呢我们就是完成最后一项就是通过七牛云完成我们用户头像的这个上传和保存的这个工作那我们要做的事情呢首先第一件事在今天给各位提供的这个资料当中啊准备好了我封装的一个工具的这么一个代码
[00:33] 好了后单工具代码我们打开它就是一个轻扭upload utils打开它呢这个代码呢简单的和各位做一个介绍这个里面是我定义的一些公共的一些代码片段当然了我需要做一个修改首先第一个我们的asset key好了这边secret key好了接下来第三个就是我们的存储空间的位置OK存储空间的位置那接下来呢还有一个我们要进行访问是不是有一个访问的
[01:05] 对应的这么一个域名地址我把这个域名地址也做一个替换那这样一来我基本的配置就已经搞定了那搞定了之后这里面呢通过new对象的时候可以创建出我们的上传管理器应该还有音响并且这边是华东地区还有音响吧好了那接下来呢这边就开始进行上传那上传的时候我提供两个参数第一个参数我们的文件名称文件名
[01:36] 那这个文件名是不是就等于我们之前说过的那个key没错吧好了接下来第二个就是文件的bat数组那其实呢对于七牛银来说它除了可以支持本地文件上传之外它还可以支持以文件这个bat数组的形式上传当然了里面的代码逻辑都跟之前差不多差不多那需要各位注意的是我这边呢选择的是覆盖上传的形式这种来做的覆盖上传两个参数
[02:09] 也就是说你要对哪个文件情覆盖要把这个文件名也携带过来OK那全部都上传完成之后我有一个返回值各位来看那返回值如何拼接的通过一个字符创PRIX在上边这就是我们字符创那这个不就是我们的请求的域名地址吗那请求域名地址接上它返回的一个key那这个key其实就代表的是我们的文件名称没错吧
[02:39] 那接上文件名称这个引以来是不是就拼接好了一个UIL路径啊那接下来呢我加一个问号T等于这个问号T等于是不是我们刚才访问的时候说过有可能它会有缓存所以我加了一个随机字符串所以这边呢我加一个随机当前时间的一个字符串去构造返回的请求路径这个都能理解吧所以呢在我们这边要想完成这个功能的话很简单直接把这个工具类Ctrl Ccall到
[03:09] 我们SaaS人力资源管理系统里面的common目录下就放到YouTube下拷过来那拷过来之后这边肯定会报错因为还没有坐标那打开碰文件也把相应的这个坐标给它填充过来好了这个坐标呢在什么位置在今天这个资料当中呢也给各位准备好了相应的坐标那当然了你如果不想用资料里面的我们刚才自己写demo案例的时候也有相应的坐标直接把坐标Ctrl C
[03:41] copy过来即可好了这边让他耐心耐心等待他编译成功我们这边代码呢就不会有问题了OK代码不会有问题了那接下来我们关注的就是如何把之前上传的Data UIL的形式改造成上传到我们的金牛云存储里好了我们找到之前写好的代码部分Controller找到user Controller我们关注的是文件上传
[04:16] 好了upload那我们所有的内容的全部都是在Service当中进行的编写所以我这回还是改造servicecontrol c把之前的这种data url的形式改成我们上传到奇牛云存储奇牛云存储好了那这个如何去做呢其实也不难其实也不难那首先第一个也是根据id查询
[04:50] 那接着第二件事这回就不是构造什么Data URL了我们是不是可以借助我们刚才的工具类上传到七牛云那接着是不是也能返回一个请求路径也是请求的一个URL没错吧那请求URL有了以后是不是更新这个头像的请求地址所以这个代码我们只需要修改第二部分即可好了这回我们就是将图片上传到七牛云服务存储
[05:20] 请求云存储接着获取到请求路径其实就可以了那这个代码呢也比较简单我们直接new一个刚才构造的工具类七牛upload youtube打点里面有一方法叫做upload那upload两个参数那第一个参数我们指的是上传图片名称那这个上传图片名称是一个固定的是一个独一无二的值
[05:52] 跟某一个用户仅绑定那绑定的比较紧密的是不是可以用用户的ID啊所以user打点get ID独一挖的一个用户一个那接下来第二个代表的是我们图片的byte数组所以我这边byte数组如果获取fail里面都有所以fail打点get bytes那这样一来我们能够得到一个返回的img UL好了那接下来呢我们
[06:25] 进行更新返回那这样一来我这个代码呢其实也已经改造完成了那改造完成之后我们可以重新启动一下系统微服务上传一张图片看一下是否能够保存到奇牛云这边OK那这边让它慢慢启动我对奇牛云里面的这个内容呢做一个简单的管理刷新一下奇牛云这个存储空间里面的文件把这个文件呢我就给它删掉了
[06:57] IHRM broker没问题那接下来呢我们找到代码部分已经刷新重新登录好了登录制定了之后关注的是员工里面的服务随便用一个吧就AG123好了接下来注意我开始上传了我现在用002走好了各位来看这边有已经替换成了002这么一张图片那我们需要关注一下就是七牛云里面
[07:34] 是否把002代表的图片上传过来了刷新一把我们可以看到当前确实有这么一张图片并且这边可以进行一个简单的预览是不是就是刚才我们上传的图片接下来我们看一下数据库对于我们刚才上传的一张图片来说这边是不是应该替换成请求的URL路径了没错吧OK这样一来我们这种方式存到七牛云里面其实也已经搞定了
[08:05] 那其实呢对于我们第二节讲的金牛云存储主要的其实就是和各位来聊一下如何快速的去申请一个金牛云存储的这么一个账号以及通过它提供的SDK完成图片的一个上传功能当然了对于这些代码来说都比较简单可以参考人家给我们准备的文档去写一个demo快速的构建我们的工程就可以了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用七牛云 SDK 实现文件上传功能，并将其集成到一个员工信息管理系统中。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IntelliJ IDEA 中的 QiniuDemo.java 文件，其中包含使用 UploadManager 上传文件的代码，以及测试方法 testUpload02() 的执行结果。
画面2：在 Windows 资源管理器中，显示了 QiniuUploadUtil.java 文件，准备用记事本打开。
画面3：在记事本中打开 QiniuUploadUtil.java，展示初始化配置和上传方法的代码，包含 accessKey、secretKey、bucket 和 prefix 的硬编码。
画面4：在记事本中，对 QiniuUploadUtil.java 的代码进行修改，将 bucket 值改为 "ihrm-bucket"。
画面5：在记事本中，对 QiniuUploadUtil.java 的代码进行修改，将 prefix 值改为 "http://pkbivgfrm.bkt.clouddn.com/"。
画面6：在 IntelliJ IDEA 中打开 ihm_parent 项目的 pom.xml 文件，展示其中的 Maven 依赖配置，包括 shiro-core、shiro-redis、poi、poi-ooxml 等。
画面7：在 IntelliJ IDEA 中，展示 QiniuDemo.java 文件中的 testUpload01() 方法，其中包含配置、上传管理器和上传文件的代码。
画面8：在 IntelliJ IDEA 中，展示 UserController.java 文件，包含用于获取和更新用户信息的 REST 接口。
画面9：在 IntelliJ IDEA 中，展示 UserService.java 文件，包含用于上传用户头像的 uploadImage 方法，其中使用了 Base64 编码。
画面10：在 IntelliJ IDEA 中，展示 UserService.java 文件，对 uploadImage 方法进行修改，将 Base64 编码的图片上传到七牛云存储。
画面11：在 IntelliJ IDEA 中，展示项目结构，准备运行 UserService 的 uploadImage 方法。
画面12：在浏览器中，显示 iHRM 系统的登录页面，输入用户名和密码后点击“登录”按钮。
画面13：在浏览器中，显示 iHRM 系统的员工详情页面，包含员工信息和头像上传功能。
画面14：在 SQLyog 数据库管理工具中，展示用户表（user）的数据，包含用户名、密码、创建时间等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//设置断点持续文件进度操作
FileRecorder fileRecorder = new FileRecorder(localTempDir);
UploadManager uploadManager = new UploadManager(cfg, key, upToken);
try {
    Response response = uploadManager.put(localFilePath, key, upToken);
    DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
    System.out.println(putRet.key);
    System.out.println(putRet.hash);
} catch (QiniuException ex) {
    Response r = ex.response;
    System.err.println(r.bodyString());
} catch (QiniuException ex) {
    //ignore
}
```

画面3：
```java
import com.qiniu.storage.model.DefaultPutRet;
import com.qiniu.util.Auth;
import java.util.Date;

public class QiniuUploadUtil {
    private static final String accessKey = "CQoUdRVa7CLsaurzivQSI_pEDCeHDW3yFEmvvw";
    private static final String secretKey = "3RMPbH5JxgQosOFr4mXHJK5JfRm6AHIQq7sS1R";
    private static final String bucket = "test-bucket";
    private static final String prefix = "http://pkbivgfrm.bkt.clouddn.com/";
    private UploadManager manager;

    public QiniuUploadUtil() {
        //初始化基本配置
        Configuration cfg = new Configuration(Zone.zone0());
        //创建上传管理器
        manager = new UploadManager(cfg);
    }

    public String upload(String imgName, byte[] bytes) {
        Auth auth = Auth.create(accessKey, secretKey);
        //构造覆盖上传token
        String upToken = auth.uploadToken(bucket, imgName);
        try {
            Response response = manager.put(bytes, imgName, upToken);
            DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
            return prefix + putRet.key + "?" + new Date().getTime();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return null;
    }
}
```

画面6：
```xml
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-core</artifactId>
    <version>1.3.2</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-redis</artifactId>
    <version>1.3.0</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml-schemas</artifactId>
    <version>4.0.1</version>
</dependency>
```

画面7：
```java
//将图片上传到七牛云服务器
//1.要上传用户图片信息（用户Id=key）
//2.访问图片
//上传窗口分配的：http://pkbivgfrm.bkt.clouddn.com
//上传的文件名
//更新图片之后，访问的时候，再请求连接加上上传时间戳
public void testUpload01() {
    //配置一个需要在Zone0区域的配置类
    Configuration cfg = new Configuration(Zone.zone0());
    //其他参数参考文档
    //上传管理器
    UploadManager uploadManager = new UploadManager(cfg);
    //生成上传凭证，然后准备上传
    String accessKey = "CQoUdRVa7CLsaurzivQSI_pEDCeHDW3yFEmvvw";
    String secretKey = "3RMPbH5JxgQosOFr4mXHJK5JfRm6AHIQq7sS1R";
    String bucket = "ihrm-bucket";
    //图片路径
    String localFilePath = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\资源\\资源\\1001.png";
    //存入存储空间的文件名
    String key = "test";
```

画面9：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    //1.根据id查询用户
    User user = userDao.findById(id).get();
    //2.使用DataUrl格式存储图片（将图片byte数组进行base64编码）
    String encode = "data:image/png;base64," + Base64.encode(file.getBytes());
    System.out.println(encode);
    //3.更新用户头像地址
    user.setStaffPhoto(encode);
    //4.返回
    userDao.save(user);
    return encode;
}
```

画面10：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    //1.根据id查询用户
    User user = userDao.findById(id).get();
    //2.使用DataUrl格式存储图片（将图片byte数组进行base64编码）
    String encode = "data:image/png;base64," + Base64.encode(file.getBytes());
    System.out.println(encode);
    //3.更新用户头像地址
    user.setStaffPhoto(encode);
    //4.返回
    userDao.save(user);
    return encode;
}
```

画面10（修改后）：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    //1.根据id查询用户
    User user = userDao.findById(id).get();
    //2.使用DataUrl格式存储图片（将图片byte数组进行base64编码）
    String encode = "data:image/png;base64," + Base64.encode(file.getBytes());
    System.out.println(encode);
    //3.更新用户头像地址
    user.setStaffPhoto(encode);
    //4.返回
    userDao.save(user);
    return encode;
}
```

画面10（最终修改）：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    //1.根据id查询用户
    User user = userDao.findById(id).get();
    //2.使用DataUrl格式存储图片（将图片byte数组进行base64编码）
    String encode = "data:image/png;base64," + Base64.encode(file.getBytes());
    System.out.println(encode);
    //3.更新用户头像地址
    user.setStaffPhoto(encode);
    //4.返回
    userDao.save(user);
    return encode;
}
```

画面10（最终修改）：
```java
public String uploadImage(String id, MultipartFile file) throws

