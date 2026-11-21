# 12.前后端集成测试-前期准备

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\12.前后端集成测试-前期准备【海量资源尽在 666java.com】.mp4
- 时长 12分2秒（音频 722s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面呢我们进入前后端集成测试前后端分离开发的过程是前端工程师和服务端工程师按照接口文档约定各自开发各自的功能那么当一个完整的模块开发完成或者说一个系统开发完成的时候呢那么双方呢会在约定的时间集中进行集成测试那其实简单理解呢就是
[00:27] 把前端工程部署起来把我们的服务端工程部署起来然后开始测试我们开发的所有的业务功能和业务流程那比如之前我们开发的商户注册自制申请支付参数配置这些功能我们之前在服务端开发的过程呢都是使用Postman来进行测试对吧那那个呢仅限于服务端接受的测试那接下来呢我们会把这个前端工程也部署起来
[00:56] 然后通过前端来请求我们服务端的这些接口好那么接下来呢我们做一些准备工作那么这个准备工作呢这里面大概有以下几点我们说这个如果前后端进行机程测试或者说正式的环境下的话那用户呢需要登录从前端登录对吧登录成功之后呢前端要展示当前用户的信息那么这时候呢他就需要来调用服务端给他提供的
[01:26] 获取登录用户的商户信息对简单理解呢就可以理解为就是当前登录用户是哪个商户呢那么前端的调用这个接口呢就把当前登录这个商户的信息拿到然后呢在前端展示另外一块内容呢就是要解析Token那么在之前我们没有集成SaaS没有和前五端进行连条的时候呢当初我们是通过一个测试工具类
[01:55] 来生成了一个临时的Token大家应该还有印象是吧那现在呢我们已经接入了SaaS那么并且呢我们现在呢要和前后团进行测试那用户肯定是通过前端来登录来请求我们的这个SaaS认证系统所以这个时候呢我们就需要各个微服务呢就需要去解析前端给我们发过来的一个正式的Token
[02:24] 那之前我们也有解析Token从Token当中拿上户ID对吧那那个时候呢我们用的这个工具类大家有印象但是现在呢我们需要把这个工具类替换一下只需要替换这个工具类啊那么我们说各个接口当中去获取从Token当中获取上户ID的那个代码是不需要替换的只需要把这个工具类替换一下另外还有一些就是因为还是
[02:52] 我们刚才说的嘛要解析正式Token你解析的过程当中呢这里面还需要我们增加一个接口就是根据租户ID来查询商户信息大概就是这些准备工作啊好了那么接下来我们就开始来做那第一个事呢是当那个商户登录成功前端要请求我们的接口来拿当前商户的信息对吧所以这时候呢我们来我们需要写一个接口
[03:19] 大家看这个代码应该也能看得懂上面是我们商户服务的代码下面是商户平台应用的代码商户平台应用对外暴露http对吧你看这时候你看这个url你看前面有一个卖意思也就是获取当前这个用户他的信息那这里边大家看到他是没有参数的对不对那这个时候通过这一行代码你能能够理解
[03:45] 那么这个是从Token当中来解析出来商户ID对吧然后再根据商户ID来查询这个商户信息所以呢在我们的Service里头啊我们去定义一个根据商户ID来查询商户信息的接口那这个呢就是Double接口对吧在商户服务里面来找一下往前翻啊看一下这个接口当中有没有啊应该好像有了你看大家看到了吗
[04:18] 这是之前实现的对吧我们应该是最前边那好那这个接口大家看一下正确性吧因为最毕竟这个代码早了你看现在我们要根据ID来查询商户的信息拿到了一个entity对吧而现在呢你看是不是要转成DTO那其实这块代码的话我们基本上可以使用对我们有一个叫什么呀merchant converter是吧
[04:47] 然后呢Entity哎错了啊Entity转成DTO你把这个放进去是不是就行了这个接口就完工了这是商户服务提供的W接口是吧那另外还有一个就是在商户平台应用提供HTTP接口那这个呢我们也需要来写一下看好往上吧看一下啊
[05:14] 这是根据ID这是当初我们测试的啊现在我们要写这个接口啊那这个接口呢各位它呢是不需要参数的刚才你也看见了对吧然后呢它最终返回的肯定是商户的信息对吧那么大家看这个URL那这里面我就直接把这个讲义上面的URL拷过来好注意看放到这儿这是不是就是我们说的获取当前登录用户的这个商户信息啊
[05:43] 那这里边我们是不是就需要从Token当中来拿到获取商户的ID对吧那这个时候就用这个工具类了这是商户ID就拿到了然后呢调用Service就刚才我们写的这个Double的接口然后呢去根据商户ID来查这个接口也完工了大家看到了吗
[06:14] 那么大家看还有什么这个接口一会儿咱们做完先不用测试啊一会儿因为这个接口很简单一会儿我们直接挂上前端呢来测这个接口就行后面还有一个解析Token解析Token这一块呢我们刚才说了嘛因为现在是正式Token了原来这个工具类呢它是来解析我们当初的什么临时的Token是吧所以这个工具类需要替换一下啊那看一下讲义看一下啊
[06:42] 我给大家在资料文件夹下边我就准备了替换的代码那边有一个正式的你看是不是有一个解析正式TokenUtil然后这里面你看这就是我们说的这两个一个工具类一个login user还有一个这个是干啥用语我给你说我们先把它拿到这来考到我们商户平台应用下面
[07:12] 对吧考进去啊考进去之后呢大家看这个工具类这个工具类还报错以后我要补一个方法以后再说看到这个工具类大家可以看到它是要做什么事呀你看原来的方法我就屏蔽了你看见吗原来是直接从token当中来解析出这个商户ID那现在呢现在它会先解析出一个什么对租户ID一个租户ID有时候老师啥是租户ID
[07:43] 我们知道一个商户是不是就对应SaaS系统的一个租户啊那这个你也知道这个用户是通过SaaS系统登录的对吧那登录完了之后SaaS系统会把当前这个商户所对应的租户ID给这个前端返回来前端呢去请求的时候他传过来的是什么对租户ID这个租户ID就在这个Jason当中那在Jason当中呢他就拿到了这个什么租户的ID
[08:09] 拿到诸号ID这时候呢就要调用一个方法根据诸号ID来查询这个对应的商务信息一会我们把这个方法补一下就OK了这里边你看好这儿因为它要调用double服务的接口你看这里边它是不是需要从这个我们的SpringSpring的这个上下文当中来拿这个bin大家看到吗所以这个呢是我们也考进去的一个这个Spring上下文的一个构建的一个bin好所以其实
[08:39] 我们刚才考进去这三个东西都是为了干嘛来解析Token然后呢从Token当中解析出租户ID根据租户ID来查询商务信息另外还有一个Filter这个Filter呢也是需要我们去拷贝的一个东西因为你要知道现在是正式的Token了那么正式的Token呢这里边呢它就会需要怎么弄啊就是每次请求的时候呢进行一个Filter的
[09:07] 拦截你看这里边呢它有一系列的拦截包括还是教研token啊解析token所以我们根据这个需要啊我们呢这么弄我们就把这个类呢直接考到我们的这个common项其实这些东西都是我们在搭建这个系统的基础工程的时候呢
[09:30] 是用的编写的一些类因为我们根据教学需要原来最初是一个临时的套文现在呢我们就要改成正式套文那就需要这些刚才我考进去的这些工具类好那么刚才你也看到了在这个工具类当中它就需要一个接口根据租户ID来查询商户的信息所以这里边各位我们仍然在商户服务的这个Service当中
[10:00] 我们来把这个根据租户ID对吧根据租户ID有人说老师那根据租户ID那怎么查询这个商户的信息呢其实这个数据库大家还有印象吗在商户表当中其实是有一个租户ID的对不对所以我们完全可以让他去查询商户表然后呢根据租户ID来查询商户的信息对吧
[10:29] 好那接下来我们把这个借口直接实现一下吧那这怎么做呀其实很简单吧应该是merchant Mapper然后现在他要去查查谁呀直接查slack的1那拿到slack的1大家注意怎么做呀你看是不是要拼装条件这时候是用传进的租户ID来和我们说的这个商户表当中的租户ID做一个匹配其实查询的这个方法比较简单
[10:59] 但是呢你得知道商户表有一个租户ID是吧好那这里边呢我们说你要用slag1这里边我们就用一个lamb是吧然后呢这里边还跟以前方法一样只不过现在条件变成了什么就变成了我们要根据租户的ID刚才我们是不是根据商户ID现在根据租户ID来查一个商户对吧
[11:26] 好这样的话我们就拿到了这个商户的信息最后呢你就用我们的converter把它转一下对OK这样我们这个接口也就完工了这个接口呢同样一会儿呢我们再进行测试啊好那到这儿为止我们的前期准备工作我们开发了一个根据ID查询商户信息根据租户ID查询商户信息然后还有呢解析token等等
[11:56] 这三步就完成了一会我们再做部署前端好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解商户平台应用如何通过集成测试获取商户信息，涉及服务层、控制器层代码及Token解析的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT，章节为“1.1 测试需求”，说明本次测试是前后端联调测试，重点是商户平台应用获取登录商户信息。
画面2：PPT内容延续，展示在MerchantServiceImpl中定义queryMerchantById方法，用于根据商户id查询商户信息。
画面3：IDE中展示MerchantServiceImpl.java代码，包含queryMerchantById方法，其中调用merchantMapper.selectById，并将查询结果转换为MerchantDTO。
画面4：IDE中展示MerchantServiceImpl.java代码，光标在return merchantDTO;语句处，下方有注释说明该方法用于注册商户成功后获取商户信息。
画面5：IDE中展示MerchantController.java代码，包含getMyMerchantInfo接口，用于获取当前用户的商户信息。
画面6：IDE中展示MerchantController.java代码，光标在getMyMerchantInfo方法中，注释说明从token中提取商户id。
画面7：IDE中展示SecurityUtil.java代码，包含getMerchantId方法，用于从请求头的Authorization中解析并提取商户id。
画面8：IDE中展示SecurityUtil.java代码，光标在getMerchantId方法中，下方有getUserId方法的代码片段。
画面9：IDE中展示MerchantController.java代码，光标在getMyMerchantInfo方法中，注释说明从token中提取商户id。
画面10：文件资源管理器中显示TokenAuthenticationFilter.java文件，用于解析token。
画面11：IDE中展示TokenAuthenticationFilter.java代码，包含从userMap中获取权限信息并设置到request的逻辑。
画面12：IDE中展示MerchantServiceImpl.java代码，光标在queryMerchantByTenantId方法中，展示查询商户信息的SQL语句。
画面13：IDE中展示MerchantServiceImpl.java代码，光标在queryMerchantByTenantId方法中，展示使用LambdaQueryWrapper进行条件查询的代码。
画面14：PPT内容，章节为“1.2.2 服务端解析Token”，说明在进行功能测试时需要修改SecurityUtil及TokenAuthenticationFilter.java文件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@Override
public MerchantDTO queryMerchantById(Long merchantId) {
    Merchant merchant = merchantMapper.selectById(merchantId);
    MerchantDTO merchantDTO = MerchantConvert.INSTANCE.entity2dto(merchant);
    return merchantDTO;
}
```

画面3：
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

画面5：
```java
@GetMapping(value = "/my/merchants")
public MerchantDTO getMyMerchantInfo() {
    //从token中提取商户id
    Long merchantId = SecurityUtil.getMerchantId();
    return merchantService.queryMerchantById(merchantId);
}
```

画面6：
```java
@GetMapping(value = "/my/merchants")
public MerchantDTO getMyMerchantInfo() {
    //从token中提取商户id
    Long merchantId = SecurityUtil.getMerchantId();
    return merchantService.queryMerchantById(merchantId);
}
```

画面7：
```java
public class SecurityUtil {
    @Test
    public static Long getMerchantId() {
        HttpServletRequest request = (HttpServletRequest) RequestContextHolder.currentRequestAttributes().getRequest();
        String jsonToken = request.getHeader("authorization");
        if (StringUtils.isEmpty(jsonToken) || !jsonToken.startsWith("Bearer ")) {
            throw new RuntimeException("token is not as expected");
        }
        jsonToken = jsonToken.substring(7);
        jsonToken = EncryptUtil.decodeStringBase64(jsonToken);
        JSONObject jsonObject = JSON.parseObject(jsonToken);
        return jsonObject.getLong("merchantId");
    }
}
```

画面8：
```java
public static LoginUser getUser() {
    ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder.currentRequestAttributes();
    if (servletRequestAttributes == null) {
        HttpServletRequest request = servletRequestAttributes.getRequest();
    }
}
```

画面11：
```java
Map<String, List<String>> userMap = (Map<String, List<String>>) request.getAttribute("user_authorities");
if (userMap == null) {
    log.error("json-token中该用户（）没有权限信息", tenantId);
    throw new BusinessException(code: 99991, desc: "调用服务方json-token中没有权限信息");
}
return userMap;
```

画面12：
```java
public MerchantDTO queryMerchantByTenantId(String tenantId) {
    merchantMapper.selectOne(new LambdaQueryWrapper<Merchant>().eq(Merchant::getTenantId, tenantId));
    return null;
}
```

画面13：
```java
public MerchantDTO queryMerchantByTenantId(String tenantId) {
    merchantMapper.selectOne(new LambdaQueryWrapper<Merchant>().eq(Merchant::getTenantId, tenantId));
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“1 集成测试”，子标题“1.1 测试需求”，内容说明本次测试是前后端联调测试，重点是商户平台应用获取登录商户信息。
画面2：PPT标题为“1.2.1 商户平台应用获取登录商户信息”，内容说明在MerchantServiceImpl中定义queryMerchantById方法，根据商户id查询商户信息。
画面14：PPT标题为“1.2.2 服务端解析Token”，内容说明在进行功能测试时需要修改SecurityUtil及TokenAuthenticationFilter.java文件。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

