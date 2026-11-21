# 16.支付渠道参数配置-支付渠道参数查询-交易服务接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\16.支付渠道参数配置-支付渠道参数查询-交易服务接口实现【海量资源尽在 666java.com】.mp4
- 时长 8分31秒（音频 511s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面呢我们来编写支付渠道参数查询的接口那么这个接口在哪里使用呢大家知道我们支付渠道参数配置的时候呢这里边有个表单对吧如果这个支付渠道参数已经配置好了那么这个表单是比较显示已经配置的支付渠道参数啊所以这里边呢我们是需要来写一个查询的那这里边这个查询接口呢它包括两个注意看啊第一个呢是根据我们的这个什么
[00:27] 根据APP应用ID和服务类型来查到它所配置的所有支付渠道的参数它是个列表因为我们之前说了在这张表当中现在你配的是一个微信的这个接口支付渠道对吧但是我们说这个C扫币它还会使用支付宝的这个接口因为你是个聚合接口对不对它既支持微信也支持支付宝所以这里边我们是会有多条记录的
[00:55] 也就是根据应用和服务类型我们可以查到多条所以这里边呢我们说第一个接口呢我们要根据应用和服务类型来查到它所有支付渠道的这个参数另外还有一个就是那我想查具体某一个支付渠道的参数呢那你就根据应用根据服务类型和根据具体的支付渠道的代码然后来查一个具体的参数
[01:18] 这两个都是在前端来配置支付渠道参数的时候所使用的所以我们都需要把它给实现了好那么首先我们还是先做交易服务的接口再做商户平台应用的接口来我们根据刚才我们梳理的这个需求呢我们就开始来定义这个接口了那么首先呢我们在交易服务的API当中我们来把这个写一下啊第一个呢我们说是要查一堆的什么支付渠道的这个参数列表对吧
[01:49] APP ID还有一个是什么是就是我们说的服务类型服务类型就是它好了那现在呢我们把这个写好了之后呢它最终返回的是一个列表返回哪个列表返回肯定是支付渠道参数的列表好它传进来的是根据应用和服务类型来查询支付
[02:18] 支付渠道参数的什么列表也就是多条这是应用的ID这是服务类型的code这没错吧好我们刚才又说了嘛我们现在还需要一个接口这个接口呢是不是查这个支付渠道参数列表了是查某一个支付渠道的参数懂吗所以这时候呢我们就需要另外一个接口看啊名字跟他不一样啊但是参数比他多了个啥
[02:49] 我相信大家要知道第一个应用和服务类型得有对吧那你刚才是查了是所有支付渠道的这个什么参数列表我现在呢想查某一个支付渠道那你是不是得把这个支付渠道给拿过来呀好那也就是说我们说这个支付渠道的这个叫做PayChannel我们得把它拿到这儿对不对好那么它最终返回的肯定是一个
[03:18] 支付渠道的参数所以它就不是list了那这个应该是什么呀是根据应用服务类型以及支付渠道的代码支付渠道的代码然后呢查询什么查询该支付渠道的参数配置信息懂吗一个是查列表一个是查某一个参数好
[03:50] 那么我们来看上面这个就还是应用ID了这个是服务类型这个上就是支付渠道的代码没错吧好那下面呢我们就把这两个接口呢实现一下其实我们在实现接口的时候啊你呢慢慢慢慢的也把我们整个的表的关系结构呢包括业务呢也都熟悉了对吧好那首先我们来看这个那这个的话我们是不是要查列表啊跟什么呀根据应用
[04:21] 和这个服务类型来查哪张表查支付渠道参数表就是这张表就这张表没错吧好那么你要知道啊我们现在根据应用和服务类型应用和服务类型在这个表当中它是一个绑定ID对不对所以说我们现在应该是先注意听先根据应用和服务类型找到他们的什么绑定
[04:53] ID这绑定ID在前边我们是不是写了一个私有方法你是不是就直接可以用这个私有方法来拿到对不对那我拿到了之后呢我是不是拿到一个绑定ID这个绑定ID同样的道理我们也要判断一下吧如果你你这个借口是对外公开的如果人家传了一个错误的应用那如果没有绑定ID你还会查吗所以说它如果为空的话那我们就直接返回一个空就完事了
[05:24] 否则的话这里边就要返回咋了是不是就要根据这个绑定ID来查询我们说的支付参数表量就是根据它应用和服务类型的绑定ID绑定ID来查询什么支付渠道参数表的记录懂吧好那支付渠道参数表那就是PayChannel然后呢Param
[05:56] Mapper然后这里边呢注意啊我们要怎么查Pay小写然后呢它是点Slack是不是类似的对吧然后NEO Lambda好这里边呢我们写Pay ChannelChannel然后呢这是参数然后这里边就是EQ那我们说根据绑定ID来查那其实就是你找到绑定ID就是这个应用服务类型的绑定ID好然后呢你把这个
[06:31] 我们刚才查到这个绑定ID呢把它拿进去这样的话我们是不是就得到了这个什么这个list对不对得到这个list之后呢我们是不是就可以返回了那返回的话这里边你看它是不是需要一个转换呀对不对然后把这个list转成DTO啊各位搞定了吧那么下边我们说你这个是根据应用复类型查所有的支付
[07:00] 渠道的参数列表那下边是不是根据应用服务类型以及支付渠道代码来查某一个支付渠道的这个什么参数啊所以各位我怎么弄啊怎么写啊那你其实我们可以这么做吧你可以根据什么根据应用服务类型查询参数列表有时候老师不是查单个吗你怎么还查参数列表呢你听我说完呀你先查列表这个列表当中一定包括
[07:30] 当前要查询的这个支付渠道的参数我说的没错吧因为它是这个应用和服务类型所有的这个参数对不对对吧既然包括了那我们就便利它呗对不对我们便利它了之后呢我们就看你当前要哪个支付渠道那么我呢就给你返回哪个支付渠道懂这意思吧你现在呢你看这是不是支付渠道呀你想要
[08:01] 这个支付渠道行如果他等一趟好那么我就给你返回这个支付渠道配置的什么配置的参数各位看懂了吗对这就是我们说的一个是查所有支付渠道的这个参数一个是查单个支付渠道的参数那这个交易服务里边这个两个查询接口咱们是不是就写完了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解支付服务渠道参数查询接口的定义与实现，包括接口方法签名、参数说明、数据库查询逻辑及结果转换。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档目录结构，当前选中“5.4.4 交易服务支付渠道参数配置接口(2)”，内容为“5.5.1.1 接口定义1”，说明根据应用和服务类型获取原始支付参数，结果可能是多个（支付宝param、微信param）。
画面2：展示接口定义，方法签名：PayChannelService接口中定义queryParamByAppPlatformAndPayChannel方法，参数为appId、platformChannel、payChannel，返回类型为PayChannelParamDTO，抛出BusinessException。
画面3：展示IDE中项目结构，选中“MerchantController”，代码中注释“根据应用、服务类型和应用与服务类型的绑定id”，参数为appId、platformChannelCode、payChannel。
画面4：展示IDE中代码，方法签名：List<PayChannelDTO> queryPayChannelByPlatformChannel(String platformChannelCode) throws BusinessException，参数为platformChannelCode，返回类型为List<PayChannelDTO>，抛出BusinessException。
画面5：空白画面，无内容。
画面6：展示IDE中代码，方法签名：public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException，参数为appId、platformChannel，返回类型为List<PayChannelParamDTO>，抛出BusinessException。
画面7：展示IDE中代码，方法签名：public PayChannelParamDTO queryPayChannelParamByAppPlatformAndPayChannel(String appId, String platformChannel, String payChannel) throws BusinessException，参数为appId、platformChannel、payChannel，返回类型为PayChannelParamDTO，抛出BusinessException。
画面8：展示IDE中代码，方法签名：public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException，参数为appId、platformChannel，返回类型为List<PayChannelParamDTO>，抛出BusinessException。
画面9：展示IDE中代码，方法签名：public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException，参数为appId、platformChannel，返回类型为List<PayChannelParamDTO>，抛出BusinessException。
画面10：展示IDE中代码，方法签名：public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException，参数为appId、platformChannel，返回类型为List<PayChannelParamDTO>，抛出BusinessException。
画面11：展示IDE中代码，方法签名：public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException，参数为appId、platformChannel，返回类型为List<PayChannelParamDTO>，抛出BusinessException。
画面12：展示IDE中代码，方法签名：public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException，参数为appId、platformChannel，返回类型为List<PayChannelParamDTO>，抛出BusinessException。
画面13：展示IDE中代码，方法签名：public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException，参数为appId、platformChannel，返回类型为List<PayChannelParamDTO>，抛出BusinessException。
画面14：展示文档目录结构，当前选中“5.4.4.1 接口定义”，内容为“5.5.1.2 接口实现”，展示支付宝支付方式的多种类型，包括H5支付、小程序支付、人脸支付、当面付、APP支付、手机网站支付、电脑网站支付、免密支付、商户单卡、安全检测、全部文档。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
在PayChannelService接口中定义queryPayChannelParamByAppAndPlatform方法：
```java
/**
 * 获取指定应用指定服务类型下所包含的某个原始支付参数
 * @param appId 应用id
 * @param platformChannel 服务类型
 * @return
 */
PayChannelParamDTO queryParamByAppPlatformAndPayChannel(String appId, String platformChannel) throws BusinessException;
```

画面2：
```java
/**
 * 获取指定应用指定服务类型下所包含的某个原始支付参数
 * @param appId 应用id
 * @param platformChannel 服务类型
 * @param payChannel 支付渠道
 * @return
 * @throws BusinessException
 */
PayChannelParamDTO queryParamByAppPlatformAndPayChannel(String appId, String platformChannel, String payChannel) throws BusinessException;
```

画面3：
```java
//根据应用、服务类型和应用与服务类型的绑定id
* @param appId
* @param platformChannelCode
* @param payChannel
* @return
```

画面4：
```java
/**
 * 支付渠道参数列表
 * @return
 * @throws BusinessException
 */
List<PayChannelDTO> queryPayChannelByPlatformChannel(String platformChannelCode) throws BusinessException;
```

画面6：
```java
/**
 * 根据应用、服务类型和支付渠道查询支付渠道的参数配置信息
 * @param appId
 * @param platformChannel 服务类型code
 * @param payChannel 支付渠道代码
 * @return
 */
public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException;
```

画面7：
```java
/**
 * 根据应用、服务类型和支付渠道查询支付渠道的参数配置信息
 * @param appId
 * @param platformChannel 服务类型code
 * @param payChannel 支付渠道代码
 * @return
 */
public PayChannelParamDTO queryPayChannelParamByAppPlatformAndPayChannel(String appId, String platformChannel, String payChannel) throws BusinessException;
```

画面8：
```java
/**
 * 根据应用、服务类型和支付渠道查询支付渠道的参数配置信息
 * @param appId
 * @param platformChannel 服务类型code
 * @param payChannel 支付渠道代码
 * @return
 */
public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException;
```

画面9：
```java
/**
 * 根据应用、服务类型和支付渠道查询支付渠道的参数配置信息
 * @param appId
 * @param platformChannel 服务类型code
 * @param payChannel 支付渠道代码
 * @return
 */
public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException;
```

画面10：
```java
/**
 * 根据应用、服务类型和支付渠道查询支付渠道的参数配置信息
 * @param appId
 * @param platformChannel 服务类型code
 * @param payChannel 支付渠道代码
 * @return
 */
public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException;
```

画面11：
```java
/**
 * 根据应用、服务类型和支付渠道查询支付渠道的参数配置信息
 * @param appId
 * @param platformChannel 服务类型code
 * @param payChannel 支付渠道代码
 * @return
 */
public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException;
```

画面12：
```java
/**
 * 根据应用、服务类型和支付渠道查询支付渠道的参数配置信息
 * @param appId
 * @param platformChannel 服务类型code
 * @param payChannel 支付渠道代码
 * @return
 */
public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException;
```

画面13：
```java
/**
 * 根据应用、服务类型和支付渠道查询支付渠道的参数配置信息
 * @param appId
 * @param platformChannel 服务类型code
 * @param payChannel 支付渠道代码
 * @return
 */
public List<PayChannelParamDTO> queryPayChannelParamByAppPlatform(String appId, String platformChannel) throws BusinessException;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“5.5 支付渠道参数查询”，子标题“5.5.1 交易服务渠道参数查询接口”，子子标题“5.5.1.1 接口定义1”，内容为“1) 根据应用和服务类型获取原始支付参数param，结果可能是多个（支付宝param 微信param）”。
画面14：标题为“5.4.4.1 接口定义”，内容为“5.5.1.2 接口实现”，展示支付宝支付方式的多种类型，包括H5支付、小程序支付、人脸支付、当面付、APP支付、手机网站支付、电脑网站支付、免密支付、商户单卡、安全检测、全部文档。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

