# day03-18-传统登录实现方式-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-5 实现传统登录方式并分析问题
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-5 实现传统登录方式并分析问题\day03-18-传统登录实现方式-定义接口_【海量资源尽在 666java.com】.mp4
- 时长 7分2秒（音频 422s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 注册功能实现完之后呢咱接下来该实现啥功能大家说对大家自然就会想到注册完就是要进行什么呀登录要不然我注册干嘛对不对我注册就是为了将来能够进行什么呀对登录其实不管是注册还是咱接下来要实现登录其实这个业务大家应该都是很熟悉的业务也熟悉其实代码大家也比较熟悉你看注册无非它主要就是增删改查当中的什么呀增嘛最终的效果增
[00:33] 那么登录呢登录应该是增删改查当中的什么呀对查询其实说白了登录就是查一查数据库查一查表看看你提交过来的账号和密码是否什么呀存在或者说是否正确那如果账号密码都存在就是登录成功对吧有一个不存在或者不正确它就是登录什么呀失败这个业务非常的简单咱看这个表比如这个account
[01:04] 这咱们账户表对不对这里边有账号对吧你看这是咱加密户的这个密码对吧等等那你看我将来无非就是查一下这个表比如说如果我们用手机号登录的话无非就是判断一下这个手机号和这个密码哎我在这个表里边查一下它是否存在存在的话那就是登录成功否则就是登录什么呀失败啊又非常简单而且呢我们把这种实现方式呢是称之为是传统的实现方式那传统的实现方式大家最熟
[01:35] 也最简单那咱接下来呢就是先按照这种传统的这种实现方式先把登录功能给实现了那首先跟之前的套路是一样的首先也是先定义什么呀接口对那我们找到API工程这功能应该是放到Occount这边的啊因为它是统一账户中心吧找到这个接口在这里边呢我们接下来需要再
[02:05] 定义一个方法用来实现什么功能没错登录功能先写注释吧好我们实现对用户登录那咱接下来先定义方法发明还用想吗这就不用想了吧那一定是login对不对那你接下来要思考的就是这个方案有没有参数有没有返回值呢先说参数吧有没有参数那一定得有吧
[02:40] 登录嘛你一定是要提交过来或者说前段一定要传过来什么呀登录信息嘛最起码就是账号和什么呀密码对不对那我们在这呢也给大家提供了一个DTO类专门封装这个登录信息了这个类呢我们还是去这个公共类这个文件夹里边找大家看应该是谁啊对应该是他啊二个countloginDTO点加看名字就知道好我们control c
[03:10] 然后给他粘过来粘到这你看这是咱注册时候用的那个DTO对不对好Ctrl V把它粘过来粘过来之后你看这有注释他说封装账户登录的信息这里边你看是不是有用户名手机号密码等等反正咱需要东西这里边都已经有了我这个参数就准备用这个类了就是accaccountaccount叫什么
[03:40] login DTO就用它来进行封装这是参数那有没有返回值那一定得有那跟上边是一样的对没错跟这是一样也是用的rest response当然这个范形我们用的是account DTO因为这里边的返回的数据或者说属性会更多一些所以我们一般是这样你看你也观察到套路一般前端往后端传数据我们是不是都是用
[04:14] 这种专门设计的一个DTO对象来封装数据对吧那么你在增杀改查完了之后一般会返回这么一个DTO对象来封装数据所以说这是咱这里边玩的一个套路咱把这个注释给补一下吧at termterm呢就是这个参数作用呢就是封装用户登录信息对吧
[04:45] 返回值呢我就写个at return吧留到这at r1 t u rn好就这样这是接口咱们定好定好之后呢还是跟以前一样咱顺手把Controller里边这个方法来一个空实现先放了嗯Controller应该是book count里边的Controller找一找他现在应该要报错了对不对我们把这个方法来一个空实现扔到这儿有点卡啊稍等
[05:30] 好方法已经生成了生成之后呢咱还像往前一样把一些注视啥的或者一些注解啥的给加上去这个我就不再自己敲了啊这些东西嗯大家应该都比较熟悉我就从奖励里面直接沾过来整个这一块吧我就全考过来了看到这对这时候呢你看一看啊看一看这里边的东西呃这块是不是sweiger注解对吧啊这个逗号是不是变成中文的我改一下
[06:10] 你从pdf讲义里边要粘东西的话一定要注意这些细节然我建议你最好是敲一敲这块是不是死了个诸姐我就不再说了这是不是他的这个访问路径吧啊访问路径啊L证明啥咱以前提过呀你看在这L证明这个请求并不是直接暴露给前端去访问的那至于他将来是有谁访问的到时候再说啊这就是一个请求路径咱先这么先写一下
[06:40] 另外提醒大家注意这儿这儿这儿这儿是不是也得加这个东西这个很容易忘了我们要求前端发过来的数据点是什么格式对JSON格式所以说我们要加request body住进那么到目前为止咱们登录功能的接口定义这一块我们就搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 Spring Boot 项目中，如何在 AccountController 中定义并实现用户登录接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示数据库中 p2y_account 表的结构，包含 id、mobile、password 等字段，用于存储用户账户信息。
画面 2：展示 IntelliJ IDEA 中项目结构，包含多个微服务模块，如 account-Service、consumer-Service 等，当前选中的是 gateway-server。
画面 3：在 AccountAPI.java 文件中，定义了注册接口 register，参数为 AccountRegisterDTO。
画面 4：在 AccountAPI.java 文件中，光标位于 login 方法的起始位置，准备编写登录接口。
画面 5：在 AccountAPI.java 文件中，光标位于 login 方法的起始位置，准备编写登录接口。
画面 6：在 AccountAPI.java 文件中，通过智能提示选择 AccountLoginDTO 类型，准备编写登录方法。
画面 7：在 AccountAPI.java 文件中，完成 login 方法的定义，参数为 AccountLoginDTO。
画面 8：在 AccountAPI.java 文件中，完成 login 方法的定义，参数为 AccountLoginDTO。
画面 9：在 AccountController.java 文件中，定义了获取手机验证码的接口 @GetMapping("/sms/{mobile}")。
画面 10：在 AccountController.java 文件中，定义了用户注册接口 @PostMapping("/accounts") 和登录接口 @PostMapping("/accounts/session")。
画面 11：展示 PPT 内容，标题为“在AccountController中实现login方法”，并展示了登录接口的代码示例。
画面 12：在 AccountController.java 文件中，高亮显示了登录接口 @PostMapping("/accounts/session")。
画面 13：在 AccountController.java 文件中，高亮显示了登录接口 @PostMapping("/accounts/session")。
画面 14：在 AccountController.java 文件中，高亮显示了登录接口 @PostMapping("/accounts/session")。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```sql
id
mobile
password
```

画面 3：
```java
/**
 * 注册 保存信息
 */
@Param accountRegisterDTO
@return
RestResponse<AccountDTO> register(AccountRegisterDTO accountRegisterDTO);
```

画面 4：
```java
login();
```

画面 6：
```java
AccountLoginDTO (cn.ictast.wanningzp.api.account.model)
```

画面 7：
```java
login(Account);
```

画面 8：
```java
/**
 * 用户登录
 */
@Param accountLoginDTO 登录用户登录信息
@return
RestResponse<AccountDTO> login(AccountLoginDTO accountLoginDTO);
```

画面 9：
```java
@ApiOperation("获取手机验证码")
@ApiImplicitParam(name = "手机号", dataType = "String")
@GetMapping("/sms/{mobile}")
```

画面 10：
```java
@ApiOperation("用户注册")
@ApiImplicitParam(name = "accountRegisterDTO", value = "账户注册信息", required = true,
        dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping("/accounts")
public RestResponse<AccountDTO> register(@RequestBody AccountRegisterDTO accountRegisterDTO) {
    return RestResponse.success(accountService.register(accountRegisterDTO));
}

@ApiOperation("用户登录")
@ApiImplicitParam(name = "accountLoginDTO", value = "登录信息", required = true,
        dataType = "AccountLoginDTO", paramType = "body")
@PostMapping("/accounts/session")
@Override
public RestResponse<AccountDTO> login(AccountLoginDTO accountLoginDTO) {
    return null;
}
```

画面 11：
```java
@ApiOperation("用户登录")
@ApiImplicitParam(name = "accountLoginDTO", value = "登录信息", required = true,
        dataType = "AccountLoginDTO", paramType = "body")
@Override
public RestResponse<AccountDTO> login(@RequestBody AccountLoginDTO accountLoginDTO) {
    return null;
}
```

画面 12：
```java
@ApiOperation("用户登录")
@ApiImplicitParam(name = "accountLoginDTO", value = "登录信息", required = true,
        dataType = "AccountLoginDTO", paramType = "body")
@PostMapping("/accounts/session")
@Override
public RestResponse<AccountDTO> login(AccountLoginDTO accountLoginDTO) {
    return null;
}
```

画面 13：
```java
@ApiOperation("用户登录")
@ApiImplicitParam(name = "accountLoginDTO", value = "登录信息", required = true,
        dataType = "AccountLoginDTO", paramType = "body")
@PostMapping("/accounts/session")
@Override
public RestResponse<AccountDTO> login(AccountLoginDTO accountLoginDTO) {
    return null;
}
```

画面 14：
```java
@ApiOperation("用户登录")
@ApiImplicitParam(name = "accountLoginDTO", value = "登录信息", required = true,
        dataType = "AccountLoginDTO", paramType = "body")
@PostMapping("/accounts/session")
@Override
public RestResponse<AccountDTO> login(AccountLoginDTO accountLoginDTO) {
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 11：
标题：在AccountController中实现login方法
内容：
- 改变中国教育，我们正在行动
- 黑马程序员
- 北京市昌平区建材城西路金隅办公楼一层 电话：900-618-9090
- 2. 功能实现
- 在AccountService中新增登录接口login:
- ```java
  @ApiOperation("用户登录")
  @ApiImplicitParam(name = "accountLoginDTO", value = "登录信息", required = true,
          dataType = "AccountLoginDTO", paramType = "body")
  @Override
  public RestResponse<AccountDTO> login(@RequestBody AccountLoginDTO accountLoginDTO) {
      return null;
  }
  ```

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

