# day12-2-满标放款-接口1-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-2-满标放款-接口1-功能实现2_【海量资源尽在 666java.com】.mp4
- 时长 19分20秒（音频 1160s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 业务层的接口上咱定义好之后呢接下来我们就应该去实现类当中实现功能但是这呢先给大家强调一点咱这个功能呢实现起来是非常非常复杂的啊为什么因为我们前面说过这个接口一啊它是咱们整个业务的一个什么样路口那么在接口一里边实现功能的时候它自然就包含什么接口二接口三还有什么呀接口四所以说呢这个代码编写起来整体会比较复杂它把这四个阶段全部
[00:30] 包含进来那咱先找一找咱们的这个右层的实现类啊这已经报错因为咱刚才是不是在接口里边新增了一个方法吗好咱把这个方法给它生成一下在这对不对那咱前面刚才说过了啊就是说这个整个代码编辑起来比较复杂所以说咱分成四个阶段第一个阶段就是什么呀这个你看讲义或者说看这个什么呀看这个图都行
[01:05] 你看咱在讲义的这个需求分析这一块也非常明确的提出来第一个阶段就是生成什么呀放款明细这是第一阶段第二阶段是要干什么呀第二阶段就是放款第三阶段就是修改状态最后一个阶段呢最后一个阶段就是请求还款啊你看一下咱的讲义第二阶段放款对吧修改状态最后一个阶段就是启动还款咱
[01:54] 这个代码也是拆分成这个四个阶段四块咱一个一个来先说第一阶段第一个阶段我们说了目的就是干什么呀对生成放款明细啊这里边据来说呢都有哪些这个明细信息要生成啊呃主要就是这个一个是标的的信息标的的信息还有什么信息啊投标的信息主要是这俩有了这俩的话我们就可以生成这个什么呀
[02:32] 放缓明细了啊所以说咱一个一个来吧那首先怎么得到这个标的信息啊这个标的信息简单多了对不对这儿传过来的不就是标的的什么呀ID嘛对不对那根据ID获取标的信息怎么写啊咱有一个方法叫什么呀应该很熟了对get by ID这儿传进来ID我们这儿就得到了一个什么对象project对象这不是什么就有了
[03:00] 对标底信息就有了然后呢我们还需要得到什么呀投标信息啊就是都谁投了这个什么呀标对不对这个投标信息我们全部都要查出来这有可能很有可能是一个什么呀集合嘛因为我们说了一个标底可以由多个人进行什么呀对进行投标所以这应该是一个集合那其实说白了就是查什么信息啊其实说白了就是查这个表查tender表tender表查这个表
[03:35] 查查数据呢怎么查呢我们有一个条件就是根据标底的ID我只查某个标底的这个什么呀相当于就是投标记录了啊说完了那这个查询呢也比较简单我们先用query warp先构造什么呀查询条件没有一个query warp那我们的条件我们刚才说了是不是就一个吗就是query warp点怎么封装就是那个那个那个什么呀标底的ID等于多少对不对
[04:07] 那就是我们用Lambda的写法Lambda.EQ吧是不是EQ哪个字段呢哪个字段呢就是我们的投标表当中的哪个字段对标底的ID这个值呢不就是什么呀这个参数嘛第一个参数嘛就标底的ID嘛这是不咱就把条件给它封装好封装好之后呢咱进来执行查询怎么查呢因为这是投标信息表所以我们需要通过
[04:37] tender map他有一个方法应该叫select list对不对然后呢把这个谁啊query wrap封装好的这个条件放进去那他就根据这个标的ID进行了投标信息的一个什么呀查询那他查出来的就是一个什么呀集合封装成了什么呀tender投标记录吗tender list
[05:04] 那你看咱目前这个投标信息啊或者投标记录咱也就得到得到之后呢我们就可以拿着这两块信息来去干什么呀生成这个放款明细看看这个怎么整那到底啥是放款明细啊其实这个放款明细很简单它就是把这个标底信息以及跟它相关的投标信息然后呢再连同这个什么呀佣金相关的这套东西呢它给你封装到
[05:35] 一起就是封装到一个类一个对象当中然后一起给你展示出来其实非常像像这个什么非常像咱们在超市买的东西你付完钱是不是会给你打印一个购物小票那个小票不就是你的购物明细吗上面你都买什么东西多少钱等等等等其实咱现在要的就是这么一个东西放款明细那这里边的话我们准备这样我们准备把这个生成放款明细呢这块代码抽出来放到封装到一个方法里边
[06:06] 然后在这呢进行调用就行那咱就在下边吧publicpublic我先起个名字吧发个名啊gneat生成的意思对吧l o a n r e q u r e q u e s t就这么一个方法这个方法就是专门来生成放款明信了那它怎么生成呢我们刚才说了它是不是需要标底信息对吧所以说我们这有个参数就是
[06:42] project他还需要什么信息啊投标信息对吧投标记录嘛那个集合嘛一个集合啊tendertender list吧还有就是什么呀佣金啊这个是非常非常重要的佣金这是我们要的参数啊我们在这个方案里边呢一会呢就是就会根据这三个参数的信息呢来生成什么呀放缓明细说白了就是把他们封装到一个类当中那封装到哪个类里边呢
[07:19] 我们这提前准备好了一个类大家看一下叫Lun request咱看他应该考到什么地方啊API depository是吧好我们给他拿过来API depository他是放到这了啊针过来啊他说他已经存在了是吧啊那应该是我之前考过了那考过的话我们就直接打开看一眼你看这里边都封上了什么信息啊
[07:58] 什么信息你看是不是有佣金啊标的的编码啊流水号啊对象的ID啊你看这些信息其实是不是我们刚才传过来那几个参与员应该都包含了有对不对然后呢这里边还包含一个什么呀Long Detail Request我们看这里边都有啥这里边呢就是一个啊放款金额还有一个什么呀要留意号那这些信息呢我们也都可以从那三个业务当中给他不是那三个业务就是三个参与当中获取出来这咱大概熟悉一下
[08:29] 接下来的话咱就是要在这个方法里边从这里边干什么呀取我们想要的数据然后给它封装成什么类型的一个对象返回呀就是non什么呀request所以说呢我们这个方案的返回值就是non request我把这个注视也加一下咱这个方案是干嘛的呀是根据什么呀标的和投标信息
[09:03] 生成什么呀给放款那这里边这个代码具体怎么写呢咱一起来看一下其实这里边代码说白了就是怎么着啊就是就是给这个对象的属性给他干什么付值他要啥值你想办法获取到然后费他就是这么一个过程咱一个一个来吧比如说他要什么呀要什么东西呀他是不是要要一个什么ID呀
[09:36] project number 呀还有什么平台用金呢咱一个一个来呗先把这几个这个这个值先给他对不对先封装进去再说那我们这边就这样吧先直接是要 new一个对象啊law requestnew not request然后开始往里边进行封装首先封装这个标底的 id 吧他就那几个属性标底的 id 怎么封装啊我们调他的这个
[10:12] 一个叫setter id吧是不是刚才大家看到setter对id这个id其实就是标的的id标的id从那来啊那参数不就是那个标的吗他的什么呀get id方法就得到了这不是封装进一个吗然后再封装什么我们再封装刚才大家看到是吧还有一个什么平台佣金吗这个都是比较简单的咱快速封装一下平台佣金封装平台佣金
[10:43] 直接调这个对象的set方法然后呢这个值不就是咱这个第三个参数是不是呃这个地方的话我们最好是处理一下啊这个平台用机呢我们最好判断它我若为空吧不为空的话我给它转换成还得转换成什么呀big decimal类型的啊你看它这里呀是不是big decimal类型的所以说这儿的话我最好是加一个判断非空的一个判断因为这儿传进来的是字符串类型啊
[11:16] 那我这就是string什么呀youtube.is什么呀not blank对吧不为空的情况下哎我才把这个值呢给它封装到这个对象里边但是呢你直接封装不行你得给它转换成什么类型big decimal类型哎这样就可以了是不是这是我们把平台用金给它封装进去了然后还有啥挑个简单的标底的编码这简单然后接下来我们封装
[11:51] 封装标的编码那直接就封装了啊调用他的set方法set谁啊叫project number对吧那这个值从哪来呢还是从第一个参数project对象里边直接调用他的get方法不就拿到手了吗对不对这是封装了几个了三个了哪三个呀这两个加上最后一个对吧那咱接下来开始封装这个请求流水号吧
[12:23] 这个请求流量呢我们需要新生成一个呃为啥新生成呢大家看一下这个图我们现在是不是在汇总这个什么呀呃标题和投标信息成形成这个什么方法明信那这个呃方法明信生成完之后呢我们将来是要通过非远程请求然后发到什么地方发给这个谁呀存款代理服务呢是不是大家看这个图对不对选中呢既然呢它呃是一次交易啊或者说是一次请求
[12:51] 我们就需要生成一个什么呀request number咱们之前发标投标是不是都是如此那咱就直接生成一个这个请求流水号直接掉他的什么方法叫注释吧我们这呢是封装请求流水号load request点叫set什么呀request number
[13:19] 这个情侣号是怎么生成的大家有印象吗我们是不是之前写的有工具类吗叫code什么呀对code numberutil啊他有个方法叫get number然后这里边是不是要传过来一个code prefix code这么一个对象是不是就是他了那我们这个要的是不是就是这个什么呀code request的prefix啊这个大家应该都有印象是不是请求流水号的什么呀请注意那这是第几个我们也封装好了
[13:53] 对第四个啊就是这个请求流水号那目前你看看我们应该是这四个是不是全部封上好就剩一个什么呀对放很明细就是这个一个集合吗details这里边我们重点是要得到这里边的值这里边有值的封上人对象放到集合里边就行了啊这边都啥呢我刚才说了一个是放款金额一个是啊也是一个什么呀也有流水号啊那其实说白了这里边主要是要得到这个什么呀放款其实说白了就是这样啊
[14:22] 你看我们呃刚才是不是查出来一个图标记录封装成利似的集合了他这个地方啊大家注意他这个地方是不是也是利一个利似的集合但是他这个集合里边他只要什么呀他只要这个tender表里边的两个数据两个数据哪两个数据呢你刚才看到就这俩一个是图标金额嘛其实放在那就是图标金额还有就是那个那个要流水号啊其实就是这个tender表里边的一个这个谁要问你找找啊一个这个值
[14:53] 就这个投标镜了还有一个那个流水号呢流水号这里边应该有流水号没有吗我们找一找啊应该是在这儿啊request number也就是说呢他其实主要就是要一个request number和这个什么呀投标镜就要打下的东西所以我们接下来要做的事就是这样我们要便利这个集合从这个对象里边是不是只取咱刚才说的那两个值
[15:30] 然后取出来之后呢封装成这个对象然后再把这个对象呢给他放到这个什么呀就存到这么一个集合里面就行就这个意思那咱接下来就开始编码了啊那咱提前先创建一个集合呗这个集合的范型刚才大家看到就是这个law and detail request我们先把这个空集合先给他造出来我们就叫短一点吧details吧newreleased我要便秘谁啊
[16:02] 对我家其实要便利的就是这个tender list便利的过程当中呢从这个对象里面取两个值封装到谁啊law and detail request然后再存到这个集合里面就OK了那咱就用这个lambda的这种写法来进行便利是这个fetch嘛等一下咱以前写过了啊这里边怎么写啊便利的过程当中我们取出来的是不是每一个tender对象吧然后取出来这个tender对象之后呢我们要做的事就是
[16:35] 从这里边取两个数据然后把它存到这个什么呀Long detail request 里边就OK了所以我们接下来需要创建这个对象等于NEO创建完之后呢我们就取一个值存一个值呗一个是叫set谁呀对投标进额投标进额就是从这个什么呀tender对象里边来取就行了还有就是呃这个谁呀那个那个流流水号是不是
[17:08] 那也是从tender里边取这个get request number就给大家看是不是我们就要这个两两个值你把它取出来封装好之后呢我们需要把这个对象呢给它添加到什么呀集合里面你看这个封装是不是就搞定了对不对那最后的话你就需要把这个集合给它封装到learn request里边这样它的setter方法集合是这个然后呢把details这个集合给它放进去
[17:41] 这就是最终是不是就全部搞定了对不对然后呢返回这个money request完事啊我刚才给大家说了嘛这个什么呀放缓明信就是把标的信息啊还有投标记录当中的一部分信息对不对还有这个什么呀平台佣金啊给他汇总到一起封装到一个叫lone request的这个对象里面然后这个将来我们可以干什么呀发给谁啊
[18:07] 发表存款代理服务或者说也可以返回到前面的页面展示一下都可以啊这就叫放款明细那我们目前的话啊这个放名气这个功能就实现了那在这儿我是不是需要调用一下才行啊对不对那就是生生成什么呀对放款明细然后呢直接是不是就调用就行了那把这个project的对象呀还有这个谁呀
[18:37] tender list还有这个什么呀对这个平台拥机呢作为三个参数呢就传回去传去之后呢它是不是有返回值吗大家有印象吧对它封装到一个learn request这么一个对象里边那咱接下来是不是要接收一下因为一会要用的啊那就是learn request就这样就行对吧那目前的话咱这是第几阶段的待会就搞定了这是第几段
[19:09] 第几阶段一就是第几阶段第一阶段第一阶段但全部搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在项目中通过 Service 层代码，将项目和投标信息封装成 LoanRequest 对象，用于后续的贷款审批流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 DepositAgentApiAgent 接口，定义了多个 REST 映射方法，如 createProject、userAutoPreTransaction、confirmLoan 等。
画面 2: 展示了 ProjectServiceImpl.java 中 loansApprovalStatus 方法，其中调用了 getById 方法获取项目信息。
画面 3: 展示了 LambdaQueryWrapper 的构造方法和常用方法，如 lambda、eq、like、orderDesc 等。
画面 4: 展示了 ProjectServiceImpl.java 中 loansApprovalStatus 方法，其中创建了 QueryWrapper 并设置了查询条件。
画面 5: 展示了 LoanRequest.java 类的定义，包含 details、projectNo、requestNo、commission 等字段。
画面 6: 展示了 LoanRequest.java 类中 projectNo 和 requestNo 字段的定义。
画面 7: 展示了 ProjectServiceImpl.java 中 generateLoanRequest 方法，其中调用 setCommission 设置佣金。
画面 8: 展示了 ProjectServiceImpl.java 中 generateLoanRequest 方法，其中调用 setProjectNo 设置项目编号。
画面 9: 展示了 ProjectServiceImpl.java 中 generateLoanRequest 方法，其中调用 setRequestNo 设置请求流水号。
画面 10: 展示了 ProjectServiceImpl.java 中 generateLoanRequest 方法，其中调用 CodeUtil.get() 生成请求流水号。
画面 11: 展示了 DQLyng Professional 64 的数据库管理界面，显示了 pgy_transaction_1 数据库的表结构。
画面 12: 展示了 ProjectServiceImpl.java 中 generateLoanRequest 方法，其中创建了 LoanDetailRequest 对象并设置属性。
画面 13: 展示了 ProjectServiceImpl.java 中 generateLoanRequest 方法，其中调用 setDetailsList 设置 LoanDetailRequest 列表。
画面 14: 展示了 ProjectServiceImpl.java 中 loansApprovalStatus 方法，其中创建了 QueryWrapper 并设置了查询条件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package cn.itcast.wanxingzp.transaction.agent;

import ...

@FeignClient(value = "depository-agent-Service")
public interface DepositoryAgentApiAgent {
    @PostMapping(value = "/depository-agent/1/createProject")
    public ResResponse<String> createProject(ProjectDTO projectDTO);

    @PostMapping("/depository-agent/1/user-auto-pre-transaction")
    ResResponse<String> userAutoPreTransaction(
            UserAutoPreTransactionRequest userAutoPreTransactionRequest);

    @PostMapping("/depository-agent/1/confirm-loan")
    ResResponse<String> confirmLoan(LoanRequest loanRequest);

    @PostMapping("/depository-agent/1/modify-project-status")
    ResResponse<String> modifyProjectStatus(ModifyProjectStatusDTO modifyProjectStatusDTO);
}
```

画面 2:
```java
@Override
public String loansApprovalStatus(Long id, String approveStatus, String commission) {
    // 1. 生效说明
    // 2. 标的信息
    Project project = getById(id);
    // 3. 投标信息
    // 4. 启动还款
}
```

画面 3:
```java
public class LambdaQueryWrapper<T> {
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean condition;
    private Function<T, ?> column;
    private Collection<?> coll;
    private boolean

