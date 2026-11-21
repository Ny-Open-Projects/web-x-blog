# 11-二维码生成：通过zxing生成二维码到本地

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\11-二维码生成：通过zxing生成二维码到本地_【海量资源尽在 ubkz.com】.mp4
- 时长 8分57秒（音频 538s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 刚才呢简单的对我们的刷领登录需求做了一个分析那在需求分析的阶段我们说过一个需要通过二维码的形式来让用户进行手机扫描那这个二维码我们如何生成那这个二维码呢其实我们借助的是Google开源的这么一个工具来去生成二维码了那接下来呢我们就可以一起使用这个工具
[00:28] 来看一下一个二维码如何给它生成出来那在今天资料当中呢给各位准备了一个就是我们的一个基本的一个代码其中呢这边有一个POM文件那这个POM文件里面已经把我们这个Google提供的二维码工具的坐标给各位准备好了那接下来呢我把这个坐标Ctrl Ccopy到我们之前写
[00:52] 百度云AI的这个工程当中我们先来看一下去创建一个二维码如何去做好了把它引入到我们的POM工具当中Ctrl V Copy过来好了这边呢已经把坐标引进来了那接下来呢我就可以在这边写一个测试类一起来看效果New创建一个Class好了我们叫做QRTestQR CodeQR Code Test好了那接下来
[01:29] 这边呢为了简单我就使用一个闷方法的形式来进行测试了那对于一个二维码来说呢首先对于我们而言如何进行生成那咱们需要知道二维码它的一个本质那对于二维码它的本质其实就是将一些信息隐藏到一张图片当中嘛没错啊那所以在这边呢我先去准备一些我们的信息二维码中的比如说信息那这个信息呢准备好了之后接下来我们就可以通过通过
[02:01] Google提供的这个包叫做ZSYN通过这个包去生成二维码好了通过ZSYN生成二维码其实也有一些小的细节问题咱们写代码的时候一边写咱们一边来进行讲解首先对于二维码来说我们一般网里存的其实就是一个网站通过手机扫描跳转到这一个网站来私讯我们可以给它来一个C1 TNTcontent就等于这边随便写一个
[02:32] http 爱冒号比如说呢3w.itcast.cn 传之播客的官方网站好了那接下来呢通过这一星生成二维码那生成二维码呢其实这边可以以两种形式的哎给各位进行一个演示那这两种形式呢咱们先来看第一种形式就是可以把它保存到一张本地图片当中到本地地图片
[02:59] 那其实除了保存到本地图片之中呢它还提供另外一种情况就是支持以叫做base别写base64了就data UIL的形式来体现了是来体现好了那接着呢我们先来看第一种情况就是生成一张图片保存到本地那这种情况我们如何去做呢其实不管是这两种哪种方式它的一个书写的结构基本上都差不多那在我们来说保存到本地
[03:32] 那我们首先获取一个对象或者需要创建一个叫做QR Code Writer对象Writr对象好了那获取了这个QR Code Writer对象那接下来呢我们需要进行我们的生成图片或者生成图像的一个进行配置就是基本配置好了基本配置
[04:09] 那这个基本配置配置结束之后那接下来呢我们就可以通过借助它的一个对象将我们生成的二维码保存到我们的一个本地路径当中本地OK那接下来这些代码我们把它补充完整首先第一件事就是获取一个QR Code Writer那对于这个QR Code Writer呢这个对象我们直接把它New出来其实就可以了OK以下包好了Writer等于New一个对象出来好了那这样一来QR
[04:42] code writer对象我们创建好了那创建好了之后可以通过这个writer对象通过这个writer对象进行一些基本的二维码的一个配置打点其中有一个叫做encode那这个encode里面有很多个参数那这几个参数呢也给各位简单的做一个说明那这个参数其中第一个参数就是我们要进行编码的我们的二维码信息好了二维码信息有了之后接着
[05:13] 第二个就是你生成这个图片的我们叫做格式也好或者样式也搞或者类型也好OK那写了接着第三个第三个就是你生成这个图片的我们叫做宽度好了接着第四个参数就是我们生成图片的一个长度OK那好了接下来
[05:36] 我们把这个方法给它补充完整首先第一个二维码信息我们content存进去即可接着第二个图片类型这个图片类型我们可以点入到它这个方法里面简单的来看一下其中第二个参数是一个叫做broadcode format各位它是一个枚举类型它可以生成很多种这种图像的形式或者图像的类型我们关注的是二维码就是QR code所以这边我直接枚举打点QR code即可
[06:07] OK好了那接着后面两个参数呢都比较简单宽度比如说我就用200那长度我也用200那这样一来我们经过它的一个编码那其实这里面就是把我们整个生成图像的配置做了一个分析或者做了一个配置说明那接下来得到了一个对象BitMarket Trace好了那接下来
[06:28] 我们的基本配置都已经搞定了那接下来就是想方设法的把一张图片保存到本地那保存到本地如何去做呢其实也简单通过一个工具类来做好了这个工具类呢我们一起来找一下好了叫做marktrace2imagewriter这些工具类这些工具类里面有一个方法打点有一个叫做writer2path这么一个方法
[06:58] 那这个方法呢接收三个参数第一个就是我们的配置第二个就是一个叫做format这个format是你生成图片的一个格式那么生成图片可能有png可以gopj等等很多种类型所以第二个参数是图片的格式第三个是你这个文件的路径OK那接下来呢我们就把这个方法给它补充完整那第一个参数我们刚才说过了第一个参数我们刚才说过了就是我们这边的配置就是bt对象拿过来好了接着第二个参数各位来看
[07:28] 是我们的生成图片的一个类型OK那我们就以png的形式来进行输出好了第三个参数第三个参数是一个pass对象所以我这边构造一个叫做pass对象path好了这边呢以下包OK那这个pass如何去获取呢其实也比较简单我们可以new一个fill那这个fill可以指定一下你想把一张图片保存到什么地方
[07:56] 比如说呢我就想把它保存到我们今天的这个资料当中Ctrl C这个路径直接call过来那接下来给它起一个名字比如说我就叫做test.png好了接着打点调用方法我们的主要目的是得到这个pass对象所以打点点to pass那这样一来pass我们的路径对象也已经获取到了当然了这边呢有一个异常我这边直接
[08:25] 写一个最大就可以了OK那这样一来我的基本的这些代码咱们就已经写好了写好了我们可以运行一把一起来看一下效果走好了这边已经运行成功了我们来看一下我们刚才是否生成了一个test.png那各位我打开如果各位感兴趣的话可以通过手机扫描当前的这个RM看一下它是否能够进入到我们刚才写好的这个我们叫做网站地址OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 ZXing 库在 Java 中生成二维码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：显示文件资源管理器，当前路径为“ihrm/day11”，其中包含“SaaS-HRM--第11章.pdf”和“人脸登录.png”两个文件。
画面2：IntelliJ IDEA 中打开项目“face-demo”，显示项目结构，包含 src、test、pom.xml 等。
画面3：在 IDEA 中打开并显示 pom.xml 文件，其中定义了项目依赖，包括 java-sdk、junit、zxing-core、zxing-javase 等。
画面4：在 IDEA 中打开并显示 QRCodeTest.java 文件，光标位于 package 声明后。
画面5：在 IDEA 中，QRCodeTest.java 文件中，main 方法内光标位于 String 类型变量声明处，下方有注释“//1.二维码中的信息”和“//2.通过zxing生成二维码”。
画面6：在 IDEA 中，QRCodeTest.java 文件中，main 方法内光标位于 import 语句后，提示选择 com.google.zxing.qrcode.QRCodeWriter 类。
画面7：在 IDEA 中，打开并显示 com.google.zxing 包下的 BarcodeFormat.class 文件，其中定义了 AZTEC、CODABAR、CODE_39、CODE_93、CODE_128、DATA_MATRIX、EAN_8、EAN_13、ITF、MAXICODE、PDF_417、QR_CODE、RSS_EXPANDED、UPC_A、UPC_E、UPC_EAN_EXTENSION 等枚举值。
画面8：在 IDEA 中，QRCodeTest.java 文件中，main 方法内已声明变量 content，并创建了 QRCodeWriter 对象 writer，光标位于 BarcodeFormat 类型变量后，提示选择 BarcodeFormat 枚举值。
画面9：在 IDEA 中，QRCodeTest.java 文件中，main 方法内光标位于 MatrixToImageWriter 类的 writeToFile 方法后，提示选择方法参数。
画面10：在 IDEA 中，QRCodeTest.java 文件中，main 方法内光标位于 writeToFile 方法后，提示选择 MatrixToImageWriter 类的 writeToFile 方法。
画面11：在 IDEA 中，QRCodeTest.java 文件中，main 方法内已编写完整代码，调用 MatrixToImageWriter.writeToPath 方法生成二维码，光标位于方法调用后。
画面12：显示文件资源管理器，当前路径为“ihrm”，其中包含 day1 至 day11 文件夹，以及“加1.2课程saas-ihrm大表.xlsx”文件。
画面13：在 IDEA 中，QRCodeTest.java 文件中，main 方法内已编写完整代码，光标位于 main 方法末尾，下方显示“Compilation completed successfully in 1s 167ms (moments ago)”。
画面14：显示图像查看器，打开名为“test.png”的文件，其中包含一个二维码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3 的 pom.xml 内容：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>cn.itcast</groupId>
    <artifactId>face-demo</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>com.baidu.aip</groupId>
            <artifactId>java-sdk</artifactId>
            <version>4.0.0</version>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13</version>
        </dependency>
        <dependency>
            <groupId>com.google.zxing</groupId>
            <artifactId>core</artifactId>
            <version>3.2.1</version>
        </dependency>
        <dependency>
            <groupId>com.google.zxing</groupId>
            <artifactId>javase</artifactId>
            <version>3.2.1</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

画面6 的代码片段：
```java
import com.google.zxing.qrcode.QRCodeWriter;
public class QRCodeTest {
    public static void main(String[] args) {
        //1.二维码中的信息
        //2.通过zxing生成二维码
        String content = "http://www.itcast.cn";
        QRCodeWriter writer = new QRCodeWriter();
        //二维码配置
        //1.二维码信息
        //2.图片类型
        //3.长度
        //4.宽度
        //5.保存二维码到本地
        writer.encode(content, BarcodeFormat.QR_CODE, 200, 200);
    }
}
```

画面11 的代码片段：
```java
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.QRCodeWriter;
import java.io.File;
import java.io.IOException;

public class QRCodeTest {
    public static void main(String[] args) throws Exception {
        //1.二维码中的信息
        //2.通过zxing生成二维码（保存到本地图片，支持以data url的形式体现）
        String content = "http://www.itcast.cn";
        //创建QRCodeWriter对象
        QRCodeWriter writer = new QRCodeWriter();
        //二维码配置
        //1.二维码信息
        //2.图片类型
        //3.长度
        //4.宽度
        //5.保存二维码到本地
        BitMatrix bt = writer.encode(content, BarcodeFormat.QR_CODE, 200, 200);
        MatrixToImageWriter.writeToPath(bt, "png", new File("test.png"));
    }
}
```

画面13 的代码片段：
```java
import java.io.File;
import java.nio.file.Path;

public class QRCodeTest {
    public static void main(String[] args) throws Exception {
        //1.二维码中的信息
        //2.通过zxing生成二维码（保存到本地图片，支持以data url的形式体现）
        String content = "http://www.itcast.cn";
        //创建QRCodeWriter对象
        QRCodeWriter writer = new QRCodeWriter();
        //二维码配置
        //1.二维码信息
        //2.图片类型
        //3.长度
        //4.宽度
        //5.保存二维码到本地
        BitMatrix bt = writer.encode(content, BarcodeFormat.QR_CODE, 200, 200);
        MatrixToImageWriter.writeToPath(bt, "png", new File("test.png"));
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

