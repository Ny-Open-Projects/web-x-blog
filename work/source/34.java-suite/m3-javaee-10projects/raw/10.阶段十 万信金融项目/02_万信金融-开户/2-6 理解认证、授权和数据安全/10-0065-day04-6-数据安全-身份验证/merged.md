# day04-6-数据安全-身份验证

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-6 理解认证、授权和数据安全
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-6 理解认证、授权和数据安全\day04-6-数据安全-身份验证_【海量资源尽在 666java.com】.mp4
- 时长 8分5秒（音频 483s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好这个完整性搞定之后呢咱接下来就剩最后一个问题了就是身份验证呃大家看一看啊为什么还要是这个身份验证呃因为呢即使我们保证了数据的机密性和完整性啊其实这里边还存在一些问题第一个问题就是什么问题就是这个摘要的安全性就是这个摘要它有可能被伪造啊啥意思啊大家看一下这是咱刚才演示的这个效果对吧
[00:28] 一旦这个数据的内容发生了变化这个摘要的这个结果是不是两次就不一样但是这个内容大家有没有想这个内容也会被伪造你比如说如果人家知道了你的摘要算法很有可能会这么做即使啊这个原始的数据内容发生了变化人家也可以把这个结果给伪造成这个明白什么意思吧伪造成这个其实就是说数据内容已经变了但是
[00:57] 你会发现呢你得到的这个结果就是这两个东西其实是什么呀还是一样的因为第二次我们摘要出来的这个摘要的这个结果被干什么呀被篡改被伪造伪造成跟原来的是一样的明白什么意思吧所以说这个东西也需要进行什么呀加密也需要进行加密怎么加密呢就是咱第一步第一个问题里边涉及到机密性是不是说它的这个安全性也得进行保证那还有第二个问题第二个问题就是
[01:28] 消息的发送方如何确定比如说A要给我发消息我怎么确定这个消息一定是A发给我的不是B发给我这咋确定是不是所以你会发现了即使我们分别保证了机密性还有这个什么完整性但是仔细想想这里边还有一项问题那这个问题怎么解决呢这就是要进行身份验证其实这个身份验证一会儿大家会明白身份验证就是把机密性和完整性给综合到一起进行使用就行了
[01:58] 你看咱前面在讲机密性和完整性的时候是分开的对吧机密性就是我加密解密完整性就是我摘要是不是那身份验证其实相当于是把机密性和什么完整性综合到一起我既保证了机密性又保证了完整性综合到一起的话还能确定这个什么呀身份还能进行身份验证所以具体怎么做呢咱进来看看你看他是这样做的看好了啊他说发送方将消息的原文
[02:29] 就是明文嘛使用摘要算法生成摘要这是咱刚才说过然后他还要用私钥对摘要进行什么呀加密你看这一句话就表明了我们既用到了机密性又用到了什么呀完整性嘛你看摘要这个东西不就是完整性里边的吗然后呢我们又用私钥对摘要进行什么呀加密这个私钥比如咱刚才讲的机密性当中的那个非对称加密算法明白吧然后生成的这个东西有一个专业的数据叫数字签名
[02:59] 数字签名啊也就是这个相当于就是能证明身份的那个那个那个那个东西数字签名这非常非常重要那然后接收方怎么办呢接收方这的接到消息之后呢他要用公钥对这个数字签名进行解密那为啥是公钥呢因为他加密的时候用的是什么呀私钥我们前面讲过公钥和私钥是不是一对一对的对不对啊所以你用私钥加密这边就得用什么呀公钥解密只要你能解密成功
[03:28] 其实这个时候呢就已经证明了对方的什么呀身份你要你解密失败了那就肯定证明不了对方的身份因为我刚才强调这个非对称算法这个公钥和私钥是成对出现啥意思啊我在这给大家强调一下成对是什么意思啊你看好就说A公钥A私钥还有B公钥和什么呀B私钥啥意思呢
[04:02] 比如你用A公钥加密了就只能用A私钥进行解密你不能用B私钥进行解密你明白什么意思吧你用B公钥进行加密了你就只能用B私钥进行解密你无法用A私钥进行什么呀解密这叫成对那你用A公钥加密的东西我要是用A私钥进行解密了解密成功了那不就证明对方的身份了是不是因为他们是成对出现了嘛然后呢我们再用这奥算法
[04:33] 把那个JL是不是给他也生成一下对吧然后对比一下前后这两个JL是否相同相同就证明这个数据也没有被修改是不是也验证了这个完整性对不对所以说呢其实身份验证就相当于是把机密性和完整性给综合到一起来运用一下就行那我们这儿呢也有一个例子一块代码给大家演示这个效果同样的还是这个代码呢大家不用去研究看看这个效果就行你看它这是
[05:03] shae v字啊s a啥意思这不就是机密性加上什么呀完整性吗是不是shae是这个gel算法是保证那什么呀是跟什么有关完整性有关的而sa是什么呀是一个加密算法吧是不是它是这个机密性所以说它是一个综合运用吗刚才就是这样说的呃那这块的代码其实主要就是两个方法了你看一下散方法就是进行签名了
[05:32] 进行签名你看他是用私钥进行签名用公钥进行验签嘛就解密嘛是这个方法然后呢这个verify是进行什么验签的那咱接下来看这个效果就行了来咱看这块测试代码你看他首先是不是得到了这个什么密钥对是不是这个get0是公钥get1是私钥然后呢原始数据是传输博客然后接下来你看他说假设啊我们模拟的嘛
[06:03] A向B发送数据使用的是私钥生成签名调用的这个方法刚才大家看到三方用私钥然后生成的签名长什么样他会给你打印出来让你看看那B那边收到这个签名之后呢他会进行什么呀Verify会进行验签就是相反的一个操作嘛然后呢他把这个验签后的这个数据也给你打印出来然后要么成功要么什么呀失败嘛大概呢就是这么一个
[06:35] 效果那咱们接下来走一走看一看走咱看一下这个控制台的打印你看这是什么公钥这是什么私钥然后传输博客这是原始数据生成的签名就长这样然后B这边收到A的数据之后进行了什么验签用公钥进行验签验签出来的当然我们这肯定是验签成功了你看它跟这的值是什么是一样的就证明验签成功
[07:08] 所以最后呢大家一定要注意啊我们这个数字签名这一块其实是综合运用了什么呀机密性和完整性综合运用最终达到的一个效果这是整个数据安全相关的整个这一套东西吧给大家整体介绍了一下最后还是给大家强调一下这里边呢这个机密性啊完整性啊包括最后这个数字签名整个这一套东西呢我们在后边P2P项目的开发过程当中都会用到
[07:35] 那这里边呢就是重在是以理解为主啊知道呢我刚才讲的这些东西都是干嘛至于这里边的这些代码大家不用去管我们在P2P项目当中将来这些代码都是封装好啊封装成类封装成方法大家直接拿用就是到时候讲的时候哎你得知道哎什么叫这个什么呀加密算法对吧什么叫这个什么呀摘要什么叫数字签名哎提到这些东西你得知道是咋回事就OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

