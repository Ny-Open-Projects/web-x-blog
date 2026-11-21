# 用 ZXing 把一段文字生成本地二维码图片：QRCodeWriter 三步出图

刷脸登录的需求里已经定下：PC 登录页要展示一张二维码，手机扫一扫，才能把拍照环节接到手机上。方案落到工程上，第一个要回答的问题非常基础：Java 后端怎么把一个 URL 字符串变成一张真能扫出来的图片？自己画点阵、写纠错编码显然不现实，这一课用现成的开源库把这件事压到三行核心代码。

## 先给结论

- ZXing 是 Google 开源的条码库，Java 侧生成二维码引入 `core` 与 `javase` 两个坐标即可，课程使用 3.2.1 版本。
- 生成流程固定三步：`new QRCodeWriter()`、`writer.encode(...)` 得到 `BitMatrix`、`MatrixToImageWriter.writeToPath(...)` 写文件。
- `encode` 有四个参数：二维码内容、`BarcodeFormat.QR_CODE`、宽度、高度，宽高单位是像素，课程用 200 乘 200。
- 二维码的本质是把文本编码进黑白点阵图片，扫码器解码后还原出原字符串，content 写的是什么，扫出来就是什么。

## 二维码的本质：把字符串藏进一张图片

二维码（QR Code，Quick Response Code）看上去是一堆黑白方块，本质是一张点阵图：黑色模块代表 1，白色模块代表 0，原文本经过编码和纠错运算铺进这些模块里。手机扫码时反过来解码，把点阵还原成字符串。所以生成二维码这件事，输入是任意文本，输出是一张图片，图片里藏的就是这段文本。

这也是刷脸登录方案能成立的根基：二维码内容设计成带唯一标志 code 的落地页地址，手机扫码后打开的就是这个地址，code 参数顺带被带到了落地页，后续拍照上传、状态查询全靠它串联。生成二维码只是手段，让 code 跨设备传递才是目的。

生成用的 ZXing 支持很多码型，`BarcodeFormat` 枚举里能看到 `AZTEC`、`CODE_39`、`CODE_128`、`EAN_13`、`PDF_417`、`QR_CODE` 等十几个成员，分别对应不同行业的条码规范。做二维码只关心其中一个值：`BarcodeFormat.QR_CODE`。

## 引入依赖：core 加 javase 两个坐标

在 `pom.xml` 里加入两组坐标：

```xml
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
```

两个依赖分工明确：`core` 是编码解码的核心算法，`QRCodeWriter`、`BitMatrix`、`BarcodeFormat` 都在里面；`javase` 是 Java SE 平台的图形辅助包，把点阵渲染成 `BufferedImage`、再输出成文件的工具类 `MatrixToImageWriter` 位于其中的 `com.google.zxing.client.j2se` 包。只引 `core` 的话，编码能算出来，图片却画不出来。

## 三步生成一张本地二维码

```java
import com.google.zxing.BarcodeFormat;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.QRCodeWriter;

import java.io.File;

public class QRCodeTest {
    public static void main(String[] args) throws Exception {
        // 1. 二维码中的信息
        String content = "https://www.example.com/faceLogin";
        // 2. 通过 ZXing 生成二维码，保存到本地图片
        // 创建 QRCodeWriter 对象
        QRCodeWriter writer = new QRCodeWriter();
        // 编码：内容、图片类型、宽度、高度
        BitMatrix bt = writer.encode(content, BarcodeFormat.QR_CODE, 200, 200);
        // 3. 把点阵写入本地文件
        MatrixToImageWriter.writeToPath(bt, "png", new File("test.png").toPath());
    }
}
```

`encode` 的四个参数逐个对应：

| 参数 | 传什么 | 含义 |
|---|---|---|
| 第一个 | `content` | 要编码进二维码的文本信息 |
| 第二个 | `BarcodeFormat.QR_CODE` | 码型，枚举里选 QR_CODE |
| 第三个 | `200` | 生成图片的宽度，像素 |
| 第四个 | `200` | 生成图片的高度，像素 |

`writeToPath` 接收三个参数：编码得到的 `BitMatrix`、图片格式字符串 `"png"`、目标路径。路径对象用 `new File("test.png").toPath()` 构造，文件名可以换成任意绝对路径。方法声明会抛出受检异常，测试类里直接 `throws Exception` 交给 JVM 即可。

运行 `main` 方法，控制台打出编译通过的信息后，工作目录里就多出一张 `test.png`，用手机扫一下，浏览器打开的正是 content 里写的那串地址。整条数据通路如下图：

```mermaid
flowchart LR
    A["content 字符串"] --> B["QRCodeWriter.encode 编码"]
    B --> C["BitMatrix 黑白点阵"]
    C --> D["MatrixToImageWriter.writeToPath 渲染写盘"]
    D --> E["test.png 本地图片"]
    E --> F["手机扫码解码"]
    F --> G["还原出 content"]
```

图里最关键的一步是 `encode` 返回的 `BitMatrix`：它不是图片，只是点阵。

## 原理细节：BitMatrix 为什么长这样

`BitMatrix` 是一个二维布尔矩阵，每个格子对应最终图片上的一个模块，true 是黑、false 是白。它刻意与图像格式解耦：同一份点阵，既可以渲染成 png，也可以渲染成 jpg，还可以转成 `BufferedImage` 直接写进内存输出流（下一课的 DataURL 就是这么做的）。谁负责把布尔矩阵变成像素，谁负责把像素变成文件，职责被切在 `MatrixToImageWriter` 这一层。

`MatrixToImageWriter` 提供三个出口：`writeToFile` 接收 `File` 对象，`writeToPath` 接收 `Path` 对象，两者本质相同，NIO 的 `Path` 是更推荐的路径表达；第三个出口 `toBufferedImage` 不落盘，把点阵转成内存图片对象交还调用方。图片格式由第二个参数决定，png 是无损压缩、模块边缘清晰，扫码识别率最稳，生成场景几乎都选它。

宽高参数的取值也有讲究：200 乘 200 生成的图，手机在一臂距离内轻松识别；内容越长，同样像素下的模块越密，识读越吃力。内容特别长时要么加大尺寸，要么精简 content，这也是后面设计二维码内容时只放一个短地址加 code 的原因之一。

## 常见误区

- **只引 `core` 不引 `javase`**：`QRCodeWriter`、`BitMatrix` 都能 import，到 `MatrixToImageWriter` 这一行直接报找不到类。渲染输出工具在 `javase` 包里，两个坐标缺一不可。
- **把 `writeToPath` 的第三个参数直接传 `File`**：该方法接收的是 `Path`，传 `File` 编译不过。用 `new File(path).toPath()` 转一下，或者改用 `writeToFile`。
- **宽高写成 10、20 这类小值**：点阵太密、像素太少，手机对不上焦。生成场景从 200 起步，内容长就再放大。
- **以为生成图片会自动建目录**：目标路径的父目录不存在时写文件直接抛异常，先确保目录存在。

## 面试可能被问到的问题

1. 面试官追问：「Java 里生成二维码的核心流程是什么？」
   答：用 ZXing 库三步完成：创建 `QRCodeWriter`，调 `encode` 传入内容、`BarcodeFormat.QR_CODE`、宽高，得到 `BitMatrix` 点阵；再用 `MatrixToImageWriter` 把点阵输出，写文件用 `writeToPath`，输出到响应流可以用 `toBufferedImage` 配合 `ImageIO`。

2. 面试官追问：「`BitMatrix` 是什么？为什么返回它而不是直接返回图片？」
   答：它是二维布尔矩阵，一个格子对应图片上一个黑白模块，只描述点阵不绑定图像格式。与格式解耦后，同一份点阵可以渲染成 png、jpg，也可以转 `BufferedImage` 写进内存，输出方式由调用方按场景选择。

3. 面试官追问：「`core` 和 `javase` 两个依赖各负责什么？」
   答：`core` 是编码解码核心，含 `QRCodeWriter`、`BitMatrix`、`BarcodeFormat`；`javase` 是 Java SE 图形辅助层，`MatrixToImageWriter` 在其中，负责把点阵渲染成 `BufferedImage` 并写出文件或流。只引 `core` 无法产出图片。

4. 面试官追问：「二维码的 content 能放哪些内容？扫码之后发生什么？」
   答：任意文本，常见是 URL、JSON 或纯标识。扫码端解码后得到原字符串：是 URL 就会提示打开，是标识就交给业务处理。刷脸登录场景放的是带 code 参数的落地页地址，扫码即把唯一标志带到手机端。

5. 面试官追问：「生成二维码为什么必须指定 `BarcodeFormat`？」
   答：ZXing 是通用条码库，同一套 `encode` 入口支持 QR_CODE、CODE_128、PDF_417 等多种码型，编码规则和输出点阵完全不同，必须用枚举显式声明要哪种码，否则库不知道按什么规范编码。

## 配套资料

- 工程化工具类（同一套三步流程的封装版，输出 DataURL）：`materials/code/02/day11-刷脸登录/day11-刷脸登录/资源/代码/工具类/QRCodeUtil.java`
- 依赖坐标与测试类：资料包未含独立 demo 工程，文中 `QRCodeTest` 示例为按本课视频写法补全，坐标与 `QRCodeUtil.java` 中使用的 ZXing 版本一致（3.2.1）
