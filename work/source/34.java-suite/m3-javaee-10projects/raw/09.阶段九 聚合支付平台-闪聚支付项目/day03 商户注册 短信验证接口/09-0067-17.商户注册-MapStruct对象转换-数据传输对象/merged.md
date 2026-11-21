# 17.商户注册-MapStruct对象转换-数据传输对象

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\17.商户注册-MapStruct对象转换-数据传输对象【海量资源尽在 666java.com】.mp4
- 时长 5分4秒（音频 304s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来学习一个知识点叫做MapStruct对象转换咱先不要看前面的MapStruct咱先看后面对象转换什么是对象转换呢所以这里边我们要理解一下数据传输对象那么在我们代码开发当中你会发现我们用到了很多用于接收数据传输数据的对象类型比如说在Service层当中我们用到的是DTO
[00:30] 我说的Service呢指的是专门对外暴露服务的这个业务服务接口还有在我们说的应用这一块就是对外提供http接口给前端的应用层这一块它使用的是什么view它是和前端打交道的对不对所以其实你还要知道其实在数据持久层这一块它用的是什么呢它既不是DTO
[00:59] 也不是VU数据持久层我们用的是MyBitX Plus你要知道我们生成了一堆的entity是不是就是与数据库表对应的这些实体类型对不对所以这些都是数据传输对象就是我们一个请求过来首先前端请求数据到application应用层然后呢它会调用服务层的接口
[01:26] 来进行业务处理最后保存数据库这每一层都有自己的数据传输对象用来接收数据用来传输数据给下一层这就是我们说的什么数据传输对象目前这三种我们都接触了一个是VL用于接收前端的一个是DTO用于在业务层进行接收数据处理的一个是entity实体类型用于在持久层来做处理的
[01:57] 看这个图呢大家看到有什么特点吗那我觉得刚才我大概都说明白了唯一有那么一点点特点的就是这儿就是在application应用层这儿呢它既可以用VO也可以用DTO大家看到了吗对有时候老师为啥呀VO大家理解VO是不是就是我们说面对前端用户界面给他提交过来的数据他用VO来接但为什么他又可以用DTO呢DTO不是业务层的东西吗
[02:28] 那我给你举个例子吧你比如说现在呢我们说要添加用户添加用户的时候呢Service层他肯定建一个添加用户的DTO没错吧那这个时候呢你会发现这个前端请求过来的添加用户的信息它是完全和DTO里边的这个字段属性完全一一对照的那你说我们还有必要建一个VU吗就没有了所以我们直接拿DTO来用就行了对
[02:56] 那你说老师那直接可以用entity不可以在这在应用层在前端这不可以你要注意这个应用层呢你只能用veo或者detail那么你不能用后边的这个什么entity这就是我们说的数据传输对象对那有时候又说了老师那如果我这用entity了咋弄我是不是这个代码就跑不通了
[03:19] 那当然不是你用那些数据也能接受也能传但是唯一一点的就是为什么我们每一个层都要用指定不同的这种对象类型你要知道这个意思我给你举个简单的例子比如说刚才我们做商户注册的时候各位我是不是在前端我专门定义了一个接收商户注册信息的一个view对不对那你看这里边我接收的数据
[03:48] 里边有一个叫验证码的key和验证码那我问你如果你用entity这个持久层的对象类型那它会有这个什么有这个验证码的key和验证码因为你根本就不把验证码的key和验证码保存到数据库所以说呀entity里边是不可能有这些信息的呀对不对entity里边是和数据库字段对应的能理解我的意思吧那你说老师那还不简单吗你在entity里头咱们
[04:17] 你没有吗你再加几个字段不就行了不行因为我们知道你现在用的这个entity对象是要严格和数据库字段一一对应的所以我们不要在这里边乱加东西那我们需要采用的方法就是每一层用每一层的对象唯一需要大家注意的就是这个前端这一块可能有些灵活建议你用VL如果DTO正好够你使用那你就不用定义端读的VL了这就是我们说的数据传输对象
[04:46] 好这里面描述的很清楚说这个应用层就是我们说的application你可以用DTO也可以用Vue我们建议你用Vue服务层用DTO持久层用entity好这就是我们说的数据传输对象的概念我们先理解一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解商户注册功能中数据传输对象（DTO）的定义、使用规范及在不同层级（应用层、服务层、持久层）的传输规则。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT内容，讲解数据传输对象（DTO）的三种类型：MerchantRegisterVO、MerchantDTO、entity，并附带一个应用层→服务层→持久层的流程图。
画面2：展示IDE中MerchantController.java的代码，其中包含一个用于测试的@GetMapping("/hello")方法和一个用于商户注册的@PostMapping("/merchants/register")方法，该方法中使用了merchantService.createMerchant(merchantDTO)。
画面3：IDE中展示项目结构，鼠标悬停在“Merchant”包上。
画面4：PPT内容，继续讲解数据传输对象的定义和用途。
画面5：PPT内容，展示本项目数据传输对象的规范，包括应用层、服务层和持久层的传输规则。
画面6：PPT内容，展示数据传输对象的规范，强调应用层使用DTO结尾的对象传输。
画面7：IDE中展示MerchantController.java的代码，其中包含一个用于商户注册的@PostMapping("/merchants/register")方法，该方法中使用了merchantService.createMerchant(merchantDTO)。
画面8：IDE中展示MerchantRegisterVO类的代码，其中包含多个字段，如mobile、username、password、verifyKey、verifyCode。
画面9：PPT内容，展示数据传输对象的规范，强调应用层使用DTO结尾的对象传输。
画面10：IDE中展示MerchantRegisterVO类的代码，其中包含多个字段，如mobile、username、password、verifyKey、verifyCode。
画面11：IDE中展示Merchant类的代码，其中包含多个字段，如merchantName、merchantNo、merchantAddress。
画面12：IDE中展示Merchant类的代码，其中包含多个字段，如idCardFrontImg、idCardAfterImg、username。
画面13：PPT内容，展示数据传输对象的规范，包括应用层、服务层和持久层的传输规则。
画面14：PPT内容，展示数据传输对象的定义和用途。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2代码：
```java
@PostMapping("/merchants/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    //校验验证码
    smsService.checkVerifyCode(merchantRegisterVO.getVerifykey(), merchantRegisterVO.getPhone());
    //传入商户信息
    MerchantDTO merchantDTO = new MerchantDTO();
    merchantDTO.setMobile(merchantRegisterVO.getMobile());
    merchantDTO.setUserName(merchantRegisterVO.getUserName());
    merchantDTO.setPassword(merchantRegisterVO.getPassword());
    merchantDTO.setVerifyKey(merchantRegisterVO.getVerifyKey());
    merchantDTO.setVerifyCode(merchantRegisterVO.getVerifyCode());
    //调用服务层
    return merchantService.createMerchant(merchantDTO);
}
```

画面7代码：
```java
@PostMapping("/merchants/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    //校验验证码
    smsService.checkVerifyCode(merchantRegisterVO.getVerifykey(), merchantRegisterVO.getPhone());
    //传入商户信息
    MerchantDTO merchantDTO = new MerchantDTO();
    merchantDTO.setMobile(merchantRegisterVO.getMobile());
    merchantDTO.setUserName(merchantRegisterVO.getUserName());
    merchantDTO.setPassword(merchantRegisterVO.getPassword());
    merchantDTO.setVerifyKey(merchantRegisterVO.getVerifyKey());
    merchantDTO.setVerifyCode(merchantRegisterVO.getVerifyCode());
    //调用服务层
    return merchantService.createMerchant(merchantDTO);
}
```

画面8代码：
```java
public class MerchantRegisterVO implements Serializable {
    @ApiModelProperty("商户手机号")
    private String mobile;
    @ApiModelProperty("商户用户名")
    private String username;
    @ApiModelProperty("商户密码")
    private String password;
    @ApiModelProperty("验证码key")
    private String verifyKey;
    @ApiModelProperty("验证码")
    private String verifyCode;
}
```

画面11代码：
```java
@TableField("MERCHANT_NAME")
private String merchantName;
@TableField("MERCHANT_NO")
private Long merchantNo;
@TableField("MERCHANT_ADDRESS")
private String merchantAddress;
```

画面12代码：
```java
@TableField("ID_CARD_FRONT_IMG")
private String idCardFrontImg;
@TableField("ID_CARD_AFTER_IMG")
private String idCardAfterImg;
@TableField("USERNAME")
private String username;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、4、5、6、9、13、14：PPT标题为“2.4.4 MapStruct对象转换”，子标题为“2.4.4.1 数据传输对象”。内容包括：
- 数据传输对象（DTO）的三种类型：MerchantRegisterVO、MerchantDTO、entity。
- 一个流程图：Application → DTO → Service (Dubbo) → Entity → Mapper。
- 本项目数据传输对象的规范：
  1. 应用层：如没有接口参数的特殊要求，应用层使用DTO结尾的对象传输，否则单独定义VO结尾的对象传输。
  2. 服务层：统一使用DTO结尾的对象传输。
  3. 持久层：统一使用Entity对象传输。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

