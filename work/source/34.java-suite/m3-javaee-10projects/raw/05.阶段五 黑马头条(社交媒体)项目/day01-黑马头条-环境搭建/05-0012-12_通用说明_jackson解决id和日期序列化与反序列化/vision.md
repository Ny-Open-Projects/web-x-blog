# 画面线理解：12_通用说明_jackson解决id和日期序列化与反序列化

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\12_通用说明_jackson解决id和日期序列化与反序列化【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:14, 02:33, 03:15, 03:38, 04:27, 04:49, 05:28, 06:03, 06:39, 06:55, 07:22, 07:29, 07:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:32:14

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
