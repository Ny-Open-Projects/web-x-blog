# 21.支付参数配置-创建应用-商户服务接口

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\21.支付参数配置-创建应用-商户服务接口【海量资源尽在 666java.com】.mp4
- 时长 13分50秒（音频 831s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们就来实现商户的应用创建那么这里边首先我们看我们的系统交互的序列图首先前端会填写应用的信息然后请求到我们商户平台应用商户平台应用请求商户服务来保存应用信息整个流程是比较简单的好 那么来我们首先来创建我们的商户服务的接口
[00:24] 这个我之前应该大家说过了如果你要先写接口2那么这个接口2当调商户服务的时候由于商户服务的接口没有写这个接口是写不完整的所以我们先写商户服务的接口再写商户平台应用的接口好了那么我们来看首先我们要定义接口现在是创建应用创建应用我们需要哪些参数分析一下首先我们可以打开我们的商户服务的工程首先在API这里头我们要定义接口在这对吧好
[00:54] 那么这里边呢注意啊我们说它是一个应用管理相关的这是商户的一个Service所以这里边呢我就建议大家呢单独的我们来去定义一个什么APP的Service而这个Service呢其实主要是用于放应用管理相关的接口这里边我们写一个新的interface好这个就是应用管理相关的接口
[01:21] 好那么这里边呢刚才我们说了嘛他需要来创建应用是吧创建应用需要哪些参数呢我们分析一下吧第一应用的信息还有什么哪个商户创建的应用你商户的ID是不是需要没错吧好那么应用的信息这里边是在Service当中我们通常用DTO那么这里边有个APP的DTO这里边是不是有了好DTO的事已经搞定那接下来我们是不是就需要来写我们的这个接口的方法名了好
[01:52] 那么我们来根据讲义保持一致啊这是CREATE APP然后这里面呢我们来定义一个那最终呢做创建完成应用的话我们准备把这个应用信息给它返回去然后呢返回之就是APP DTO然后呢它呢要把商户的这个什么ID传过来是哪个仓户创建应用然后呢你要把应用的这个信息给我对不对然后如果抛异常的话我们要让它抛出什么自定义的异常
[02:22] 这是不是就是我们说的什么呀叫做创建应用咱们就写完了好创建应用这里边大家一定记着啊分析一些什么接口我们要先分析了这个接口的什么职责然后再分析它的一个参数啊我们说它呢就是用来创建应用的创建应用的它需要的是一个什么商户的ID然后还需要一个什么应用的信息那返回的就是一个什么创建什么创建成功的
[02:53] 啊应用的什么信息嗯好那么这样的话我们是不是就可以在啊这是一个APP的这个接口吗对吧然后接下来我们是不是就可以在这个接口实现里面去写了嗯那这里面来看一下啊在这定义一个那这个是一个double接口是吧所以这里面呢我们是要用什么Service用double的这个注解来标示一下好
[03:24] 然后呢还要让它去实现刚才我们写的这个这个把它改一个名啊改个名这个后边末尾咱加一个impl行吧然后这样的话让它实现app serviceapp Service是吧好这是不是就是一会儿在这写就行了吗然后这里面呢将来我们是不是就可以让它给注入app Mapper通过这Mapper来操作好
[04:00] 这是我们的这个三户服务这一块的什么这个接口包括刚才我说的这个接口的定义是吧好了那现在呢我们把接口定义OK了之后呢我们再看它的具体实现怎么实现呀也就是说现在呀你是要在这儿最终要调用我们的APP Mapper是不是向我们的应用表来插入数据对那这个应用表大家应该还没有见面吧来看一下
[04:32] 在商户的这个数据库当中我们看有一个APP看见吧然后它这里边呢你看有商店的名称就是我们的应用的名称对吧还有所属的商户还有什么公钥还有授权的回调地址这两个回头我们用到再说那现在呢各位我们是不是就可以知道组件这一块呢组件呢组件它是一个什么是自征的吗组件组件不是自征的吧
[05:00] 但这个APP ID组件它可以自动生成用Mapdesk Plus但APP ID我们需要给它生成一个唯一的ID这是专门的一个什么应用的ID懂吧所以这里边我看讲义生成APP应用ID我们用UUID的方式是不是告诉你了然后另外还有一点就是应用的名称要有唯一性我们要校验应用的名称还有一点商户资质申请审核没有通过你不允许创业应用也就是你还不是我们正式的商户
[05:30] 对不对这是不是就是我们接口的这个什么详细的一个内容啊所以各位我们现在要实现整个接口的这个内容我们是不是需要把刚才我们讲一上的这些需求一个一个都实现就OK了懂吧好那下面呢我们来看那具体怎么实现呢那接下来是不是就开始写代码了如果我们要进行这个DTO和这个entity之间的一个转换我们就需要来编写一个converter
[05:59] 这个我觉得大家应该清说熟路了所以这个过程呢在讲义当中你直接把它考过去就行你也可以回头我给你提供代码你也可以直接把我的代码拿过去就是这个converter不用再去手中敲了好了那下面呢我们来看吧这里边我们要做啥那就开始写借口了在这个里边呢首先根据我们刚才分析的这一堆我们来写第一步就是校验嘛校验合法三数里边首先第一如果
[06:28] 提供的merch的这个ID然后呢围空或者APP的一个应用信息围空那我问你你还让它执行吗不执行了所以这里边呢你就利用一个business是吧然后呢这里边给它一个什么具体的错误代码这错误代码应该大家知道这是传入对象围空或缺少必要的参数好那接下来我们还要做啥是不是就是校验
[06:56] 商户是否通过什么知识审核对不对那降低商户是否通过知识审核怎么做那你就需要来查商户了吧对不对要查商户的话那我们是不是就需要来调用商户的这个Mapper了没错吧好那商户的Mapper那我们因为有商户的ID的嘛所以这里边呢你就直接slag的by ID
[07:26] 商户的ID放进去这是不是就查到了对不对当然话又说过来了如果这个ID传的是错误的也就是它是空那你还让它继续走吗不走了吧所以那你也抛一场对吧这个抛的一场应该是叫做商户不存在对不对那如果有的话那你这时候呢你就需要取出它的什么呀要取出这个什么这个商户的资质申请的什么状态这个状态呢
[07:54] 在三户表当中我们当初申请通过了之后它是不是一个二啊对不对现在呢我们来看一下啊你看打开在三户的表当中我们来看一下它里面怎么说的审核通过是二那么我觉得应该不是二的都不能都算非正式用户是吧所以这里面呢我们就判断如果说呀这个什么啊它不是二不是二这个大家看懂代码了吧就是它
[08:26] 不等于这时候呢我们说他还没有资质审核通过对不对三户未审核通过不能创建应用好那这个是不是就完了那么后边还有一个就是生成应用的什么ID对吧生成应用的ID的话这里边呢我们就可以来叫做你看这应用的ID它是什么类型看一下啊应用的ID看这
[08:58] 选一下它是吧然后这里面应用的ID是不是一个字符串类型啊所以这里面呢我们来看啊它就是APP ID等于悠悠ID行不行悠悠ID然后呢这是不是就OK了应用的ID成了那接下来还有那么保存应用的信息那应用的名称要为一所以这时候呢我们是不是还要校验应用的名称啊我觉得校验的东西都可以放前头行不行
[09:28] 教验应用的名称需要为一那应用的名称怎么教验呀应用名称的话你就需要干嘛你就需要来查一下这个根据这个名称来查一下那其实根据名称来查一下我觉得这个名称如果人家没有给你填我觉得在这你可以怎么弄啊你可以来判断一下应用的名称唯空不唯空啊如果说它唯空了那这直接都过不去了大家理解吗这不就是应用的名称吗
[09:57] 如果它违控了这就提示了你关键的参数违控不能进行下边操作了好那如果说不违控的话这里面呢你看它是不是就可以拿到应用的名称了对不对拿到应用名称好这就是应用的名称那好那应用的名称你要怎么做这是不是传入的应用名称呀传入的应用名称你需要查数据库对不对查数据库的话这里边呢我写一个具体的一个举步方法吧
[10:23] 这个局部方法呢我们就可以来校验用的名称我们和蒋英保持一致这个方法名来往下翻这就是我们准备写一个sale方法啊专门给这个去用最终我们要校验这个名称啊它就是最终返回一个布尔类型如果说已经存在那么它就是一个什么啊一个布尔的一个什么结果我们来看一下啊如果说它存在那么我们就把它返回一个处它不存在我们是force
[10:56] 所以看这个名称写的应该也是见闻之意啊就是是否存在某一个什么APP的什么内幕好了那这里边呢怎么写呢APP Mapper我们主要是查嘛slack的countnew一个lamb的然后呢他的这个什么query wrapper然后呢我们现在是不是需要去给他填这个什么他的一些条件呀好那这里怎么填呀
[11:23] 那我们主要是要填的是它的这个根据名称来匹配嘛所以这样的话我们是不是就得到了一个count呀得到一个count的话如果说这个count它的值是大于0的那我认为它是不是就存在了否则的话是不是就是force呀所以在这儿我们要校验的话这个方法这个sale方法主要是判断应用名称是否存在对不对如果存在是不是返回
[11:52] 处了所以我们只要在这来校验一下就行了用本地方法好APP内容对不对好那这里边呢我们看对如果说有时候太智能了也不好是不是啊这个写的这个代码好看好那如果它是存在了那么你是不是就它这是一个处啊它这个处的话那你是不是要抛一层了抛一个一层抛啥一层就是应用的名称
[12:25] 已经存在对不对好应用的名称已经存在我们来看一下吧这个是应用名称已存在请使用其他名称好那这样的话那校验如果都没有抛异常后边就开始正常执行对不对好那正常执行了那这里边这一堆校验是不是就完事了应用的ID我是不是已经生成了那接下来我们最终是要调用谁啊就是这个appmap然后insert是不是要传一个entity
[12:54] 穿entity的话我们又直接把这个DTO你把它转一下不就完事了吗行不行所以我们就用刚才我们创建的一个converter我们把这个什么啊entity把这个DTO要转成entity懂吗好那我就转成了转成了一个entity转成一个entity之后呢你就要给它设置我们说的APP ID了这ID是不是在这生成了然后把它放进去懂了吗
[13:23] 你最后要返回是不是一个DTO要返回一个DTO这个entity里边有ID了是不是你就可以怎么弄你就可以在returnreturn的时候你把这个entity再把它转成DTO返回给什么调用方就行了这就是整个的什么创建应用的一个什么商户服务的接口实现咱们就做完了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在商户平台创建应用的接口实现，包括定义数据传输对象、接口契约、数据库表结构以及核心业务逻辑的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示系统交互流程图，说明商户平台应用与商户服务之间的交互步骤，包括创建应用、保存应用信息、校验并保存商户应用信息等。
画面2：展示项目结构，重点是AppDTO类，其中定义了商户名称、商户ID、公钥、回调地址等属性。
画面3：展示接口定义，AppService接口中定义了createApp方法，用于创建应用。
画面4：展示接口实现，AppServiceImpl类实现了AppService接口，包含createApp方法的实现。
画面5：展示数据库表结构，包括APP_ID和APP_NAME字段，以及对应的索引。
画面6：展示AppCovert接口的定义，用于对象转换。
画面7：展示createApp方法的实现，包括校验商户信息、生成应用ID、保存商户应用信息等步骤。
画面8：展示商户实体类Merchant的属性，包括商户名称、地址、类型等。
画面9：展示应用ID生成的逻辑，使用UUID方式生成。
画面10：展示异常处理，包括BusinessException和各种运行时异常。
画面11：展示数据库操作，使用appMapper进行数据插入。
画面12：展示应用名称唯一性校验的SQL语句。
画面13：展示应用名称唯一性校验的Java代码。
画面14：展示保存应用信息的代码，包括设置应用ID、商户ID、转换对象、插入数据库等操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@ApiModelProperty(value = "商户名称")
private String appName;
@ApiModelProperty(value = "应用公钥（RSA1thSHA256）")
private Long merchantId;
@ApiModelProperty(value = "我收回调地址")
private String notifyUrl;
```

画面3：
```java
public interface AppService {
    /**
     * 创建应用
     * @param merchantId 商户ID
     * @param appDTO 应用信息
     * @return 创建成功的应用信息
     * @throws BusinessException
     */
    AppDTO createApp(Long merchantId, AppDTO appDTO) throws BusinessException;
}
```

画面4：
```java
import com.shanjuay.merchant.api.dto.AppDTO;
import org.apache.dubbo.config.annotation.Service;

public class AppServiceImpl implements AppService {
    /**
     * 创建应用
     * @param merchantId 商户ID
     * @param appDTO 应用信息
     * @return 创建成功的应用信息
     * @throws BusinessException
     */
    @Override
    public AppDTO createApp(Long merchantId, AppDTO appDTO) throws BusinessException {
```

画面5：
```sql
CREATE TABLE app (
    id bigint(20) NOT NULL,
    app_name varchar(50) NOT NULL,
    app_id varchar(50) NOT NULL,
    ...
);
```

画面6：
```java
@Mapper
public interface AppCovert {
    AppCovert INSTANCE = Mappers.getMapper(AppCovert.class);
    AppDTO entity2dto(App entity);
    App dto2entity(AppDTO dto);
    List<AppDTO> listentity2dto(List<App> app);
}
```

画面7：
```java
if (merchantId == null || appDTO == null) {
    throw new BusinessException(CommonErrorCode.E_30009);
}
// 1) 校验商户是否通过资质审核
if (merchant == null) {
    throw new BusinessException(CommonErrorCode.E_20002);
}
// 校验商户资质状态
merchant.
```

画面8：
```java
public class Merchant {
    private String getBusinessLicenseImg();
    private String getContactsAddress();
    private String getIdCardFroning();
    private String getIdCardRear();
    private String getMerchantAddress();
    private String getMerchantName();
    private String getMerchantWo();
    private String getMobile();
    private String getTel();
}
```

画面9：
```java
// 应用ID使用UUID方式生成
String appid = UUID.randomUUID().toString();
```

画面10：
```java
// 异常处理
throw new BusinessException(CommonErrorCode.E_30009);
```

画面11：
```java
// 保存应用信息
app.setAppId(RandomUtil.getUUID());
app.setMerchantId(merchant.getId());
App entity = AppCovert.INSTANCE.dto2entity(app);
appMapper.insert(entity);
return AppCovert.INSTANCE.entity2dto(entity);
```

画面12：
```java
// 校验应用名是否已被使用
@Param appname
public Boolean isExistAppName(String appname) {
    Integer count = appMapper.selectCount(new QueryWrapper<App>()
            .eq(App::getAppName, appname));
    return count.intValue() > 0;
}
```

画面13：
```java
// 为防止应用名重复
private Boolean isExistAppName(String appname) {
    Integer count = appMapper.selectCount(new LambdaQueryWrapper<App>().eq(App::getAppName, appname));
    return count > 0;
}
```

画面14：
```java
// 保存应用信息
app.setAppId(RandomUtil.getUUID());
app.setMerchantId(merchant.getId());
App entity = AppCovert.INSTANCE.dto2entity(app);
appMapper.insert(entity);
return AppCovert.INSTANCE.entity2dto(entity);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4.1 需求分析”，子标题“4.1.1 系统交互流程”。架构图显示“浏览器/APP”指向“商户平台应用”，再指向“商户服务”，最后返回“创建应用成功”。
画面6：PPT标题为“4.2.1.2 接口实现”，内容为“定义AppCovert负责对象转换”。
画面14：PPT标题为“4.2.2 商户平台应用创建应用接口（接口②）”，子标题“4.2.2.1 接口定义”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

