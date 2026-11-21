# 画面线理解：10-七牛云存储：实现员工头像保存

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\10-七牛云存储：实现员工头像保存_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:38, 00:56, 01:25, 02:54, 03:21, 03:34, 04:10, 04:31, 05:38, 06:34, 07:05, 07:27, 08:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:28:00

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
