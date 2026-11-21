# day03-5-校验手机号功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-5-校验手机号功能实现3_【海量资源尽在 666java.com】.mp4
- 时长 14分45秒（音频 885s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢我们把MP相关的这个Mapper接口啊配置文件呢包括一些配置是吧都已经补充上了接下来咱就该编写业务层的代码就ServiceService这一块写完之后呢Controller里边一定要用把这个代码一补充咱整个这一块的功能就搞定了啊所以咱接下来开始编写业务层的代码这个业务层咱之前写的是不是有业务层的代码
[00:28] 就咱实现上个功能吗获取延长码的时候已经有业务层了啊咱找一找这是业务层的什么呀接口这是业务层的什么呀对实现类哎这个时候大家要想一个问题我们现在实现的这个功能是不是要校验手机号是否存在我们说了是不是要查数据库哎大家想一想咱们前面讲过呀MP是不是对业务层有封装啊你还有印象没有来来来看看这儿啊讲一里边对就是这儿
[01:00] 是不是有封装提供了一个接口还有一个什么呀实现类那我们应该怎么做呀当时讲过应该怎么做呀对让我们的接口去继承他的接口让我们的实现类是不是继承他的实现类然后该有的是不是就都有了使用起来超爽的事是不是那咱这个代码现在需要改造改造啊这应该怎么改啊Ectance它叫I什么呀对Service这里边是不是要给一个什么东西啊是实体类吧是实体类不是
[01:31] 我们查一下啊你看是实体类吧对不对所以我这儿应该写ACC OUN T是不是对实体类要这么改造一下然后呢这个实现类这儿是不是也得改造一下实现类这儿也得继承MP的一个实现类它应该是叫叫啥名叫serviceimplserviceimpl
[02:02] 这里是不是要提供两个范围第一个应该是那个Mapper我们叫accaccountmapper然后呢是实体类啊叫account对报错报错吗这没导进来吗导报好了没错所以说呢咱首先要对咱之前的这个右层的代码改造一下啊要要把
[02:35] MP封装的那一套东西拿过来咱一会编代码就省事了那咱接下来就编写业务层的代码业务层咱是不是首先也要定义一个什么呀方法对吧在接口里边定义一个方法方法名还是叫checkmobilemobile想一想吧咱需要几个参数是不是跟Controller一样嘛对不对因为将来是Controller.servicecontroller里边当时你还有印象吗几个参数呀三个嘛
[03:07] 一个是手机号一个是那个key是吧还有一个就是什么验证码反而值还有有印象吗是一个数字吗就比较零就表示这个这个手机号不存在一就表示存在所以我们返回一个零一就行了所以我们首先在右层的接口里边把这个方法先定义一下定义完之后呢在这来实现这个方法好就是这个方法这里边咋实现呢这里边咱就要把
[03:43] 两个功能都体现一下啊这两个功能一个是校验短信验证码一个是校验手机上这两个功能咱都要在这个地方集中体现一下而这个校验短信验证码咱是不是已经实现过了在哪实现的呀是不是在这个smsservice里边对吧那咱在这是不是调用一下就行了呀sssms对吧Service.r它叫verify什么呀smscode然后把这个key
[04:12] 还有谁呀扣的给他不就完了吗这不就是校验什么呀这个验证码对不对吗是不是这功能就有那有了之后咱接下来只需要实现什么校验这个手机号是否存在那这个是不是要查数据库了对不对那查数据库的话我只是判断它存在不存在我不需要就是查出来这条数据具体的信息那我是不是应该只是查那个记录数就行了记录数
[04:43] 就是抗它嘛抗它啊我只要这个记录说比如说查不出来那记录说就是零嘛查出来的记录说应该就是一嘛因为手机号也不允许重复它肯定就是一那这应该调哪个方法呢那你要不知道的话要么你查MP的官方文档要么你看这啊点进去然后呢我们看一看它这里边都有哪些方法你不用看了第三个就是你看名字又猜出来这个就是查询什么呀
[05:14] 这个记录说的嘛count对不对所以说我们既然要调呢就是count的方法好那咱在这就直接干什么呀对调用c o u n t没错count的方法咱调呢是这个啊就是它是不是要求你传进来一个这个query warp对吧query warp你还有印象吗是干嘛的呀对它是我们的条件什么呀构造器这个当时在讲mp的时候给大家举了好几个例子嘛哎咱这需要用到它吗
[05:48] 需要用这个东西吗我们现在在实现啥功呢是不是判断这个手机号是否存在那你说这是不带条件的一个查询那我是不是需要去表里边做查询带一个什么条件那就是mobile等于什么是不是所以我这是需要一个条件的需要一个条件那因此呢按照之前的写法我应该这么写query什么呀warp我直接是不是就new一个就行了对不对那这里边有范形吗这边有范形没有有啊
[06:19] 你看咱以前写的这个例子里边你看QualWarp你看是不是实体类嘛对不对好我们这呢实体类是ACCUNT对吧QualWarp是直接NU的等于NUQUERYQualWarp对没错NU完之后怎么通过它来封装条件呢很简单它里边是不是提供了一堆的方法那咱这个功能当中是不是判断手机号
[06:49] 等于什么什么什么那等于你还有印象吗最常见的一个方法是比如EQ对吧这个第一个参议是字段名第二个参议是不是就是传过来的这个手机号有印象吧这个字段名的话你最好是确认一下你要么去表里边确认要么是去什么呀实体类当中确认我们看一下它就叫什么呀Mobile那我们这就写一个MOBILE可以吧对
[07:19] 这样子的话我们就把这个条件给干什么呀封装好封装好之后呢你就把这个谁啊Warp扔到这就可以了那他就根据这个条件做了什么查询啊对记录数的一个查询似乎语句不用写啊不用写他帮你生成那然后的话我们是不是就可以声明一个变量来接收一下这个值我们刚才分析过了我们说这个值要么是零要么是什么呀一吗是不是
[07:49] 如果手机号不存在那就是0如果手机号存在它就是1因为手机号不允许重复那最终的话我们就可以返回这么一个结果return COUNT怎么写呢大于0然后就是问号1冒号0三元运算符有印象吧能看懂我写的这是什么意思吗count大于0就证明这个手机号存在存在就返回1不存在就返回什么呀
[08:24] 就这个意思这个代码应该能看懂吧你看跟咱之前用的这个什么呀这个VARP没啥区别啊对不对没有啥区别只不过这呢我们调的是conner这个方法说这样写我们这个功能就实现了但是这呢我想给大家推荐另外一种写法另外一种写法什么写法呢大家注意看我把这行代码给你注释掉给你注释掉然后它还有什么玩法呢这玩法咱以前没讲过啊
[08:56] 你注意看一下它还支持Lambda表示的那种写法啊你看好Warp这个对象呢我们点出来一个方法你看LambdaLambda表示这个Lambda表示咱以前应该很早的时候学过吧对不对很早时候学过那么Lambda表示这种写法是怎么玩的呢它有啥好处呢来我先给你写一下啊你先调一下这个Lambda方法证明呢我后边要给它写的是这个Lambda表示不是传统的那种写法了
[09:23] 但是接下来你这个条件还不变是吧还是EQ是吧还是这个判断手机号等于什么什么什么对吧但是你看你接下来掉的这个EQ跟原来这个EQ可不一样哪一点不一样你注意看啊原来这个EQ来我给你放开你看这个EQ它的第一个参数看一下啊第一个参数什么类型String它要的是不是一个字段名是不是来你再看看咱现在这个EQ看看
[09:53] 这还是什么一个字符刷类型的一个数据吗不是啊这是一个什么呀一个接口啊一个接口那这样呢我们就可以写什么呀Lambda表达式后边这个值不变吧对不变所以说这两个EQ方案可不一样了啊那这个时候呢我第一个参照怎么给呢就要写Lambda表达式了ACC你看这有提示你看这有提示啊我是要比较或者说我是要判断是不是手机号的对不对
[10:22] 那你看Count这个实体类当中谁是表示这个手机号的是不是这个getMobile对不对对就这么写后边这个值呢还是咱传过来的Mobile你可以这么写这是LAM的表达式的这种写法你对比一下有个同学说老师这不用对比了我不会用这种的这种明显比上面这个干什么呀要多写好多代码对不对而且这个我感觉还不太好理解是不是我宁愿用这种你用这种也可以
[10:53] 用这种可以我只是把这种写法也给你介绍一下给你介绍一下但是呢这种写法Lambda这种写法它也不是说没有一点好处的有啥好处大家看看你觉得呢没好处吗你光看着它的这个不好是不是就写的稍微麻烦一些它的好处又在于这个地方不容易写错你想一想你看原来的这种写法这儿是不是自己要写这个列明对吧
[11:26] 那万一你小手一抖不小心写错了呢那么怎么避免这种问题呢那你看我们拉姆拉比尔社这种写法是不是就不容易写错因为这种写法它的第一个参数它并不是说是你自己手写的一个字段名而是相当于是不是这个通过实体类里边的这个这是应该是它的那个getter方法对不对你是选了一下不需要你手写那有没有老师那这将来到底是不是这个字段名呢是 是字段名
[11:56] 其实它内部是这么工作的你这不是相当于是告诉它我调用Pant类当中的这个GetMobile方法对不对那你看这个实体类当中你看你的MobileMobile上面是不是配的这个字段名就叫什么Mobile所以说其实呢这种写法最终还是得到了这个什么字段名就最终还是要这个字段名无非的区别就是原来这种写法字段名是你自己手写的而这呢是通过这种Lamb表是获取的
[12:27] 所以这种呢更不容易出错但是就稍微麻烦一些这种呢有可能你稍微不认真他会出错啊就是写错字段名了将来就会报错所以这两种方式呢各有各的优缺点吧萝卜白菜各有所爱你自己挑一个用一用就OK了所以这是业务层的代码咱就写到这写完之后咱是不是把control顺手给他补充完善一下就行了对不对哎你看咱的control当时是不是
[12:56] 只是return null了一下对不对那现在就简单了我这里边只需要干什么调用一下业务层不就完了吗对不对那就是AC account Service调用这个谁check什么对mobile然后把这三个参数全扔过去mobilekey还有谁对code全扔过去扔过去之后
[13:22] 咱的Controller给前端页面是不是要返回这么一个类型的数据对不对那怎么办呢我们直接调用它的success方法就行了一个静态方法rest response.success对然后呢我们把调用业务层它返回的这个值封装到里边就行了它返回不就是一个01吗是不是那扔到这里边封装进去然后呢最终返回就行了
[13:52] 这个代码你一定能看懂啊你看我们刚才说了这个checkmobile最终是不是返回的一个整数啊01嘛你有印象吧然后呢我们把这个01呢给它封装到这里边了啊咱调呢是它的一个静态方法你看不懂的话你点进去看看吧这个代码是不是success的方法是不是静态的对不对然后你刚才是不是把01给传进来0101传进来你看它自己内部自己丢了一个对象把这个01是不是放到这个result里边了
[14:20] 这不是响应过去的内容吗然后把它返回了这个代码你自己打开看一下就能看懂那这样子的话咱们的业务层还要扛出了这个代码就全部写完了那这个写完之后呢咱们整个哪一块功能对教验手机号和短信验证码整个这块功能就全部写完了那咱一会就要进行什么呀功能测试了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 MyBatis-Plus 实现手机号和验证码的校验功能，包括配置、接口定义、服务实现和控制器编写。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中关于修改 Apollo 配置和 Mapper 接口的说明，以及 MyBatis-Plus 的依赖配置。
画面2：展示 AccountService 接口定义，包含 getSMSCode 方法。
画面3：在 AccountService 接口中添加 extends RuntimeException。
画面4：在 AccountServiceImpl 类中定义 getSMSCode 方法，调用 SmsService。
画面5：在 AccountService 接口中添加 checkMobile 方法。
画面6：在 AccountServiceImpl 类中实现 checkMobile 方法，调用 smsService.verifySmsCode。
画面7：在 AccountServiceImpl 类中完成 checkMobile 方法的实现，使用 QueryWrapper 进行数据库查询。
画面8：展示 PDF 文档中 MyBatis-Plus 的 Wrapper 类结构，重点是 AbstractLambdaWrapper。
画面9：展示数据库表 p2p_account 的创建语句，包含字段定义和字符集设置。
画面10：在 AccountServiceImpl 类中使用 QueryWrapper 进行条件查询。
画面11：在 AccountServiceImpl 类中使用 LambdaQueryWrapper 进行条件查询。
画面12：在 AccountServiceImpl 类中使用 LambdaQueryWrapper 进行条件查询，使用 getMobile 方法。
画面13：在 AccountController 类中定义 checkMobile 方法，使用 @PathVariable 注解接收参数并调用 Service 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependency>
    <groupId>com.baidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
</dependency>
```
画面2：
```java
package cn.itcast.wanxing2p.account.Service;

import cn.itcast.wanxing2p.common.domain.RestResponse;

public interface AccountService {
    RestResponse getSMSCode(String mobile);
}
```
画面3：
```java
public interface AccountService extends RuntimeException {
    RestResponse getSMSCode(String mobile);
}
```
画面4：
```java
@Service
public class AccountServiceImpl extends AccountService {
    @Autowired
    private SmsService smsService;

    @Override
    public RestResponse getSMSCode(String mobile) {
        return smsService.getSMSCode(mobile);
    }
}
```
画面5：
```java
public interface AccountService extends AccountService {
    RestResponse getSMSCode(String mobile);
    Integer checkMobile(String mobile, String key, String code);
}
```
画面6：
```java
@Service
public class AccountServiceImpl extends ServiceImpl<AccountMapper, Account> implements AccountService {
    @Autowired
    private SmsService smsService;

    @Override
    public RestResponse getSMSCode(String mobile) {
        return smsService.getSMSCode(mobile);
    }

    @Override
    public Integer checkMobile(String mobile, String key, String code) {
        smsService.verifySmsCode(key, code);
    }
}
```
画面7：
```java
@Override
public Integer checkMobile(String mobile, String key, String code) {
    QueryWrapper<Account> wrapper = new QueryWrapper<>();
    wrapper.eq("mobile", mobile);
    int count = count(wrapper);
    return count > 0 ? 1 : 0;
}
```
画面8：
```java
Wrapper(com.baidou.mybatplus.core.condition)
    AbstractWrapper(com.baidou.mybatplus.core.condition)
    AbstractLambdaWrapper(com.baidou.mybatplus.core.condition)
    LambdaQueryChainWrapper(com.baidou.mybatplus.core.condition)
    QueryWrapper(com.baidou.mybatplus.core.condition)
    UpdateWrapper(com.baidou.mybatplus.core.condition)
```
画面9：
```sql
CREATE TABLE `t_user` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `user_name` VARCHAR(20) NOT NULL COMMENT '用户名',
  `password` VARCHAR(20) NOT NULL COMMENT '密码',
  `name` VARCHAR(30) NOT NULL COMMENT '姓名',
  `age` INT(11) DEFAULT NULL COMMENT '年龄',
  `email` VARCHAR(50) DEFAULT NULL COMMENT '邮箱',
  `create_time` DATETIME DEFAULT NULL COMMENT '创建时间',
  `update_time` DATETIME DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
```
画面10：
```java
@Override
public Integer checkMobile(String mobile, String key, String code) {
    QueryWrapper<Account> wrapper = new QueryWrapper<>();
    wrapper.eq("mobile", mobile);
    int count = count(wrapper);
    return count > 0 ? 1 : 0;
}
```
画面11：
```java
@Override
public Integer checkMobile(String mobile, String key, String code) {
    QueryWrapper<Account> wrapper = new QueryWrapper<>();
    wrapper.lambda().eq(Wrapper::getMobile, mobile);
    int count = count(wrapper);
    return count > 0 ? 1 : 0;
}
```
画面12：
```java
@Override
public Integer checkMobile(String mobile, String key, String code) {
    QueryWrapper<Account> wrapper = new QueryWrapper<>();
    wrapper.lambda().eq(Account::getMobile, mobile);
    int count = count(wrapper);
    return count > 0 ? 1 : 0;
}
```
画面13：
```java
@GetMapping("/checkMobile")
public RestResponse checkMobile(@PathVariable String mobile, @PathVariable String key, @PathVariable String code) {
    return accountService.checkMobile(mobile, key, code);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8：PPT 标题为“5.1 比较操作”，下方列出比较操作符：eq（等于）、ne（不等于）、gt（大于）、ge（大于等于）、lt（小于）、le（小于等于）。
画面9：无 PPT 标题，仅展示 SQL 语句。

5) 不要评价画面美观，不要输出与课程无关的内容。

