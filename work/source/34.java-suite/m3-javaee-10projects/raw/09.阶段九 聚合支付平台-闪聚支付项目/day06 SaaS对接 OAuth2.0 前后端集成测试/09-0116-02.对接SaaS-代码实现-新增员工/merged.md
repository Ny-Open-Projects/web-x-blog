# 02.对接SaaS-代码实现-新增员工

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\02.对接SaaS-代码实现-新增员工【海量资源尽在 666java.com】.mp4
- 时长 12分49秒（音频 769s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下边呢我们来实现新增员工的接口那么我们知道员工呢在商务平台叫员工那么其实它对应到SaaS里边呢就叫用户这个用户信息是一个非常重要的信息因为大家知道最终用户使用账号密码来登录我们的散具支付平台对不对所以这里边我们在新增员工的时候呀我们是要进行
[00:23] 一些数据的校验的那比如说账号呢是要在这个三户里面是唯一的手机号呢也要在这个三户里面是唯一的包括它的一些必要的数据呢比如说它的这个手机号格式是否正确呀包括它的账号啊都不能为空好那下边各位我们现在就来做这个新增员工的接口那么同样的道理我们还是在原来三户服务
[00:49] Service然后我们来做新增员工新增员工的话这里边我们肯定需要传一个staff的这个什么呀这个DTO好那么关键这个接口比刚才新增门店的复杂点在哪呢其实就是它有一系列的校验所以这里边呢我们把校验的逻辑呢我们要说清楚那这个呢就是
[01:15] 员工的信息传进来返回肯定是新增成功的这个什么员工的信息那这里边有几点啊然后我们来实现的话注意好这里边我们要知道员工对应于SaaS的用户对不对所以这里边呢我们肯定先要做什么做参数的什么合法性交易那另外呢还有就是我们说过这个在
[01:45] 同一个什么商户下在同一个商户下这个员工的账号和手机号必须为一那这个意思呢也就是说这个商户A下边他会添很多员工对吧那么这个员工的账号在这个商户下边他必须是唯一的那一会我们要查数据库交易一下如果有这个账号就不能添了那另外呢如果他那个
[02:12] 要输入手机号吗手机号也必须为一因为后边可能我们要用手机号登录是吧所以这里边呢有两个唯一的校验在同一个商户下员工的账号要为一那另外呢在同一个商户下员工的手机号也要为一所以这两个都要校验好那下面呢我们先简单的校验一些这个它的参数的比如说飞空啊或者什么校验的啊那如果说它为空的话对吧或者说
[02:42] 那我们说了嘛他这个手机号是不是非常重要对不对手机号呢我们其实可以这么做我们用这个Lan3这个包当中的easy blank来校验好或者说那账号你不填行吗是不是也不行对所以我们来校验账号你也不能为空
[03:08] 没错吧那这样的话如果出现了这个账号和手机号当然还有一个也不能唯空你猜猜啥你账号登录我们说是不是还得需要密码呀所以密码的话其实也不能唯空好那这里面呢它有一个什么有一个密码呀看一下啊
[03:36] 那员工信息这里边呢各位是没有密码的那么我们稍后呢在商户注册那个那个那个方法当中来教研密码就行了因为将来这个方法是被商户注册我们之前写的你看往上翻翻到这儿这是不是商户注册对吧这里头我们将来要往里边放一个什么放一个密码因为密码呢要写到SaaS当中那现在呢我们就把它加一下好看一下啊这个是密码
[04:09] 对吧好这个是什么叫做嗯上啊叫做用户的密码他在注册的时候不是要输入密码吗对那一会呢我们就在这个啊商户注册这个方法里面来校验一下密码嗯那这里面当然现在也可以去校验一下好这个是不是就是如果说密码为空那我们也不允许他注册是吧这是不是就OK了好接着啊
[04:42] 再接着回来写我们的这个叫做添加员工将来这个方法会被刚才我们说讲义上说的第几步第四步我们要进行统一调用现在我们分开把这几个新增员工新增门店的结构给他写完好那这样的话各位我们这个新增员工的参数合法性交验就完了如果说他有问题了那我就抛一个异常是不是抛一个异常
[05:10] 这里边我们可以用异常代码传入对象围攻或缺少必要的参数就OK了那下边还有一个教研就是在不同的商户下员工的账号是在同一个商户下对不对你不同的商户下员工的账号当然可以相同但是一个商户下边那这一个他的人的账号和手机号必须是唯一所以这里边我们也要去教研
[05:33] 好那么我们来和讲义的方法我们保持一致啊这里面我写两个sale方法一个是教研手机号的一个是教研账号的对吧好来看一下那么我们来看啊这个sale方法这个呢我准备给它返回一个什么呀那个布尔类型就行了那让它给我传入手机号传入商户的ID我来看看数据库有没有如果有那我就认为已经存在了行吧好那
[06:02] 布尔类型对不对然后呢这里边我们刚才说了嘛需要一个手机号还需要一个啥这个商户的什么ID然后现在呢我们要拿着这两个参数来进行什么这个员工他的手机号在同一个商户下是唯一的这么一个教验对吧
[06:29] 好那如果说不存在的话那我们就你看这个方法是easy exit是吧所以也就是说如果存在我给它返回true如果不存在呢就是false好那我们是需要去查询什么呀查询员工吧所以这里边呢我们要把员工的Mapper注进来好来员工的Mapper呢是在staff然后呢Mapper
[06:59] 是不是就OK了然后呢接下来我们看你怎么查呀那你看好啊先看看它你看它里边字段有三户ID吧还有一个手机号你看你是不要把这两个字段关联查询对吧联合查询联合查完了之后呢如果存在记录是不是就是表示已经存在这个记录了所以这里边呢我们slack的什么呀count吧然后内有一个lambd然后呢这里边看好
[07:28] 那你要查手机号那你就得用啥对用手机号作为条件然后呢你还得用商户的ID作为条件商户的ID在这个表当中我们看它是叫做Marketing ID对吧好OK了如果说它查到Count那么我们就直接返回什么呀
[07:56] 对如果它大于0那我认为是不是就是存在量所以这样的话我们是不是就可以在这儿在刚才的那个这里这是手机号的校研是吧那我们这调一下然后呢我们传进去手机号对吧还有一个商户的ID这样我们是不是就得到了这个然后它报了一个错你看报啥错这个是一个lang好
[08:25] 然后呢那么他得到了他的这个是否存在的这个标记如果说他等于true的话各位就说明已经存在了已经存在的话我们就要抛出异常说这个账号这个用户的手机号在商户下已经存在我们找一下叫做我们不要这么早了来找到我们的讲义好这是根据
[08:53] 手机号校验嘛它有这么一个标记我们看一下有没有的话我们还得加好这个你点开看一下叫手机号也存在是不是啊好那么接下来还有是要校验账号吧那校验账号的方法跟它是不是就是类似呀那我们也是和讲义的方法保持一致啊这个是有一个叫做对账号是否存在的一个校验好那账号如果校验的话你这里头要写user name了对不对
[09:24] 好然后呢还有一个商户的ID对吧好那么这一堆查询的话其实有一点变一下就行了这就变成了谁呀对你是要查账号嗯也就是user name这样是不是就行了对吧那这个校验和上边啊区别在于它是员工的账号在同一商户下是唯一的这是user name
[09:53] 那好那同样的道理在前边呢我们也进行一个对私有方法的调用啊我们让他把这个账号传给我们然后呢再把这个什么商户的ID给我们然后这样的话我们是不是就可以判断如果说他存在了那么我们是不是就可以抛出异常而这个异常呢指的就是什么账号已存在对吧用户名已存在看见吗
[10:23] 好这样的话我们所有的校验工作就完事了那教员工作完事了之后呢接下来我们是不是就直接开始调用staff的这个什么呀Mapper然后呢insert好insert的话这里边呢由于它是对吧dto所以这里边我们要转一下用staff的converter我们刚才考进去的一个converter好然后呢来用dto转成entity
[10:51] 这样我们转完了之后注意啊现在我们需要做一件事哎对你现在是不是就是插入了对吧然后呢插入完了之后呢你当然也可以去给它转成DTO回传对吧来看一下啊这个过程跟刚才我们新增门店是一样的啊就不说了那我说说什么呀看好打开我们的员工注意关键点在这首先这里边有几个点你看有一个叫什么
[11:21] 姓名职位这些东西呢都是传过来的但是有一个叫门店ID是不是啊门店ID这个非常重要那门店ID的话那各位就需要你这里边呢来设置它了设置员工的什么所属门店懂吧员工所属门店员工的所属门店怎么设置你刚才各位
[11:49] 你刚才是不是已经新增门店了将来我们新增完门店了之后呢就可以把这个ID呢传给这个这个对象所以这里边呢你看这里边你看它有一个东西你看是不是有一个叫做store ID啊但这store ID其实你要注意是在这个员工的DTO当中已经存在的如果他没有这个门店ID咱们是不允许让他去什么
[12:14] 新增的所以我建议你在这呢你把这个校验条件加上懂吧这很重要啊这是一个lang对吧lang的话我们就不能用这个is blank了我们用如果它等于空懂吧所以这里边呢我们就不用在这设了好那这样的话我们说这个员工的信息我们是不是就插入成功了对吧然后后边我们要做的事是不是就给这个员工和门店
[12:46] 设置一个绑定关系就完事了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解商户服务中新增员工接口的实现，包括接口定义、StaffDTO数据结构、业务校验逻辑（手机号与用户名唯一性）及数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档“1.4.2 商户服务新增员工接口”的“1.4.2.1 接口定义”部分，说明接口需接收员工数据、请求新增员工、并返回结果。同时指出在MerchantService接口类中定义该接口，代码片段为：
```java
/**
 * 商户新增员工
 * @param staffDTO
```

画面2：展示IDE中MerchantService接口定义，包含方法：
```java
StoreDTO createStore(StoreDTO storeDTO) throws BusinessException.
//新增员工
StaffDTO createStaff(StaffDTO staffDTO) throws BusinessException;
```

画面3：展示MerchantServiceImpl.java中createStaff方法的实现，包含参数校验：
```java
public StaffDTO createStaff(StaffDTO staffDTO) throws BusinessException {
    //参数合法性校验
    if(staffDTO == null || ...)
```

画面4：展示StaffDTO类的定义，包含字段及注解：
```java
/**
 * StaffDTO
 */
public class StaffDTO implements Serializable {
    private static final long serialVersionUID = 10L.
    @ApiModelProperty(value = "主键")
    private Long id;
    @ApiModelProperty(value = "商户ID")
    private Long merchantId;
    @ApiModelProperty(value = "姓名")
    private String fullName;
    @ApiModelProperty(value = "职位")
    private String position;
    @ApiModelProperty(value = "用户名(关联统一用户)")
    private String username;
```

画面5：展示createStaff方法中对手机号的校验逻辑，包含注释和代码：
```java
//手机号格式校验
if (!StringUtils.isMobilePhone(mobile)) {
    throw new BusinessException(CommonErrorCode.E_10011);
}
//手机号是否已存在
if (StringUtils.isNotBlank(mobile)) {
    if (count > 0) {
        throw new BusinessException(CommonErrorCode.E_10012);
    }
}
```

画面6：展示文档“1.4.4.1 接口说明”，说明SaaS系统为用户提供注册租户的接口，包含注释：
```java
/**
 * 创建租户如果已存在则返回租户信息，否则新增租户、新增租户管理员，同时初始化权限
 * 2.手机号已存在，禁止创建
 * 3.创建租户对应账号时，需要手机号，账号的用户名密码
 * @param createTenantRequest 创建租户请求信息
 * @return
 */
TenantDTO createTenantAndAccount(CreateTenantRequestDTO createTenantRequest);
```

画面7：展示MerchantService接口中queryMerchantById方法的实现：
```java
@Override
public MerchantDTO queryMerchantById(Long id) {
    Merchant merchant = merchantMapper.selectById(id);
    MerchantDTO merchantDTO = new MerchantDTO();
    merchantDTO.setId(merchant.getId());
    merchantDTO.setMerchantName(merchant.getMerchantName());
    return merchantDTO;
}
```

画面8：展示isExistStaffByMobile方法的实现，包含注释和代码：
```java
Boolean isExistStaffByMobile(String mobile, String merchantId) {
    staffMapper.selectCount(new LambdaQueryWrapper<Staff>().eq(Staff::getMobile, mobile).eq(Staff::getMerchantId, merchantId));
}
```

画面9：展示isExistStaffByMobile方法的实现，包含注释和代码：
```java
//在同一个商户下员工的手机号唯一
Boolean existStaffByMobile(String mobile, Long merchantId) {
    staffMapper.selectCount(new LambdaQueryWrapper<Staff>().eq(Staff::getMobile, mobile).eq(Staff::getMerchantId, merchantId));
}
```

画面10：展示isExistStaffByMobile方法的实现，包含注释和代码：
```java
//在同一个商户下员工的手机号唯一
Boolean existStaffByMobile(String mobile, Long merchantId) {
    if (existStaffByMobile(mobile, merchantId)) {
        throw new BusinessException(CommonErrorCode.E_10013);
    }
    return null;
}
```

画面11：展示isExistStaffByUserName方法的实现，包含注释和代码：
```java
Boolean isExistStaffByUserName(String username, Long merchantId) {
    Integer count = staffMapper.selectCount(new LambdaQueryWrapper<Staff>().eq(Staff::getUsername, username).eq(Staff::getMerchantId, merchantId));
    return count > 0;
}
```

画面12：展示createStaff方法中对用户名的校验逻辑，包含注释和代码：
```java
//在同一个商户下员工的用户名唯一
Boolean existStaffByUserName(String username, Long merchantId) {
    if (existStaffByUserName(username, merchantId)) {
        throw new BusinessException(CommonErrorCode.E_10014);
    }
}
```

画面13：展示createStaff方法中对员工信息的插入操作，包含注释和代码：
```java
//员工手机号在同一个商户下唯一
Boolean existStaffByMobile(String mobile, Long merchantId) {
    if (existStaffByMobile(mobile, merchantId)) {
        throw new BusinessException(CommonErrorCode.E_10019);
    }
    //设置员工工作部门
    Staff staff = StaffConvert.INSTANCE.dto2Entity(staffDTO);
    staffMapper.insert(staff);
    return StaffConvert.INSTANCE.entity2DTO(staff);
}
```

画面14：展示isExistStaffByUserName方法的实现，包含注释和代码：
```java
/**
 * 根据账号判断员工是否在指定商户存在
 * @param username
 * @param merchantId
 * @return
 */
private boolean isExistStaffByUserName(String username, Long merchantId) {
    LambdaQueryWrapper<Staff> lambdaQueryWrapper = new LambdaQueryWrapper<Staff>();
    lambdaQueryWrapper.eq(Staff::getUsername, username).eq(Staff::getMerchantId, merchantId);
    int i = staffMapper.selectCount(lambdaQueryWrapper);
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上文要点中完整抄录）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（无PPT或架构图/流程图）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

