# 画面线理解：11-二维码生成：通过zxing生成二维码到本地

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\11-二维码生成：通过zxing生成二维码到本地_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:32, 00:50, 01:12, 01:30, 02:26, 04:56, 05:51, 06:06, 06:53, 07:26, 07:40, 07:57, 08:35, 08:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:00:23

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
