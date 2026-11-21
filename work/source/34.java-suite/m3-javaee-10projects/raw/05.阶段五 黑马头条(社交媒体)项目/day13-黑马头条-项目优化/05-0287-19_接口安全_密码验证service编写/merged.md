# 19_接口安全_密码验证service编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\19_接口安全_密码验证service编写【海量资源尽在 666java.com】.mp4
- 时长 6分48秒（音频 408s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去编写代码来去实现一下咱们验证的工作首先咱们要去先去查询当前的用户查询数据库中的数据然后这时候你首先要去准备一个MIPRMIPR其实已经准备好了就是咱们之前是用过的通过当前手机号去查询某一个用户这个地址有点问题咱们可以改一下MIPR下边的APP下边的他没问题好这么着
[00:28] 这是这个应有了你不用再去写了下面咱们去写当前的Service那Service咱们分两分两次写第一个是有一个专门验证的Service然后咱们再去写咱们的流利好吧这时候你可以先去打开我把它给关了然后你打开谁打开当前的logv服就这个然后在这去定义一个Service右键在这去创建一个类应该是一个接口是吧叫volidatevri
[01:01] 然后是Service它是一个接口这个呢就是咱们会设计种方式啊当然这个在实际的项目中呢有可能会选择一种咱们在这儿去可以去设置两三种是吧比如说咱们有迪圣加密迪圣加密是DES当然还有一个叫做ES那这个咱们并没有讲这并没有讲你可以在百度上去找一找那还有什么呢
[01:34] 咱们有一个叫做散列算法说的是MDU当然这里边有一个加盐加盐操作咱们是有一个Salt这个东西咱们就先说到这下面就去写它的方法这个方法刚才说了咱们要去有这种三个一个是DSC另外一个是MDU第三个是这种加盐的操作
[02:07] 嗯行那我们去设置下public然后呢第一个呢就我们要去返回一个boot里行不行啊统一返回就是boot里行啊一个呢是vali然后是dvalidatevalidate吧好吧desc我们都大写好吧ds啊好传达参数是啥呢参数的话是一个apuser好这是什么呢叫user好吧第二个啥呢第二还是apuser那为什么有两个apuser
[02:37] 叫dbdb啊就叫他好吧为什么是这样啊首先呢这个呢是从前台传过来的一个参数那这个呢是从数据库中查出来的这时候咱们主要是写当前的逻辑就可以啊好这样呢这是des验证验证啊然后下面还有两个啊咱们再去学习啊public然后都是返回boot的型啊如果说是密码一样的话咱们就返回住一样咱们就返回force啊
[03:11] 然后这个是叫validatevalidate谁呢叫md5好吧这个猜数也是一样apuserapuser这是user啊是dpuser这是db好下面还有一个啊还有一个这个是md5md5验证上面还有一个就是加盐的操作啊public然后boolean行然后是validate什么呢
[03:46] 有一个叫with fit参数还是这个还是这个东西就是APAP就是他第一个是那第二个还是他这是DB参数不一样这边这是MD5加盐验证MD5加盐验证那行那这个写完之后咱们就可以去写他的实现咱们在这再去创建一个类在这去拷贝一下
[04:25] 在这儿创建一个叫他impl好吧然后咱们就写具体的逻辑首先让他去实现当前那个validateservice让他被sprint管理Service好当然你也可以把它改为什么compound一样其实这个东西咱们就不再去说了然后首先第一个该怎么去验证
[04:55] 这东西比较简单咱们直接判断就可以了判断啥判断db.r有一个叫做getpassword然后是.ecos那ecos谁ecos.d.e.s.utils.r咱们有一个叫做encode然后是user.getpassword就是当前密码去加密一下最终的如果说他俩一样的话咱们就return可以了非常简单
[05:25] 下面还有两个咱们要再去设置一下这是第一个这是验证的一个DS那MD5其实这个思路是一样也是只是用的工具类不一样也是user.getpassword.ecosecos是谁还是MD5.utils.有一个encode也把它给加密这是怎样这个应该是叫做user.getpassword
[05:55] 这个咱们可以把它改成db其实一样你改前面改后面是一样的如果说他俩一样的话就return要不行的话就return force这还有一个来看一下这个其实也是调的方法来看一下首先是db.getPassword然后.equals这个是md5.utils.有一个叫做encode with start
[06:26] 一个是user.getSource第二个是db.getSite那这样就可以了如果他俩还是一样那这样的话咱们这个方法我写完了那写完之后咱们先断一下一会咱们再去写咱们的具体的登录的逻辑

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在登录服务中实现基于DES算法的密码校验功能，包括接口定义、实现类编写及工具类调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Mapper接口定义，包含注释“通过手机号查询用户”，并列出方法签名 `ApUser selectByAppPhone(String phone);`，以及对应的XML映射文件 `ApUserMapper.xml` 内容：
```xml
<select id="selectByAppPhone" resultMap="BaseResultMap">
    <include refid="Base_Column_List" />
    from ap_user where phone = #{phone} limit 1;
</select>
```

画面2：展示项目结构，选中模块 `Service-mycat`，并显示其内部的 `pom.xml` 文件。

画面3：展示 `ValidateService.java` 接口文件，定义了 `validateDES` 方法的签名。

画面4：在 `ValidateService.java` 中，为 `validateDES` 方法添加了 `@Override` 注解。

画面5：在 `ValidateService.java` 中，为 `validateDES` 方法添加了 `@Service` 注解。

画面6：在 `ValidateService.java` 中，导入了 `com.heima.login.Service.ValidateService`、`com.heima.model.user.pojos.ApUser` 和 `com.heima.utils.common.DESUtil`。

画面7：展示 `ValidateServiceImpl.java` 文件，定义了 `validateDES` 方法的实现。

画面8：在 `ValidateServiceImpl.java` 中，为 `validateDES` 方法添加了 `@Override` 注解，并开始编写校验逻辑。

画面9：在 `ValidateServiceImpl.java` 中，编写了 `validateDES` 方法的校验逻辑，使用 `DESUtil.encode` 对用户密码进行加密并比较。

画面10：在 `ValidateServiceImpl.java` 中，为 `validateWithSalt` 方法添加了 `@Override` 注解。

画面11：在 `ValidateServiceImpl.java` 中，为 `validateWithSalt` 方法添加了 `@Override` 注解，并开始编写校验逻辑。

画面12：在 `ValidateServiceImpl.java` 中，为 `validateWithSalt` 方法添加了 `@Override` 注解，并开始编写校验逻辑。

画面13：在 `ValidateServiceImpl.java` 中，为 `validateWithSalt` 方法添加了 `@Override` 注解，并开始编写校验逻辑。

画面14：在 `ValidateServiceImpl.java` 中，编写了 `validateWithSalt` 方法的完整校验逻辑，使用 `DESUtil.encodeWithSalt` 对用户密码进行加密并比较。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第2点中各画面的要点描述。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

