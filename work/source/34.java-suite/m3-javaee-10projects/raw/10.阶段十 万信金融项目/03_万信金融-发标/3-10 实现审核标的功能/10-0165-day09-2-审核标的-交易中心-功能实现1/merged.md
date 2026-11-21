# day09-2-审核标的-交易中心-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-10 实现审核标的功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-10 实现审核标的功能\day09-2-审核标的-交易中心-功能实现1_【海量资源尽在 666java.com】.mp4
- 时长 9分56秒（音频 596s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢咱们把审核标的这一块的两个接口全部定义好那咱接下来就开始实现功能那么功能实现这一块呢我们也分成两块是不是跟接口一一对应嘛一个是交易中心这一块我们要实现一个功能还有就是存款代理服务这边也要实现功能这个功能我们再明确一下交易中心这边其实是收到前端发过来这个审核的这个结果之后呢稍作数据的处理
[00:31] 那接下来他就要通过飞应对吧通过飞应啊把标的信息给他发送到存款代理服务这一块而存款代理服务这边是不是也要做一些处理处理完之后呢他也要把标的信息给发送到哪要发送但是他是发送到哪银行那这所以这个地方呢要提醒大家注意啊2.2这一块是通过飞应因为交易中心和存款代理服务是不是都是咱P2P项目当中的微服务对不对
[01:01] 但是注意了存款代理服务在发送标的信息到银行那边的时候这可不是用飞影啊因为银行那边可不归咱管他这呢是要通过发送什么HTB请求的啊一个直连接口所以这两个地方都要发送这个什么呀标的信息但是用的技术可是不一样的啊这需要大家注意的呃那咱们接下来按照顺序吧先搞定哪一块我们先搞定交易中心这一块的功能
[01:31] 交易中心这块刚才咱们说了他是不是需要通过飞运发起一个远程访问到从外代理服务因此我们这样是不是需要做一个准备工作就是在交易中心这边定义一个飞运代理是不是咱看一看讲义吧因为这个东西对于大家说都非常简单了咱之前在开发这个登录开户的时候这种情况很常见所以你看我们在交易中心这边首先就是定义一个飞运代理
[01:59] 他的作用就是将来我们要通过他往存贯代理微服那边发送什么呀对标底信息这是fine client这是那个访问路径访问路径这一块呢再次提醒大家注意一个细节咱以前这个吃过这个亏入了这个坑是不是就这一层的这个这个路径要写上以前我就忘记了我是不是直接又从这写但实际上这也得加上这是那个微服的基本访问路径嘛其他的这些东西是不是跟那个接口
[02:31] 就扛出来那边那你直接站过来就行了这是这个非硬接口吧非硬代理我们需要提前做这么一个准备工作那咱找到这个谁啊交易中心是这吧对不对新建一个接口咱跟蒋毅名字保持一致然后呢这个代码呢我就不再编写了啊这个对于他来说都是很熟悉的一些东西啊好这是接口呢咱就编好这是非硬代理接口
[03:13] 那咱接下来的话就接着实现功能我们接下来功能是不是要去哪个层啊是不是应该是先是数据访问层但是数据访问层呢咱之前已经搞过了那咱就直接去哪对右层Service这一块也是先在右层定一个接口然后再去对实现功能右层接口当中的方法跟Controller里边基本上是一样的来看一下是不是还是一个
[03:48] 标的来的一个结果是不是反而值就是一个字符串我们把这块代码来拷贝到右层作为业务层当中接口当中的一个新的一个方法就是审核标的这块就不在过头说了我们接下来重点要编写的代码就是右层实现类当中方案里面的代码是不是那咱接下去实现类里边该报错了是不是好我们把这个方案给生成一下OK
[04:34] 这里边的代码就需要我们重点去编写了这里边我们都需要做哪件事情我们前面在实际图里边给大家说过其实审核的结果是在前端都已经产生了大家看这个图还是咱前面界面前面的界面这其实它点击完审核之后这会弹一个窗上面是通过还是不通过其实它在点击通过不通过的时候审核的结果就已经产生了
[05:05] 所以这个结果是在前端产生然后直接发送到咱们后端的并不是在后端产生的结果所以这里边你要注意的就是这儿这个地方你看它前端发的请求我们说是不是先到来controllercontroller是不是在到达咱这个Service那么前端发过来请求里边就包含有ID和这个什么通过未通过的这个结果那这个值到底是多少呢我们可以让大家看一下前端的代码这是咱那个管理平台的前端是不是
[05:36] 你找到这个文件夹里边的这个页面然后大家看这是不是就是咱看到的那个审核那个按钮你看这点击它的时候是调用一个方法handle click是不是咱找一找往下表在这对不对你看它是否通过审核通过拒绝然后呢你再看这这样其实将来就是往我们后段发请求了你会发现它传入两个数据一个就是ID就是那个标底的ID一个就是1或者说什么呀
[06:10] 二是这个样子吗我们接下来你可以再找一找这个方法是吧我们再往上面在这ID1是不是他传回去其实就是一你看这当然如果这里边走开启的话就出问题的话他仍然也会掉了这个发起Var然后传回去的是几二你看这里边做判断了如果是一怎么着如果是二你看这就是什么
[06:44] 拒绝审核你明白什么意思吗所以通过审核我们传过来的值是多少1然后咱接下来还是回到这个代码里面我们确定了这如果通过审核这个值就是几啊1啊而这个id就是传过来的那个审审核的那个什么样标的来的这是我们需要知道的两个参数的值都是啥那具体的接下来咱这个发里边都需要实现啥功能呢咱简单先分析分析第一个我们要实现的功能就是根据id
[07:17] 那就是这个ID了然后呢查询标的什么样信息因为咱拿到手的只有一个什么样ID啊对吧咱拿到手的只有一个ID但将来我是要把这个所有的这个标的信息就是跟ID有关的所有的标的信息是不是要全都发到银行那边那边要保存嘛是不是所以我们要根据ID查询标的的一个什么样信息并转换为DTO对象
[07:52] DTO对象这是咋回事呢因为我们根据ID查询出来这个标题信息它是project的类型project但是我们需要把project类型的对象转换成什么project DTO为什么呀这大家现在应该知道我们在通过网络传输数据的时候全部都是通过DTO对象来传所以我们必须封装成DTO对象或者转换成DTO对象这个转换咱以前不经常做吗第二个呢由于咱们这个是涉及到交易嘛
[08:21] 是不是发标它就是一种交易所以说它一定会生成什么流水号这个流水号其实就是相当于交易的一个交易的一个ID一个唯一标识这个流水号我们要生成生成流水号之后接下来这个相当于该处理的一些业务或者一些数据就出现了出现之后我们接下来就要干什么通过非远程访问谁对存管代理服务
[09:00] 把标的信息传输过去叫做这个事咱前面是不是一开始刚才是不是先写了那个非应代理吗我站到我们就可以通过他去这个发送这个标的信息那发到那个从外代理服务那边之后那边是要处理接这边就要干什么呀根据什么呀对给你结果他这边要收到结果给你结果修改我们是不是有一些状态要修改
[09:35] 修改状态如果失败这边也涉及到失败的问题如果失败就抛什么就抛一场大概的代码也不是很复杂大概就是五个步骤需要大家先清楚

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解一个项目创建与审核功能的实现，包括定义Feign接口、实现Controller层、Service层方法，以及前端Vue表格交互逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了IDE中“万方金融”项目结构，当前在“3.5.2 功能实现”章节。
- 画面右侧是PPT内容，标题为“3.5.2 功能实现”，子标题“3.5.2.1 交易中心审核标的信息”。
- PPT内容：1. 定义一个Feign代理接口，用于向存管代理服务发送标的信息；2. 在ProjectService接口中新增projectsApprovalStatus方法，用来审核标的信息。
- 画面中代码片段：
  ```java
  @ApiOperation(value = "向存管系统发送标的信息")
  @ApiImplicitParams({
      @ApiImplicitParam(name = "projectDTO", value = "向存管系统发送标的信息",
          required = true, dataType = "ProjectDTO", paramType = "body")
  })
  @PostMapping("/createProject")
  public RestResponse<String> createProject(@RequestBody ProjectDTO projectDTO) {
      return null;
  }
  ```

画面2：
- 展示了IDE中“万方金融”项目结构，当前在“3.5.2 功能实现”章节。
- 画面右侧是PPT内容，标题为“3.5.2 功能实现”，子标题“3.5.2.1 交易中心审核标的信息”。
- PPT内容：1. 定义一个Feign代理接口，用于向存管代理服务发送标的信息；2. 在ProjectService接口中新增projectsApprovalStatus方法，用来审核标的信息。
- 画面中代码片段：
  ```java
  @FeignClient(value = "depository-agent-Service")
  public interface DepositoryAgentApiAgent {
      @PostMapping(value = "/depository-agent/l/create-project")
      public RestResponse<String> createProject(ProjectDTO projectDTO);
  }
  ```

画面3：
- 展示了IDE中“万方金融”项目结构，当前在“3.5.2 功能实现”章节。
- 画面右侧是PPT内容，标题为“3.5.2 功能实现”，子标题“3.5.2.1 交易中心审核标的信息”。
- PPT内容：1. 定义一个Feign代理接口，用于向存管代理服务发送标的信息；2. 在ProjectService接口中新增projectsApprovalStatus方法，用来审核标的信息。
- 画面中代码片段：
  ```java
  @ApiOperation(value = "向存管系统发送标的信息")
  @ApiImplicitParams({
      @ApiImplicitParam(name = "projectDTO", value = "向存管系统发送标的信息",
          required = true, dataType = "ProjectDTO", paramType = "body")
  })
  @PostMapping("/createProject")
  public RestResponse<String> createProject(@RequestBody ProjectDTO projectDTO) {
      return null;
  }
  ```

画面4：
- 展示了IDE中“万方金融”项目结构，当前在“3.5.2 功能实现”章节。
- 画面右侧是PPT内容，标题为“3.5.2 功能实现”，子标题“3.5.2.1 交易中心审核标的信息”。
- PPT内容：1. 定义一个Feign代理接口，用于向存管代理服务发送标的信息；2. 在ProjectService接口中新增projectsApprovalStatus方法，用来审核标的信息。
- 画面中代码片段：
  ```java
  @ApiOperation(value = "向存管系统发送标的信息")
  @ApiImplicitParams({
      @ApiImplicitParam(name = "projectDTO", value = "向存管系统发送标的信息",
          required = true, dataType = "ProjectDTO", paramType = "body")
  })
  @PostMapping("/createProject")
  public RestResponse<String> createProject(@RequestBody ProjectDTO projectDTO) {
      return null;
  }
  ```

画面5：
- 展示了IDE中“万方金融”项目结构，当前在“3.5.2 功能实现”章节。
- 画面右侧是PPT内容，标题为“3.5.2 功能实现”，子标题“3.5.2.1 交易中心审核标的信息”。
- PPT内容：1. 定义一个Feign代理接口，用于向存管代理服务发送标的信息；2. 在ProjectService接口中新增projectsApprovalStatus方法，用来审核标的信息。
- 画面中代码片段：
  ```java
  @FeignClient(value = "depository-agent-Service")
  public interface DepositoryAgentApiAgent {
      @PostMapping(value = "/depository-agent/l/create-project")
      public RestResponse<String> createProject(ProjectDTO projectDTO);
  }
  ```

画面6：
- 展示了IDE中“万方金融”项目结构，当前在“3.5.2 功能实现”章节。
- 画面右侧是PPT内容，标题为“3.5.2 功能实现”，子标题“3.5.2.1 交易中心审核标的信息”。
- PPT内容：1. 定义一个Feign代理接口，用于向存管代理服务发送标的信息；2. 在ProjectService接口中新增projectsApprovalStatus方法，用来审核标的信息。
- 画面中代码片段：
  ```java
  @ApiOperation(value = "向存管系统发送标的信息")
  @ApiImplicitParams({
      @ApiImplicitParam(name = "projectDTO", value = "向存管系统发送标的信息",
          required = true, dataType = "ProjectDTO", paramType = "body")
  })
  @PostMapping("/createProject")
  public RestResponse<String> createProject(@RequestBody ProjectDTO projectDTO) {
      return null;
  }
  ```

画面7：
- 展示了IDE中“万方金融”项目结构，当前在“3.5.2 功能实现”章节。
- 画面右侧是PPT内容，标题为“3.5.2 功能实现”，子标题“3.5.2.1 交易中心审核标的信息”。
- PPT内容：1. 定义一个Feign代理接口，用于向存管代理服务发送标的信息；2. 在ProjectService接口中新增projectsApprovalStatus方法，用来审核标的信息。
- 画面中代码片段：
  ```java
  @ApiOperation(value = "向存管系统发送标的信息")
  @ApiImplicitParams({
      @ApiImplicitParam(name = "projectDTO", value = "向存管系统发送标的信息",
          required = true, dataType = "ProjectDTO", paramType = "body")
  })
  @PostMapping("/createProject")
  public RestResponse<String> createProject(@RequestBody ProjectDTO projectDTO) {
      return null;
  }
  ```

画面8：
- 展示了IDE中“万方金融”项目结构，当前在“3.5.2 功能实现”章节。
- 画面右侧是PPT内容，标题为“3.5.2 功能实现”，子标题“3.5.2.1 交易中心审核标的信息”。
- PPT内容：1. 定义一个Feign代理接口，用于向存管代理服务发送标的信息；2. 在ProjectService接口中新增projectsApprovalStatus方法，用来审核标的信息。
- 画面中代码片段：
  ```java
  @FeignClient(value = "depository-agent-Service")
  public interface DepositoryAgentApiAgent {
      @PostMapping(value = "/depository-agent/l/create-project")
      public RestResponse<String> createProject(ProjectDTO projectDTO);
  }
  ```

画面9：
- 展示了IDE中“万方金融”项目结构，当前在“3.5.2 功能实现”章节。
- 画面右侧是PPT内容，标题为“3.5.2 功能实现”，子标题“3.5.2.1 交易中心审核标的信息”。
- PPT内容：1. 定义一个Feign代理接口，用于向存管代理服务发送标的信息；2. 在ProjectService接口中新增projectsApprovalStatus方法，用来审核标的信息。
- 画面中代码片段：
  ```java
  @ApiOperation(value = "向存管系统发送标的信息")
  @ApiImplicitParams({
      @ApiImplicitParam(name = "projectDTO", value = "向存管系统发送标的信息",
          required = true, dataType = "ProjectDTO", paramType = "body")
  })
  @PostMapping("/createProject")
  public RestResponse<String> createProject(@RequestBody ProjectDTO projectDTO) {
      return null;
  }
  ```

画面10：
- 展示了IDE中“万方金融”项目结构，当前在“3.5.2 功能实现”章节。
- 画面右侧是PPT内容，标题为“3.5.2 功能实现”，子标题“3.5.2.1 交易中心审核标的信息”。
- PPT内容：1. 定义一个Feign代理接口，用于向存管代理服务发送标的信息；2. 在ProjectService接口中新增projectsApprovalStatus方法，用来审核标的信息。
- 画面中代码片段：
  ```java
  @Feign

