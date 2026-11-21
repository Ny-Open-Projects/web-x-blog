# 画面线理解：11.商户资质申请-上传证件-接口实现-上传工具类

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\11.商户资质申请-上传证件-接口实现-上传工具类【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:32, 01:01, 01:31, 01:56, 02:23, 03:44, 04:08, 04:33, 05:25, 05:58, 06:45, 07:09, 07:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:08:03

1) 这一组画面整体在讲什么（一句话）：
在 common 工程中编写七牛云上传工具类，该工具类被 FileService 调用，实现文件上传功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程目录结构，当前讲解 2.4.2 完善代码，具体为在 common 工程中编写七牛云上传工具类，该工具类被 FileService 调用。
画面 2: 在 IDE 中定位到 QiniuUtils.java 文件，准备编写上传工具方法。
画面 3: 在 QiniuUtils.java 中，将鼠标悬停在 public static void 之上，查看方法签名。
画面 4: 在 QiniuUtils.java 中，编写上传文件的代码，包括获取上传凭证、上传文件、解析响应等逻辑。
画面 5: 在 QiniuUtils.java 中，编写上传文件的代码，包括获取上传凭证、上传文件、解析响应等逻辑。
画面 6: 在 QiniuUtils.java 中，编写上传文件的代码，包括获取上传凭证、上传文件、解析响应等逻辑。
画面 7: 在 QiniuUtils.java 中，编写上传文件的代码，包括获取上传凭证、上传文件、解析响应等逻辑。
画面 8: 在 QiniuUtils.java 中，编写上传文件的代码，包括获取上传凭证、上传文件、解析响应等逻辑。
画面 9: 在 QiniuUtils.java 中，编写上传文件的代码，包括获取上传凭证、上传文件、解析响应等逻辑。
画面 10: 在 QiniuUtils.java 中，编写上传文件的代码，包括获取上传凭证、上传文件、解析响应等逻辑。
画面 11: 在 QiniuUtils.java 中，编写上传文件的代码，包括获取上传凭证、上传文件、解析响应等逻辑。
画面 12: 在 QiniuUtils.java 中，编写上传文件的代码，包括获取上传凭证、上传文件、解析响应等逻辑。
画面 13: 在 IDE 中展示项目结构，定位到 common 工程下的 QiniuUtils.java 文件。
画面 14: 在 FileServiceImpl.java 中，编写上传文件的业务逻辑，调用 QiniuUtils.uploadQiniu 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
</dependency>
```
画面 2:
```java
public class QiniuUtils {
    //提供上传文件工具方法，accessKey, secretKey, bucket, fileName
    public static void uploadQiniu(String accessKey, String secretKey, String bucket, String fileName) {
        //构造一个带指定 Region 对象的配置类，指定存储区域，和存储空间选择到区域一致
        Configuration cfg = new Configuration(Region.huanan());
        //其他参数参考类注释
        UploadManager uploadManager = new UploadManager(cfg);
        //默认不指定key的情况下，以文件内容的hash值作为文件名
        String key = UUID.randomUUID().toString() + ".png";
        FileInputStream fileInputStream = null;
        try {
            String filePath = "F:\\develop\\shanjupay\\1.png";
            fileInputStream = new FileInputStream(new File(filePath));
            //得到本地文件的字节数组
            byte[] bytes = IOUtils.toByteArray(fileInputStream);
            //认证
            Auth auth = Auth.create(accessKey, secretKey);
            String upToken = auth.uploadToken(bucket);
            //上传
            Response response = uploadManager.put(bytes, key, upToken);
            //解析上传成功的结果
            DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
            System.out.println(putRet.key);
            System.out.println(putRet.hash);
        } catch (QiniuException ex) {
            Response r = ex.response;
            System.err.println(r.toString());
            try {
                System.err.println(r.bodyString());
            } catch (IOException e2) {
                //ignore
            }
        } catch (IOException ex) {
            //ignore
        }
    }
}
```
画面 3:
```java
public class QiniuUtils {
    //提供上传文件工具方法，accessKey, secretKey, bucket, fileName
    public static void uploadQiniu(String accessKey, String secretKey, String bucket, String fileName) {
        //构造一个带指定 Region 对象的配置类，指定存储区域，和存储空间选择到区域一致
        Configuration cfg = new Configuration(Region.huanan());
        //其他参数参考类注释
        UploadManager uploadManager = new UploadManager(cfg);
        //默认不指定key的情况下，以文件内容的hash值作为文件名
        String key = UUID.randomUUID().toString() + ".png";
        FileInputStream fileInputStream = null;
        try {
            String filePath = "F:\\develop\\shanjupay\\1.png";
            fileInputStream = new FileInputStream(new File(filePath));
            //得到本地文件的字节数组
            byte[] bytes = IOUtils.toByteArray(fileInputStream);
            //认证
            Auth auth = Auth.create(accessKey, secretKey);
            String upToken = auth.uploadToken(bucket);
            //上传
            Response response = uploadManager.put(bytes, key, upToken);
            //解析上传成功的结果
            DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
            System.out.println(putRet.key);
            System.out.println(putRet.hash);
        } catch (QiniuException ex) {
            Response r = ex.response;
            System.err.println(r.toString());
            try {
                System.err.println(r.bodyString());
            } catch (IOException e2) {
                //ignore
            }
        } catch (IOException ex) {
            //ignore
        }
    }
}
```
画面 4:
```java
public class QiniuUtils {
    //提供上传文件工具方法，accessKey, secretKey, bucket, fileName
    public static void uploadQiniu(String accessKey, String secretKey, String bucket, String fileName) {
        //构造一个带指定 Region 对象的配置类，指定存储区域，和存储空间选择到区域一致
        Configuration cfg = new Configuration(Region.huanan());
        //其他参数参考类注释
        UploadManager uploadManager = new UploadManager(cfg);
        //默认不指定key的情况下，以文件内容的hash值作为文件名
        String key = UUID.randomUUID().toString() + ".png";
        FileInputStream fileInputStream = null;
        try {
            String filePath = "F:\\develop\\shanjupay\\1.png";
            fileInputStream = new FileInputStream(new File(filePath));
            //得到本地文件的字节数组
            byte[] bytes = IOUtils.toByteArray(fileInputStream);
            //认证
            Auth auth = Auth.create(accessKey, secretKey);
            String upToken = auth.uploadToken(bucket);
            //上传
            Response response = uploadManager.put(bytes, key, upToken);
            //解析上传成功的结果
            DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
            System.out.println(putRet.key);
            System.out.println(putRet.hash);
        } catch (QiniuException ex) {
            Response r = ex.response;
            System.err.println(r.toString());
            try {
                System.err.println(r.bodyString());
            } catch (IOException e2) {
                //ignore
            }
        } catch (IOException ex) {
            //ignore
        }
    }
}
```
画面 5:
```java
public class QiniuUtils {
    //提供上传文件工具方法，accessKey, secretKey, bucket, fileName
    public static void uploadQiniu(String accessKey, String secretKey, String bucket, String fileName) {
        //构造一个带指定 Region 对象的配置类，指定存储区域，和存储空间选择到区域一致
        Configuration cfg = new Configuration(Region.huanan());
        //其他参数参考类注释
        UploadManager uploadManager = new UploadManager(cfg);
        //默认不指定key的情况下，以文件内容的hash值作为文件名
        String key = UUID.randomUUID().toString() + ".png";
        FileInputStream fileInputStream = null;
        try {
            String filePath = "F:\\develop\\shanjupay\\1.png";
            fileInputStream = new FileInputStream(new File(filePath));
            //得到本地文件的字节数组
            byte[] bytes = IOUtils.toByteArray(fileInputStream);
            //认证
            Auth auth = Auth.create(accessKey, secretKey);
            String upToken = auth.uploadToken(bucket);
            //上传
            Response response = uploadManager.put(bytes, key, upToken);
            //解析上传成功的结果
            DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
            System.out.println(putRet.key);
            System.out.println(putRet.hash);
        } catch (QiniuException ex) {
            Response r = ex.response;
            System.err.println(r.toString());
            try {
                System.err.println(r.bodyString());
            } catch (IOException e2) {
                //ignore
            }
        } catch (IOException ex) {
            //ignore
        }
    }
}
```
画面 6:
```java
public class QiniuUtils {
    //提供上传文件工具方法，accessKey, secretKey, bucket, fileName
    public static void uploadQiniu(String accessKey, String secretKey
