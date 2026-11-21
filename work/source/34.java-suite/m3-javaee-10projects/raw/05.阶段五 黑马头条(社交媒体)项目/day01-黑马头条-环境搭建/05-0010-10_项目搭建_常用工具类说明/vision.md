# 画面线理解：10_项目搭建_常用工具类说明

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\10_项目搭建_常用工具类说明【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:40, 01:01, 01:05, 01:09, 01:14, 01:33, 01:48, 01:51, 02:08, 02:16, 02:50, 03:09, 03:20, 03:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:30:49

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
