# 18_接口安全_常用加密算法介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\18_接口安全_常用加密算法介绍【海量资源尽在 666java.com】.mp4
- 时长 8分33秒（音频 514s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们来去说一下第四块内容就是接口安全咱们先看一下这个功能需求啊那可以先读一下这段话嗯说什么呢在互联网的世界里呢安全是一个避不开的话题哎如何让用户的信心呢在保护下访问应用不暴露在互联网啊被他人获取盗用是吧就需要了解加密相关的知识那这份呢咱们主要啊是从密码加密和验证啊这两个功能去说啊
[00:28] 咱们的会去改造咱们之前的登录的系统改造啊那改造之后呢这个呢咱们需要去用密码去验证了咱们之前的是没有做任何这种加密的处理的好吧那这个这个呢这个内容啊主要是多了两块内容第一个呢就是登录啊咱们要去做验证登录之前呢咱们需要去了解一些这种加密的工具类看看到底有哪些好吧那这个接口咱们需要去改造是吧那这个接口你看
[00:57] 这个呢是一个v2也是一个v2看一下我们之前是差不多的这也是个v2然后这个东西啊这个这个路径写的有问题啊怎么可以去搜一下啊叫AP user是吧我们把这个笔记稍微改一改啊那应该是当前这个类啊那响应的呢一般一般的话怎么都是一个response啊这个没有写啊没有写没有写吧但是大家要要能够清晰啊
[01:28] 然后下面会有一些工具类咱们去介绍一下咱们重点去介绍两个一个是MD5另外一个是DSC另外一个是DSC这两个工具类你们目前的系统中是没有的你需要去拷贝把这两个工具列拷贝到当前的common模块下面common模块应该是YouTube下面的common这个包下边好打开我这边已经打开了就是当前的有一个叫做MD5另外一个是DSC
[01:56] DES啊DES啊那就这两个啊咱们把这两个简单说一说就可以啊首先呢来看一下MD5它MD5加密呢它呢是一种什么呢它是一种这种不可逆的不可逆啊那不可逆的意思呢就是说你没办法去解密没办法去解密啊比如说我现在啊是有这么工具的呀咱们可以简单去测一下啊第一种方式呢就是我可以在书记库中直接存一个四复串比如说我的密码是123456
[02:26] 那我去存的时候呢可以看一下你看就是在数据库中去存了这么一个串啊就是存了这么一个串啊但这个串呢它是一个不可逆的刚才说了啊这时候你直接存进去就可以了然后呢用户去登录的时候呢他输入123456咱们再把它给加密完之后呢再去给用户跟那个数据库中去查出来去比对一下这两个串一样不一样就可以了一样的话就说明你的密码输入对了不一样的话那就密码是有问题的是吧
[02:58] 这是一个这种MD也是比较常用的一种方式但还有种方式那种是种方式有可能的不太好为什么说不太好呢我一下这个串呢但是固定的比如说你要再加一次你看怎么可以拷贝出来啊你可以再加密试试你看别管是加密多少次是不是都是当前这个串是吧有你啊
[03:31] 那这样的话有可能会被破解的可能有被破解的可能那你说不是不可逆的吗其实呢这个你在网上去搜啊有很多的这种东西啊怎么可以来关了比如说咱们这有一个叫做什么来着百度M5解密有很多是吧你可以搜一下说我我可以把刚才这个串啊保备一下回完之后呢你直接放到这直接点查询这个结果是不是就出来了这个只是一个
[04:08] 的结果比如说你要是有什么现在只是一个数字是吧你要是有一些字母有一些这种标点符号大小写再区分一下这个解密是不太容易的不太容易的他也是通过这种海量的数据比对然后最终是找到当前的一个串有的公司是这种密码单密的时候咱们会有一个加盐加盐的操作加盐的操作其实就是你再去
[04:35] 再去找另外一个串比如说这是你的密码我再给你一个延这个就是123456是一个延但这样加密完之后它就跟这个就不一样跟这个就不一样了你看它是下面的另外一个字母串这是加延之后的效果你说这个延固定之后比如说我的延就是123456那加延之后的效果那不还一样吗这不是串是不是还是一样的你再一次加密是不是还是这个什么4F结尾的你可以看一下
[05:06] 你看是不是73224F是不是一样啊这样啊它每一个用户有可能是有不同的延每个用户有不同的延你再去保存用户或者要去新增一个用户的时候呢你可以给它不同的延咱们现在是这个123456是一个写死的你在真正实际操作的时候呢你可以给根据当前不同的用户去给不同的延咱们可以看一下当前的咱们的表咱们找到APU4这个表
[05:38] 你看当前这个用户你看这个用户呢比如说这是当前的用户名啊一般的手机号啊根据手机号是吧然后呢是查到一个用户啊然后呢这是他的言123啊这个言也是123是吧当然这个密码这是密码是吧根据密码去比例啊那有可能呢你的你的这个言呢是这样啊有可能是一样的啊这样的话每一个用户的言不一样他这时候比例的四副份就不太一样啊当然你查数据库的时候呢你需要去把
[06:08] 当前的用户查出来拿到他的运用密码和言然后呢再去加密然后再去比对就可以了好吧啊这也是一种方式啊嗯行那这个咱们就说到这儿然后下面呢咱们就可以再去说另外一种啊这是一个MD5比较常用的一种方式啊然后还有还有啥呢还有个DSDS是吧这个呢是一个这种嗯叫对称加密那什么叫对称呢就是刚才说了MD5呢它是一个这种不可逆的
[06:37] DES它是一个可逆的操作可逆的效果是啥你可以看一下下面是有例子比如说这个密码是一个password111然后你需要去加密这个就加密了加密之前你需要去先把它转成16件制转一下16件制然后转完之后你就可以去加密加密之后咱们这样就可以去打印一下当前的效果比如说你执行走
[07:08] 看一下这个效果你看这个是当前这个密码当前这个密码呢然后是先转成了16进制然后呢又给它加密这是它加密后的操作好吧然后呢这里边还有一个东西当然也可以去解密刚才说了也可以解密啊调当前这个方法就可以去解密那解密之后呢咱们就可以打印一下其实就是这么一个东西并且把它转成了当前的一个16进制数然后呢
[07:34] 你就可以再次去解密啊但是那个16进制你转成二进制的byte数组是吧然后呢你再把它转成什么呢转成一个这种spin就可以了好吧那这个呢就是嗯最终呢就能获取到你一开始的密码这是一个对称加密在这里边啊你要去加密的时候呢有一个叫做key这key呢其实就是算是一个密钥啊这个密钥的话目前的话呢加密和解密这个密钥必须一样啊怎么现在目前是写死的但是这个思路你要知道啊
[08:04] 这个密钥也可以变动也可以变动就是你后期的话你也可以去保存这么一份密钥只要是拿到相同的密钥再拿到你的密码就能去加密也能去根据这个密码和密钥去进行干嘛解密就这两个操作好吧那行那这个咱们就介绍两个一个是MD5不可逆的一个是DES是一个可逆的应该是叫做对称的加密好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

