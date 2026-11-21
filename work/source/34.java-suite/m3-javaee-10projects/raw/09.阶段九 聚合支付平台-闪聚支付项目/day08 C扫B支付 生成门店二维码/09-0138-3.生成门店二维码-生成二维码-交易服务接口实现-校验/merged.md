# 3.生成门店二维码-生成二维码-交易服务接口实现-校验

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\3.生成门店二维码-生成二维码-交易服务接口实现-校验【海量资源尽在 666java.com】.mp4
- 时长 11分44秒（音频 704s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下边呢我们就继续来实现交易服务生成二维码的URL那根据刚才我们定义的接口我们说前边是需要来校验一下应用是否属于商户门店是否属于商户然后呢再拼装数据最终输出这个一个URL那校验应用是否属于商户当前我们是不是在交易服务看见了吗那你说这个校验应该谁来做
[00:25] 对就大家每写一个接口或者每调用一个接口你马上想到这接口在哪个服务是不是啊那么应用商户应该是在商户服务对吧所以接下来呢我们是需要在商户服务当中去写两个接口一个是校验应用和商户的一个合法性一个是校验门店和商户的一个合法性校验校验方法呢很简单就是看看应用是否和商户是匹配的门店和商户是否是匹配的
[00:55] 所以这个教验的接口呢你给我两个参数啊一个是应用的ID一个是商户的ID然后呢教验通过呢我就给你返回了一个true教验失败呢就给你返回一个false所以这里边呢我们在哪里啊应用和商户的一个合法性教验的话这里边呢各位我们是可以在商户服务当中各位可以看到是不是有很多的Service啊是不是有一个应用的Service啊我们在这儿
[01:24] 所以这里边呢你要给我两个参数啊一个是APP ID一个是什么morechint ID然后呢你给我返回一个布尔类型懂吧好这就是一个什么一个教验好那这个呢就表示教验啥呀教验应用是否属于商户是吧好
[01:56] 那么那现在呢我们就可以在商户的实现当中把这个教研接口写了来虽然这个接口应该怎么写呀就是现在呢我要教验这个应用是否属于一个商户这个应用数据在哪呀应用是不是在APP这张表你看这个应用我给它传一个ID你要看看这个是否属于某一个商户那其实很简单我就要查询这张表这个记录存在说明
[02:25] 这个应用和三户的ID是不是就表示合法那我就查询这个APP表然后呢根据应用ID和三户ID来查如果查到就说明就说明它合法就数据库表示这个记录是存在的对不对所以这里边呢我们就来查询一下好那就是APPMapper嘛然后呢Select Account行吧好那这样的话我们怎么查呀你现在查的是应用表嘛
[02:56] 所以这里边呢就是应该是有EQ用用哪个你现在要查的是应用ID吗应用ID一个条件还有一个还有一个啥还有一个条件就是商户商户的ID你现在是不是要根据这两个条件来查询这个APP的这个这样应用表对吧如果说查到记录了就说明它大于零
[03:28] 那是不是就表示存在也就是说true表示什么存在吧false就表示不存在吧是不是啊好这个教验就OK了是不是很简单那么接下来还有一个教验啊在这个琐碎的工作呢我们把前期工作都要做好一个是门店它呢是否合法那这个呢其实也很简单我们在这个另外一个Service就是这个
[03:56] Machine的Service里边我们来写那门店嘛所以这里边肯定要给我传一个什么门店的ID对吧然后还有一个商户的ID最终呢你是要给我返回一个什么布儿类型对不对哎跟刚才一样哎那这个呢其实就是叫校验门店是否属于商户对吧好弄好了吧弄好了之后呢在这
[04:27] 写实现然后呢把这个接口呢报出来好那接下来这里头你这个方法跟刚才是不是应该一样门店的表你打开瞧瞧是不是有一个叫storestore你看里边有个商户ID吧对吧还有门店ID所以其实各位我们也是这么来查那就是store和map然后呢select content对吧然后呢这里边lambd那这个呢是要查store这张表
[04:57] 所以这里面的EQ这个是哪个呀ID嘛门店的ID嘛然后门店的ID这个是应该是小写门店的ID门店的ID的话除了这个条件还有啥是不是还应该有一个商户的ID商户的ID是这个叫Machine ID各位这是不是又得到一个Count这时候呢就是Count如果大于0就表示
[05:31] 什么呀是不是就是错就表示存在对不对然后呢如果是false呢不存在我问你这两个教练接口咱们是不是非常快速的把它给搞定了有时候老师搞定了好像他报错你没发现吗你看这不是报错吗这是咋回事看一下这个错误是啥
[06:11] 那你其实鼠标放上去我们可以看一下说啥呀说这个这个参数你看这个注解很智能他和他不一样是吧好是不是搞定了搞定了之后接下来我们继续回到我们的生成二维码URL的一个接口中回到哪里交易服务对吧那现在你是要校验吗校验各位你在这是不是就可以去
[06:41] 去调用它了对吧那你这里边肯定是要传入reference谁呀appservice对不对还得传进去一个注进去一个什么呀morechain Service对吧好教验教验的这个动作啊它是一个是教验应用一个是教验门店嘛所以各位看我的讲义
[07:12] 咱们讲一上是这么写的就是说干脆我们写一个私有方法来把这两个教验了老师怎么还写私有方法因为你现在是不是要教验商户ID和应用ID的合法性你不用在这去调这个Service在这再调一下干脆我们统一来写一个私有方法写私有方法是啥意思你就给我传进去什么APP ID你再给我传进去一个什么
[07:43] 门店ID你再给我传进去一个merchant ID看这个参数和讲义我们保持一致啊这个是商户ID在前对你把这三个ID给我传到这个私有方法中有人说不明白不明白很简单呀这啥意思来我这方法是不是可以建起来呀这是不是就是一个私有方法那私有方法这个这干嘛的
[08:10] 这是不是就来教验我们说的商户ID应用ID以及门店的ID的合法性对吧那我的意思就是这么个意思就在这教验一下是吧一个方法里面去教验那有老师要教验不通过呢教验不通过的话很简单咋简单抛一场是不是那我们是不是就可以来来查询一下这个应用ID和商户ID那现在各位我是不是就查到了这么一个结果
[08:41] 你看这个还不一样的这个是什么呀浪类型对吧你看我们现在原来写的这个三户ID是不是浪类型啊对吧这几个接口注意这个类型你得把握准了三户ID都是浪类型我们把它先简单的稍微处理一下很简单啊就把这个参数的类型改成浪好那这样的话各位我们再回到这
[09:10] 如果说呀现在我们去校验他得到一个什么如果是truth是不是表示存在如果是false的话呢是不是就表示不存在那不存在我问你是不是就要抛一场对不对抛一场那抛一场的话抛什么一场呢说明这个什么这个应用是不合法的应用是不合法的我们看一下啊这代码太多了
[09:42] 看这个代码是什么你可以点开瞧瞧你看点这不叫应用不属于当年商户下面是一个门店不属于当年商户看见了吧所以它的教验方法在一个私有方法当中我们去调用就行了然后呢这里边这要查的是什么呀是门店门店和商户对吧门店和商户就这个那你给我传门店的ID商户的ID传进去了吧
[10:14] 传进去了传进去了好像也不对你看对吧这也不对这不对是为啥因为这个方法它这个门店ID其实它也是个浪类型我们当时写的比较快是不是都是写成字部算类型了没关系我们把它改一下就行了很快的好那现在呢我们继续在这写这样的话跟刚才是不是一样的方法
[10:42] 上面这个是不是就是来根据应用的ID和商户的ID来查询啊是吧查询相当于就是校验了是吧如果查到了就没事如果查不到是不是就抛一场了对不对那这个呢是根据什么来查根据门店的ID和商户的ID来查询那同样的道理啊如果如果没有查到
[11:11] 对这时候呢得炮一个异常这炮6这是个6异常就表示啥叫门店不属于当前商户这是不是有一个校验的修法吗那在这是不是就校验了对吧那在这校验完了之后呢我们就可以组装URL所需要的数据了组装URL所需要的数据然后呢再干嘛再对拼装成一个具体的URL好了那么当前我们完成了这个门店应用以及商户的校验
[11:40] 我们呢先写到这儿好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现商户应用与门店的关联校验逻辑，包括创建支付入口、校验商户与门店关系、以及处理相关业务异常。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 TransactionServiceTest 测试类中 createStoreQRCode 方法的代码，其中包含注释说明“根据商户应用生成支付入口的url”，并显示了方法签名和部分逻辑。
画面2：展示 AppService.java 文件中 queryAppByMerchant 方法的定义，包含注释“根据应用id查询应用信息”和方法签名。
画面3：展示 AppService.java 文件中 queryAppByMerchant 方法的实现，使用 AppConvert.INSTANCE.entity(app) 返回 AppDTO 对象。
画面4：展示 AppService.java 文件中 queryAppByMerchant 方法的实现，使用 Lambda 表达式进行条件判断。
画面5：展示 MerchantService.java 文件中 queryStoreByMerchant 方法的定义，包含注释“门店列表的查询”和方法签名。
画面6：展示 MerchantService.java 文件中 queryStoreByMerchant 方法的实现，使用 LambdaQueryWrapper 进行条件查询。
画面7：展示 MerchantService.java 文件中 queryStoreByMerchant 方法的实现，使用 LambdaQueryWrapper 进行条件查询。
画面8：展示 MerchantService.java 文件中 queryStoreByMerchant 方法的实现，使用 LambdaQueryWrapper 进行条件查询。
画面9：展示 TransactionService.java 文件中 TransactionService 接口的定义，包含注释“@Service”和“@Reference”注解。
画面10：展示 TransactionService.java 文件中 createStoreQRCode 方法的实现，显示了方法签名和部分逻辑。
画面11：展示 AppService.java 文件中 queryAppByMerchant 方法的定义，包含注释“根据应用id查询应用信息”和方法签名。
画面12：展示 TransactionService.java 文件中 verifyAppBeforeStore 方法的实现，包含注释“根据商户应用id查询商户”和“根据门店id查询门店”，并显示了异常抛出代码。
画面13：展示 MerchantService.java 文件中 queryStoreByMerchant 方法的定义，包含注释“门店列表的查询”和方法签名。
画面14：展示 TransactionService.java 文件中 verifyAppBeforeStore 方法的实现，包含注释“根据商户应用id查询商户”和“根据门店id查询门店”，并显示了异常抛出代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public String createStoreQRCode(QRCodeDto qrCodeDto) throws BusinessException {
    //根据商户应用生成支付入口的url，需要将传入的参数转成json，用base64编码
    String url = null;
    return url;
}
```

画面2：
```java
List<AppDTO> queryAppByMerchant(Long merchantId) throws BusinessException {
    //根据应用id查询应用信息
    return appDTO;
}
```

画面3：
```java
return AppConvert.INSTANCE.entity(app);
```

画面4：
```java
public boolean condition(Function<App, ? extends Object> column, Object val) {
    return null;
}
```

画面5：
```java
void bindStaffToStore(Long storeId, Long staffId throws BusinessException {
    //门店列表的查询
    PageVO<StoreDTO> queryStore(String storeId, String merchantId);
}
```

画面6：
```java
@Param Wrapper<Store> queryWrapper(String merchantId) {
    LambdaQueryWrapper<Store> wrapper = new LambdaQueryWrapper<>();
    wrapper.eq(Store::getMerchantId, merchantId);
    return wrapper;
}
```

画面7：
```java
public Boolean queryStoreByMerchant(String storeId, String merchantId) {
    Integer count = storeMapper.selectCount(new LambdaQueryWrapper<Store>().eq(Store::getMerchantId, merchantId));
    return count > 0;
}
```

画面8：
```java
public Boolean queryStoreByMerchant(String storeId, String merchantId) {
    Integer count = storeMapper.selectCount(new LambdaQueryWrapper<Store>().eq(Store::getMerchantId, merchantId));
    return count > 0;
}
```

画面9：
```java
public class TransactionServiceImpl implements TransactionService {
    @Reference
    AppService appService;
}
```

画面10：
```java
@Override
public String createStoreQRCode(QRCodeDto qrCodeDto) throws BusinessException {
    //根据商户应用生成支付入口的url，需要将传入的参数转成json，用base64编码
    String url = null;
    return url;
}
```

画面11：
```java
AppDTO getAppById(String appId) throws BusinessException.
```

画面12：
```java
private void verifyAppBeforeStore(Long merchantId, String appId, Long storeId) {
    Boolean isExist = appService.queryAppByMerchant(appId, merchantId);
    if (!isExist) {
        throw new BusinessException(CommErrorCode.E_200005);
    }
    Boolean isExist = merchantService.queryStoreByMerchant(storeId, merchantId);
    if (!isExist) {
        throw new BusinessException(CommErrorCode.E_200006);
    }
}
```

画面13：
```java
PageVO<StoreDTO> queryStoreByPage(StoreDTO storeDTO, Integer pageNo, Integer pageSize);
```

画面14：
```java
private void verifyAppBeforeStore(Long merchantId, String appId, Long storeId) {
    Boolean isExist = appService.queryAppByMerchant(appId, merchantId);
    if (!isExist) {
        throw new BusinessException(CommErrorCode.E_200005);
    }
    Boolean isExist = merchantService.queryStoreByMerchant(storeId, merchantId);
    if (!isExist) {
        throw new BusinessException(CommErrorCode.E_200006);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

