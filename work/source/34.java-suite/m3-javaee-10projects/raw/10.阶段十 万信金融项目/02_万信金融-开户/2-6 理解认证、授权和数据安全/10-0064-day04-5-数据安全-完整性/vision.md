# 画面线理解：day04-5-数据安全-完整性

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-6 理解认证、授权和数据安全
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-6 理解认证、授权和数据安全\day04-5-数据安全-完整性_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:20, 01:26, 01:28, 01:30, 01:34, 01:37, 01:39, 01:40, 01:53, 01:59, 02:02, 02:03, 02:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:43:52

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
