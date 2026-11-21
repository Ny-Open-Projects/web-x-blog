# 13.支付入口-解析ticket

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\13.支付入口-解析ticket【海量资源尽在 666java.com】.mp4
- 时长 9分13秒（音频 553s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们把支付入口的确认页面呢进行完善那么大家也看到现在页面当中的数据是空的啊那下面我们要完善我们怎么完善呢首先呢大家知道那么当用户扫码的时候呢这里边它是不是会啊传入一个ticket那么这个ticket的这个参数大家注意这个ticket的这个参数呢是需要我们去干嘛把它解析出来的那这个ticket各位
[00:29] 它是base64编码对json数据编码那我们是不是把它要解析出来那么解析出来之后呢我们就可以把这个数据呢传到我们说的这个什么呀这个页面中这个页面里面所需要的数据是不是就可以显示出来了对这是第一个我们要做的事第二个事呢就是要解析客户端的类型也就是最终啊我们不能通过浏览器去浏览这个页面我们要从手机来扫
[00:59] 对吧那手机扫的话大家也知道要么用微信扫要么用支付宝扫所以我们要在这个入口这儿我们要干嘛去解析客户端的类型客户端类型目前我们就两种一种是什么微信的客户端一种是支付宝的客户端对这是我们要是要做的事好那接下来我们就准备开始做了首先我们第一个是要准备
[01:27] 确认页面所需要的数据我是不是要做这件事那么准备确认页面所需要的数据的话很显然我们是需要做一件事就是要解析这个ticket那怎么解析ticket它是base64编码base64编码的话我们是不是有一个什么有一个工具类大家有印象吗我们当初是去用的是我们这个common当中的一个工具类然后呢
[01:57] 如果我们进行编码的时候是什么呀Encoder解码的话就是Decoder然后我们把Tag放进去这样的话我们是不是就得到了这么一个什么JSONJSON串对吧因为它本身就是个JSON串那么拿到了这个JSON串注意拿到了这个JSON串之后你注意我们要把它转成什么转成对象那个老人让它转成什么对象呢注意
[02:26] 这个当初我们在生成这个URL的时候啊嗯我们是把呃一些这个看啊我们找一下啊找一下当初生成URL嗯我们找哪里啊找这个交易服务的这个Service嗯然后这里边呢我们当初是不是就有一个方法叫创建这个什么二维码啊二维码你看这里边是不是有一个叫啊pay order这个DTO这个是不是就是我们说的你看是不是把这个对象转成了JS
[02:57] 那你说这个jensen其实是把这个对象转成的是吧那我们要解析这个ticket的话那么我们就可以把jensen串再转回这个对象你说老师那为啥要转成为这个对象那好取数据啊现在你这个jensen串你是不是不太好方便取数据啊对不对好看讲义啊那么到这呢我们需要做一件事啊注意在解析ticket当中啊我们是需要把这个这个数据的这个类型啊
[03:27] 包括这个pay order can cover这个我在这个资料文件夹给大家已经提供了你需要呢去考出来然后呢我们去把它考到我们的哪里啊那个交易服务然后呢这里边呢我们把它考到我们交易服务因为这两个类还不是一个地方首先这个pay order DTO你要考到交易服务的DTO里头
[03:59] 懂吧原来的我们把它覆盖了因为原来的这个属性呢过少现在呢我考进去的这个可能一些后边我们所需要的一些属性呢我就添进去了啊好那另外我们要做的是把我们给大家提供的这个convertconvert这个是干嘛的对象转换对象转换这里头呢那你要在这你把它考进去是吧原来有了原来有了
[04:28] 好那么考进去之后呢注意这里边呢嗯他就需要他又有一个问题了你看哈有一问题他还需要一个东西需要这个东西没关系啊我们先暂时啊你把它给先屏蔽掉回头我们需要了再把它放开现在这两个对象我都考进去了啊后边会用好那么接下来我们要做的事是什么呀回到这儿我们是不是就可以将这个Jason Chuan转成对象对吧转成对象那转成对象怎么转
[04:58] 用fast json然后呢解析然后呢把json串放进去转成哪个对象就是我们说的这个payorder.dto因为刚才我们已经查代码了我们发现原来我们就是把这个dto的对象转成json然后呢用base64编码然后变成一个ticket然后呢放到支付入口的参数这
[05:28] 对吧所以你现在要去解析的话你肯定是把这个Jason再转回成这个对象对吧那么各位我们现在解析这个Taggate我们现在已经转成对象了接下来要干嘛呢你要注意这个是不是就是我们的入口页面没错吧你现在要做的事很简单因为你的这个页面上呀它是需要一些数据的
[05:55] 其实这个内置对象之前我们学过他就是什么拿到请求的数据这个请求的数据当初我给大家测试了大家还有意见吗请求的数据就是问号懂吧然后就这样通过http url kvalue这个串的格式来拼能理解吗所以这个入口页面后边是要以这种kvalue串的方式来跟参那么跟的这个参数正好一页面
[06:25] 就这个确认页面呢就会把它解析出来所以我们现在说这个Controller这个入口这一块它要做一件事它做什么事呢它要将这个对象的这个属性和值它把它组成一个什么URL的keyvalue串就是就是我们说这个URL后边问号一个key一个value一个key一个value就是这种
[06:53] 组成一个什么组成一个参数的一个KVL串然后呢放到我们说的这个入口的这个后边然后这个页面页面里边当初的这个free marker的这个指令啊它就可以干嘛呀去读取到这个参数了大家能懂这个逻辑吗所以我们现在要做的事啊就是你找到control啊我们现在要做我们是要把这个对象转成这个串
[07:22] 那转成这个串了那咋转呀因为我们项目有好多这个非常好用的什么呀工具类你把这个对象放进去它就通过什么通过反射的技术呢就可以把里边的属性一个一个的都解析出来一解析出来之后呢它就会组成一个什么刚才我所说的K-Value串好那这样的话我拿到了这个K-Value串了各位很显然
[07:53] 我后边就简单了问号然后呢加上这个参数我问你这是不是就搞定了这是不是就是一个整个take的解析的一个什么一个过程了后边我们是不是就可以去测试一下好行不行大家理解这个过程了吗首先你把这个Jason把这个take的转成Jason对吧然后呢把它转成对象然后呢通过工具类我们呢把这个对象里边的这个属性把它拿出来组成一个KVL串
[08:21] 有时候老师这工具类需要我们去掌握吗不需要大家呢有兴趣的私下呢去看一下其实呢它的实现方式你仔细看也都是大家所学习过的一些技术都是Java基础的东西所以其实它的作用就是方便我们开发私下有兴趣的可以看一下那么我们更主要的是把它放到我们说的这个什么业务逻辑和技术方案的这个开发上面好
[08:47] 那这个开发我们是不是就做过了做过了之后呢现在我们就可以来测试了吧怎么测试我们当然还是需要一系列的测试流程生成二维码然后呢去请求他懂这意思吗你不能随便在后边出输入一堆这个tick的那肯定解析失败嘛好那么这个开发我们先到这稍后进行测试好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过控制器接收支付请求参数，解码并转换为 Java 对象，最终生成支付票据并跳转到支付页面。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示支付页面的前端界面，包含商户名称、订单号、金额输入框和“立即支付”按钮。右侧是浏览器开发者工具，显示 HTML 结构和样式。
画面 2: 在 IDE 中，展示 `PayController.java` 文件，其中 `payEntry` 方法接收 `ticket` 参数，准备数据并返回 `forward:/pay-page`。
画面 3: IDE 中展示项目结构，鼠标悬停在 `TransactionBootstrap.java` 上，显示其内容为 Spring Boot 启动类。
画面 4: IDE 中展示 `PayController.java` 文件，高亮显示 `payEntry` 方法，注释说明接收 `ticket` 参数并解码。
画面 5: Windows 资源管理器中，右键点击 `IntelliJ IDEA` 文件，弹出菜单，显示“打开方式”选项。
画面 6: IDE 中展示 `PayOrderDTO.java` 文件，定义了支付订单的属性，如 `appId`、`channel`、`outTradeNo` 等。
画面 7: IDE 中弹出“Copy file”对话框，提示复制 `PayOrderConvert.java` 文件到指定目录，用户点击“OK”。
画面 8: IDE 中 `PayController.java` 文件，高亮显示 `JSON` 类的导入语句，准备使用 JSON 工具类。
画面 9: IDE 中 `PayController.java` 文件，展示 `payEntry` 方法中将 `ticket` 解码为 JSON 字符串，再转换为 `PayOrderDTO` 对象，最后生成支付 URL 并返回。
画面 10: 浏览器中，支付页面 URL 后面添加了 `ticket` 参数，页面加载成功。
画面 11: IDE 中展示 `pay.html` 文件，其中包含表单元素，如隐藏字段 `appId`、`channel`、`outTradeNo` 等，以及文本输入框。
画面 12: 浏览器中，支付页面加载，用户在“订单号”输入框中输入内容，页面显示加载中状态。
画面 13: IDE 中展示 `ParseURLPair.java` 文件，定义了 `parseURLPair` 方法，用于解析 URL 参数。
画面 14: IDE 中 `PayController.java` 文件，高亮显示 `payEntry` 方法，注释说明接收 `ticket` 参数并解码，然后解析参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@GetMapping("/pay-entry/{ticket}")
public String payEntry(@PathVariable("ticket") String ticket, HttpServletRequest request) {
    // 准备确认页面所需要的参数
    String jsonStr = EncryptUtil.decodeUTF8StringBased(ticket);
    return "forward:/pay-page";
}
```

画面 3:
```java
package com.shanjiupay.transaction;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class TransactionBootstrap {
    public static void main(String[] args) {
        SpringApplication.run(TransactionBootstrap.class, args);
    }
}
```

画面 4:
```java
@GetMapping("/pay-entry/{ticket}")
public String payEntry(@PathVariable("ticket") String ticket, HttpServletRequest request) {
    // 准备确认页面所需要的参数
    String jsonStr = EncryptUtil.decodeUTF8StringBased(ticket);
    return "forward:/pay-page";
}
```

画面 6:
```java
private String appId; // 业务方应用ID，服务内部使用无意义，服务与服务之间
private String channel; // 合并支付的渠道，此处使用渠道编码
private String outTradeNo; // 用户订单号
private String subject; // 订单标题
private String body; // 订单描述
private String currency; // 交易币种
private Integer totalAmount; // 订单金额，单位分为
private String optional; // 自定义数据
private String analysis; // 每笔交易的交易明细，用户自定义
private String extra; // 交易备注，用于交易明细
private String authCode; // 付款码，支付宝或者微信支付“付款”产生的付款码
private String device; // 设备，微信等设备
private String clientIp; // 客户端IP
```

画面 8:
```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;
import com.alibaba.fastjson.serializer.ToStringSerializer;
import com.alibaba.fastjson.serializer.ValueFilter;
import com.alibaba.fastjson.serializer.JSONSerializer;
import com.alibaba.fastjson.serializer.PropertyFilter;
import com.alibaba.fastjson.serializer.SerializeConfig;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer.SerializeWriter;
import com.alibaba.fastjson.serializer

