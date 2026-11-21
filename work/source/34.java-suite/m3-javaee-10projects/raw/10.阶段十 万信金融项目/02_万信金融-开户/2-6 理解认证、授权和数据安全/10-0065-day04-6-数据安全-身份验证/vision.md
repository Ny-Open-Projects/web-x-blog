# 画面线理解：day04-6-数据安全-身份验证

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-6 理解认证、授权和数据安全
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-6 理解认证、授权和数据安全\day04-6-数据安全-身份验证_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 03:08, 03:22, 04:30, 04:46, 04:57, 05:23, 05:26, 05:44, 06:21, 06:40, 07:07, 07:20, 07:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:44:46

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 SHA1 作为摘要算法、RSA 作为签名加密算法，实现数字签名的生成与验证过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 IDEA 编辑器中 RSAEncrypt.java 文件的 sign 方法，其中包含注释说明参数和返回值，并在终端显示了两次摘要计算的十六进制结果。
画面 2: 展示 PPT 页面，图示“Signature”通过箭头指向另一个“Signature”，下方文字说明接收方如何使用公钥解密数字签名以完成身份验证。
画面 3: 与画面 2 内容相同，为 PPT 页面的延续展示。
画面 4: 与画面 2、3 内容相同，为 PPT 页面的延续展示。
画面 5: 展示 PPT 页面，标题为“四、身份验证”，内容讨论了即使数据完整性和机密性得到保证，仍需解决如何确定消息来源不是第三方伪造的问题。
画面 6: 展示 PPT 页面，图示“Signature”和“Digest”并列，中间有“?”，下方文字说明使用 SHA1 作为摘要算法、RSA 作为签名加密算法的签名及验签过程，并展示 sign 方法的代码片段。
画面 7: 与画面 6 内容相同，为 PPT 页面的延续展示。
画面 8: 展示 IDEA 编辑器中 RSAEncrypt.java 文件的 sign 方法，光标位于方法体内部，终端显示了两次摘要计算的十六进制结果。
画面 9: 展示 IDEA 编辑器中 RSAEncrypt.java 文件的 verify 方法，代码逻辑用于验证签名。
画面 10: 展示 IDEA 编辑器中 DataSecurityTest.java 文件，代码逻辑用于生成签名并验证签名。
画面 11: 与画面 10 内容相同，为代码的延续展示。
画面 12: 展示 IDEA 编辑器中 DataSecurityTest.java 文件的运行结果，终端输出了“随机生成的a方公钥”、“原文：传智播客 生成签名”、“验证签名成功”等信息。
画面 13: 与画面 6 内容相同，为 PPT 页面的延续展示。
画面 14: 与画面 6 内容相同，为 PPT 页面的延续展示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
keyMap.put(0, publickeyString); //表示公钥
keyMap.put(1, privateKeyString); //表示私钥
return keyMap;
```
```java
public static final String SIGN_ALGORITHMS = "SHA1WithRSA";
```
```java
/**
 * RSA签名
 * @param content 待签名数据
 * @param privateKey 私钥
 * @param input_charset 编码格式
 * @return 签名值
 */
```
画面 6:
```java
public static final String SIGN_ALGORITHMS = "SHA1WithRSA";
```
```java
/**
 * RSA签名
 * @param content 待签名数据
 * @param privateKey 私钥
 * @param input_charset 编码格式
 * @return 签名值
 */
```
```java
public static String sign(String content, String privateKey, String input_charset) {
    try {
        PKCS8EncodedKeySpec priPKCS8 = new PKCS8EncodedKeySpec(decoder.decode(privateKey));
        KeyFactory keyf = KeyFactory.getInstance("RSA");
        PrivateKey priKey = keyf.generatePrivate(priPKCS8);
        Signature signature = Signature.getInstance(SIGN_ALGORITHMS);
        signature.initSign(priKey);
        signature.update(content.getBytes(input_charset));
        byte[] signed = signature.sign();
        return encoder.encodeToString(signed);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return null;
}
```
画面 9:
```java
public static boolean verify(String content, String sign, String public_key, String input_charset) {
    try {
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        byte[] decoder = decoder.decode(public_key);
        PublicKey publicKey = keyFactory.generatePublic(new X509EncodedKeySpec(decoder));
        Signature signature = Signature.getInstance(SIGN_ALGORITHMS);
        signature.initVerify(publicKey);
        signature.update(content.getBytes(input_charset));
        boolean verify = signature.verify(decoder.decode(sign));
        return verify;
    } catch (Exception e) {
        e.printStackTrace();
    }
    return false;
}
```
画面 10:
```java
Map<Integer, String> akeMap = RSAEncrypt.genKeyPair(); //a方对应的公私钥
System.out.println("随机生成的a方公钥为：" + akeMap.get(0) + "，a方私钥为：" + akeMap.get(1));
String content = "传智播客";
System.out.println("-------------a向b发送数据，使用a的私钥生成签名-------------");
String signature = RSAEncrypt.sign(content, akeMap.get(1), input_charset = "utf-8");
System.out.println("原文：" + content + " 生成签名：" + signature);
System.out.println("-------------b接收到a发的数据，使用a的公钥验证签名-------------");
if (RSAEncrypt.verify(content, signature, akeMap.get(0), input_charset = "utf-8")) {
    System.out.println("验证签名成功：" + signature);
} else {
    System.out.println("验证签名失败！");
}
```
画面 12:
```text
随机生成的a方公钥为：MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMjZU6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z6Z8yQ97Z
