# 10_项目搭建_常用工具类说明

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\10_项目搭建_常用工具类说明【海量资源尽在 666java.com】.mp4
- 时长 3分26秒（音频 206s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下面呢咱们去介绍一下工具类啊在整个开发的过程中呢或者说在任何项目的开发过程中肯定会有很多的工具类来去让这个项目或者某些类的去使用那当然黑马头条里边呢它也有很多的工具类需要咱们去知道啊首先呢咱们这个工具类啊我要说一下这个工具类呢咱们已经提供好了
[00:26] 那这个工具类呢你应该熟悉它到底有哪些作用好那咱们一个一个去说其实咱们目前的话呢应该是先熟悉这几个工具类好那这个工具类在哪呢这个工具类呢就在当前的UTU这个工具这个这个工程下边啊是打开这里面呢是有一个commoncommon里面呢是有这么多东西刚才说了咱们先熟悉几个啊
[00:55] 首先呢,咱们打开一个叫Data YouTube那这个呢,都是一些日期的一些处理的转换的是吧或许当年日期的啊一些工具类大家呢,可以看一看啊应该在任何项目中像这样的工具类应该有很多当然还有一个叫日期转换的工具类大家也可以去看一看,OK因为这个在单本中去再去写的话可能比较,我后头比较高这是第一,第二个呢,可能单本比较乱
[01:23] 第三个呢就是你抽出来之后呢显得干净是吧重用几率就比较高OK这是工具列啊下面还有一些关于文件的工具类是吧还有一个就是叫IDsUtils那这个呢就是咱们刚才说的那个要数字的混淆怎么混淆呢其实这里边用到了一个AES的一个加密
[01:47] 加密然后是这边是有两块第一个是加密第二个是解密既然能加当然也能解是吧这个就是最深加密好大家也可以去看一看这个主要就是像这些工具类刚才说了这项目里有很多你只需要能够知道它某一个方法的作用即可然后下面还有些工具再看一看下大家掌握的知道的吧应该是有一个叫URL的签名URL签名的工具类
[02:16] 还有一个就是下面有一个JWT有一个JWT的生成生成和解析那这个JWT呢其实咱们之前应该是有过认识啊它呢会去产生一大就是一个字幕串这个字幕串里边呢就是个JSONJSON呢主要是存的就是用户的信息主要是可以
[02:41] 可以给用户生成一个token然后每次用户请求的时候呢可以把token带过来然后去解析当前这个串获取到用户信息好然后下面还有一个Thread local那Thread local的话loco里边呢咱们现在主要是掌握或者说知道一个就可以啊就是app Thread local utils它呢就是可以把当前的这种appapp用户就是移动端的用户呢给放进去
[03:09] 然后也可以取出来放到当前的现成中好行那目前的这些工具类呢咱们就先介绍在这里然后大家呢在课下呢也可以去点开当前的项目去查看一下当前的一些工具类

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个名为“heima-leadnews”的Java项目中，`utils`模块下各个工具类（如日期工具、数据转换、文件、加密、线程本地、JWT）的代码实现与结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDEA项目结构，选中`heima-leadnews-utils`模块，右侧显示文档“6.2 工具类说明”，列出`IdUtils`、`UrlSignUtils`、`AppJwtUtils`等工具类。
画面2：打开`DateUtils.java`，展示日期格式常量定义和`getCurrentDate()`方法，注释显示“获取当前日期”。
画面3：在`DateUtils.java`中，展示`getDateToString(Date date)`方法，用于将日期对象格式化为字符串。
画面4：在`DateUtils.java`中，展示`getCurrentDate()`方法使用`DATE_TIME_FORMAT`格式化当前日期。
画面5：打开`DataConvertUtils.java`，展示`convert`和`unConvert`方法，用于对象转换。
画面6：打开`FileUtils.java`，展示`readStringFromResource`方法，用于读取资源文件内容。
画面7：打开`IdUtils.java`，展示`encrypt`和`decrypt`方法，用于加密和解密长整型和字符串。
画面8：在`IdUtils.java`中，展示`decrypt`方法的实现，使用`SecretKeySpec`和`Cipher`进行解密。
画面9：在IDEA中，选中`heima-leadnews-utils`模块下的`com.heima.utils.common`包。
画面10：在IDEA中，选中`heima-leadnews-utils`模块下的`com.heima.utils.common`包。
画面11：在IDEA中，选中`heima-leadnews-utils`模块下的`com.heima.utils.jwt`包。
画面12：打开`AppThreadLocalUtils.java`，展示`userThreadLocal`线程本地变量和`setUser`、`getUser`方法。
画面13：在IDEA中，选中`heima-leadnews-utils`模块下的`com.heima.utils.threadlocal`包。
画面14：打开`AppJwtUtils.java`，展示JWT相关常量和`getToKen`方法，用于获取用户token。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
public static String DATE_TIME_FORMAT = "yyyy-MM-dd HH:mm:ss";
public static final String DATE_TIME_STAMP_FORMAT = "yyyy-MM-dd HH:mm:ss";
//2019年07月05日 14:00:32
public static String DATE_TIME_FORMAT_CHINESE = "yyyy年M月d日 HH:mm:ss";
```

画面3：
```java
public static String dateToString(Date date) {
    String datestr = null;
    SimpleDateFormat df = new SimpleDateFormat(DATE_TIME_FORMAT);
    datestr = df.format(date);
    return datestr;
}
```

画面4：
```java
public static String getCurrentDate() {
    String datestr = null;
    SimpleDateFormat df = new SimpleDateFormat(DATE_TIME_FORMAT);
    datestr = df.format(new Date());
    return datestr;
}
```

画面5：
```java
public static Object convert(Object value, Annotation[] annotations) {
    Object convertValue = value;
    if (null != dateConvert) {
        convertValue = dateConvert(value, dateConvert);
    }
    return convertValue;
}

public static Object unConvert(Object value, Annotation[] annotations) {
    Object convertValue = value;
    DateConvert dateConvert = getDateConvert(annotations);
    if (null != dateConvert) {
        convertValue = unDateConvert(value, dateConvert);
    }
    return convertValue;
}
```

画面6：
```java
package com.heima.utils.common;

import ...

public class FileUtils {
    /**
     * 读取资源中的第一行内容
     * @param in
     * @return
     * @throws IOException
     */
    public static String readStringFromResource(InputStream in) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        return br.readLine();
    }
}
```

画面7：
```java
private static final String KEY_AES = "AES";
private static final String KEY_SECRET = "12345678901234561234567890123456";

public static String encrypt(Long number) throws Exception{
    String src = String.format("%016d", number);
    return encrypt(src);
}

public static Long decryptLong(String src) throws Exception{
    String val = decrypt(src);
    return Long.valueOf(val);
}

public static Integer decryptInt(String src) throws Exception{
    String val = decrypt(src);
    return Integer.valueOf(val);
}

private static String encrypt(String src) throws Exception {
    byte[] raw = KEY_SECRET.getBytes();
    SecretKeySpec skeySpec = new SecretKeySpec(raw, KEY_AES);
    Cipher cipher = Cipher.getInstance(KEY_AES);
    cipher.init(Cipher.ENCRYPT_MODE, skeySpec);
    byte[] encrypted = cipher.doFinal(src.getBytes());
    return bytesToHexString(encrypted);
}

private static String decrypt(String src) throws Exception {
    byte[] raw = KEY_SECRET.getBytes();
    SecretKeySpec skeySpec = new SecretKeySpec(raw, KEY_AES);
    Cipher cipher = Cipher.getInstance(KEY_AES);
    cipher.init(Cipher.DECRYPT_MODE, skeySpec);
    byte[] encrypted = cipher.doFinal(src.getBytes());
    String originalString = new String(original);
    return originalString;
}
```

画面8：
```java
private static String decrypt(String src) throws Exception {
    byte[] raw = KEY_SECRET.getBytes();
    SecretKeySpec skeySpec = new SecretKeySpec(raw, KEY_AES);
    Cipher cipher = Cipher.getInstance(KEY_AES);
    cipher.init(Cipher.DECRYPT_MODE, skeySpec);
    byte[] encrypted = cipher.doFinal(src.getBytes());
    String originalString = new String(original);
    return originalString;
}
```

画面12：
```java
package com.heima.utils.threadlocal;

import com.heima.model.user.pojo.AppUser;

public class AppThreadLocalUtils {
    private final static ThreadLocal<AppUser> userThreadLocal = new ThreadLocal<>();

    /**
     * 设置当前线程中的用户
     * @param user
     */
    public static void setUser(AppUser user) {
        userThreadLocal.set(user);
    }

    /**
     * 获取线程中的用户
     * @return
     */
    public static AppUser getUser() {
        return userThreadLocal.get();
    }
}
```

画面14：
```java
package com.heima.utils.jwt;

import ...

public class AppJwtUtils {
    // TOKEN的有效期一天
    private static final int TOKEN_TIME_OUT = 3600;
    // 加密算法
    private static final String TOKEN_ENCRY_KEY = "MDA4ZjIyY2Q0NjJmZDMzM2N2ZDU0OTg2Nzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0MjIzNzg0NjI0

