# 12-二维码生成：通过zxing生成dataUrl的二维码

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\12-二维码生成：通过zxing生成dataUrl的二维码_【海量资源尽在 ubkz.com】.mp4
- 时长 7分1秒（音频 422s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 当然我们说过其实这个二维码有很多种形式除了我们这边要保存到本地图片之外其实还只能以Data URL的形式来进行体现接下来我们就可以Ctrl C Ctrl V复制一份下来上面这个我就把它注释掉了接下来我们测试的就是同样的也是生成一个二维码这回是生成Data URL形式的二维码
[00:31] 那我们都知道这个Data UIL形式的二维码呢其实它就是一个字符串没错吧OK那接下来呢我们来看一下如何去做首先呢在我这边呢我把这个基本的一些注释都给它去掉刚才都写过了那我们创建了QI Writer这个对象之后当然了也需要一些基本的配置那接着我想说的是这一回我们就不是把它保存到本地当中了我们这回需要
[01:00] 生成一张图片接着拿到这个图片的流信息进行base64的一个编码处理其实就可以所以对于我来说接下来我们要做的事情一共有这么几点首先第一点就是说我这边需要创建一个随便创建一个比如说就叫做beta arrayoutputstream创建它的主要目的其实就是接收图片里的我们叫做beta数组因为我们都知道
[01:32] Data UIL其实就是对BAT数组里面的这些数据进行BASE64的一个字符串的处理OK好了那创建这个之后呢我们接下来要完成的事情就是将我们的二维码数据以BAT数组的形式保存到我们的这个BAT数组当中保存进去保存进去之后那我们接下来要完成的事情就是对我们的
[02:04] BAT数组进行base64处理所以一共就这么几个步骤当然了也不难比较简单好了接下来我们就开始一个一个来做首先BAT output streamOK我就叫OS了等于new一个出来
[02:27] 好了那NEO出来了数组之后那接下来我们要做的事情呢其实就是将二人码数据以BAD数组的形式保存到我们这个OS对象里面那这个我们如何去做注意这个也比较简单我们可以借助一个工具类叫做ImageIOImageIO对象好了ImageIO对象它有一个方法直接可以打点Write注意可以直接打点Write
[02:59] W R I T E那我们在往里写的时候其实这个是什么呢就是把一个就是把一张图片呢其实给它写入W R I T EOK 第一个那其实这个方法呢就是把一张图片呢给它写入到一个我们叫output stream当中各位来看第二个方法output stream当中那好了我们接住第二个方法那第二个方法呢需要接收这么几个参数首先呢第一个参数
[03:33] 第一个参数是一个什么什么image这么一个对象第二个参数format name第三个就是我们的output stream那接下来呢这三个参数里面其中我把这参数也写一下第一个参数是什么呢其实是我们的一个image对象好了那接着第二个参数是我们的图片类型图片形式图片格式好了那接着第三个参数第三个参数呢是一个output stream那其实呢前后两个参数都比较简单那第一个参数我们如何给它构造
[04:07] 那构造第一个参数是我们接下来要完成的点我们构造第一个参数也不难直接也是通过我们之前写过的一个工具类好了toImageWriter打点这回就不是说WriteToPass了我们这回要做的事情ToBuffer
[04:36] image好了那接着把我们这边的配置bt传过来那这样一来其实就能得到一个叫做buffer的image这么一个对象那这个其实就可以把它理解为我们的一个图片对象那接下来我们参数第一个有了那接下来第二个参数我们还是以png的形式进行体现那接下来第三个参数output stream我们的os对象也拿过来
[04:57] OK那这样一来经过了我们的一个处理那我们这个OS对象里面其实就已经包含了所有图片的二进制的一个数组那接下来我们要完成最后一件事情最后一件事情也比较简单就是要对这个OS对象里面的字节数组进行base64的编码处理好了我们可以base64打点encode抱歉basebse好了我们这边可以base64
[05:33] 当然了我们这边就用这个64 utils吧好了打点好了它有一个方法叫做encode那encode的时候呢其实就是对一个byte数组进行64编码的一个处理那我们这个byte数组在哪全部都在OS对象当中OS打点叫做to byte array直接获取里面的byte数组那这样一来呢其实我们就得到了一个字符串但是我们说过我们要想
[05:58] 让他在浏览器当中可以给他直观的展示出来我们前面是不是还要加一个base64里面代表dataurl的这么一个可以把它理解为一个头没错吧所以接下来呢我们可以对他进行一个输出new一个死讯当然我习惯以这种方式写new一个死讯前面加上我们的头信息那好了接着后面加上我们的encode编码之后的代码那前面我们可以给他加上代表dataurl的头data
[06:27] 注意我们这边是一个图片我们之前也说过image好了接着图片形式png这都没问题分号base64都好OK那这样一来那这样一来我打印的其实就是一个base64的一张图片好了我们执行一把好了这边执行成功可以把这个Ctrl C Copy过来打开我们的浏览器在浏览器部分我们看一下是不是一个二维码
[06:56] 那各位我们这个二维码其实也已经展示出来了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

