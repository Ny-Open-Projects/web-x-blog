# day06-5-开户第一阶段-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-5-开户第一阶段-功能实现1_【海量资源尽在 666java.com】.mp4
- 时长 7分33秒（音频 454s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢我们把第一阶段生成开户数据这块的接口全部都定义好了啊定义好之后呢咱接下来就按照接口进行功能实现那这个功能实现咱从哪开始呢这里边呢大家要注意了啊因为在这个开户过程当中啊在整个开户的这个过程当中呢我们涉及到银行卡操作银行卡就是Bank Card银行卡
[00:30] 所以说呢这个里边呢我们可能会涉及到一些增加改善的一些操作所以说呢我们首先要做的第一件事呢就针对银行卡这一块先把它的数据访问层相关东西给搞定就是MapperMapper接口还有它的映射配置文件我们要把这个准备工作先做因为一会儿呢咱们在实现相关功能的时候就涉及到银行卡的一些操作比如说查询对吧我要查
[00:56] 这个某某用户他要开户吗我要查一查这个用户是不是已经绑定了什么银行卡等等等等一些信息所以说这里边你看这说了嘛我们要单独抽取出来一个什么呀处理银行卡业务的一个结合那我们首先就要把他的数据访问层先搞定那数据访问层呢我们这块呢仍然使用的是mybattiesplus就是MP那大家回忆一下我们以前在用MP来这个实现数据访问层的时候是不是非常简单
[01:25] 我们只需要定义一个接口去继承他的接口然后呢这个接口里边我们不需要定义任何方法就继承下一堆增长干啥对不对然后再提供一个相配一套的硬设配用件就搞定和咱家先把这块的事情做一下那咱就找哪大家这个要注意啊我们说了这个刚才定义接口的时候是分两块一个是用户中心一个是存款代理对吧那咱功能实现也是分两块你看这功能实现一个是用户中心一个是什么呀存款代理咱现在
[01:55] 按照顺序仍然是先去哪运货中心啊那咱去运货中心这边consumer啊我们找到什么呀我们应该要找到一个包叫Mapper是吧就这个这是咱以前在实现运货中心的时候增删改善对应的这个Mapper接口还有一些配置文件对吧那接下来咱单独创建一个针对银行卡我们需要先定义一个什么呀接口啊
[02:24] 这个跟奖励保持一致吧叫Bank Card什么Mapper我们粘过来然后粘过来之后你一定要注意这个接口一定要继承什么呀对MP的这个什么呀BaseMapper而且还要指定这个什么呀Bank CardBank Card这个实体内这个范形好我们直接继承一下叫什么呀叫Base对吧BASEBase叫什么呀Mapper
[02:56] 看好啊别引错包了啊就是MP的然后这边有一个范形就是那个银行卡那个范形就是bankcard啊BANKCARD那这个实体类现在不存在不存在的话大家不用编写啊呃你在实现开会的过程当中如果碰见这些类啊你直接去资账文件夹里边类这里边就找就行了你看这是不是有个什么呀bankcard然后你看一下他是在哪个包里边你给他粘过去就行了
[03:27] consumer entity是不是那我们给他粘过来就行control c然后呢就是哪就这个地方粘过来米昂卡这个实体类哎这边呢我们就可以导入过来了对不对还报错了bank看了已经导过来了呀啊我们这儿是一个什么呀接口啊刚才没有选我换成intrfac对interface大家看这样就不报错了对不对
[04:02] 那这个接口是不是就定好了就这么简单啊呃千万不要认为这里边是一个空间口因为这有一个什么呀继承那然后呢看这啊我们是不是这个接口有一个对应的什么呀映射配文件对不对好我们接下来把这个映射配文件也创建一下还记得咱以前是不是自己创建过这个一个模板啊对不对那这里边呢这个名字应该是叫b a n k bankc a r d
[04:30] 然后呢MAPP一样对吧点击OK然后这里边需要配个什么东西这里边是不是需要配这个这个这个路径这个接口路径对吧你看以前你配的是不是这个接口的这个路径那我们现在呢就是就这个接口吧是不是路径这样应该有提示我们直接敲cn点atcast点再点对吧应该是谁呀consumer.Mapper
[05:00] 第二谁呀对我们叫bank card来吧哎这样子的话我们就把银行卡操作的这个什么数据访问槽啊就把这块这个代码就搞定这个搞定完之后呢咱再做一个事情啊做一个什么事情呢就是我们要搞一个分音带这个为什么要做这个事呢大家看上我们第一阶段在讲序分析的时候我们说过了啊大家看这个图我们说了用户中心将来要发数据到哪
[05:32] 到存管代理服务这边他这边是要进行签名加密对不对所以说呢这里边涉及到一个分译的远程调用那我们在用户中心这边是要提供一个分代理就是那个接口这大家都比较熟了啊这个代理大家看这是不是那咱接下来的话把这个分代理也创建好那应该是在哪个包啊二进的这个包里吧对不对这是咱以前在实现这个注册的时候对不对调用的account这个代理
[06:01] 那咱这边的话再新建一个接口啊这要改一改那名字呢跟这边保持一致吧depository urgentapi就是我们一看这个名字知道调那是存款代理服务这个接口那这里边都需要配啥呢第一个你要通过分评client这个注解来设置一下我要远程调用哪个微服务对不对然后呢再进来通过post map这个注解来设置我具体要调微服务里边的
[06:32] 哪个control了哪个方法这应该是呃这个谁啊从管代理服那边某个control了某个方法配的这个路径是不是其实我们一般的做法是不是打开这个从管代理微服找到那个方法把这一块整个全部干什么烤过来就行了这一块呢我就不再呃演示了因为这个东西呢对于大家来说应该都比较熟悉了好我们直接粘过来这个代表大家能看懂就行了这是整个这一块吧我们把这稍微改一下
[07:09] 对那么将来的话我们有了这个代理的话我们的框架是不是会我们为我们生成代理类以及代理对象然后将来就通过那个代理对象啊就可以从用户中心这边往什么呀对往存款代理服那边发这个数据那边就可以进行什么呀加密或者做进一步的处理这是咱先把这个工作相当于一个准备工作给搞定一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在“万方金融”项目中，开发人员正在为“用户中心生成开户数据”功能编写代码，涉及创建Mapper接口、XML配置文件以及Feign客户端接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT内容，标题为“3.3 第一阶段: 生成开户数据”，子标题“3.3.1 需求分析”和“3.3.2 接口定义”，并列出具体开发任务，包括在ConsumerAPI中新增createConsumer方法和在ConsumerController中实现该方法。
画面2：IDE中显示项目结构，当前选中“wanningzp-depository-agent-Service”模块，控制台显示配置同步失败的日志。
画面3：IDE中显示项目结构，当前选中“wanningzp-consumer-Service”模块，控制台显示配置同步失败的日志。
画面4：IDE中打开“BankCardMapper.java”文件，光标位于类声明处。
画面5：IDE中“BankCardMapper.java”文件中，光标位于“extends BaseMapper<BankCard>”处，提示“Identifier expected”。
画面6：Notepad++中打开“BankCard.java”文件，内容为空。
画面7：IDE中“BankCardMapper.java”文件中，光标位于接口声明处。
画面8：IDE中右键“Mapper”目录，弹出创建新文件的菜单。
画面9：IDE中打开“ConsumerMapper.xml”文件，光标位于XML声明处。
画面10：IDE中“ConsumerMapper.xml”文件中，光标位于“namespace”属性处。
画面11：PPT内容，标题为“3.3.3 功能实现”，列出开发任务，包括创建Feign客户端和新建BankCardService接口。
画面12：PPT内容，与画面11相同。
画面13：IDE中打开“DepositoryAgentApiAgent.java”文件，光标位于接口声明处。
画面14：IDE中“DepositoryAgentApiAgent.java”文件中，光标位于“@PostMapping”注解处。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 生成开户请求数据
 * @param consumerRequest 开户信息
 * @return
 */
RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);
```

画面4：
```java
package cn.iteast.wanningzp.consumer.Mapper;

public class BankCardMapper extends
```

画面5：
```java
package cn.iteast.wanningzp.consumer.Mapper;

import com.baomidou.mybatisplus.core.Mapper.BaseMapper;

public class BankCardMapper extends BaseMapper<BankCard> {
```

画面7：
```java
package cn.iteast.wanningzp.consumer.Mapper;

import cn.iteast.wanningzp.consumer.entity.BankCard;
import com.baomidou.mybatisplus.core.Mapper.BaseMapper;

public interface BankCardMapper extends BaseMapper<BankCard> {
```

画面9：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0/EN"
"http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="cn.iteast.wanningzp.consumer.Mapper.ConsumerMapper">
</Mapper>
```

画面10：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0/EN"
"http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="cn.iteast.wanningzp.consumer.Mapper.BankCardMapper">
</Mapper>
```

画面11：
```java
@FeignClient(value = "depository-agent-Service")
public interface DepositoryAgentApiAgent {
    @PostMapping("/depository-agent/1/consumers")
    RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest);
}
```

画面13：
```java
package cn.iteast.wanningzp.consumer.agent;

public interface DepositoryAgentApiAgent {
```

画面14：
```java
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@FeignClient(value = "depository-agent-Service")
public interface DepositoryAgentApiAgent {
    @PostMapping("/depository-agent/1/consumers")
    RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“3.3 第一阶段: 生成开户数据”，子标题“3.3.1 需求分析”和“3.3.2 接口定义”，列出具体开发任务。
画面11：PPT标题“3.3.3 功能实现”，列出开发任务，包括创建Feign客户端和新建BankCardService接口。
画面12：与画面11相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

