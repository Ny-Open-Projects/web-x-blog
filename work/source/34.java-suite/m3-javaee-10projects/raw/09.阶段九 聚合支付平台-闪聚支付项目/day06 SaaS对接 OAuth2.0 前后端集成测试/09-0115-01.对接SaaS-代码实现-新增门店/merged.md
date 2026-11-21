# 01.对接SaaS-代码实现-新增门店

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\01.对接SaaS-代码实现-新增门店【海量资源尽在 666java.com】.mp4
- 时长 7分4秒（音频 424s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面呢我们来实现对接SaaS的具体过程那么根据简便分析的在我们商户平台呢我们需要做以下几个工作第一呢我们要新增员工员工呢要所属于一个门店所以我们还要新增门店那这个门店呢应该是这个商户的一个根门店就是一个大的一个什么组织结构还有一个就是门店的管理员
[00:26] 那新增的这个员工呢就默认作为门店的管理员你可以理解为这个商户的总经理好还有最后呢就是我们在要调用我们SaaS平台的接口然后呢完成租户的注册用户的新增以及用户和租户的关系绑定等等好那么这四步呢我们分别来执行首先呢我们打开我们的商户平台
[00:54] 那在商户平台当中啊我们要做的事刚才说了是不是要新增员工新增门店等等对吧好那么我们打开数据库啊这里边呢我们要先看一下在我们商户平台其实是有几张表我们当初还没有说的啊这个是应用表在我们之前创建应用用过了这个是商户表是吧那后面这几张表大家看一下对那这个呢是staff他是一个叫啥
[01:22] 它是我们的员工员工表下面呢是我们的门店表门店表那么还有呢就是员工和门店的关系表那么他们呢都是隶属于某一个什么商户的对吧所以呢各位我们在新增员工的时候你看这儿是不是有一个叫商户ID啊那包括门店这里边呢你也可以看到是不是有一个叫所属商户是吧好
[01:51] 那么表结构我们清楚了之后呢下面我们要做的是不是就是像这个staff这个表当中我们要插入数据像到这个表当中我们要插入数据最后呢我们给他俩呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃呃
[02:21] 我们新增接口了这个呢叫新增员工是吧好那么我们呢根据刚才根据我们的讲义流程吧你看这边首先是新增门店有了门店我们在新增员工的时候是不是才能拿到门店的ID啊好那我们先写新增门店门店然后呢再写新增员工最后呢我们将什么呀
[02:51] 将这个员工和门店进行绑定也就是某个员工属于哪个门店好那么新增门店的话就是像我们的SDAO这张表当中来插一条记录默认刚开始注册商户的时候插的门店呢是一个根门店就相当于是我们一个什么这个商户这个公司的一个基础的架构呢先放到这然后
[03:18] 接下来我们有一个模块叫门店管理的话那在这里头会添什么部门业务部呀然后呢什么营销部啊等等啊这些好那么我们继续回到讲义上看这个门店的添这个接口呢是新增门店的接口那比较简单吧也就是我们只要去干嘛揣入我们的门店的信息是不是就可以了然后呢
[03:48] 如果说有问题我们依然是抛出一场当然门店新增成功之后由于你需要这些门店的信息你是不是需要把这个门店的信息再返回来对吧所以这就是我们的新增门店的借口这个是门店的信息是吧那这个返回的是不是就是新增成功的门店信息好
[04:14] 那么这个接口弄好了之后呢接下来我们直接在商户服务当中啊咱们把它实现一下看好然后在这里边呢找到我们的Service好然后呢我们把这个方法报出来那如果要新增门店我们肯显然是要住到什么呀把我们的门店的Mapper呢住进去啊好就是它那么这里边呢我们来看这个方法就
[04:46] 比较简单因为它是和新增这个商户是一块操作的应该是在同一个事务是吧所以这里面呢我们说这个商户还没有的这个注册的时候呢这个门店肯定也没有所以呢我们就准备直接怎么弄呀insert就可以了只不过这里边呢我们是需要去把它给什么转换一下转换一下那这里边呢我们是不是需要一个转换的这个
[05:16] Converter 是吧好 那下面呢我们来拿一下这个Converter那我们到资料目录当中我们来拿一下这个Converter来我们找到我们的资料这里边我们是需要两个一个是门店一个是员工的好 我们把它拿过来之后呢拷到我们的Converter目录那这个时候呢在这儿啊我们就直接可以用这个什么Converter
[05:40] 然后这里边呢我们要做的是DTO转成entity啊然后把DTO放进去这个时候呢这个entity呢是不是就OK了好然后呢我们把这个entity把它放到我们的insert方法各位这个时候呢我们是不是就成功了那么这个呢就是我们说的新增门店新增门店OK了之后呢接下来我们是不是就可以
[06:06] 返回新增门店的信息啊那返回的话其实这里边我们需要把什么entity转成dto然后把他们再返回去这样的话我们这个新增门店的接口是不是就写好了这个呢就比较简单啊当然这里边呢你也可以干嘛呀你也可以打印一行的日志回头我们方便我们进行调试对吧好这里边呢我们可以
[06:32] 那么我们知道打热制这里面我们可以用long book这里面我们加一个什么sl4g这个注解好然后在这里面呢我们就login for是吧然后呢叫新增门店的信息对不对然后这里面呢我们是不是就可以把它按照讲义上我们把它转成json是不是就打印出来是不是就行好新增门店的接口呢我们就写好了
[07:01] 稍后我们再写新增员工好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解商户服务中新增门店接口的定义与实现，包括数据库表结构查看、DTO类生成、接口方法编写及转换器实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，讲解商户服务新增门店接口的定义，需生成StoreDTO类，并在MerchantService接口中定义createStore方法。
画面2：在数据库管理工具中查看pay_channel_param表结构，字段包括CHANNEL_ID、CHANNEL_CODE、BUNDLE_CODE。
画面3：查看store表结构，字段包括ID、STORE_NAME、MERCHANT_ID、PARENT_ID、STORE_STATUS、STORE_CODE，索引为ID。
画面4：查看store_staff表结构，字段包括STORE_ID、STAFF_ID，索引为STORE_ID。
画面5：回到课程文档，展示接口定义部分，强调生成StoreDTO类。
画面6：文档中指出需在MerchantServiceImpl类中实现createStore方法。
画面7：在IDE中展示MerchantService接口定义，包含注解@Param、@ApiImplicitParam和throws BusinessException。
画面8：展示MerchantServiceImpl类中createStore方法的实现，包含参数校验、商户实体查询、状态设置、数据插入等逻辑。
画面9：展示MerchantServiceImpl类中createStore方法的实现，方法体为空。
画面10：在文件资源管理器中显示convert文件夹，包含文件nt-1（新格式）。
画面11：在IDE中打开StaffConvert.java文件，展示接口定义，包含INSTANCE、entity2dto、dto2entity、listentity2dto等方法。
画面12：在IDE中展示StaffConvert类中dto2entity方法的实现，包含entity2dto、listentity2dto等方法。
画面13：在IDE中展示MerchantService类的注解，包括@Configuration、@ApiImplicitParam、@ApiImplicitParams、@PathVariable、@RequestBody、@Slf4j、@Service、@Transactional等。
画面14：在IDE中展示MerchantService类中createStore方法的实现，包含日志记录、数据插入、返回值等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 商户下新增门店
 * @param storeDTO
 */
StoreDTO createStore(StoreDTO storeDTO) throws BusinessException;
```

画面6：
```java
@Override
public StoreDTO createStore(StoreDTO storeDTO) throws BusinessException {
    return null;
}
```

画面11：
```java
package com.shanjujay.merchant.convert;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public interface StaffConvert {
    StaffConvert INSTANCE = Mappers.getMapper(StaffConvert.class);

    Staff entity2dto(Staff entity);
    Staff dto2entity(StaffDTO dto);
    List<StaffDTO> listentity2dto(List<Staff> staff);
}
```

画面12：
```java
entity2dto(Store entity);
listentity2dto(List<Store> staff);
```

画面13：
```java
@Configuration
@ApiImplicitParam(name = "merchantId", value = "商户ID", required = true, dataType = "Long")
@ApiImplicitParam(name = "merchantDTO", value = "商户信息", required = true, dataType = "MerchantDTO")
@Slf4j
@Service
@Transactional
public class MerchantService {
```

画面14：
```java
log.info("新增门店: {}", JSON.toJSONString(storeDTO));
storeMapper.insert(entity);
return StoreConvert.INSTANCE.entity2dto(entity);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

