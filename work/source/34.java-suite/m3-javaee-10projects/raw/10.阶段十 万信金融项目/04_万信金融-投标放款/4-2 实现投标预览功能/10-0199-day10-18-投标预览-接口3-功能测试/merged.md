# day10-18-投标预览-接口3-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-18-投标预览-接口3-功能测试_【海量资源尽在 666java.com】.mp4
- 时长 3分14秒（音频 194s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才我们把接口三的功能开发完毕了大家看一下接口三也比较简单啊主要是查一下借款人的一些基本信息啊那大家注意这儿查是从哪查是从用户服务中心来查的啊这个大家一定要注意当然我们还做了一个小处理嘛查到这个呃用户的信息之后呢我们对身份证号是做了一个处理分别得到他的年龄啊生日啊以及性别对吧
[00:29] 最终呢我们把这些数据都封装到Borrower DTO对象里边然后返回了那咱接下来就进行测试呃这个测试的时候大家注意你要把这个谁呀Consumer这个微服给它启动起来啊因为咱们前两个接口在测试的时候主要是谁啊交易中心对吧那这个呢它涉及到用户中心啊所以说这个微服你也记得把它给启动起来启动起来之后呢我们哎还是在Swagger里边测试吧
[00:56] 那这时候你打开sweger的话应该打开的是对consumer的sweger我们刚才提到了嘛这个我们查询借款人信息是跟谁有关对用户中心所以说你看这边这个该启动服务都启动过了sweger也打开了咱接下来进行测试应该是哪个应该是这个应该是这个获取借款人用户信息那我们是不是try一下对不对他这边很简单就传过去这个用户的ID就行了
[01:29] 那咱看看咱们前面测试的时候呃咱当时是拿上哪个用户测的呀这俩是投标人啊我们现在测试的是借款人的信息借款人是谁呢那你要看这个标是谁发的吗谁发了这个标谁就是借款人吗对不对你看这是0657这个标底的ID对不对那我们去这个project的表里边找一找你看0657是不是然后呢你看这是呃那谁发的标啊
[02:00] 27啊consumer ID是27的这个人他发的标他就是这款人对不对那然后呢我们去这个谁啊去consumer这边找到consumer表然后看这个谁啊ID是27的对吧这个人是左丘对吧这是他的身份证号啊等等其他的一些信息那这还是提醒大家你在做这个测试的时候有些数据你需要自己造一下啊或者有些数据你需要自己改一改啊这是需要大家注意的
[02:30] 那咱们接下来就进行测试吧非常简单我们把这个谁啊他的ID是多少27是不是我们给他拿过来就行了然后呢执行咱们看一看状态码是200证明成功了是不是然后呢你看是左丘吧然后你看这是他的身份证号我们根据身份证号得到了他的什么年龄啊这个什么呀生日啊还有这个性别包括其他的信息
[02:57] 我们全部得到然后也返回了是不是将来我们是不是就可以给他展示到这个地方对不对原始接款人的基本信息这是哪个功能对接口三这个功能我们也测试完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个用户服务模块的代码实现、API 接口测试以及其在 P2P 平台业务流程中的角色。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示了 IntelliJ IDEA 中的项目结构，左侧是 `wanning2p` 项目下的 `wanning2p-consumer-Service` 模块。
- 右侧是 `ConsumerService` 类的代码，包含 `BeanUtils.copyProperties` 方法调用和 `getById` 方法。
- 代码片段：
  ```java
  BeanUtils.copyProperties(consumerDTO, borrowerDTO);
  Map<String, String> cardInfo = IDCardUtil.getlInfo(borrowerDTO.getlDNumber());
  borrowerDTO.setAge(new Integer(cardInfo.get("age")));
  borrowerDTO.setBirthday(cardInfo.get("birthday"));
  borrowerDTO.setGender(cardInfo.get("gender"));
  return borrowerDTO;
  private ConsumerDTO getById(Long id) {
      Consumer entity = getBvById(id);
      if (entity == null) {
          log.info("id为[{}]的用户信息不存在", id);
          throw new BusinessException(ConsumerErrorCode.E_140101);
      }
      return convertConsumerEntityToDTO(entity);
  }
  ```

画面 2：
- 显示了 IntelliJ IDEA 中的项目结构，聚焦在 `wanning2p-consumer-Service` 模块。
- 底部控制台显示了日志信息，包含 `NettyCleanSelector` 和 `SH4loggerFactory` 的信息。

画面 3：
- 与画面 2 类似，显示了 IntelliJ IDEA 的项目结构和控制台日志。

画面 4：
- 与画面 2、3 类似，显示了 IntelliJ IDEA 的项目结构和控制台日志。

画面 5：
- 显示了 Swagger UI 页面，标题为“万信金融P2P平台-用户服务API文档”。
- 页面显示了 API 列表，包括 `/consumers`、`/hello`、`/h1`、`/balances/{userNo}`、`/currConsumer/{mobile}` 等。

画面 6：
- 显示了 Swagger UI 页面，聚焦在 `/consumers` 接口。

画面 7：
- 显示了 Swagger UI 页面，聚焦在 GET `/my/borrowers/{id}` 接口，参数为 `id`，类型为 `Integer (64)`。

画面 8：
- 显示了 DBeaver 数据库客户端，连接到 `p2p_transaction` 数据库。
- 查询结果表 `t_user` 中显示了用户数据，包括 `CONSUMER_ID`、`USER_NO`、`PROJECT_ID` 等字段。

画面 9：
- 显示了 DBeaver 数据库客户端，连接到 `p2p_transaction` 数据库。
- 查询结果表 `project` 中显示了项目数据。

画面 10：
- 与画面 7 类似，显示了 Swagger UI 页面，聚焦在 GET `/my/borrowers/{id}` 接口。

画面 11：
- 显示了 Windows 桌面，多个窗口同时打开，包括 DBeaver、Swagger UI、WPS 文档、IntelliJ IDEA 等。
- 窗口标题显示了“万信金融-用户服务API文档”、“ApolloPortal”、“adminService”、“configService”等。

画面 12：
- 显示了 Swagger UI 页面，聚焦在 GET `/my/borrowers/{id}` 接口。
- 在参数输入框中输入了 `27`。
- 在响应区域显示了对应的 curl 命令和请求 URL。

画面 13：
- 显示了一个 P2P 平台的借款页面截图。
- 页面显示了借款信息，包括年利率 10%、期限 12 个月、总额 29,100 元。
- 页面底部有一个“授权出借”按钮。

画面 14：
- 显示了一个业务流程图。
- 流程图从左到右依次为：`浏览器/APP` → `交易中心` → `用户服务` → `存管通道服务` → `存管系统`。
- 流程图中的步骤包括：获取借款人信息、保存借款人信息、通过银行生成签名、保存交易信息、创建投标信息、更新交易状态等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上述要点中完整抄录）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- PPT 标题：无明确标题，但画面 13 和 14 显示了 P2P 平台的借款页面和业务流程图。
- 架构图/流程图结构：
  - 画面 14 的流程图：
    - `浏览器/APP` → `交易中心`（步骤 1.1-1.4）
    - `交易中心` → `用户服务`（步骤 1.5-1.6）
    - `用户服务` → `存管通道服务`（步骤 2.1-2.2）
    - `存管通道服务` → `存管系统`（步骤 2.5-2.6）
    - `存管系统` → `存管通道服务`（步骤 2.7-2.8）
    - `存管通道服务` → `用户服务`（步骤 2.9-2.10）
- 表格数据：
  - 画面 8：`t_user` 表数据，包含 `CONSUMER_ID`、`USER_NO`、`PROJECT_ID` 等字段。
  - 画面 9：`project` 表数据，包含 `PROJECT_ID`、`PROJECT_NAME`、`PROJECT_STATUS` 等字段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

