# 05_自媒体文章自动审核_aliyunAI_图片审核测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\05_自媒体文章自动审核_aliyunAI_图片审核测试【海量资源尽在 666java.com】.mp4
- 时长 7分34秒（音频 454s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们来说一下这个图片的审核啊那图片审核呢其实你也可以去打开当前的这个算是API文档啊你可以打开当前的这个介绍介绍里边呢其实刚才咱们也看到了其实你可以打开谁呀打开当前的SDKSDK里边有个Java SDK里边呢是有一个叫做图片审核图片审核啊咱们下面是往下看啊其实这个是一个Java的例子你可以去参考
[00:29] 当然我这边已经提供好了一个例子咱们直接用它就可以在这里边有两种方式可以去传当前的图片内容第一个是传的是URL这URL的话就是什么意思呢就是你可以在网络上访问的一个图片的路径这是一个URL还有第二种方式第二种方式就是你可以去传一个本地的图片到这然后你可以去进行检测这个传的方式就是本地的一个路径看到了吧
[00:59] 那这个咱们目前采用的是第一种方式第一种方式就是当前传输网络上的一张图片进行审核好吧那这样我还是去从当前的这个地考过来考完之后咱们再去说一下当前这个类考到哪考到当前阿里云这个下边有些没有咱们可以导入一下比如说getbook下面是set也是logbook
[01:30] 下面还有我们再往下看这些都是阿里云的因为咱们已经导入了阿里云的一个小SDK所以说你可以直接导入然后再往下看有没有Date是日期然后这个也是阿里云的导入完之后现在就没有错了没有错之后咱们可以简单去看一下这个类首先这个是一些配置跟刚才那个文本是差不多的我就不再去说了然后这里边的内容其实咱们不用管
[02:02] 最主要的是它要接收什么参数这个参数的话就只有一个叫什么list是一个字符串的image4其实你要传一个图片可以你也可以传多张图片它可以一下子审核多张图片那审核多张图片的时候其实就是封装了当前一个list但是这个list里边咱们一开始传的时候只是传了当前的一个当前的什么URL是吧其实你要往当前这个对象里边再去加一个
[02:31] data id还有再去加URUR其实就是这个UR然后还有time其实把这个时间都加上最终你要装到list然后再去把这个作为参数去往后传就可以了或者往那个当前的阿里的接口去传就可以了行这块内容其实已经封装完了其实你不用去管那下面有一个东西大家需要知道哪块呢就这一块了就这块呢其实你看这个就是你要设置的一些场景这个场景的话呢其实你可以设置很多个
[03:00] 很多个已经比如logo是吧像这个像什么ad还有这东西那是啥意思呢就这这个要是不是不明白啥意思呢你可以这样啊像这个logo是logo是吧没啥可说的然后ad呢是广告那这两个是什么意思呢你可以干嘛呢你可以打开当前图片审核这个接口啊咱们再可以去看一眼然后还是找到当前API参考里边有一个叫做图片图片呢是有一个图片审核同步检测
[03:29] 其实打开那个异物也是也是可以的啊然后下面你看啊当前咱们可以找一找啊咱们这里边是有个他其实呢就是他这里边是叫含文字含什么呢爆孔内容的就图片啊图片的文字含爆孔内容的咱们还有啥呢你可以看啊然后是这文字啊当前那个文本里边当前那个图片的文文本里边是射黄内容的
[03:56] 是吧你还可以干嘛呢还可以去设置一些雪凶的是吧还有什么特殊装饰的还有武器的是吧还有什么设阵的打斗的咱们都可以进行检测都可以进行检测啊但是咱们现在啊我目前只设置了四种只设置了四种啊因为这样啊它这个是收费啊是这是用这个图片审核跟微卖审核都是收费的啊关于这个图片审核呢收费还是挺高
[04:22] 目前如果说你要是没有定当前流量包的话当前的当前的二维接口它是你每一个图片你审核了几个场景它就按一次计算比如说你现在是一张图片过来然后你要去审核这四个场景那就是审核了四次假如你十张你审核这四个场景那就是四十次这个收费目前是一块八一千次一块八一千次
[04:51] 行那这个这个你作为了解就可以那到咱们上班的时候呢这是公司所需要考虑的问题好吧行啊那这个咱们就先说到这啊先说到这然后下面咱们要传的大家也知道了要传的就是一个list集合是吧里边呢咱们需要去传一些URL然后下面还有啊最终呢他也会去返回当前的这个东西我也直接return的是他他这里边呢其实也有这三个刚才说了哪三个还知道吧
[05:19] 其实在这写一下也行是吧那第一个是pass是吧pass是通过还是什么pass是通过还是什么review是吧review是什么人工审核还有block这是什么呢这是审核不通过是吧这是不通过行那这个你知道一下最终咱们是要通过当前的返回的这些字符块进行业务处理然后下面咱们就可以来去测试一下
[05:57] 那这测试的话其实咱们还可以在当前那个阿里的Test上去测试那这个呢我在这去准备了一张图片啊咱们可以直接考过来好这个图片是这样啊这个图片的话是一个远程的一个阿里云上的一张图片啊可以打开看看能不能打开啊好回车啊这是我上传的一张图片好吧拿到图片之后呢这时候啊你就可以进行审核了你要传的就是一个LIS这个LIS机盒里边就装的是
[06:31] 一个一个的图片啊一碗肉好吧行那这时候咱们就可以在这去打印啊比如说咱们在这再去加一个东西好吧试一下啊咱们可以去点执行请求口好稍等啊我正在加载环境稍等这个调用完成了啊咱们可以看一下当前的过程啊那这个是不是就pass
[07:03] 是吧pass啊但它里边啊也有一些级别有些级别啊那但是如果说你要是找一张嗯符合这种场景的图片呢它也可以进行去检测那我这会儿呢并就不找这些其他的图片了啊但这个图片能审核是没问题的好吧这接口啊咱们也调通了行那这个代码啊大家呢需要去熟悉一下一会儿呢咱们去审核文章的时候呢就来去使用当前封装好的这两个啊第一个是文本第二个是
[07:32] 图片的深厚好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用阿里云的图片风险检测服务（ImageSyncScan）进行图片内容审核，并通过 Java SDK 实现调用和结果处理。

2) 按时间顺序列出每张画面的要点：
画面1: 展示阿里云图片风险检测服务的业务接口文档，说明支持的场景包括图片智能审核、图文违规识别、图片二进制识别、图片不合规识别、图片Mgo识别，并列出各场景对应的产品。
画面2: 展示接口文档中的“ImageSyncScanRequest”同步图片风险检测接口，列出支持的区域（如cn-beijing, cn-shanghai等）和功能描述。
画面3: 展示Java代码示例，导入相关依赖包，定义Main类并初始化DefaultProfile和ImageSyncScanRequest客户端。
画面4: 展示Java代码，构建JSON对象task，设置datab、url、time字段，添加到list中，然后通过httpBody.put("tasks", list)发送请求。
画面5: 展示Java代码，定义AliyunImageScanRequest类，使用@ConfigurationProperties注解加载aliyun.properties配置文件。
画面6: 展示Java代码，设置ImageSyncScanRequest的连接超时和读取超时时间，并尝试执行doAction方法。
画面7: 展示Java代码，使用@ConfigurationProperties注解加载aliyun.properties配置文件。
画面8: 展示Java代码，设置要检测的场景（如logo, porn, ad, terrorism），并为每张图片创建一个task对象。
画面9: 展示阿里云图片风险检测服务的“准备工作”页面，说明需要创建AccessKey与AccessSecret。
画面10: 展示Java代码，设置ImageSyncScanRequest的协议为HTTP，并设置要检测的场景。
画面11: 展示Java代码，处理图片审核结果，根据taskCode判断是否成功，若成功则输出scene和suggestion。
画面12: 展示一张身份证图片，用于演示图片审核功能。
画面13: 展示Java测试类AllTest，调用AliyunImageScanRequest的imageScanRequest方法并打印响应结果。
画面14: 展示Java代码，处理图片审核结果，根据taskCode判断是否成功，若成功则输出scene和suggestion。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3:
```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.aliyuncs.DefaultProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.ClientProfile;
import com.aliyuncs.http.ProtocolType;
import com.aliyuncs.http.MethodType;

