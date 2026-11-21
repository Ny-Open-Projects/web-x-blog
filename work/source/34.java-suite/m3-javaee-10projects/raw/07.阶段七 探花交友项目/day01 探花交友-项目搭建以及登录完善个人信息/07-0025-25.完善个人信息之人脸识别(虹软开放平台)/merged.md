# 25.完善个人信息之人脸识别（虹软开放平台）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\25.完善个人信息之人脸识别（虹软开放平台）_【海量资源尽在 666java.com】.mp4
- 时长 11分49秒（音频 709s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下人脸识别这个技术那么人脸识别这个技术呢目前还是比较成熟的一种技术啊那么其实我们的技术选择也是很多的那么我们可以选择一些比如说像阿里云呢去提供的这样的一些这个服务那么其实阿里云的这个收费啊这个服务的收费还是不低的啊所以说呢我们还是去寻找一些其他的解决方案
[00:29] 那么其实现在呢有一个比较好的解决方案的叫什么呢就是这个红软开放平台它呢是专注于去做人脸识别啊这样的一些这个平台啊这样的一些应用的那么关键是呢它是可以免费使用的啊去免费使用的那么我们可以来打开它的官网呢我们可以来看一下啊那么这个呢就是红软其实像我们的很多的一些这个企业都在使用它这个技术比如说像小米呢
[00:59] 魅族呢这样的企业呢也都在使用他的一些这种技术专注于去做这个人脸识别啊这样的一些这种技术包括可以看到他做一些全景成像啊这样的一些技术啊那么我们其实在这呢我们主要是想看到的什么呢就是他的一些这个人脸识别啊我们来看一下啊那么人脸识别这个技术呢你可以看到他是可以是不是就做哎可以看到啊这样的一些这个识别对吧
[01:29] 那么比如说这种人脸识别目前有很多的应用场景包括有些这个小区的门禁呢或者说我们去这个做高铁的时候呢可以刷脸呢等等都是一些人脸识别的一些应用了那么这个平台就非常优秀的一个平台而且呢它是一个可以免费使用的一个平台啊好嘞好那么简单介绍之后啊那我们就来使用一下
[01:54] 那么我们想要去使用这个平台的这个SDK的话那我们先要去注册一个开发者账号那么这个是比较容易的直接去注册就可以了那么来看一下那么我这边的需要去登录一下好那么我的这个账号呢就登录成功了那么登录成功之后呢红软这个平台呢是需要大家先去做一个这个实名认证的实名认证的那么
[02:23] 在这个位置大家可以去上传你的一些身份证的信息就可以去完成一个实名认证了OK好下面我们就来看一下怎么样去使用它那么首先我们需要去创建一个应用那么可以看到在这个位置有一个创建应用你可以选择一些场景的行业就可以了创建完成之后我们就可以来给我们的
[02:52] 应用的去添加一个SDK比如说我们可以选择这种人脸识别的SDK然后选择这个平台的版本等等添加就可以了那么要注意的是就是那么如果你是没有做实名认证的话那么你是不能够去下载SDK使用的那么必须是这个实名认证之后才能够去做一个使用所以是这样的然后要注意的是这个SDK它是可以免费使用
[03:22] 但是呢它有时是有效期的就是说你这个SDK呢它可以使用一年但是到一年之后呢需要重新再激活一次那么这个SDK可以继续做一个使用啊那么在后面我们写这个代码的时候也会给大家去说一下好嘞那么我的我在这个位置呢为我的这个应用添加了两个SDK那么一个呢就是Windows的一个就是Linux的
[03:48] 那么windows呢就是在我在开发的时候呢我去使用的而linux呢就是在我如果要发布到生产环境的话那我这个会使用到的那么大家需要把这两个sdk呢都下载下来那么我在这个位置呢也给大家下载下来了就是在红染在这啊两个sdk那么我们怎么样去使用它呢我们需要把这个就以windows为例啊那我们把它解压开解压开之后呢我们其实可以看到这个位置有一些这个示例代码
[04:17] 是一代码可以打开来看一下怎么样去写这个代码他都写的非常的清楚都是各种的用法好那么然后还有什么就是在这个下面是关键那么这个jar 包就是我们通过我们的加号程序要去调用这个SDK的一个驱动包注意这个是驱动包它并不是真正的SDK它是一个这个驱动包那么我们通过
[04:43] 他呢去调用啊那么真正SDK的逻辑其实在这个里面实现啊就是打包了一些这个DL文件那么我们需要把这个V64就是这几个文件呢给它解压出来存储到你磁盘中的某一个位置这个一定要注意然后呢我们需要把这个驱动包要安装到我们的本地仓库因为我们是要根据Maron去做一个构建但是呢这个jar 包呢并没有上传到
[05:12] 这个我们的Manual的中央仓库所以是没有办法通过在线直接下载的需要去把它安装一下这个大家注意一下好嘞那么接下来呢我们来看一下具体的这个逻辑的一个编写那么刚刚我说的说过就说把这个jar 包需要安装到本地仓库那么这个呢就是一个安装命令那个我就不安装了那么大家可以自己去安装一下那么
[05:38] 我在这个位置已经安装成功了那我就可以直接使用了那么我来把它拷贝一下然后呢去找到我们这个工程然后呢我继续把它添加到下面来放到这那么就可以成功的去引入进来了那么下面我们就开始去做一个使用的这个刚刚我是不是也提到了就说你使用是免费的但是呢首次使用的需要联网进行激活激活之后呢可以离线使用了
[06:04] 使用周期是一年一年之后还需要联网再次激活就OK了好那么下面我们去创建一个application这个文件已经有了添加几个配置那么我这个配置我们之前是不是已经就加入进来了但是这个里面内容是唯空的没有对吧所以我们需要来找一下APP ID和SDK Key以及我们这个lab pass那么我们先来看一下它
[06:32] 那么它是在我们的本地的这个位置你看这个我刚才所说的就是需要把我们的压缩包里面这几个DL我们就解压出来放到这我就放到这个F盘下面扣的这个目录下面了好那么我们就可以直接去使用它了那么我们来找到这两个参数就OK了好来找一下那么我们可以看到APPK是在这个位置对吧复制成功了那考到这来要记住把前面这个APP
[07:01] ID这个要去掉然后呢这个呢也复制一下到这就是SDK的这样的一个值好把它呢也去掉这样的话呢就OK了好嘞好那么接下来呢我们就可以来编写这个代码了那么在这个位置写了一个这样的一个Service那我们把这个Service呢也拷贝过来那我们把这个逻辑给大家讲一下大家就明白了
[07:25] 那么在这个Service中呢其实我们就是去初始化了导入了一些相关的一些这个参数的值然后呢我们在这个位置写了一个init就是我们初始化的这样一个方法那么这个呢是在我们的这个这个在spin的这个生命周期中啊就是当我们这个bin创建完成实力化之后啊然后呢我们去做一个对它做一个初始化那么初始化呢就需要按照
[07:51] 这个SDK的一些这个用法那么这个代码呢大家可以通过前面我所说的这个它提供了一个示例代码中能够找到相关代码的一个编写那么在这个里面呢其实我们可以看到这个代码的逻辑啊就是我们先初始化一个这个Face Engine就是Face这样的一个引擎然后呢把这个APP ID和SDK Key去传递过去然后呢去做一个在线做一个激活
[08:19] 对吧再先做一个激活那么然后呢给他设置一些这样的一些配置啊然后呢去设置一些功能比如说我们要支持年龄的识别呢还有这个性别的识别呢啊等等然后呢去初始化这个引擎然后初始化之后呢就拿到这个引擎那么最终我们是需要通过这个引擎呢去做一些相关的操作那么他判断是否是人像非常简单那么直接通过这个引擎去调用他的一些方法把我们这个图片
[08:48] 这相关的信息传递给他他呢就会给我们会返回一些这个数据啊那么返回的这个他返回的是一个就是人脸的一个列表什么意思呢就是我们一张图片中呢可能有多个人脸他呢返回的是这个人脸在这个图片中的一些这个坐标的位置啊所以说是一个这个集合那么如果这个集合不为空那就代表着这个我们是人像如果
[09:17] 在这个图片中找不到人脸的话那么就是什么呢非人像啊这个逻辑大家能够想明白吧哎OK好那么我们把这个代码编写完了之后呢我们就来做一个测试啊那么大家就明白了那我们把它呢就呃啊就它吧我们把它拷贝到哪里呢就拷贝到这个里面来吧好然后呢我们可以来测试一下当然这个我F盘这个图片是不存在的
[09:44] 那么在资料中我为大家提供了这么几张图片比如说我们先来看一下这张图片这个是一个漂亮的一个妹子然后我们来看一下他能不能够去帮我们识别到这个下面的什么呢下面的应该叫什么呢T点T点这部机好那我们来看他我们来让他识别一下看他是否能够识别这是一个人像呢
[10:13] 好那我们稍微等待一下它的执行OK那么可以看到这个结果呢是在这个位置返回的去处啊那么我们接下来可以让它去呃去识别一下我们这个11点啊JPG然后呢我们去走好那么我们可以看到这个的测试结果呢就是False那么所以说它的识别还是比较准确对吧这个图片显然就没有人脸就不是人像而后面的这个呢它就是人像那么这个同样它也是啊
[10:46] 那么大家可以去根据这三张图片测试一下大家也可以找一些其他图片去测一下啊那么我找了一些图片去测基本上还是很OK的所以说呢我们现在是不是就可以去直接调用这个Service用这个方法啊就可以了哎OK那么当然了大家也可以去体验一下他提供的一些其他的方法比如说这个可以查看这个人的这个性别呢然后呢可以查看这个人的这个年龄呢啊等等
[11:12] 性别还是比较准确的年龄可能不一定准确啊因为现在有很多这种什么美颜呢滤镜呢等等那么导致这个年龄应该不是很准确啊大家可以去体验一下因为我们现在的需求呢是只要识别是人像啊就可以了是一个比较基础的一个应用好嘞好那么这个呢其实就是我们给大家所讲的这个人脸识别啊这样的一个技术的一个使用
[11:37] 那么在这我们所使用的是这个红软的开放平台是一个非常优秀的这样的一个平台啊也OK好嘞好那么关于这个人脸识别的一个技术的讲解就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用虹软（ArcSoft）的人脸识别 SDK，在 Java 项目中进行集成、配置和功能测试。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Typora 文档，内容为“4.2. 人脸识别”，并附带人脸检测功能演示图和返回结果（如：errorcode: 0, top 10: 0, ...）。
画面2：浏览器打开虹软官网首页，展示“全景技术”等宣传内容。
画面3：浏览虹软官网“人脸检测”技术特性页面，包含“高准确率、高智能、高性能、低功耗、易整合”等图标。
画面4：在虹软开发者中心，查看“我的应用”页面，显示“探花交友”应用的 SDK 下载信息，包括 APP ID 和 SDK KEY。
画面5：在开发者中心页面，弹出“我的文件工具”窗口，显示下载的 SDK 文件夹。
画面6：在文件资源管理器中，显示下载的两个 SDK 压缩包：ArcSoft ArcFace Java Linux x64 V2.2.zip 和 ArcSoft ArcFace Java Windows x64 V2.2.zip。
画面7：在 IntelliJ IDEA 中打开项目 pom.xml 文件，展示添加的依赖项：joda-time 和 arcsoft-sdk-face。
画面8：在 Typora 文档中，展示“4.2.3. 开始使用”部分，包含配置 application.properties 的内容：
# 通过参数配置(在配置文件中填对应的参数)
arcsoft.appid=**************
arcsoft.sdkkey=**************
arcsoft.libPath=F:\code\WIN64
画面9：在 IntelliJ IDEA 中，展示 FaceEngineService.java 文件，初始化引擎的代码，包含 @Value 注解和初始化逻辑。
画面10：继续展示 FaceEngineService.java 文件，配置功能参数的代码，如 setSupportAge、setSupportFace3DAngle 等。
画面11：继续展示 FaceEngineService.java 文件，初始化引擎并检测人脸的代码。
画面12：在 IntelliJ IDEA 中，展示 TestFaceEngineService.java 文件，编写测试方法 testCheckIsPortrait。
画面13：在 IntelliJ IDEA 中，展示 TestFaceEngineService.java 文件，执行测试并输出结果“true”。
画面14：在 Typora 文档中，展示“4.2.4. 测试”部分，包含测试类的代码片段，如 @PostConstruct 注解和初始化逻辑。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面7 pom.xml 片段：
<version>2.8.3</version>
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
</dependency>
<dependency>
    <groupId>com.arcsoft.face</groupId>
    <artifactId>arcsoft-sdk-face</artifactId>
    <version>2.2.0.1</version>
</dependency>

画面8 application.properties 片段：
# 通过参数配置(在配置文件中填对应的参数)
arcsoft.appid=**************
arcsoft.sdkkey=**************
arcsoft.libPath=F:\code\WIN64

画面9 FaceEngineService.java 片段：
@Value("${arcsoft.appid}")
private String appId;
@Value("${arcsoft.sdkkey}")
private String sdkKey;
@Value("${arcsoft.libPath}")
private String libPath;
private FaceEngine faceEngine;
@PostConstruct
public void init() {
    FaceEngine faceEngine = new FaceEngine(libPath);
    int activeCode = faceEngine.activeOnline(appid, sdkKey);
    if (activeCode != ErrorInfo.MOK && activeCode != ErrorInfo.MERR_ASP_ALREADY_ACTIVATED) {
        LOGGER.error("引擎激活失败");
        throw new RuntimeException("引擎激活失败");
    }
    // 初始化引擎
    EngineConfiguration engineConfiguration = new EngineConfiguration();
    engineConfiguration.setDetectMode(DetectMode.ASP_DETECT_MODE_IMAGE);
    engineConfiguration.setDetectFaceOrientPriority(DetectOrient.ASP_OP_O_ONLY);
    // 功能配置
    FunctionConfiguration functionConfiguration = new FunctionConfiguration();
    functionConfiguration.setSupportAge(true);
    functionConfiguration.setSupportFace3DAngle(true);
    functionConfiguration.setSupportFaceDetect(true);
    functionConfiguration.setSupportGender(true);
    functionConfiguration.setSupportLiveness(true);
    functionConfiguration.setSupportIRLiveness(true);
    engineConfiguration.setFunctionConfiguration(functionConfiguration);
    int initCode = faceEngine.init(engineConfiguration);
    if (initCode != ErrorInfo.MOK.getValue()) {
        LOGGER.error("初始化引擎出错");
        throw new RuntimeException("初始化引擎出错");
    }
    this.faceEngine = faceEngine;
}

画面12 TestFaceEngineService.java 片段：
@Test
@RunWith(JUnit4ClassRunner.class)
public class TestFaceEngineService {
    @Inject
    private FaceEngineService faceEngineService;
    void testCheckIsPortrait() {
        File file = new File(pathname);
        boolean checkIsPortrait = this.faceEngineService.checkIsPortrait(file);
        System.out.println(checkIsPortrait); // true/false
    }
}

画面13 TestFaceEngineService.java 片段：
@Test
@RunWith(JUnit4ClassRunner.class)
public class TestFaceEngineService {
    @Inject
    private FaceEngineService faceEngineService;
    void testCheckIsPortrait() {
        File file = new File(pathname);
        boolean checkIsPortrait = this.faceEngineService.checkIsPortrait(file);
        System.out.println(checkIsPortrait); // true/false
    }
}

4) PPT 标题、架构图/流程图的结构、表格数据：
画面8：Typora 文档中包含标题“4.2.3. 开始使用”，并附带配置说明。
画面14：Typora 文档中包含标题“4.2.4. 测试”，并附带测试类代码片段。

5) 无。

