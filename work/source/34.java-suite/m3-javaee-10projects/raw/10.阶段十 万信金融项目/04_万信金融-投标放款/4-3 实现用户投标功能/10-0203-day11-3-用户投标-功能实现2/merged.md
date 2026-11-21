# day11-3-用户投标-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-3 实现用户投标功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-3 实现用户投标功能\day11-3-用户投标-功能实现2_【海量资源尽在 666java.com】.mp4
- 时长 5分37秒（音频 337s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们做了一些准备工作对吧第一个是我们检查阿卜罗上我们有没有配置这个最小图标金额还有一个呢是咱实现了一个功能啊就是查询当前用户的账户余额这个功能那针对这个查询账户余额这个功能我们接下来还要再做补充为什么要做补充呢接下来大家看一看咱目前开发的这个
[00:30] 查询账户余额这个功能你看这这个访问路径这是不是L开头的对不对大家应该有印象我们之前说过了L开头的这种服务是给谁去请求去使用的呀是给我们的后端微服务对吧比如说交易中心对吧就可以往这发请求来获取什么呀账户余额那前端能往这发请求获取
[01:00] 这个账户余额吗不行啊那L开头的这个服务啊他是专门给后端微服务去请求去访问的但是呢我们的前端的确也有这种什么需求我们的前端他也会发请求要要什么东西要当前用户的账户余额啊那那你你在前端登录成功之后你是可以查自己的这个什么呀余额信息带啊是不是这很正常的一个功能吗我得看看哎
[01:30] 我这个账户还有多少钱是不是所以说前端也有这个需求那么我们接下来干脆专门针对前端啊也实现一个类似的这种功能那大家看一看你看这啊你说考虑到前端呢他也需要获取这个什么账户者啊因此呢我们在这个consumer API这个介绍当中呢我们专门提供一个供前端去使用的这么一个方法
[01:58] 功能都一样也是获取账户的什么呀余额的但是呢这个呢是专门给什么呀前端去访问的那我们找到这个接口在这个接口里边呢我们再新增一个方法Consumer的是不是你注意跟上面做对比啊你看他俩的区别只在于这个什么呀一个有参数一个什么呀没有参数而这个是给谁去用呢我们刚才说了给
[02:31] 也对后端微服务去访问的而咱新增了这个方案是给谁啊前端去访问的其实功能基本上都是一样的那新增了一个方案之后呢我们接下来是不是要回到control的里边来实现这个方法他这应该已经报错了我们把这个方法先生成一下好稍等一下啊我们生成到这儿了对不对生到这儿之后呢正好跟他做一个对比啊我们说他俩区别就是一个有参数一个没参数啊但实际上都是用来获取
[03:06] 当前用户的账户余额的那这个实验起来就简单了呀我们这个查询账户余额的功能是不是都封上了这个发里是不是那我们在这也可以进行什么呀调用啊然后把当前登录用户的这个有用的number是不是发给他就行了这就完事了这个功能很简单你看我们的讲义大家看一眼你看我们是不是也是直接调呢这个方法但是想办法需要想办法吧
[03:37] 当前登录用户的这个user number获取到认识他是不是就行了那怎么获取当前登录用户的这个user number你看上面来我们通过这个security youtube这个工具类是不是就可以得到当前登录用户得到他手机号我们以前是不是实现过一个方法叫get by mobile是不是就可以查出来这个当前登录用户的信息这个信息里边就包含有什么呀对user number啊所以说呢这个比较简单咱接下来写一下啊我解好代码我们先使用这个工具类
[04:08] 导到当前登录用户然后进一步导到他的什么呀手机号然后呢我们就可以调用要从咱之前实现的一个方法叫get by什么目标根据手机号来查询什么呀对用户的信息那这个方法返回值是consumer DTO对不对我们就接收一下吧consumer DTO那在这个DTO对象里面是不是就包含有那个谁啊user number我们调用他的
[04:39] 对给特方法我们就得到得到他之后呢我们是不是接下来代码就跟这儿是一样的对吧我们直接调封装好的这个方法就可以查询到用户的账户余额了把它给直接对包起来就OK了所以说吧这是咱们专门针对什么呀前端啊他的这个查询用户账户余额的这个需求我们又补充了一块代码
[05:09] 这儿别忘了是不是还少什么东西啊还得配一个访问路径呢这个可不能忘了跟奖励保持一致那将来呢我们在测试的时候你就会发现了前端的确会往这发请求来获取当前登录用户的账号余额然后获取到这个余额之后它会展示到这个前端的这个界面这是这一块吧我们做了一个补充

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在万向金融项目中，实现ConsumerAPI接口的“获取用户可用余额”功能，涉及在ConsumerController中定义方法、在ConsumerAgent中暴露远程调用接口、以及在ConsumerService中调用底层数据访问层。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了课程PPT内容，标题为“2.1 预案：用户中心接口改造”。
- 内容A：检查Apollo是否配置最小投资金额，显示配置项：min.investment.amount = 100.0。
- 内容B：实现查询用户余额功能，在ConsumerAPI接口中新增查询当前余额的方法，代码片段：
  ```java
  /**
   * 获取当前登录用户余额信息
   * @param userNo 用户编码
   * @return
   */
  RestResponse<BalanceDetailsDTO> getBalance(String userNo);
  ```
- 内容C：在ConsumerController类中实现该方法，代码片段：
  ```java
  @Override
  @ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
  @GetMapping("/balances/{userNo}")
  public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
  }
  ```

画面2：
- 展示了ConsumerAPI接口中新增的getBalance方法的实现代码，代码片段：
  ```java
  String url = depositoryURL + "/balance-details/" + userNo;
  BalanceDetailsDTO balanceDetailsDTO = new Request.Builder()
      .url(url)
      .build()
      .execute()
      .body().string();
  if (response.isSuccessful()) {
      balanceDetailsDTO = JSON.parseObject(response.body().string(), BalanceDetailsDTO.class);
      return RestResponse.success(balanceDetailsDTO);
  } else {
      log.warn("调用存管系统失败", url, e);
      return RestResponse.validFail("获取失败");
  }
  ```

画面3：
- 展示了IDEA中ConsumerAPI接口的代码，其中包含获取用户信息和获取用户余额的方法。

画面4：
- 展示了IDEA中ConsumerAPI接口的代码，其中包含获取用户信息和获取用户余额的方法，鼠标选中了获取用户余额的方法。

画面5：
- 展示了IDEA中项目结构，选中了ConsumerAPI接口。

画面6：
- 展示了ConsumerController类中定义的获取用户信息、获取借款人信息、获取用户可用余额的方法。

画面7：
- 展示了ConsumerController类中定义的获取用户可用余额的方法，代码片段：
  ```java
  @Override
  @ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
  @GetMapping("/balances/{userNo}")
  public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
      return getBalanceFromDepository(userNo);
  }
  ```

画面8：
- 展示了课程PPT内容，标题为“2.1 预案：用户中心接口改造”。
- 内容D：在ConsumerApiAgent接口中新增getBalance方法，供交易中心远程调用查询当前余额，代码片段：
  ```java
  @GetMapping("/consumer/1/balances/{userNo}")
  public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo)
  ```
- 内容E：考虑到前端也需要获取账户余额，所以在ConsumerAPI接口中新增供前端调用的查询当前余额的方法，代码片段：
  ```java
  /**
   * 获取当前登录用户余额信息
   * @param userNo 用户编码
   * @return
   */
  RestResponse<BalanceDetailsDTO> getBalance();
  ```
- 内容F：在ConsumerController类中实现该方法，代码片段：
  ```java
  /**
   * 获取当前登录用户余额信息
   * @param userNo 用户编码
   * @return
   */
  RestResponse<BalanceDetailsDTO> getBalance();
  ```

画面9：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  return RestResponse.success(consumerService.getBalanceFromDepository(userNo));
  ```

画面10：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  @Override
  @ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
  @GetMapping("/balances/{userNo}")
  public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
      return getBalanceFromDepository(userNo);
  }
  ```

画面11：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  public RestResponse<BalanceDetailsDTO> getBalance() {
      return getBalanceFromDepository(consumerDTO.getUserNo());
  }
  ```

画面12：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  public RestResponse<BalanceDetailsDTO> getBalance() {
      return getBalanceFromDepository(consumerDTO.getUserNo());
  }
  ```

画面13：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  public RestResponse<BalanceDetailsDTO> getBalance() {
      return getBalanceFromDepository(consumerDTO.getUserNo());
  }
  ```

画面14：
- 展示了ConsumerController类中获取用户可用余额的方法，代码片段：
  ```java
  public RestResponse<BalanceDetailsDTO> getBalance() {
      return getBalanceFromDepository(consumerDTO.getUserNo());
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 获取当前登录用户余额信息
 * @param userNo 用户编码
 * @return
 */
RestResponse<BalanceDetailsDTO> getBalance(String userNo);
```

画面2：
```java
String url = depositoryURL + "/balance-details/" + userNo;
BalanceDetailsDTO balanceDetailsDTO = new Request.Builder()
    .url(url)
    .build()
    .execute()
    .body().string();
if (response.isSuccessful()) {
    balanceDetailsDTO = JSON.parseObject(response.body().string(), BalanceDetailsDTO.class);
    return RestResponse.success(balanceDetailsDTO);
} else {
    log.warn("调用存管系统失败", url, e);
    return RestResponse.validFail("获取失败");
}
```

画面6：
```java
@Override
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
@GetMapping("/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
    return getBalanceFromDepository(userNo);
}
```

画面8：
```java
/**
 * 获取当前登录用户余额信息
 * @param userNo 用户编码
 * @return
 */
RestResponse<BalanceDetailsDTO> getBalance();
```

画面9：
```java
return RestResponse.success(consumerService.getBalanceFromDepository(userNo));
```

画面10：
```java
@Override
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
@GetMapping("/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
    return getBalanceFromDepository(userNo);
}
```

画面11：
```java
public RestResponse<BalanceDetailsDTO> getBalance() {
    return getBalanceFromDepository(consumerDTO.getUserNo());
}
```

画面12：
```java
public RestResponse<BalanceDetailsDTO> getBalance() {
    return getBalanceFromDepository(consumerDTO.getUserNo());
}
```

画面13：
```java
public RestResponse<BalanceDetailsDTO> getBalance() {
    return getBalanceFromDepository(consumerDTO.getUserNo());
}
```

画面14：
```java
public RestResponse<BalanceDetailsDTO> getBalance() {
    return getBalanceFromDepository(consumerDTO.getUserNo());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
- PPT标题：2.1 预案：用户中心接口改造
- 内容A：检查Apollo是否配置最小投资金额，显示配置项：min.investment.amount = 100.0。
- 内容B：实现查询用户余额功能，在ConsumerAPI接口中新增查询当前余额的方法。
- 内容C：在ConsumerController类中实现该方法。

画面8：
- PPT标题：2.1 预案：用户中心接口改造
- 内容D：在ConsumerApiAgent接口中新增getBalance方法，供交易中心远程调用查询当前余额。
- 内容E：考虑到前端也需要获取账户余额，所以在ConsumerAPI接口中新增供前端调用的查询当前余额的方法。
- 内容F：在ConsumerController类中实现该方法。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

