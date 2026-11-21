# 画面线理解：12-二维码生成：通过zxing生成dataUrl的二维码

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\12-二维码生成：通过zxing生成dataUrl的二维码_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:18, 00:36, 00:46, 02:27, 03:01, 03:40, 04:17, 04:44, 05:23, 05:34, 05:52, 06:45, 06:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:01:14

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 ZXing 库在 Java 中生成 data URI 格式的二维码，并最终在浏览器中展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示生成本地 PNG 图片二维码的完整代码，包含注释和 import 语句。
画面2：在 IDE 中右键点击 main 方法，弹出运行/调试选项，准备执行代码。
画面3：代码中注释“//生成data uri形式的二维码”被选中，准备修改方法名。
画面4：将方法名改为“生成data uri形式的二维码”，并调整代码结构。
画面5：在代码中添加了 `ByteArrayOutputStream os = new ByteArrayOutputStream();` 用于存储二进制数据。
画面6：在 IDE 中输入 `ImageIO.write(...)` 并触发自动补全，显示可用方法。
画面7：在 IDE 中输入 `ImageIO.write(...)` 并触发自动补全，显示可用方法。
画面8：在 IDE 中输入 `ImageIO.write(...)` 并触发自动补全，显示可用方法。
画面9：在 IDE 中输入 `ImageIO.write(...)` 并触发自动补全，显示可用方法。
画面10：在 IDE 中输入 `Base64` 并触发自动补全，显示可用的 Base64 相关类。
画面11：在 IDE 中输入 `Base64` 并触发自动补全，显示可用的 Base64 相关类。
画面12：在 IDE 中输入 `Base64` 并触发自动补全，显示可用的 Base64 相关类。
画面13：在 IDE 中输入 `Base64` 并触发自动补全，显示可用的 Base64 相关类。
画面14：在浏览器中显示生成的二维码，地址栏显示 data URI 格式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import java.io.file;
import java.nio.file.Path;

public class QRCodeTest {
    public static void main(String[] args) throws Exception {
        //1.二维码的信息
        String content = "http://www.licast.cn";
        //2.通过zxing生成二维码(保存到本地图片，支持以data url的形式体现)
        //创建QRCodeWriter对象
        QRCodeWriter writer = new QRCodeWriter();
        /*
         * 1.二维码信息
         * 2.图片类型
         * 3.宽度
         * 4.长度
         */
        BitMatrix bt = writer.encode(content, BarcodeFormat.QR_CODE, width: 200, height: 200);
        //保存二维码到本地
        Path path = new File("C:\Users\ThinkPad\Desktop\ihrm\day11\test.png").toPath();
        MatrixToImageWriter.writeToPath(bt, format: "png", path);
    }
}
```

画面2：
```java
import com.google.zxing.qrcode.QRCodeWriter;
import java.io.file;
import java.nio.file.Path;

public static void main(String[] args) throws Exception {
    //1.二维码的信息
    String content = "http://www.licast.cn";
    //2.通过zxing生成二维码(保存到本地图片，支持以data url的形式体现)
    //创建QRCodeWriter对象
    QRCodeWriter writer = new QRCodeWriter();
    /*
     * 1.二维码信息
     * 2.图片类型
     * 3.宽度
     * 4.长度
     */
    BitMatrix bt = writer.encode(content, BarcodeFormat.QR_CODE, width: 200, height: 200);
    //保存二维码到本地
    Path path = new File("C:\Users\ThinkPad\Desktop\ihrm\day11\test.png").toPath();
    MatrixToImageWriter.writeToPath(bt, format: "png", path);
}
```

画面3：
```java
//生成data uri形式的二维码
public static void main(String[] args) throws Exception {
    //1.二维码中的信息
    String content = "http://www.licast.cn";
    //2.通过zxing生成二维码(保存到本地图片，支持以data url的形式体现)
    //创建QRCodeWriter对象
    QRCodeWriter writer = new QRCodeWriter();
    /*
     * 1.二维码信息
     * 2.图片类型
     * 3.宽度
     * 4.长度
     */
    BitMatrix bt = writer.encode(content, BarcodeFormat.QR_CODE, width: 200, height: 200);
    //保存二维码到本地
    Path path = new File("C:\Users\ThinkPad\Desktop\ihrm\day11\test.png").toPath();
    MatrixToImageWriter.writeToPath(bt, format: "png", path);
}
```

画面4：
```java
//生成data uri形式的二维码
public static void main(String[] args) throws Exception {
    //1.二维码中的信息
    String content = "http://www.licast.cn";
    //2.通过zxing生成二维码(保存到本地图片，支持以data url的形式体现)
    //创建QRCodeWriter对象
    QRCodeWriter writer = new QRCodeWriter();
    /*
     * 1.二维码信息
     * 2.图片类型
     * 3.宽度
     * 4.长度
     */
    BitMatrix bt = writer.encode(content, BarcodeFormat.QR_CODE, width: 200, height: 200);
    //保存二维码到本地
    Path path = new File("C:\Users\ThinkPad\Desktop\ihrm\day11\test.png").toPath();
    MatrixToImageWriter.writeToPath(bt, format: "png", path);
}
```

画面5：
```java
//生成data uri形式的二维码
public static void main(String[] args) throws Exception {
    //1.二维码中的信息
    String content = "http://www.licast.cn";
    //2.通过zxing生成二维码(保存到本地图片，支持以data url的形式体现)
    //创建QRCodeWriter对象
    QRCodeWriter writer = new QRCodeWriter();
    /*
     * 1.二维码信息
     * 2.图片类型
     * 3.宽度
     * 4.长度
     */
    BitMatrix bt = writer.encode(content, BarcodeFormat.QR_CODE, width: 200, height: 200);
    //保存二维码到本地
    Path path = new File("C:\Users\ThinkPad\Desktop\ihrm\day11\test.png").toPath();
    MatrixToImageWriter.writeToPath(bt, format: "png", path);
}
```

画面6：
```java
//生成data uri形式的二维码
public static void main(String[] args) throws Exception {
    //1.二维码中的信息
    String content = "http://www.licast.cn";
    //2.通过zxing生成二维码(保存到本地图片，支持以data url的形式体现)
    //创建QRCodeWriter对象
    QRCodeWriter writer = new QRCodeWriter();
    /*
     * 1.二维码信息
     * 2.图片类型
     * 3.宽度
     * 4.长度
     */
    BitMatrix bt = writer.encode(content, BarcodeFormat.QR_CODE, width: 200, height: 200);
    //保存二维码到本地
    Path path = new File("C:\Users\ThinkPad\Desktop\ihrm\day11\test.png").toPath();
    MatrixToImageWriter.writeToPath(bt, format: "png", path);
}
```

画面7：
```java
//生成data uri形式的二维码
public static void main(String[] args) throws Exception {
    //1.二维码中的信息
    String content = "http://www.licast.cn";
    //2.通过zxing生成二维码(保存到本地图片，支持以data url的形式体现)
    //创建QRCodeWriter对象
    QRCodeWriter writer = new QRCodeWriter();
    /*
     * 1.二维码信息
     * 2.图片类型
     * 3.宽度
     * 4.长度
     */
    BitMatrix bt = writer.encode(content, BarcodeFormat.QR_CODE, width: 200, height: 200);
    //保存二维码到本地
    Path path = new File("C:\Users\ThinkPad\Desktop\ihrm\day11\test.png").toPath();
    MatrixToImageWriter.writeToPath(bt, format: "png", path);
}
```

画面8：
```java
//生成data uri形式的二维码
public static void main(String[] args) throws Exception {
    //1.二维码中的信息
    String content = "http://www.licast.cn";
    //2.通过zxing生成二维码(保存到本地图片，支持以data url的形式体现)
    //创建QRCodeWriter对象
    QRCodeWriter writer = new QRCodeWriter();
    /*
     * 1.二维码信息
     * 2.图片类型
     * 3.宽度
     * 4.长度
     */
    Bit
