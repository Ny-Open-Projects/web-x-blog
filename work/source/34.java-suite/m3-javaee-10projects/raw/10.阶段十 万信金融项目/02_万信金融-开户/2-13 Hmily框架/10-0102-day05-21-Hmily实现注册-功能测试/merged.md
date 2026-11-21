# day05-21-Hmily实现注册-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-21-Hmily实现注册-功能测试_【海量资源尽在 666java.com】.mp4
- 时长 15分13秒（音频 914s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们已经把使用Hemily框架解决注册功能中的分布式事务问题的代码全部给编写完了接下来咱就进行功能测试这个测试呢我们重点也是测两个效果第一个呢就是都执行成功用户中心服务统一账号服务这两边哪一边都执行成功了还有一个呢就是我们让
[00:31] 统一账号服务这边失败然后观察一下用户中心这边能不能进行什么呀回滚我们就测这两块就OK了表里边的数据呢咱可以大概看一下表里边的数据目前是什么样的啊我们看看这是哪个表啊我们先看这consumer表啊是现在里边有三行数据001221是吧我看到里边呢我看到里边的话咱删一些数据啊
[01:02] 让他俩先保持一致刷新12121是吧就这样吧这是目前表里边数据咱先大概过一遍那咱接下来测试怎么测呢咱还是通过postman通过postman因为这个你看consumer这边这个注册的这个功能咱之前是不是都已经测试过了对不对都测试过咱还是通过这个postman测试就行了那咱接下来开始启动相关的服务Apollo呢这边已经启动过了
[01:32] 接下来咱看看微服咱都需要启动谁首先这个注册中心我们要启动先把它给重启一下注册中心要启动还有谁我们这个刺都不再过网关了因为过网关这个刺咱以前都刺过咱现在只是把Harmony这块代码给加进去了那咱就只启动一下Consumer和Account就够了Consumer我们用Debug模式启动
[02:04] 然后呢再起一下account这个反应比较慢呢我们是consumer开始启动了我们接下来启动一下account启动咱接下来观察一下控制台看有没有问题哎报错了报错了那account这边估计也会报错是不是咱们看consumer这边看报什么错啊呃这是丑意这是什么错呀往下找找哎看这
[02:56] 这个东西咱似乎在前面什么地方说过这个东西这个对象说我没有说过是不是在海米里是不是有一个配置类对不对有个配置类就是谁就是他他这里边提到了提到的是不是就是他你看是不是难道是咱这个配置类有问题这个代码咱直接沾过来了应该不会有问题我们看他有没有什么提示他说这
[03:31] 空置不是控制人呢他说是number format对吧哎这有具体的其实23号23号23号嗯这的意思应该是说他无法进行这个什么类型转换因为他是一个空因为这个是一个哭哭哎那这个就说明啥说明这个配置的值他没有读取到呗那为什么读取不到呢咱这些配置是不是咱呃前面在环境搭建的时候是不是放到Apollo上呀
[04:03] 是不是因为咱检查Apollo你看这里面咱当时不都配过了吗这应该是没啥问题但是他这为什么读取的时候读取不到大家觉得会是哪个问题对这里边缺一个细节啊大家一定要注意的我们应该是少做了一件事情什么事呢我一说你就想起来在这你看这个application.yml这个配偶件当中我打开了啊我打开之后你看一下这个配置这个代码很少你觉得
[04:34] 问题出在哪想一想啊想一想我们前面我们说了我们做了一件什么事啊前面前面我们是不是新建了一个这个一个名称空间对不对新建的啊就以前是没有的现在新建那你再想想这这块代码是在干嘛这块代码是在干嘛现在明白是哪个问题吧对我们这块配置是不是用来设置当前这个微服务要从Apollo上去
[05:05] 加载哪些配置对不对这里边是不是写的那些呃名称空间对吧那你看我们这里边有没有加入哪个配置啊加入这个还没这个配置啊有没有加这个配置啊没有啊这个这个是新加上来的嘛对不对说咱在这应该逗号啊这个名称空间也给他干什么呀加上要不然的话你阿卜罗那边是有的但是
[05:32] 当前这个什么呀微服务他并没有读取读取这里边的什么呀配置啊那就相当于Apollo能白配了那那肯定那个谁啊那个阿康的那边肯定也有这个问题啊可靠你他咱找一找这边肯定也得配这个东西这一个细节啊你一定要注意的就容易忘了一件事啊在这最后吧也得加进来一个这多一个逗号啊
[06:01] 这个名称空间得得得加进来啊加进来之后呢咱接下来再重启consumer重启然后呢这个谁啊这个account重启都是调试模式啊因为咱一会想加断点来观察一些这个数据咱看这次还有问题没有咱把那个Hemley那个名称空间啊给加上去哎应该是没问题你看这个logo就是这个标志已经出来了是吧那这边已经启动完了啊
[06:39] 这边应该都启动完了都这次都没有错没有错啊没有错咱控制台清了一下接下来咱就去哪postman里边进行测试啊呃咱当时你看看啊咱们跑到这吧找找这个要回顾看这个图我们是不是现在通过postman发请求先往哪先往用户中心啊你看咱以前的测试是用户中心吗对不对发请求啊
[07:08] 咱呢要要传数据过去这边要保存保存完之后是不是要远程调用同一账号这边他也要保存信息是吧咱当时传数据是不是通过body对吧当时呢是一个json格式的数据只是传过去一个手机号那咱就接着拿着这个来进行测试吧这个手机号换一换吧换一个191922吧行吧这个肯定是不存在的1922那我就直接点send了对不对直接测试了咱
[07:38] 正常情况下应该先测试这个都成功的情况是不是两边都成功的情况咱试一试那我就直接点击什么呀send走好我们看一下返回0证明是不是成功了对不对那咱去控制台看控制台有有有啥好丑的没有控制台没啥好丑的是不是控制台也没打一啥东西因为咱当时弄的日志是不是啊这也这也能看到这这是证明执行那个confirm
[08:10] 那证明应该是成功了对吧那咱直接去这个表里边了瞅瞅啊表里边咱先看看consumer吧consumer核心刚才是哪个呀R2是吧刚才是R2R2已经进来了然后看accountaccount R2也有对不对那这是都成功的情况下目前没有问题就是加入了Hemily这个代码之后呢咱这个功能还是没有任何问题
[08:39] 那咱接下来重点其实想测试的是不是有问题的情况下而且我们是希望是这样就我希望的是统一账号这边出点问题然后看看用户这边用户中心这边能不能回滚对不对因为他是先保存嘛这边是后保存嘛用户中心是事物的发起方统一账号这边是事物的参与方嘛对不对那咱找找代码找找谁呀找找康特这边对吧
[09:08] 我看到这边呢怎样找他的还是右层Service这个代码找找哪进行保存的呀这吧对吧就是这儿啊你看这儿调用的save方法吗是不是这是confirm这个代码然后哎不是啊稍等这是confirm的代码没做任何事情这是cancel是不是回过来一下吧账号又删掉了对不对那咱是不是希望这儿保存数据的时候出问题吗对不对这儿啊
[09:44] 那咱想个什么招呢想个什么招转账的时候是不是搞了一个什么控制针对不对这儿不好不太好搞控制针对不对咱这儿也没有道层也没有注入东西因为道层咱当时是靠MP对不对它封装好的C5发直接调用那咱这样咱简单粗暴一点这儿故意造一个异常得了我这么写你看行不行想想为了测试方便我加一个依附判断这里边我这么写
[10:16] accountregisterdto他是不是传过来这个手机号吗这个手机号呢我我做一个判断啊判断如果是举个例子10的话这个这个就就算是出现场了我就自己跑一个一场shrugneoruntimeexception对吧这边随便给个信息吧就就写个啥我是故意的
[10:51] 这10嘛他本身就不是手机号对吧而且谁注册的时候敢用10这个号来注册对不对所以说呢我们故意的啊故意的加这块代码让他出个错当然你要想让他抛这个异常必须是手机号是哪个号对10啊就这个逻辑大家应该能看懂很简单所以呢我将来通过普斯特曼传数据的时候手机号是不是给成10这样是不是就满足了满足了这就抛异常了对不对
[11:18] 那等于说就是让阿康的这边执行的时候是不是就出问题吗是这意思吧呃那我这加入注射吧测试用的实际看他不会这么写啊测试用那然后接下来是这样我接下需要重启谁阿康的这边重启一下因为改了代码了重启一下重启一下之后呢我们应该是在postmanpostman这个地方我应该给一个什么值啊110对
[11:52] 然后看这边启动完没有好这边已经启动完了控制台清一下啊两边控制台都清一下然后我们postman这边直接就点send了我传的是10啊走啊这边已经返回过来注册失败了是不是嗯控制台有的观察了控制台看看控制台应该是我看这边哎你看这边实行了什么呀cancel就是回过来是不是
[12:28] 咱还是去表里边看吧更直观一些啊110咱先看看consumer这边刷新没有10吧对不对啊我们看account这边刷新也没有10吧证明回货成功了然后呢咱跟当时转账一样啊我们也加一个断点吧让大家看中间这个过程嗯那我家断点一定是在哪呀是在在这对不对在这
[12:57] 就是马上就要出异常的这个地方加一个断点我们观察一下中间这个过程先控制台都先清一下还是测试这个10还是让他出问题还是这个我再点send走然后断点是不是就已经到这了对不对到这了你看这个传过来这个值是10然后我们直接去表里边观察就行了你看看consumer我们先执行的是consumer你看这边10进来没有已经进来了
[13:30] 但我看到这边肯定没有啊因为他那边跑一场了吗然后我们还要观察这个日志你看N度这个数据库是不是咱前面说咱单独创建的吗然后你看这里边是不是造了两张表这两张表是不是哈密给自己创建了对不对用来存储日志呢你看这里边这边目前没信息吗目前没有信息是吧然后他已经回滚过了吗这个咱先不用管咱重点呢是已经观察到什么呀对concern这边10
[14:03] 他应该是已经走完了吧刚才也可能是超时过了啊也可能超时过了我们直接放行让他走吧走完之后呢我们其实就是去表里边看看我看到这里边他肯定是没有110嘛对不对考虑一下考虑嘛这边刚才还看到110了嘛对不对现在也没有证明已经什么呀回滚过了啊我们看看这边的控制台你看这边是不是也跑异常了嘛对不对
[14:30] 然后呢最终其实也进行了一个什么回滚Consumer这边有日志打印吗Consumer这边报错是正常的啊你看他刚才这已经超时了其实超时就回滚了啊超时自动就回滚因为他告诉他家断点了嘛中间就是停顿了一下那这个我们也测试通过了就是我们也观察到了嘛Consumer一开始这里边存进110了但是现在没有了证明他也成功回滚了嗯这个呢就是我们用什么呀最终用
[15:03] Harmony这个框架把咱们前面注册功能当中的这个事务问题给解决掉

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Hmily 框架解决用户注册功能中的分布式事务问题。

2) 按时间顺序列出每张画面的要点：
画面1：展示用户注册的 SQL 数据库表结构和部分数据，以及对应的 Java 代码片段，其中包含 `updateWrappers` 和 `cancelRegister` 方法。
画面2：IDEA 中显示项目结构，服务启动日志，表明 Eureka Server 和 Spring Boot 服务已启动。
画面3：服务启动失败，报错信息显示 `Error creating bean with name 'hmyTransactionBootstrap'`。
画面4：展示 `HmilyConfig.java` 代码，配置 Hmily 的数据库连接、用户名、密码等参数。
画面5：展示 `application.yml` 配置文件，包含 Apollo 配置、服务 ID、命名空间和日志配置。
画面6：服务启动日志，显示 SQL 连接建立的警告信息。
画面7：Postman 中发起 POST 请求，测试注册接口，请求体包含手机号。
画面8：IDEA 中显示服务启动日志，包含服务注册和发现信息。
画面9：展示 `AccountServiceImpl.java` 代码，其中包含 `confirmRegister` 方法。
画面10：在 `confirmRegister` 方法中添加了判断手机号是否为 "110" 的逻辑，若为 "110" 则抛出异常。
画面11：Postman 中发起 POST 请求，测试注册接口，请求体包含手机号 "110"。
画面12：IDEA 中显示 `confirmRegister` 方法执行时，`accountRegisterDTO` 对象的属性值，其中 `mobile` 为 "110"，`password` 为 null。
画面13：展示数据库表 `p2p_consumer` 中的数据，包含用户注册信息。
画面14：PPT 页面，标题为“4. Hmily解决注册功能的事务问题”，子标题“4.1 业务回顾”，图示展示了“调用端/App”、“用户中心”、“统一账号服务”三个模块之间的交互流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1代码片段：
```java
public void cancelRegister(AccountRegisterDTO registerDTO) {
    log.info("cancelRegister");
    removeWrappers(AccountRegisterDTO.class, registerDTO);
    registerDTO.setMobile(null);
}
```
画面4代码片段：
```java
@Configuration
public class HmilyConfig {
    @Bean
    public HmilyTransactionBootstrap hmilyTransactionBootstrap() {
        HmilyConfig hmilyConfig = new HmilyConfig();
        hmilyConfig.setDriverClassname(env.getProperty("org.dromara.hmily.hmilyDbConfig.driverClassName"));
        hmilyConfig.setUrl(env.getProperty("org.dromara.hmily.hmilyDbConfig.url"));
        hmilyConfig.setUsername(env.getProperty("org.dromara.hmily.hmilyDbConfig.username"));
        hmilyConfig.setPassword(env.getProperty("org.dromara.hmily.hmilyDbConfig.password"));
        hmilyConfig.setTransactionTimeout(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionTimeout"));
        hmilyConfig.setIsolationLevel(env.getProperty("org.dromara.hmily.hmilyDbConfig.isolationLevel"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionType(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionType"));
        hmilyConfig.setTransactionMode(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionMode"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.set

