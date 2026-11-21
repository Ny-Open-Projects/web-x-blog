# 画面线理解：05-百度云API入门：搭建环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\05-百度云API入门：搭建环境_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:49, 00:54, 01:25, 01:36, 02:00, 02:09, 02:13, 02:35, 02:52, 04:10, 04:18, 04:39, 04:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:56:07

1) 这一组画面整体在讲如何在 IntelliJ IDEA 中创建 Maven 项目并集成百度云人脸注册 API。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程PPT，标题为“3 百度云API的入门”，子标题“3.1 搭建环境”，并给出Maven依赖配置。
画面2：在IntelliJ IDEA中打开“File”菜单，准备新建项目。
画面3：新建项目对话框，项目名称为“untitled”，项目路径为“E:\workspace\idea\hrm\untitled”，项目格式为“Java (directory based)”。
画面4：新建项目完成，项目名为“face-test”，显示项目结构。
画面5：在项目中新建模块，选择“Maven”作为模块类型。
画面6：打开“face-demo”项目的pom.xml文件，显示Maven项目的基本配置。
画面7：在pom.xml中，光标位于<dependencies>标签前，准备添加依赖。
画面8：展示课程PPT，内容为“3.2 人脸注册”，并给出Java代码示例。
画面9：在pom.xml中，已添加百度云SDK依赖，提示“Maven projects need to be imported”。
画面10：展示课程PPT，内容为“3.2 人脸注册”，并给出Java代码示例。
画面11：展示课程PPT，内容为“3.2 人脸注册”，并给出Java代码示例，包括读取图片文件的代码。
画面12：在IntelliJ IDEA中，右键点击“test”目录，选择“Paste”。
画面13：在IntelliJ IDEA中，打开“face-demo”项目的pom.xml文件，显示已添加的百度云SDK依赖。
画面14：在IntelliJ IDEA中，打开“FaceTest.java”文件，显示空的Java类。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
<dependency>
    <groupId>com.baidu.aip</groupId>
    <artifactId>java-sdk</artifactId>
    <version>4.8.0</version>
</dependency>

画面6：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast</groupId>
    <artifactId>face-demo</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>

画面7：
<dependencies>
    <dependency>
        <groupId>com.baidu.aip</groupId>
        <artifactId>java-sdk</artifactId>
        <version>4.8.0</version>
    </dependency>
</dependencies>

画面8：
//人脸注册
@Test
public void testFaceRegister() throws Exception {
    //传入可选参数调用接口
    HashMap<String, String> options = new HashMap<String, String>();
    options.put("quality_control", "NORMAL");
    options.put("liveness_control", "LOW");
    String imageType = "BASE64";
    String groupId = "itcast";
    String userId = "1000";
}

画面11：
string path = "C:\\Users\\thinkpad\\desktop\\hrm\\day11\\(资源\\图片\\001.png";
byte[] bytes = Files.readAllBytes(Paths.get(path));
String image = Base64Util.encode(bytes);

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“3 百度云API的入门”，子标题“3.1 搭建环境”。
画面8：标题为“3.2 人脸注册”，内容为“用于从人脸库中新增用户，可以设定多个用户所在组，及组内用户的人脸图片”。
画面10：标题为“3.2 人脸注册”，内容为“用于从人脸库中新增用户，可以设定多个用户所在组，及组内用户的人脸图片”。
画面11：标题为“3.2 人脸注册”，内容为“用于从人脸库中新增用户，可以设定多个用户所在组，及组内用户的人脸图片”。

5) 不要评价画面美观，不要输出与课程无关的内容。
