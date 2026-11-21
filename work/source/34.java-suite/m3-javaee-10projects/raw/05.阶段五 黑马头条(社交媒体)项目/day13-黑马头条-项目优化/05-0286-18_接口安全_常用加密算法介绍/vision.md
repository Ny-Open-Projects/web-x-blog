# 画面线理解：18_接口安全_常用加密算法介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\18_接口安全_常用加密算法介绍【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:54, 01:10, 01:28, 01:52, 02:18, 03:38, 03:52, 04:11, 06:10, 06:42, 07:35, 08:02, 08:12, 08:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:58:01

1) 这一组画面整体在讲什么（一句话）：
讲解接口安全中的加密与解密实现，包括MD5、DES算法的代码编写与测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“day11_接口安全.md”，内容为“4.1 功能需求”和“4.2 接口定义”，其中“4.2.1 基本定义”部分列出了接口名称、请求DTO和响应DTO。
画面2：在IntelliJ IDEA中，项目结构显示“com.heima.utils”包下的“MD5Utils.java”文件被选中，准备进行代码编写。
画面3：展示课程文档“day11_接口安全.md”，内容为“4.2.2 CODE定义”，列出了多个异常码及其含义。
画面4：在IntelliJ IDEA中，项目结构显示“com.heima.utils”包下的“MD5Utils.java”文件被选中，准备进行代码编写。
画面5：在IntelliJ IDEA中，打开“MD5Utils.java”文件，显示MD5加密算法的代码实现，包括MessageDigest实例化、更新和计算摘要。
画面6：在浏览器中打开CSDN博客，内容为“string转byte[]数组”和“byte[]数组转string”相关代码示例。
画面7：在浏览器中打开百度搜索页面，搜索框内输入“ml”。
画面8：在IntelliJ IDEA中，运行“MD5Utils.java”文件中的main方法，输出加密后的字符串。
画面9：在Navicat for MySQL中，打开“ap_user”表，显示用户数据，并执行UPDATE语句修改用户信息。
画面10：在IntelliJ IDEA中，打开“DESUtils.java”文件，显示DES加密算法的代码实现，包括密钥生成、初始化和加密操作。
画面11：在IntelliJ IDEA中，运行“DESUtils.java”文件中的main方法，输出加密和解密后的字符串。
画面12：在IntelliJ IDEA中，打开“DESUtils.java”文件，显示将字符串转换为字节数组的代码。
画面13：在IntelliJ IDEA中，打开“DESUtils.java”文件，显示解密方法的代码实现，包括密钥生成、初始化和解密操作。
画面14：在IntelliJ IDEA中，运行“DESUtils.java”文件中的main方法，输出加密和解密后的字符串。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
4.1 功能需求
在互联网的世界里，安全是一个避不开的话题，如何让用户的信息在传输期间不被泄露，被他人获取滥用，就需要了解相关知识，本书从密码加密和验证这个功能带你进入这个全新的领域。
本案例开发功能包括：
• 改造登录功能
• 改造登录功能进行加密验证
• 实现不同的加密工具类
4.2 接口定义
用户登录验证接口
4.2.1 基本定义
参考标准  请参考通用接口规范
接口名称  /api/v2/login/login_auth
请求DTO  com.heima.article.mysql.core.model.poios.app.ApUser
响应DTO
```

画面3：
```
4.2.2 CODE定义
PARAM_INVALID    PARAM_INVALID(501,"无效参数").
AP_USER_DATA_NOT_EXIST   AP_USER_DATA_NOT_EXIST(1000,"ApUser数据不存在").
LOGIN_PASSWORD_ERROR   LOGIN_PASSWORD_ERROR(2,"密码错误").
```

画面5：
```
public final static String encode(String str) {
    try {
        //创建并指定算法名称的摘要
        MessageDigest md = MessageDigest.getInstance("MD5");
        //使用给定的字节数组更新摘要
        md.update(str.getBytes());
        //进行计算并返回一个字节数组
        byte mDBytes[] = md.digest();
        //将字节数组转为字符串
        String hash = "";
        for (int i = 0; i < mDBytes.length; i++) {
            int temp;
            //如果某字节小于0，则转换为正数
            if (mDBytes[i] < 0) {
                temp = 255 + mDBytes[i];
            } else {
                temp = mDBytes[i];
            }
            hash += Integer.toHexString(temp);
        }
        return hash;
    } catch (Exception e) {
        e.printStackTrace();
        return "";
    }
}
```

画面6：
```
string转byte[]数组
String str = "abcd";
byte[] bs = str.getBytes();

byte[]数组转string
byte[] b = {97,98,99,100};
String res = new String(b,"UTF-8");
```

画面8：
```
System.out.println(encode(str));
System.out.println(encode("123456"));
```

画面9：
```
UPDATE `ap_user` SET `salt` = '123' WHERE (`id` = '1')
```

画面10：
```
try {
    DESKeySpec keySpec = new DESKeySpec(keyBytes);
    String algorithm = "DES";
    SecretKeyFactory keyFactory = SecretKeyFactory.getInstance(algorithm);
    SecretKey key = keyFactory.generateSecret(keySpec);
    String transformation = "DES/CBC/PKCS5Padding";
    Cipher cipher = Cipher.getInstance(transformation);
    cipher.init(Cipher.ENCRYPT_MODE, key, new IvParameterSpec(keyBytes));
    byte[] result = cipher.doFinal(content);
    return result;
} catch (Exception e) {
    e.printStackTrace();
    return null;
}
```

画面11：
```
byte[] encrypted = encrypt(content.getBytes(), key.getBytes());
System.out.println("加密后：" + byteToHexString(encrypted));
byte[] decrypted = decrypt(encrypted, key.getBytes());
System.out.println("解密后：" + byteToHexString(decrypted));

System.out.println(encode(content));
String s = new String(byteToHexString(decrypt(passcode)));
System.out.println(s);
```

画面12：
```
private static int toB(char c) {
    if (c == 'a') {
        return 0;
    }
    if (c == 'A') {
        return 0;
    }
    return c - '0';
}

private static byte[] hexToByteArray(String strIn) {
    byte[] arrIn = strIn.getBytes();
    //两个字符表示一个字节，所以字节数组长度是字符串长度除以2
    byte[] arrOut = new byte[arrIn.length / 2];
    for (int i = 0; i < arrIn.length; i += 2) {
        String strTmp = new String(arrIn, i, length);
    }
}
```

画面13：
```
private static byte[] decrypt(byte[] content, byte[] keyBytes) {
    try {
        DESKeySpec keySpec = new DESKeySpec(keyBytes);
        String algorithm = "DES";
        SecretKeyFactory keyFactory = SecretKeyFactory.getInstance(algorithm);
        SecretKey key = keyFactory.generateSecret(keySpec);
        String transformation = "DES/CBC/PKCS5Padding";
        Cipher cipher = Cipher.getInstance(transformation);
        cipher.init(Cipher.DECRYPT_MODE, key, new IvParameterSpec(keyBytes));
        byte[] result = cipher.doFinal(content);
        return result;
    } catch (Exception e) {
        e.printStackTrace();
        return null;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4 接口安全”，子标题为“4.1 功能需求”和“4.2 接口定义”，其中“4.2.1 基本定义”部分包含表格，列出了“参考标准”、“接口名称”、“请求DTO”和“响应DTO”。
画面3：PPT标题为“4.2.2 CODE定义”，包含表格，列出了“PARAM_INVALID”、“AP_USER_DATA_NOT_EXIST”和“LOGIN_PASSWORD_ERROR”及其对应的异常码和描述。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
