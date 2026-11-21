# day04-4-数据安全-机密性

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-6 理解认证、授权和数据安全
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-6 理解认证、授权和数据安全\day04-4-数据安全-机密性_【海量资源尽在 666java.com】.mp4
- 时长 9分21秒（音频 561s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 搞清楚这三个问题之后呢咱接下来是不是就要一个一个解决都解决了那数据的安全也就得到保证了那咱先搞定这个什么呀机密性那么机密性如何得到保证呢我们就要通过什么呀加密算法这里边就涉及到一些名字概念我们在这首先搞定的是什么呀机密性那机密性的这一块呢涉及到一些名字概念我们需要先跟大家说一说
[00:38] 一个是加密什么算法还有什么还有就是明文还有就是密文咱说这个名文就是原始数据比如说举个例子hello我给对方发了一个数据hello这个hello就是原始数据但是对方在收到数据的时候有可能看到的是这这么一堆乱七八糟的东西这个就是什么密文
[01:07] 那原始的数据这个明文怎么会变成这个密文呢那就是通过什么呀某种算法就是加密算法加密算法呢可以把这种明文数据给它加密成这种数据那这样子呢就提高了数据的安全性啊即使对方拿到了这个数据他也不知道这个数据表示的是什么意思哈喽这个意思明白吧这就是机密性啊他主要是靠这个加密算法把我们的原始数据给它变个样对不对然后再进行
[01:37] 传输就OK了那么在这个加密算法里边呢它整体分成两种一种叫对称加密一种叫非对称加密好大家看加密算法整体分两种对称加密和什么呀非对称加密啥意思嘞来咱进来分别说一说这个对称加密和非对称加密那这样呢我要给大家大概画一个简单的一个图你比如说这是A
[02:20] 这边呢是B这个A和B都是怎么说呢都是地下党A呢要发电报给谁啊对给B那怎么发呢对吧我这个发的这个内容啊不能让国民党知道是不是那怎么办呢就需要进行加密本来举个例子本来呢他发的这个消息的内容就是一个哈喽打个招呼对不对先相互认识一下
[02:50] 那这即使这样的内容我也不想让别人知道是不是那我就要他对他进行加密加密完之后呢哎开始传输传输到b这边b还要进行什么呀解密是不是哎解密说这呢还有一个名字概念叫解密我觉得这个大家应该知道什么意思解密是跟加密正好是什么呀相反啊解密就是把密文转换为对
[03:22] 加密就是把明文转换成什么呀密文嘛咱刚才都已经给大家说过那这里边的话什么叫对称加密算法呢注意听了啊对称加密算法辞职一下对称加密呢指的就是我们刚才是不是提到一个密码本大家有印象吗我这来一个密码本密码本对称加密算法指的是A在对哈喽这个数据加密的时候参考
[04:07] 一个密码本进行加密对吧加密完之后呢传给BB这边在进行解密的时候他参考的还是同一个什么呀密码本明白什么意思吗这叫对称加密就是注意了啊我在这给你写一下对称加密指的是怎么说呢加密和解密使用同一个什么呀它叫密钥密钥啊密钥其实指的就是我说的这个密码本
[04:40] 那你觉得接下来我们要说的非对称加密是啥意思你说非对称加密好然后大家注意了啊我们接下来说一说非对称加密大家做一个对比就行了非对称加密是啥意思呢非对称加密是有两个密码本这是一个密码本然后呢这边也有一个什么呀密码本这俩密码本是一对啊也就是说呢A这边在进行加密的时候呢用一个密码本吧
[05:19] 加密后的密文进行发送发送到B这边B呢也他也要用密码进行解密但是他用的是另外一个密码你知道什么意思吧这叫非对称加密我们在这呢总结一下非对称加密指的是加密和解密使用的是一对什么呀密要分别叫什么呀公
[05:56] 药和私药是一对你比如说这个就叫这边叫公药这边就叫什么呀私药他俩是一对的理论来讲呢非对称加密的安全性要高于对对称加密算法这是这两种算法吧我们整体来介绍了一下这个具体内容的话我们在讲的里边也都有都有详细的介绍对称加密算法常见的有DSAS等等很多很多
[06:25] 非对称加密算法你看这里边他说了有几个密钥两个密钥一个叫public key一个叫private key就是简称就是公钥和什么呀私钥他们都是一对的啊你比如你用公钥加密就得用私钥进行什么呀解密它是成对的那非对称加密的算法就有RSA啊DSA啊ECC等等等等那咱接下来呢关于这一块呢还给大家整了一个例子啊就是基于RSA算法给大家演示了一下怎么生成这个公钥私钥
[06:57] 对吧怎么用公钥加密怎么用私钥解密这么一个过程那给大家说一下这个例子这些代码大家不用去研究你也不用管你只需要看一下效果就行了啊我们这不研究这个这个算法让大家看一下这个代码吧我带大家大家过一遍啊我们不详细的说你看这个方法他就是用来进行加密啊你看这个就是明文数据明文数据这个就是公钥我们用公钥
[07:28] 对这个明文数据进行什么呀加密然后你再看这这个方法就是用来解密的这是我们接收到的那个密文加密后是不是然后这个就是什么呀私钥我们用私钥进行什么呀解密就是这个方法而下面这两个方法是生成那个密钥对的我们刚才说了嘛非对称三法是不是有个公钥有个私钥这俩方法是生成公钥和私钥没了对吧
[07:58] 大概就是这几个方法里边待会你不用管它接下来大家看一下效果就这你看它首先是调用这个方法导到公钥和私钥放到MAP集合里边其中一对是公钥一对是私钥一个公钥一个私钥你看它已经打印了一下get0是公钥get1是什么呀私钥然后呢分别调用这两个方法刚才让大家看了这个方法是对明文数据进行什么呀加密的它用的是公钥进行加密
[08:29] 然后呢他把加密后的密文给你打印了一下然后呢再对这个密文进行解密解密的时候用的是什么呀私钥然后把解密后的数据也打印一下你看解密后的数据跟原来那个什么什么呀这个明文是不是一样好我们走一下看看效果就OK了你看一下这个公钥这是生成的公钥这个对于我来说就是一串的那些烙的东西对吧这是私钥他俩是一堆对不对然后你看加密后的
[08:58] 你看我们的名文是不是传之博客对不对加密之后呢就变成这个样子然后呢你在用这个谁啊私钥进行解密的时候哎他还能还原成什么呀传之博客你看什么意思吧哎这就是我们基于非对称算法给大家演示了一下加密和解密的这个过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解对称加密与非对称加密的基本概念、原理，并通过 Java 代码实现 RSA 非对称加密算法的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 页面，标题为“二、机密性”，内容包括“2.1 对称加密算法”和“2.2 非对称加密算法”，并介绍对称加密使用相同密钥，非对称加密使用公钥和私钥。
画面 2: 展示一个空白文档，内容为“机密性：加密算法：对称加密和非对称加密”，“明文：原始数据 hello”，“密文：ldksuf6d9agdfit6s9dfyhoasdhfas86df9y”。
画面 3: 在文档中绘制一个流程图，包含两个方框 A 和 B，用虚线箭头从 A 指向 B。
画面 4: 在流程图中，从方框 A（内容为“hello”）指向方框 B，中间标注“对称加密”。
画面 5: 在流程图中，从方框 A（内容为“hello”）指向方框 B，中间标注“对称加密”，并在中间增加一个方框“密码本”。
画面 6: 在流程图中，从方框 A（内容为“hello”）指向方框 B，中间标注“对称加密”，并增加一个方框“密码本”；同时，从方框 A 指向方框 B，中间标注“非对称加密”，并增加两个方框“密码本”。
画面 7: 展示 PPT 页面，标题为“2.2 非对称加密算法”，内容包括非对称加密需要公钥和私钥，以及常见的非对称加密算法如 RSA、DSA、ECC。
画面 8: 展示 IntelliJ IDEA 编辑器，打开文件 RSAEncrypt.java，代码为 RSA 公钥加密方法，包括 Base64 编码、RSAKeyFactory、Cipher 初始化等。
画面 9: 展示 IntelliJ IDEA 编辑器，打开文件 RSAEncrypt.java，代码为 RSA 签名方法，包括 PKCS8EncodedKeySpec、KeyFactory、Signature 初始化等。
画面 10: 展示 IntelliJ IDEA 编辑器，打开文件 RSAEncrypt.java，代码为 RSA 解密方法，包括 Cipher 初始化、doFinal 等。
画面 11: 展示 IntelliJ IDEA 编辑器，打开文件 RSAEncrypt.java，代码为生成密钥对的方法，包括 KeyPairGenerator、KeyPair、KeyFactory 等。
画面 12: 展示 IntelliJ IDEA 编辑器，打开文件 DataSecurityTest.java，代码为测试类，包含 main 方法和 test1() 方法，用于生成密钥对、加密和解密。
画面 13: 展示 IntelliJ IDEA 编辑器，打开文件 DataSecurityTest.java，代码为 test1() 方法，用于生成密钥对、加密和解密，并在终端中显示结果。
画面 14: 展示 IntelliJ IDEA 编辑器，打开文件 DataSecurityTest.java，代码为 test1() 方法，用于生成密钥对、加密和解密，并在终端中显示结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 8:
```java
public static String encrypt(String str, String publicKey) throws Exception {
    //base64编码的公钥
    byte[] decoded = decoder.decode(publicKey);
    RSAPublicKey pubKey = (RSAPublicKey) KeyFactory.getInstance("RSA")
            .generatePublic(new X509EncodedKeySpec(decoded));
    //RSA加密
    Cipher cipher = Cipher.getInstance("RSA");
    cipher.init(Cipher.ENCRYPT_MODE, pubKey);
    String outStr = encoder.encodeToString(cipher.doFinal(str.getBytes("UTF-8")));
    return outStr;
}
```

画面 9:
```java
public static final String SIGN_ALGORITHMS = "SHA1WithRSA";

public static String sign(String content, String privateKey, String input_charset) {
    try {
        PKCS8EncodedKeySpec priPKCS8 = new PKCS8EncodedKeySpec(decoder.decode(privateKey));
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        PrivateKey priKey = keyFactory.generatePrivate(priPKCS8);
        Signature signature = Signature.getInstance(SIGN_ALGORITHMS);
        signature.initSign(priKey);
        signature.update(content.getBytes(input_charset));
        return signature.sign();
    } catch (Exception e) {
        e.printStackTrace();
        return null;
    }
}
```

画面 10:
```java
public static String decrypt(String str, String privateKey) throws Exception {
    //base64编码的私钥
    byte[] decoded = decoder.decode(privateKey);
    RSAPrivateKey priKey = (RSAPrivateKey) KeyFactory.getInstance("RSA")
            .generatePrivate(new PKCS8EncodedKeySpec(decoded));
    //RSA解密
    Cipher cipher = Cipher.getInstance("RSA");
    cipher.init(Cipher.DECRYPT_MODE, priKey);
    String outStr = new String(cipher.doFinal(str.getBytes("UTF-8")));
    return outStr;
}
```

画面 11:
```java
public static KeyPair getRsaKeyPair() throws Exception {
    KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
    keyGen.initialize(1024);
    KeyPair keyPair = keyGen.generateKeyPair();
    return keyPair;
}

public static KeyPair getRsaKeyPair() throws Exception {
    KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
    keyGen.initialize(1024);
    KeyPair keyPair = keyGen.generateKeyPair();
    return keyPair;
}
```

画面 12:
```java
package cn.itcast.demo;

import cn.itcast.demo.RSAEncrypt;
import cn.itcast.demo.SHA256;
import org.junit.Test;

public class DataSecurityTest {
    @Test
    public void test1() throws Exception {
        Map<Integer, String> keyMap = RSAEncrypt.genKeyPair();
        String content = "传智播客";
        System.out.println("随机生成的公钥为：" + keyMap.get(0));
        System.out.println("随机生成的私钥为：" + keyMap.get(1));
        String messageEn = RSAEncrypt.encrypt(content, keyMap.get(0));
        System.out.println("加密后的字符串为：" + messageEn);
    }
}
```

画面 13:
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

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“二、机密性”，内容包括“2.1 对称加密算法”和“2.2 非对称加密算法”，并介绍对称加密使用相同密钥，非对称加密使用公钥和私钥。
画面 3: 流程图包含两个方框 A 和 B，用虚线箭头从 A 指向 B。
画面 4: 流程图包含两个方框 A 和 B，用实线箭头从 A 指向 B，中间标注“对称加密”。
画面 5: 流程图包含两个方框 A 和 B，用实线箭头从 A 指向 B，中间标注“对称加密”，并在中间增加一个方框“密码本”。
画面 6: 流程图包含两个方框 A 和 B，用实线箭头从 A 指向 B，中间标注“对称加密”，并在中间增加一个方框“密码本”；同时，从方框 A 指向方框 B，中间标注“非对称加密”，并增加两个方框“密码本”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

