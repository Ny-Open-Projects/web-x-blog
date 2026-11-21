# 05-百度云API入门：搭建环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\05-百度云API入门：搭建环境_【海量资源尽在 ubkz.com】.mp4
- 时长 5分1秒（音频 302s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 已经注册好了百度云我们的一个账号之后并且在这边也创建了应用那我们接下来呢就可以通过使用百度云AI提供的这个资料来完成一个基本的入门的这么一个操作那我们的入门操作要完成的内容呢一共有如下几点那这几点是一会儿我们实现刷脸登录必不可少的几个功能我们先来看一下单独它应该如何去做
[00:30] 那首先呢我们要做第一件事就是可以写一个工程搭建一个基本的环境其实搭建环境主要就是使用百度云AI它提供的这个EPI来完成我们的操作也就是要引入坐标了好了在这边呢打开我的idea去创建一个新的工程new一个project我个人习惯呢创建一个空的工程好了点击next那这个工程呢叫什么名字呢其实也比较简单我就给它叫一个
[01:01] Face Demo或者Test好了把它创建到什么位置呢就放到HRM下就以这个工程名字起名了OK好了工程创建好了之后New Window在新的窗口打开那接下来呢在这边我可以去创建一个新的Model当然了这是我个人习惯如果各位不想这样去做呢其实直接创建工程也可以
[01:34] 好了在这边呢我们新的模块呢是一个Mainman工程Mainman的一个模块点击Next好了这里面的这个工程名称就叫做face-demoOKgroupid cn.itcast点击NextOK点击Finish好了工程我们创建好了之后接下来引入相应的坐标那这个坐标呢是在我的资料当中也给各位提供了我们借助的是百度云提供的这个坐标来做的
[02:07] 好了这边呢我也也可以把它写一下dependence好了中间这一段直接copy过来而这个copy过来呢可能会有点问题啊我就自己写吧Ctrl Ccall过来call过来从pdf call过来呢有可能会有一些问题好了这边引入一把OK那我们观察一下这边呢其实百度云相应的它提供的这个jar 包也已经引入到我的工程当中了那引入到工程之后我们接下来可以
[02:48] 通过百度云AI完成第一个功能就是人脸注册那对于人脸注册首先跟各位解释一下它究竟是在做什么因为我们之前说过了对于百度云AI来说它的一个面部识别其实是通过某一个应用基于这某一个应用它会创建一个当前这个应用的一个人脸库就有这么一个人脸的一个面部的一个仓库在里面
[03:18] 那接下来初始化这个应用的时候他的仓库里面什么都没有所以呢我需要把我自己员工里面的一些人脸照片传过来那传过来之后接下来你想要去完成人脸登录的时候你就随便拍一张照片那随便拍一张照片交给百度云那百度云通过和人脸库里面的照片进行交叉对比
[03:44] 最终定位出你当前登录的这个人属于是谁能理解吧那我们现在要做的第一件事呢其实就是像人家这个百度云的人脸库当中先把这个照片给他注册上来OK所以呢接下来我们完成的第一件事就是注册人脸信息OK当然了注册人脸信息
[04:09] 也比较简单我们全部是通过百度云提供的一些API来做的好了回到我的idea工程当中我把代码呢写到test这个包下了创建一classcn.itcast好了我叫做百度就叫test吧.this testok好了那接下来那我这个工程呢我要进行测试的时候呢我不写闷方法了所以在这边呢我以这一unit的形式来做
[04:42] 这一样的形式我也需要去引入JUnit单元测试包当然了我这种方式我也把它引入一下JUnitJUnit好了来一版本随便来一个吧算一样OK那好了接下来在这边我们就可以写基本的代码进行测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

