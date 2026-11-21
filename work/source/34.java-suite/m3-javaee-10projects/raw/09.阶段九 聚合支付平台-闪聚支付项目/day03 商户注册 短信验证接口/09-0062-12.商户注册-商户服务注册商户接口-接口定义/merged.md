# 12.商户注册-商户服务注册商户接口-接口定义

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\12.商户注册-商户服务注册商户接口-接口定义【海量资源尽在 666java.com】.mp4
- 时长 12分18秒（音频 738s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们就开始来编写商户注册的代码那么我们前面做过需求设计我们说这个注册呢会向三个地方来写当前呢我们会向商户表来写那么我们思考一下现在我们要写代码了这个代码我们应该向哪个工程来写呢我们现在看一下咱们现在的工程都有哪些一个是商户服务对吧这个是散具配杠
[00:33] 平台应用看见吗末尾是application就是对外暴露http接口那么上面呢这个是报什么呀double服务的接口那application呢是不是会调用double服务的接口来完成整个的商户注册是吧当然你也可以看我们的交互流程图在交互流程图上写的也非常清楚前边上边这一块我们都已经完成了就是
[01:02] 前端请求商户平台应用获取手机验证码下边从第四点开始我们要实现前端请求商户平台应用来请求注册那么接口三位置呢接收到请求之后呢他会调用验证码服务来校验验证码验证码校验通过呢他就会请求谁呀商户服务就是这个接口二的位置他呢会最终把商户信息保存到数据库
[01:35] 所以这个流程图我们应该看起来是非常清楚的下面我们该下手编码了大家思考要怎么写这个代码我先问大家个问题我们是先完成接口三还是完成接口二然后我再问一个问题接口三它对外暴露什么协议的接口接口二对外暴露什么协议的接口看好圈两个圈这是接口三
[02:04] 这是接口二我问你接口三对外暴露啥协议的接口接口二对外暴露啥各位有同学应该清楚前端请求的接口都是应该暴露http然后商户服务它对外暴露什么double服务的接口干谁呀商户平台应用所以接口三应该是暴露http接口二应该是暴露double服务的接口
[02:36] 我们清楚了之后呢我们知道了那好现在我们分析应该先写哪个接口先写如果你先写接口三那你会发现这个接口三呢接收手机号然后请求验证码然后呢请求商户服务接口二由于接口二你没有实现接口三你是写不完整的大家理解我的意思吗就是如果你先写接口三由于没有接接口二的情况下接口三是写不完的
[03:08] 所以我建议你先写接口二其实这里啊也希望大家养成一个习惯在正式的开发的时候呢这接口三和接口二可能是不同的人在编写所以大家不要拿着这个需求马上想的是怎么样从Controller调到Service再调到do由这样的顺序来写你应该脱离这个层面你先写哪一层
[03:36] 我觉得大家都应该可以去开发所以要有这么一个什么意识要写任意一层都可以好那现在呢我就建议大家先写接口二先实现这个W服务的接口然后呢供接口三来调用那接口三呢在写的时候它就一气呵成就把它写完了好那现在我们来看我们要写的是商户服务注册商户的接口商户服务大家知道是不是就是我
[04:04] 刚才给大家提到了这个工程就是散区配杠马尔信这里边我们要增加一个接口好那么这里边我们要增加什么接口呢什么接口呢我们要增加一个叫做注册商户对不对那一会儿呢我们再写application里边的注册商户它会调用我们马上要写的这个double服务的接口好这个接口怎么定义呢大家想想
[04:35] 商户注册现在大家要要根据我们前面的需求分析我们说注册的时候要提交一堆信息对吧这堆信息呢他会提交给谁啊提交给我们的这个商户服务商户注册服务他会去把商户信息写入数据库他会把员工的信息也写入数据库他会和SaaS平台进行交互所以这里边我们来看
[05:03] 我们就需要知道他会接收到账号密码手机号等这些信息我们再问大家个问题现在我写这个接口就这儿我问你他接收到账号密码手机号我问你他接收不接收验证码你可能又蒙了所以我们不要离开这个交互流程图这个交互流程图写的非常清楚
[05:31] 这个验证码呢其实是在商户平台应用这一块他就去校验了所以呢商户服务他是不要验证码的商户服务呢只拿到商户的信息就开始保存数据库了就开始调用SaaS平台把这个信息写入到SaaS平台了大家理解吗所以各位注意这里边我要写的这个注册商户的这个服务的这个接口他只接收账号密码手机号懂吧
[05:58] 但是我们为了这个商户服务接口的可扩展性啊所以啊我们在定义这个接口参数的时候呢我建议你定成DTO的这种类型那这里边呢你会发现它不光有我们刚才说的账号密码手机号等等它还有很多的信息那有时候老师这些信息你刚才不是说要放在资质申请那将来保存吗没错
[06:24] 但是也不排除将来需求有变所以这里我就建议你在这里看好为了可扩展性我们使用什么样merchant DTO来接收数据那这个merchant DTO我们之前应该定义过大家看这个是不是就是一个比较全的数据对
[06:48] 所以在Service当中我们就推荐你用这种DTO的这种类型来接收数据将来的扩展起来也方便好那说到DTO了大家应该还有印象DTO是不是在业务层服务层所用到的一个什么存储的类型对吧那么这么多字段让我们去手工定义肯定是比较麻烦的所以
[07:13] 当初我给大家说啥我们说代码生成工具其实是不是也可以生成DTO我们当初在讲买杯TestPlus的时候我们是不是部署了一个叫Generator的这么一个工程那这个Generator工程其实各位它就可以生成DTO它不光可以生成Entity也就是我们DAO层的类型它也可以生成DTO那怎么做呢看好按照我的讲义来因为这个类大家当初不是你自己写的是我从官方
[07:41] 考下来然后改吧改吧给你的是吧所以你参考我的网讲义里边写的然后往你的这个代码里边去改一下就行首先我们需要在整个的这个生成类上边加一个什么变量注意看啊切换到generator然后呢在上边我们定义一个这是干啥呀这个标记就表示什么是否生成DTO
[08:14] 默认是处是吧如果你不想生成你就是force行吧现在我打上处好然后继续再看你需要在你最终生成的这个地方啊你要找找啊这个代码呢因为不是大家写的大家看着挺陌生的大家不要着急然后呢我跟你说在哪找在这这一句这一句是不是就是开始生成代码呀就在这个开始生成代码前面
[08:46] 我写这个大家应该清楚了如果当前准备生成DTO那么我们准备开启SWAG注解也就是生成的这个DTO类当中的自动把SWAG注解就加上了并且它这个命名的方式是后边末尾自动加DTO看懂吗所以注意我们只要写成这样一个配置我们就可以来生成DTO了那怎么做呀
[09:14] 我们就可以运行啊看好运行之前呀我们把这个给它干掉这是之前生成的废的啊干掉好那现在呢我们来看输入模块名大家还知道怎么做呀输入模块名玩信呢好这时候它是不是就开始生成代码了生成代码了之后大家看这里边它是会先查数据库然后生成这个数据库里边表对应的所有代码大家看这个DTO是不是就有了看见了吗
[09:49] 你把这一堆DTO啊考到我们散剧项目的商户服务的这个API工程中考进去看好全部覆盖大家看这个时候呢你会发现DTO就被我这样轻而易举的就生成考进来了大家看到了吗对这就是我们说的DTO的生成方式那后边呢如果哪个字段你想略微调整的话你就局部的调整就行了
[10:20] 后边我们再说好那这样的话我们这个接口是不是就可以动工了也就是接收数据的类型我们已经定义好了我们接口就可以来写了好那么来看一下啊首先我们要知道它最终传入进来的是一个什么Merchant DTO没错吧但是响应的呢也就是你这个商户注册成功呢通常来说商户注册成功就跟上面的查询一样我也把注册好的这个数据
[10:50] 也返回给你就是你注册的时候呢我接收到你的信息然后我写入数据库然后呢写入数据库之后呢这个组件呢就有了我会把这个组件包括全部的信息返回给你告诉你这是最新注册成功的这个什么数据所以我加一个注释大家就清楚了传入进来的是我们商户的什么注册信息返回的就是我们注册成功的商户信息
[11:19] 大家看懂了吗对这就是我们定义的一个什么接口就是注册商户的服务层的接口那么这个接口OK了之后呢我们是不是就可以在它的API对应的Service这个工程当中啊我们来写它的什么实现类了这个我相信大家应该都不陌生了吧好那在这里边呢我们是不是就可以怎么弄啊
[11:46] 就可以调用Mapper然后呢向数据库来写入记录没错吧对这就是我们说的怎么样叫商户服务注册商户的接口这个接口将来对外是暴露Double服务的接口供商户平台应用来远程调用好大家理解了吗到这
[12:11] 我们这个三户服务注册三户的接口定义就写完了一会呢我们再写这个什么实现好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解商户服务注册接口的定义、DTO类设计、以及使用MyBatis Plus代码生成工具自动生成DTO类的过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档“2.4.2 商户服务注册商户(接口②)”的“2.4.2.1 接口定义”部分，说明接口需校验账号、密码、手机号，并添加商户，返回注册结果给商户平台应用。注明本节暂不对接SaaS系统。
画面2：展示IDE中项目结构，包含`shanjunpay-merchant-application`模块及其子模块，如`shanjunpay-merchant-api`和`shanjunpay-merchant-Service`。
画面3：展示文档“2.4.2 商户注册”下的“2.4.1 系统设计”部分，包含一个数据流向图：商户表、员工表、SaaS系统三者相互关联。下方文字说明商户注册表的数据模型。
画面4：展示文档“2.4.2 商户注册”下的“2.4.1 系统设计”部分，说明商户注册流程涉及商户平台应用、商户服务、SaaS平台、验证码服务四个微服务。并分别介绍各服务职责。
画面5：展示代码，定义了`@ApiModelProperty`注解的多个字段，包括“企业名称”、“企业编号”、“企业地址”、“行业类型”、“营业执照”、“法人身份证正面”、“法人身份证反面”、“联系人”。
画面6：展示代码，定义了`public class MerchantDTO implements Serializable`类，包含`@ApiModelProperty`注解的多个字段，如“商户Id”、“企业名称”、“企业编号”、“企业地址”、“行业类型”、“营业执照”、“法人身份证正面”、“法人身份证反面”、“联系人”。
画面7：展示代码，配置了数据库连接信息，包括`jdbc:mysql://127.0.0.1:3306/shanjunpay_merchant_service`，并设置了驱动、用户名、密码。下方代码用于生成配置，设置包名。
画面8：展示代码，定义了`MyBatisPlusGenerator`类，包含`private static final Boolean IS_DTO = true;`和`public static String scanner(String tip)`方法。
画面9：展示代码，`MyBatisPlusGenerator`类中，设置了`strategyConfig.setControllerMappingHyphenStyle(true);`，并设置了实体类名和包名。下方代码用于生成后执行`autoGenerator.execute();`。
画面10：展示数据库表结构，表名为`merchant`，包含13列，如`ID`、`MERCHANT_NAME`、`MERCHANT_NO`、`MERCHANT_ADDRESS`、`MERCHANT_TYPE`、`BUSINESS_LICENSES_IMG`、`ID_CARD_FRONT_IMG`、`ID_CARD_BACK_IMG`、`CONTACT_NAME`、`CONTACT_PHONE`、`CONTACT_EMAIL`、`CREATE_TIME`、`UPDATE_TIME`。
画面11：展示IDE中`MerchantService.java`文件，定义了`public interface MerchantService`接口，包含`queryMerchantById`和`createMerchant`方法。
画面12：展示IDE中`MerchantService.java`文件，`createMerchant`方法的参数为`MerchantDTO merchantDTO`。
画面13：展示IDE中`MerchantServiceImpl.java`文件，`createMerchant`方法的实现为`return null;`。
画面14：展示文档“2.4.2 商户注册”下的“2.4.2.1 接口定义”部分，说明DTO可以使用“代码生成工具”自动生成功能，需要修改`MyBatisPlusGenerator`类中的`IS_DTO`设置为`true`，运行生成工具即可。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```java
@ApiModelProperty("企业名称")
private String merchantName;
@ApiModelProperty("企业编号")
private Long merchantNo;
@ApiModelProperty("企业地址")
private String merchantAddress;
@ApiModelProperty("行业类型")
private String merchantType;
@ApiModelProperty("营业执照")
private String businessLicensesImg;
@ApiModelProperty("法人身份证正面")
private String idCardFrontImg;
@ApiModelProperty("法人身份证反面")
private String idCardAfterImg;
@ApiModelProperty("联系人")
private String username;
```

画面6：
```java
public class MerchantDTO implements Serializable {
    @ApiModelProperty("商户Id")
    private Long id;
    @ApiModelProperty("企业名称")
    private String merchantName;
    @ApiModelProperty("企业编号")
    private Long merchantNo;
    @ApiModelProperty("企业地址")
    private String merchantAddress;
    @ApiModelProperty("行业类型")
    private String merchantType;
    @ApiModelProperty("营业执照")
    private String businessLicensesImg;
    @ApiModelProperty("法人身份证正面")
    private String idCardFrontImg;
    @ApiModelProperty("法人身份证反面")
    private String idCardAfterImg;
    @ApiModelProperty("联系人")
    private String username;
}
```

画面7：
```java
// 交易服务
dataSourceConfig
    .setUrl("jdbc:mysql://127.0.0.1:3306/shanjunpay_merchant_service?serverTimezone=Asia/Shanghai");
dataSourceConfig
    .setDriverName("com.mysql.cj.jdbc.Driver");
dataSourceConfig
    .setUserName("root");
dataSourceConfig
    .setPassword("mysql");
autoGenerator.setDataSource(dataSourceConfig);

// 生成配置
PackageConfig packageConfig = new PackageConfig();
packageConfig.setParent("com.shanjunpay");
// 如果需要手动输入包名
packageConfig.setModuleName("模块名");

// 自定义配置
InjectionConfig injectionConfig = new InjectionConfig() {
    @Override
    public void initMap() {
    }
};
```

画面8：
```java
public class MyBatisPlusGenerator {
    private static final Boolean IS_DTO = true;
    // ...
    public static String scanner(String tip) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder help = new StringBuilder();
        help.append("请输入").append(tip).append("：");
        System.out.println(help.toString());
        if (scanner.hasNext()) {
            String ipt = scanner.next();
            if (StringUtils.isNotEmpty(ipt)) {
                return ipt;
            }
        }
        return null;
    }
}
```

画面9：
```java
// ...
strategyConfig.setControllerMappingHyphenStyle(true);
// 自动将数据表中名为 user_info 格式的转为 Userinfo 命名
strategyConfig.setTablePrefix(packageConfig.getModule().toLowerCase() + "_");
// 若表名映射到实体类名，可设置为true
strategyConfig.setNaming(strategyConfig.getNaming());
autoGenerator.setTemplateEngine(new FreemarkerTemplateEngine());
System.out.println("================================ MyBatis Plus Generator ================");
if (IS_DTO) {
    globalConfig.setSwagger2(true);
    globalConfig.setEntityName("%sDTO");
    packageConfig.setEntity("dto");
}
autoGenerator.execute();
System.out.println("================================ MyBatis Plus Generator Execute Complete ================");
```

画面10：
```sql
表: merchant
Columns (13)
Field          Type          Comment
ID             bigint(20)    主键
MERCHANT_NAME  varchar(50)   客户名称
MERCHANT_NO    bigint(20)    客户编号
MERCHANT_ADDRESS varchar(255) 企业地址
MERCHANT_TYPE  varchar(50)   企业类型
BUSINESS_LICENSES_IMG varchar(100) 营业执照
ID_CARD_FRONT_IMG varchar(100) 法人身份证正面
ID_CARD_BACK_IMG varchar(100) 法人身份证反面
CONTACT_NAME   varchar(50)   联系人
CONTACT_PHONE  varchar(50)   联系电话
CONTACT_EMAIL  varchar(50)   联系邮箱
CREATE_TIME    datetime     创建时间
UPDATE_TIME    datetime     更新时间
```

画面11：
```java
package com.shanjunpay.merchant.api;
import com.shanjunpay.merchant.api.dto.MerchantDTO;
/**
 * @author Administrator
 */
public interface MerchantService {
    // 根据商户Id查询商户
    public MerchantDTO queryMerchantById(Long id);
    // 注册商户服务接口，接收账号、密码、手机号，为了可扩展性使用merchantDTO接收参数
    public MerchantDTO createMerchant(MerchantDTO merchantDTO);
}
```

画面12：
```java
// ...
public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
    // ...
}
```

画面13：
```java
// ...
@Override
public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
    return null;
}
```

画面14：
```java
// ...
DTO可以使用“代码生成工具”自动生成功能：
修改代码生成工具中的MyBatisPlusGenerator类：
public class MyBatisPlusGenerator {
    ...
    private static final Boolean IS_DTO = true;
    ...
    if (IS_DTO) {
        globalConfig.setSwagger2(true);
        globalConfig.setEntityName("%sDTO");
        packageConfig.setEntity("dto");
    }
    System.out.println("================================ MyBatis Plus Generator ================");
    autoGenerator.execute();
    ...
}
当生成dto时将IS_DTO设置

