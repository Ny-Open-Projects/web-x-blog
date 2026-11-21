# 12_通用说明_jackson解决id和日期序列化与反序列化

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\12_通用说明_jackson解决id和日期序列化与反序列化【海量资源尽在 666java.com】.mp4
- 时长 8分21秒（音频 501s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好的下面呢来介绍一下JSON的一些封装那封装啥呢各位还有没有印象在咱们讲到JSON规范的时候是不是有两个要求关于ID和日期呢打开来看一眼那自增的ID呢在网络上进行传输的时候呢是不安全的因为它自增1234这样就暴露在外边了那这时候呢咱们有要求就是需要进行加密处理
[00:28] 这里呢分为两个方向一个是从后台往前台传的时候是一个加密的另外一个方向呢是从前台往后传的时候同样也是加密的那想要完成这个事情大家来思考一下该怎么解决呢能不能定义在具体的业务上呢当然可以但是这样太麻烦了有没有更简单的方式呢当然有咱们一会儿就会去介绍好那第二个
[00:58] 第二个说这个二期类型在进行传输的时候应该是一个13位的时间戳这个解决思路是一样的都有两个方向后台到前台前台到后台下面咱们就介绍一下非常好用的解决方案就是啥呢就是用当前的JIS来进行处理好啊那下面是有那么多类那这些类到底是啥意思呢好OK不要着急咱们一块来看一眼首先呢
[01:31] 看前两个一个是Date反序列化另外一个是Date序列化那这个序列化的意思呢就是说我从日期转成什么呢13位的时间圈那这个呢这个就是从13位的时间圈转成日期类型好那下面这两个呢
[01:51] 你看这边说了啊说是序列化自增数字的混淆也就是说啊我们现在有一个1它呢会自动帮你转传的转成一个加密后的字符串正好这个是来解密这个字符串的好那这两个呢这两个主要是来过滤一些字段那什么字段呢刚才说了咱们需要进行处理的字段目前要求有两个一个是ID另外一个是Data的类型对吧好那这个呢
[02:22] 这个呢就是把上面的东西给整合一下那好啊那这个代码咋的代码代码其实都已经提供了咱们一块来打开这个工程来看一眼啊好这个代码就在common的工程下面有一个啥呢有一个叫做disk这个包下面啊咱们首先的来看第一个啊就是date这个什么去这个虚率化的一个
[02:47] 那这个Data序列化其实非常简单就是拿到这个当前Data之后呢直接有个getTime直接就是拿到了一个13位的时间圈直接写进去就完事了那反序列化更简单啊反序列化就是怎么着呢我拿到这个时间圈之后啊我直接就干嘛Nu了一个DataNu了一个Data直接返回就可以了那好啊那这个很显然就是从前台到后台去传的时候我用的是这个是吧从
[03:15] 后台到前台传输的时候用的是这个那好那这是日期是吧那关于这个数字加数字加密呢那就是这个这个和这个是吧你看啊首先咱们要进行加密的话呢用的是它那这个加密怎么加密呢比如说我拿到了某一个IDOK您现在啊就认为当前就是某一个ID那拿到ID之后干嘛呢
[03:40] 我已经加密大家这个工具类还有没有印象当前有个IDsUtils这个啊其实就是咱们之前介绍过的一个叫柱子ID的混淆器就是一个工具类他呢拿到当前一个量类型的IT之后呢把它给转了转了啥呢转了AES加密之后转成了一个字符串转成了一个字符串返回这个转完之后呢就是可能一大串的都是一些加密之后的东西了OK
[04:09] 那这个是加密啊这是加密那解密呢解密一样好来看一下啊那解密的话就是我拿到一个啥呢拿到一个浪类型或是integer类型之后呢我还是去到这个当前的idus youtube下边去解密并且呢从当前的浪类型转成啥呢转成了一个好我先看啊嗯往前开这开这啊哦对啊从一个字符块啊从一个字符块转成了一个
[04:43] 浪也行OK那这样的话呢其实就是加密和解密咱们都复完了但这里边还有两个类啊这两个类就是刚才说了这两个类的主要是来处理字段的哪些字段其实在这里边啊它也有非常好的定义咱们可以打开看一看比如说就打开这个啊你看啊就主要是这么一段代码啊首先如果说你是Data类型的话我就走这个方法那这个方法不就是日期的序列化吗
[05:10] OK如果说不是这类型如果说是ID的话呢他就走这个方法他就会干嘛就会进行加密的混淆当然那这里边啊还有一个叫什么有ID Encrypt这个诸解的属性也会走这个逻辑那他是谁呢他呢其实就是咱们刚才说的这个东西他呢就是说自定义的诸解作用在需要混淆的字段属性上
[05:38] 用于非ID的属性大家想一想为什么说非ID的属性上呢很简单吧因为ID啊咱们已经定义了就说ID它会自动去走如果说你有其他资产也要进行加密混淆的话OK也能办事也能成怎么办呢你需要加这么一个诸解在这属性上就可以了比如说啊咱们打开一个表啊
[06:03] 比如说我这已经打开了一个表比如这个咱们就是文章信息表那这个ID啊它会自动的进行加密混淆但是你发现下面还有一些什么auth ID是吧还有什么channel ID如果说我这些属性也想进行加密混淆那怎么办呢哎直接说了啊你只需要在这个属性上加这么一个诸解就可以了那怎么加呢OK咱们呢其实打开当前的一个实体内可以看一眼啊咱们的实体在哪呢在这个
[06:32] module 下面啊往下找找好这里面呢是有一个叫做 article article 里面叫 P O G O S 是吧然后有一个 article 你看呃这块啊是你看这个 id 你不用管因为他们自动的去过滤这个 id 字段但是呢如果说你这些字段和这个字段也想进行加密的话也能干也也也能做到就是你需要去加这么一个诸解就可以了那好啊那目前的话呢像刚才咱们说的这两种
[07:00] 这两种方式呢就是第一个是ID的混淆和Data的转成时间车的方式还有反转的方式啊咱们都已经讲完了那这个最终这个类或者这一工具类什么时候生效呢好咱们打开来看一下啊其实呢在下面还有最后一个类那这个类呢咱们可以找一找啊这个类呢其实我告诉你就在这就在当前的common下面这也是有一个common有一个unit那就是它
[07:31] 那它呢就是你看这有一个configuration的注解是吧还有一个addbin也就是说你在启动项目的时候把当前这个类呢给扫描进来然后呢它会自动的去把当前的返回值呢给硕射化同时呢你会发现啊这里边会执行一句话这句话呢就是去注册注册模块那这个模块呢其实就是刚才咱们说的两个跟过滤字段根据字段的不同进行序列化
[08:00] 或者说你看如果你是ID或者说你是日期的话呢那这时候呢咱们就可以干嘛呢就可以走当前的这个方法当然咱们也可以进行反序的话走的是这个方法那好那目前的话呢咱们关于JIGS的封装呢咱们就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何使用 Jackson 序列化和反序列化工具，特别是自定义序列化器（如 IdEncrypt、DateSerializer、ConfusionSerializer 等）来处理敏感字段、日期字段和混淆字段，并通过 InitJacksonConfig 配置类进行全局注册。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档中“6.4 Jackson 封装解决字段序列化及反序列化”的章节，列出主要的自定义注解和序列化器，包括 IdEncrypt、DateSerializer、ConfusionSerializer 等。
画面 2: 在 IDEA 中展示项目结构，选中 ConfusionSerializer.java 文件，右键弹出菜单，准备进行代码操作。
画面 3: 展示 DateSerializer.java 文件内容，其中包含对日期字段的序列化逻辑，使用 jsonGenerator.writeNumber() 写入时间戳。
画面 4: 展示 ConfusionSerializer.java 文件内容，其中包含对自定义字段的序列化逻辑，使用 IdUtils.encryptNumber() 进行加密。
画面 5: 展示 IdUtils.java 文件内容，包含加密和解密的静态方法，使用 AES 算法进行加密。
画面 6: 展示课程文档中“6.5 通用环境说明”章节，介绍多环境切换的配置。
画面 7: 同画面 6，文档页面未变化。
画面 8: 展示 MySQL 数据库的表结构，具体为“ap_article”表的 CREATE TABLE 语句，包含字段定义和注释。
画面 9: 展示 ConfusionSerializerModifier.java 文件内容，其中包含根据字段注解动态注册序列化器的逻辑。
画面 10: 展示 ApArticle.java 文件内容，其中包含字段定义，如 @IdEncrypt 注解的 channelId 字段。
画面 11: 展示项目结构，选中 article 包，准备查看或操作相关代码。
画面 12: 展示项目结构，选中 init 包，准备查看或操作相关代码。
画面 13: 展示 InitJacksonConfig.java 文件内容，其中包含初始化 ObjectMapper 并注册 ConfusionModule 的配置代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
主要针对一些数据进行过滤设置，使用jackson来实现，比如一些自增的id值或者一些混淆的属性，在互联网传输的过程中尽量不要轻易暴露在外面，这样安全性比较低，应该对这些自增的属性进行加密处理。
日期处理：在网络上进行传输的时候不要直接传输日期格式，传输的格式为13位时间戳，如果在每个日期字段都手动的转换是比较费时的，所以也可以做成自动转换，用的也是jackson来完成
主要的自定义包括：
• IdEncrypt 自定义注解 作用在需要混淆的字段属性上，用于非id的属性上 在 model包下
• DateDeserializer 用于处理日期输入反序列化
• DateSerializer 用于日期的序列化输出
• ConfusionSerializer 用于序列化自增数字的混淆
• ConfusionDeserializer 用于反序列化自增数字的混淆
• ConfusionSerializerModifier 用于过滤序列化处理的字段
• ConfusionDeserializerModifier 用于过滤反序列化处理的字段
• ConfusionModule 用于注解模块和修改器
• InitJacksonConfig 提供自动化配置对象Mapper，让各个框架自动处理日期和时间

画面 3:
package com.heima.common.jackson;
import ...
public class DateSerializer extends JsonSerializer<Object> {
    @Override
    public void serialize(Object value, JsonGenerator jsonGenerator, SerializerProvider serializers) throws IOException {
        if (value != null) {
            jsonGenerator.writeNumber(((Date)value).getTime());
            return;
        }
        serializers.defaultSerializeValue(value, jsonGenerator);
    }
}

画面 4:
class ConfusionSerializer extends JsonSerializer<Object> {
    @Override
    public void serialize(Object value, JsonGenerator jsonGenerator, SerializerProvider serializers) throws IOException {
        if (value != null) {
            jsonGenerator.writeString(IdUtils.encryptNumber(Long.valueOf(value.toString())));
            return;
        }
        serializers.defaultSerializeValue(value, jsonGenerator);
    }
}

画面 5:
private static final String KEY_SECRET = "12345678901234561234567890123456";
public static String encryptNumber(Long number) throws Exception{
    String src = String.format("%016d", number);
    return encrypt(src);
}
public static Long decrypt(Long src) throws Exception{
    String val = decrypt(src);
    return Long.valueOf(val);
}
public static Integer decryptInt(String src) throws Exception{
    String val = decrypt(src);
    return Integer.valueOf(val);
}
private static String encrypt(String src) throws Exception {
    byte[] raw = KEY_SECRET.getBytes();
    SecretKeySpec skeySpec = new SecretKeySpec(raw, "AES");
    Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
    cipher.init(Cipher.ENCRYPT_MODE, skeySpec);
    byte[] encrypted = cipher.doFinal(src.getBytes());
    return Base64.getEncoder().encodeToString(encrypted);
}

画面 9:
@Override
public List<BeanPropertyWriter> changePropertyWriters(SerializationConfig config, List<BeanPropertyWriter> writers) {
    List<BeanPropertyWriter> newWriters = new ArrayList<>();
    for (BeanPropertyWriter writer : writers) {
        String name = writer.getType().getPropertyName();
        if (null != writer.getAnnotation(IdEncrypt.class)
                && name.equalsIgnorecase(anotherString, "id")
                && writer.getName().equalsIgnorecase(anotherString, "id")) {
            newWriters.add(writer);
        } else if (name.contains("Date")) {
            writer.assignSerializer(new DateSerializer());
            newWriters.add(writer);
        } else {
            // 有 idEncrypt 注解的属性都会走这个逻辑，都会进行加密
            writer.assignSerializer(new ConfusionSerializer());
            newWriters.add(writer);
        }
    }
    return newWriters;
}

画面 10:
package com.heima.model.article.pojos;
import ...
@Data
public class ApArticle {
    private Integer id;
    private String title;
    @IdEncrypt
    private Long authorId;
    private String authorName;
    @IdEncrypt
    private Integer channelId;
    private String channelName;
    private Short layout;
    private Byte flag;
    private String images;
    private String labels;
    private Integer likes;
    private Integer collection;
}

画面 13:
package com.heima.common.common.init;
import ...
@Configuration
public class InitJacksonConfig {
    @Bean
    public ObjectMapper objectMapper() {
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper = ConfusionModule.registerModule(objectMapper);
        return objectMapper;
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“6.4 jackson封装解决字段序列化及反序列化”，下方列出主要的自定义注解和序列化器。
画面 6: PPT 标题为“6.5 通用环境说明”，子标题为“6.5.1 多环境切换”，内容为“在一个微服务的工程中的根目录下创建三个文件，方便各个环境的切换”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

