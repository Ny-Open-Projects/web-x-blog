# 画面线理解：day04-4-数据安全-机密性

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-6 理解认证、授权和数据安全
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-6 理解认证、授权和数据安全\day04-4-数据安全-机密性_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 02:07, 02:45, 03:53, 04:40, 06:05, 06:25, 07:00, 07:13, 07:20, 07:46, 08:02, 08:50, 09:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:43:11

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
