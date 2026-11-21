# day04-5-数据安全-完整性

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-6 理解认证、授权和数据安全
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-6 理解认证、授权和数据安全\day04-5-数据安全-完整性_【海量资源尽在 666java.com】.mp4
- 时长 3分45秒（音频 225s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那搞定了机密性之后呢咱接下来接着要搞定第二个问题就是完整性完整性我们前面说过完整性就是指的防止数据被篡改就是说我给对方发的是123对方收到的必须是什么123不能是12也不能是1234对吧那这个完整性怎么来确保对吧万一我的这个数据被篡改了对方怎么知道这个事呢他咋知道这个数据变了还是没变呢那这里边呢其实主要是通过
[00:31] 一个手段啊一个手段叫消息摘要消息摘要其实指的就是对你发送的这个数据啊他从中进行按照某种算法进行内容的一个提取然后呢最终呢他判断这个消息摘要前后这个有没有变化一旦有变化证明这个数据发生这个被有可能被什么呀篡改啊如果前后这个消息摘要一对比没有啥变化证明这个数据在
[01:00] 整个传输过程当中呢没有发生任何变化那么常见的这种摘要算法有SAE啊SA256啊MD5对吧这个我觉得大家应该是听说过的吧MD5MD5算法了对不对它是一种我们号称不可逆的一种一种算法它其实就属于消息摘要算法其实主要是为了保证数据的什么呀完整性那咱这呢也有一个例子也有一块带吧
[01:29] 但是也是跟前面一样这些呃代码包括这些例子大家不用去研究啊不用去管吧大家只需要看一看效果就行呃大家看这儿吧这里边其实你重点看这一个方案就行啊那传进来这个参数就是这个明文数据明文数据啊那这个方法呢就是呃对这个数据进行什么呀进行他用的不是md他用的是sha256啊进行加密或者进行这个消息摘要
[02:00] 那我们怎么进行测试看这个效果呢大家看这很简单你看我要传输的名文数据是不是还是传直播客对吧然后呢我分别调用这个方法调几次调两次当然我这个名文数据没有改没有改我们看看这个内容他俩是不是一样的一会儿我再改一下再看看他俩这个内容是不是一样的就行了我们第一次运行大家看一下我对传直播客这个名文数据第一次进行摘要之后是不是长这个样子对不对
[02:32] 你看上下这两个串内容一样吗很明显是不是一模一样那只要这两个东西一样就证明传这波克这个数据在传输过程当中有没有发生变化对没有发生变化那你看看假如说假如说在传输过程当中被人恶意修改比方说少了一个克字对不对那我们接下来看看它会有啥变化我们应该这么子来给大家演示这个效果少俩字吧对不对
[03:11] 这个明白什么意思吧啊然后我发送的时候是传知播客那么对方接收到时候已经变成什么呀对变成传知了咱现在走走一下你看看你看明显上下两次这个这要获得这个结果一样吗不一样哎不一样我就说明什么呀说明我传输的这个消息在这个已经被人干什么呀已经被人篡改啊就这么简单对于我们来说
[03:40] 这是什么这是完整性我们就跟大家演示到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解数据安全中的完整性概念，通过 SHA256 算法演示如何生成并验证消息摘要（Digest），并结合代码实现进行验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 第一页，标题为“一、数据安全”，内容介绍数据安全需解决的三个问题：机密性、完整性、身份验证（抗抵赖性），并以甲乙双方军队通信为例说明机密性。
画面 2: 展示 PPT 第三页，标题为“三、完整性”，内容介绍完整性可通过提取并对比消息摘要实现，消息摘要也叫数据指纹，并列出常见摘要算法：sha1、sha256、md5、crc32。
画面 3: 展示 PPT 第三页，下方出现文字“下面例子演示了 SHA256摘要算法：”，并显示 Java 代码的开头部分。
画面 4: 展示 PPT 第三页，显示 Java 代码的完整 `public class SHA256` 类的 `getSHA256` 方法的 try-catch 块。
画面 5: 展示 PPT 第三页，显示 `private static String byte2Hex(byte[] bytes)` 方法的开头部分。
画面 6: 展示 PPT 第三页，显示 `private static String byte2Hex(byte[] bytes)` 方法的完整代码，包含 `StringBuffer`、`for` 循环和 `Integer.toHexString` 的使用。
画面 7: 展示 IDEA IDE 界面，打开项目 `DataSecurity`，显示测试类 `DataSecurityTest` 中的 `test1()` 方法，用于测试 RSA 加解密，终端显示测试通过。
画面 8: 展示 IDEA IDE 界面，光标在 `test1()` 方法的末尾，终端显示测试通过。
画面 9: 展示 IDEA IDE 界面，光标在 `byte2Hex` 方法的 `for` 循环内部，显示该方法的完整代码。
画面 10: 展示 IDEA IDE 界面，光标在 `SHA256` 类的 `getSHA256` 方法的 `try` 块内，显示 `messageDigest.update(str.getBytes(charsetName: "UTF-8"))` 代码。
画面 11: 展示 IDEA IDE 界面，光标在 `getSHA256` 方法的 `catch` 块内，显示 `NoSuchAlgorithmException` 和 `UnsupportedEncodingException` 的异常处理。
画面 12: 展示 IDEA IDE 界面，光标在 `DataSecurityTest` 类的 `test1()` 方法的末尾，终端显示测试通过。
画面 13: 展示 IDEA IDE 界面，光标在 `test2()` 方法的开头，显示该方法用于测试 SHA256 摘要的两次计算。
画面 14: 展示 IDEA IDE 界面，光标在 `test2()` 方法的末尾，终端显示测试通过，输出两次摘要结果一致。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
下面例子演示了 SHA256摘要算法：
public class SHA256 {
```

画面 4:
```java
public static String getSHA256(String str) {
    MessageDigest messageDigest;
    String encodestr = "";
    try {
        messageDigest = MessageDigest.getInstance("SHA-256");
        messageDigest.update(str.getBytes("UTF-8"));
        encodestr = byte2Hex(messageDigest.digest());
    } catch (NoSuchAlgorithmException e) {
        e.printStackTrace();
    } catch (UnsupportedEncodingException e) {
        e.printStackTrace();
    }
    return encodestr;
}
```

画面 5:
```java
private static String byte2Hex(byte[] bytes) {
    StringBuffer stringBuffer = new StringBuffer();
    String temp = null;
    for (int i = 0; i < bytes.length; i++) {
```

画面 6:
```java
private static String byte2Hex(byte[] bytes) {
    StringBuffer stringBuffer = new StringBuffer();
    String temp = null;
    for (int i = 0; i < bytes.length; i++) {
        temp = Integer.toHexString(bytes[i] & 0xFF);
        if (temp.length() == 1) {
            stringBuffer.append("0");
        }
        stringBuffer.append(temp);
    }
    return stringBuffer.toString();
}
```

画面 7:
```java
public void test1() throws Exception {
    Map<Integer, String> keyMap = RSAEncrypt.genKeyPair();
    String content = "传智播客";
    System.out.println("随机生成的公钥为：" + keyMap.get(0));
    System.out.println("随机生成的私钥为：" + keyMap.get(1));
    String messageEn = RSAEncrypt.encrypt(content, keyMap.get(0));
    System.out.println("加密后的字符串为：" + messageEn);
    String messageDe = RSAEncrypt.decrypt(messageEn, keyMap.get(1));
    System.out.println("解密后的字符串为：" + messageDe);
}
```

画面 10:
```java
public static String getSHA256(String str) {
    MessageDigest messageDigest;
    String encodestr = "";
    try {
        messageDigest = MessageDigest.getInstance("SHA-256");
        messageDigest.update(str.getBytes(charsetName: "UTF-8"));
        encodestr = byte2Hex(messageDigest.digest());
    } catch (NoSuchAlgorithmException e) {
        e.printStackTrace();
    } catch (UnsupportedEncodingException e) {
        e.printStackTrace();
    }
    return encodestr;
}
```

画面 13:
```java
public void test2() throws Exception {
    String content = "传智播客";
    System.out.println(content + "：第一次摘要后的字符串为：" + SHA256.getSHA256(content));
    System.out.println(content + "：第二次摘要后的字符串为：" + SHA256.getSHA256(content));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“三、完整性”，内容包含一个流程图：
- 左侧是一个文本框，内容为一段英文文本。
- 一个箭头从该文本框指向右侧的“Hash”方框。
- 一个箭头从“Hash”方框指向右侧的“Digest”方框。
- 下方文字：“下面例子演示了 SHA256摘要算法：”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

