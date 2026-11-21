# 画面线理解：25.完善个人信息之人脸识别（虹软开放平台）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\25.完善个人信息之人脸识别（虹软开放平台）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:07, 01:29, 02:11, 04:00, 05:19, 06:16, 07:14, 07:37, 08:26, 09:28, 09:58, 10:25, 11:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:14:46

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
