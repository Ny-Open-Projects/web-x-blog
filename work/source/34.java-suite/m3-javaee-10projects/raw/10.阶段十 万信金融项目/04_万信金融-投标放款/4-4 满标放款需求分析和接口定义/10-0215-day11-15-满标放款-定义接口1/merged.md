# day11-15-满标放款-定义接口1

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-4 满标放款需求分析和接口定义
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-4 满标放款需求分析和接口定义\day11-15-满标放款-定义接口1_【海量资源尽在 666java.com】.mp4
- 时长 7分48秒（音频 469s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把满标放款这个业务的需求分析还有业务流程详细的做了一个分析那接下来呢根据之前的套路我们就需要把整个这个业务当中所涉及到的这四个接口全部给它定义出来然后呢我们就可以分成几个阶段呢对拆分成四个阶段一块一块的把整个
[00:30] 所有的功能全部实现那按照顺序的话咱应该先定义哪个接口啊对第一个接口啊接口一大家看一下这个图呃在这个图里边呢很清晰的展示出来接口一呢是不是咱整个满标放款业务总的一个入口大家看一下是不是你看咱整个这个满标放款这个业务是不是就是前端就发了这一个清照是不是啊然后后续出了一大堆的业务然后
[01:02] 在最后进行了什么样响应对不对所以说呢这个接口一呢是咱整个满标放款业务的对总的一个入口那接口一呢这里边主要涉及到就是哪个微服啊交易中心啊大家看图说话啊交易中心那么接口一里边我们具体都要实现哪个功能呢哎大家看这个时序图啊你现在哎有没有总结出来我怎么看这个时序图啊比方我们在定义接口的时候你再看
[01:33] 这个实际图的时候呢你就注意啊你就看这根柱子就行了对不对那接口一套实现的功能就在这个图的这个柱子里啊就交易中心这根柱子里啊你比如说这就要他实现贵总标的信息对吧形成方案联系还有什么功能他要往存款代理服务发这个什么呀分析请求对不对他要接收这个呃存款代理服务返回的消息然后进行数据的更新然后这样呢他还要发请求给
[02:02] 从来带你服务然后到这呢还要根据这个结果更新什么样状态对吧然后呢这儿又发请求到哪这是到对还款服务对不对启动这个还款计划然后最终呢响应给谁啊前端说这根柱子啊就是我们接口医药实现的功能啊所以大家要慢慢积累啊或者总结啊如何去看这个时序图
[02:30] 那咱接下来直接就定义这个接口啊就是第一个接口那我们是不是还是要找到谁啊对translation API啊在这个接口当中呢我们再新增一个方法那咱先通过讲义大概的了解一下这个方法大家看一下这是方法名是不是然后呢一共有几个参数啊对三个参数啊反而值呢还是rest response范形呢是字符串类型
[02:59] 咱大概了解过之后呢咱接下来就找到这个接口开始编写这个方法transcation API是这样吧好那这个方法名的话咱要跟讲义保持一致名字比较长对吧叫learns approval什么呀status一共有几个参数呀对三个参数来咱一个一个写一下第一个参数呢就是ID什么ID啊标底的ID你要审核的这个什么呀
[03:31] 标的来的你要审核谁吗这个审核哪个标的第二个参数字块类型表示这个审核的状态就是通过还是不通过啊sttus最后一个参数第三个参数也是字符串类型表示这个平台佣金啊commi ssl是三个参数然后呢这个方案还有一个返回值仍然是rest response类型的这里边的范围形呢是字符串最终的一个结果
[04:06] 这是咱把这个方法呢快速的定义了一下然后呢我们从讲义里边把这一堆注释给他拿过来格式上咱稍作调整啊然后呢我们把这三个参数都表示什么意思呢给加上去ID我们刚才说了就表示什么呀标底的ID就是你要审核哪个标底这个标底的ID我们得传过来第二个参数就是什么呀审核状态是吧这个其实跟当时咱们那个新标
[04:47] 审核的那个是一样的就是前端会弹出一个段框嘛上面是什么通过还是什么呀不通过嘛就是审核的一个结果一个状态第三个参数我们说是叫平台什么呀佣金什么叫平台佣金平台佣金说白了就是咱们这个万行金融P2P平台它的一个收入的一个来源对吧其中之一很重要的一个来源那也就是说呢我们这个平台是不是在撮合交易双方就是借款人和什么呀
[05:18] 投标人来达成这个交易我们相当于是一个平台对吧我们给你提供了相关的一些服务那我就要收取什么呀佣金我可以从每一笔交易当中都抽取什么呀这个佣金好比我们现实生活当中这个中介嘛比如说你租房子对吧房东和租客之间你通过一个一个中介机构来达成这个租房的这个交易那么中介是不是要从这个交易当中来收取这个什么呀对他们说这个服务费也行或者佣金也行其实就是一个意思
[05:47] 那我们万新金融P2P平台类似的是不是也是一个一个中介一个平台是不是所以他要收取这个佣金的啊那我们现在开发的功能是不是审核标的这个买标放款这个状态是不是已经走到买标放款了那这个时候基本上可以说是这个交易已经达成了对吧那这个时候我们就要收取什么呀对收取佣金了嗯这是咱们第一个接口就定义好了那接下来呢我们把啊
[06:18] 给他来个空时线先放了这边是不是已经包错了对吧来咱们把这个方法呢给他先生成一下稍等一下有点卡啊好在这已经生成生成完之后我们对照讲义把相关的一些注解对吧给他补充一下主要还是sweggersmvc啊相关的一些注解我们直接给他拿过来用一下就行啊还有就是这个地方这几个参数对不对
[06:55] 这边你要注意啊第三个参数我们并不是通过这传过来这个平台用金不在这传那他从哪来呢咱到时候用的时候再说我们可以搞成配置了有很多种方式那大家看一下下吧这个Swagger这一块的这个注解我就不再说了啊我们注定关注什么呀这注定关注spin mvc比如说这个啊仿路径你看这里边是不是通过RESTful的形式啊在路径里边就把第一个参数以及什么呀
[07:27] 对第二个参数的值传过来然后通过这个pass verb这个注解就赋给了这两个参数我们刚才说最后一个参数呢我们通过别的方式给是右翔这个值我们忘了改对吧这个值我们得改一下这是目前吧咱就把第几个接口定义好了对接口1就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解“万能金服”项目中交易中心的放款与还款接口定义及代码实现，包含业务流程图、接口文档和代码示例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“万能金服”业务流程图，包含“调用前端API”、“交易中心”、“存管代理服务”、“结算服务”、“存管系统”等模块，以及各模块间的交互流程（如“1.1-1.2”、“1.3”、“1.4”等步骤）。
画面2：继续展示业务流程图，聚焦“交易中心”与“存管系统”之间的交互，如“1.4”步骤中“存管系统”返回“放款成功”状态。
画面3：继续展示业务流程图，聚焦“交易中心”与“结算服务”之间的交互，如“1.5”步骤中“结算服务”返回“结算成功”状态。
画面4：继续展示业务流程图，聚焦“交易中心”与“存管系统”之间的交互，如“1.6”步骤中“存管系统”返回“放款失败”状态。
画面5：展示PPT文档“3.2.1 接口定义”，其中“3.2.1.1 交易中心放款接口(接口①)”部分，列出接口描述和接口定义，包括“在TransactionApi接口中新增loansApprovalStatus方法”。
画面6：展示IDEA开发环境，项目结构为“wanning2p_apollo”，包含“wanning2p-account-Service”、“wanning2p-transaction-Service”等模块。
画面7：展示PPT文档“3.2.1 接口定义”，其中“6) 交易中心请求还款服务启动放款”部分，以及“TransactionApi”接口定义的代码片段。
画面8：展示IDEA开发环境，打开“TransactionApi.java”文件，显示“loansApprovalStatus”方法的定义。
画面9：展示PPT文档“3.2.1 接口定义”，其中“2. 接口定义”部分，详细说明“在TransactionApi接口中新增loansApprovalStatus方法”和“在TransactionController类中实现该方法”。
画面10：展示IDEA开发环境，打开“TransactionApi.java”文件，显示“loansApprovalStatus”方法的定义。
画面11：展示IDEA开发环境，打开“TransactionController.java”文件，显示“loansApprovalStatus”方法的实现。
画面12：展示IDEA开发环境，打开“TransactionController.java”文件，显示“loansApprovalStatus”方法的实现，其中包含“@ApiImplicitParams”注解。
画面13：展示PPT文档“3.2.1 接口定义”，其中“在TransactionController类中实现该方法”部分，以及“TransactionController.java”文件的代码片段。
画面14：展示IDEA开发环境，打开“TransactionController.java”文件，显示“loansApprovalStatus”方法的实现，其中包含“@ApiImplicitParams”注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```text
3.2.1 接口定义
3.2.1.1 交易中心放款接口(接口①)
1) 接口描述
2) 交易中心根据的信息生成还款明细
3) 交易中心收到放款成功结果后，更新投标状态为：已放款
4) 交易中心请求存管代理服务修改的状态
5) 交易中心请求还款服务启动放款
6) 交易中心请求还款服务启动放款
在TransactionApi接口中新增loansApprovalStatus方法：
/**
 * 审核标的满标放款
 * @param id
 * @param approveStatus
 * @param commission
 * @return
 */
RestResponse<String> loansApprovalStatus(Long id, String approveStatus, String commission);
```

画面7：
```text
6) 交易中心请求还款服务启动放款

在TransactionApi接口中新增loansApprovalStatus方法：
/**
 * 审核标的满标放款
 * @param id
 * @param approveStatus
 * @param commission
 * @return
 */
RestResponse<String> loansApprovalStatus(Long id, String approveStatus, String commission);
```

画面8：
```java
/**
 * 用户投标
 * @param projectInvestDTO
 * @return
 */
RestResponse<TenderDTO> createTender(ProjectInvestDTO projectInvestDTO);

/**
 * 审核标的满标放款
 * @param id
 * @param approveStatus
 * @param commission
 * @return
 */
RestResponse<String> loansApprovalStatus(Long id, String approveStatus, String commission);
```

画面9：
```text
在TransactionApi接口中新增loansApprovalStatus方法：
/**
 * 审核标的满标放款
 * @param id
 * @param approveStatus
 * @param commission
 * @return
 */
RestResponse<String> loansApprovalStatus(Long id, String approveStatus, String commission);

在TransactionController类中实现该方法：
@ApiOperation("审核标的满标放款")
@ApiImplicitParams({
    @ApiImplicitParam(name = "id", value = "标的id", required = true,
            dataType = "long", paramType = "path"),
    @ApiImplicitParam(name = "approveStatus", value = "标的的状态", required = true,
            dataType = "string", paramType = "path"),
    @ApiImplicitParam(name = "commission", value = "平台佣金", required = true,
            dataType = "string", paramType = "query")
})
```

画面11：
```java
@ApiOperation("用户投标")
@ApiImplicitParam(name = "projectInvestDTO", value = "投标信息",
        required = true, dataType = "ProjectInvestDTO", paramType = "body")
@PostMapping("/my/tenders")
public RestResponse<TenderDTO> createTender(@RequestBody ProjectInvestDTO projectInvestDTO) {
    TenderDTO tenderDTO = projectService.createTender(projectInvestDTO);
    return RestResponse.success(tenderDTO);
}

@Override
public RestResponse<String> loansApprovalStatus(Long id, String approveStatus, String commission) {
    return null;
}
```

画面12：
```java
@ApiOperation("审核标的满标放款")
@ApiImplicitParams({
    @ApiImplicitParam(name = "id", value = "标的id", required = true,
            dataType = "long", paramType = "path"),
    @ApiImplicitParam(name = "approveStatus", value = "标的的状态", required = true,
            dataType = "string", paramType = "path"),
    @ApiImplicitParam(name = "commission", value = "平台佣金", required = true,
            dataType = "string", paramType = "query")
})
@PutMapping("/m/loans/{id}/projectStatus/{approveStatus}")
public RestResponse<String> loansApprovalStatus(@PathVariable("id") Long id, @PathVariable("approveStatus") String approveStatus, String commission) {
    return null;
}
```

画面14：
```java
@ApiOperation("审核标的满标放款")
@ApiImplicitParams({
    @ApiImplicitParam(name = "id", value = "标的id", required = true,
            dataType = "long", paramType = "path"),
    @ApiImplicitParam(name = "approveStatus", value = "标的的状态", required = true,
            dataType = "string", paramType = "path"),
    @ApiImplicitParam(name = "commission", value = "平台佣金", required = true,
            dataType = "string", paramType = "query")
})
@PutMapping("/m/loans/{id}/projectStatus/{approveStatus}")
public RestResponse<String> loansApprovalStatus(@PathVariable("id") Long id, @PathVariable("approveStatus") String approveStatus, String commission) {
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“万能金服业务流程图”，架构图包含“调用前端API”、“交易中心”、“存管代理服务”、“结算服务”、“存管系统”等模块，各模块间通过箭头连接，表示交互流程。
画面5：PPT标题为“3.2.1 接口定义”，其中“3.2.1.1 交易中心放款接口(接口①)”部分，列出接口描述和接口定义。
画面7：PPT标题为“3.2.1 接口定义”，其中“6) 交易中心请求还款服务启动放款”部分，列出接口定义。
画面9：PPT标题为“3.2.1 接口定义”，其中“在TransactionApi接口中新增loansApprovalStatus方法”和“在TransactionController类中实现该方法”部分，列出接口定义和实现方法。
画面13：PPT标题为“3.2.1 接口定义”，其中“在TransactionController类中实现该方法”部分，列出实现方法。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

