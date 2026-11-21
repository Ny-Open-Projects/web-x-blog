# day10-13-投标预览-接口1-功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-13-投标预览-接口1-功能实现3_【海量资源尽在 666java.com】.mp4
- 时长 7分0秒（音频 420s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把获取剩余额度这个功能的代码给编写完了编完之后呢咱把最后一个功能给搞定就是查询出界人数这个查询出界人数呢要比这个功能要简单的多那查询出界人数的话怎么查呢那咱还是要去这个tender这个表里边这个表那我们查的是不是某个标底的这个什么呀出界人数所以说咱查询的时候是不是应该有个条件还是根据这个什么呀标底的这个ID
[00:31] 所以是查询只不过这次呢不是查什么求和的对不对而是查这个什么呀对这个count就是个数就是这个记录的个数那大家想这个tender表我们前面介绍过它是不是这个投标信息表吧那这里边我们说了可以多个人对同一个标底进行什么呀投标那么我们现在要的是不是这个投标的这个记录数啊或者说这个呃出界的这个什么呀人数
[00:57] 那不就是拿着这个条件做一次查询查他出现了这个什么呀次数就行了对不对这个次数其实就是咱想要的这个什么呀对想要的这个出界人数啊所以说这个查询比较简单咱在这呢直接就开始编写代码实现这个功能那我们直接就是通过啊tender map他们有一个方法当然这个方案也是mybattlespass里边的啊一个方案叫select count对就是他sweat count然后呢我们封上条件就行了
[01:28] 封上条件了我们这次用这种写法吧就咱以前也写过就是Lambda的那种写法WRAWARPS嘛第二什么Lambda query对不对这个大家应该有印象当然我们是不是在这要加一个什么呀范形tnd然后我要封装什么条件我们说我们就是要根据什么某个标底的ID进行查询就行了
[02:03] 这里边我们就要用EQ就是相当判断那么需要判断的字段就是什么对tender里边的谁get你看是不是有个标的ID是吧值值就是project的对象调用它的get方法我们就能得到值给大家看就这么写了刚好结束
[02:33] 所以这是我们查询出来的这个什么呀初届人数注意我们进行的是抗的查询啊就是根据某个标底的ID查询出他这个记录的个份这个个份其实就是咱们要查的这个初届人数现在这两个查询都已经搞定了搞定完之后呢我们前面说过这两个数据是不是要封装到project的DTO对象里边你看咱当时让大家瞅过嘛这是不是有一个有一个生育额度还有一个初届人数吗
[03:01] 所以我们要调用他的set方法把这两个数据呢给他封装进去那就是projectdto.set找一找啊set哪个是里边东西比较多好我们看一下他这个里边的刚才那两个属性叫啥名这俩对不对好我们在这就是他了然后呢把这个查出来的结果直接呢放进去
[03:43] 这就完成了一个封装然后下面这个我也直接就直接封装了啊直接进行封装了点set还应该是叫set tinder count对就是他然后把后边这一坨代码给他整个放到这里边就OK了这就封装完了对吧
[04:15] 封装完之后呢别忘了我们在这呢还需要把这个DTO对象存到这个集合里点ADD嘛是不是然后就是project的DTO然后这才叫封装完封装完了最后呢我们直接干什么呀返回这个集合就行了这个功能咱就全部搞定了啊整体我们再快速的过一遍大家注意看我们现在实现的功能是什么呀
[04:46] 对是第一阶段接口1的功能就是获取标底的信息当然这个我们连同什么呀把什么也查了呀把剩余的额度还有出记的人数也一块查那大概的代码是这样子这一块我们做的查询就是一个查询什么呀查询标底信息的一个查询当然我们实现的功能是可以给多个ID查多个标底的信息的当然我们目前呢是我们基本上能确定吧就是传过来的ID应该是一个
[05:17] 然后呢我们单独又封装了一个方法在这个方案里边呢通过这条搜狗语句对吧查询了什么呀以投的金额某个标题的以投金额然后在这个方案里边通过计算把剩余的额度给得到然后也封装到DTO对象里边然后这块子咱刚刚写的用来查询这个出现人数的也封装到project DTO对象里边然后把这个DTO对象呢存到一个集合里边最终返回这个什么呀集合就行了这是我们
[05:45] 把什么呀接口一这个功能就搞定这功能搞定之后呢咱顺手把扛出了里边的代码给补充一下就全部完事了啊咱找到这个扛周热找到扛出了的话应该是应该是这个方法了对不对这是接口一吗你看这里边咱当时空实现了那这里边怎么做那这里边很简单是调用业务层的那个方法就行了啊project Service.queryprojectedits就是他了把它放进去对不对
[06:15] 然后呢他返回来是那个集合吗我们就要接收一下这个集合是普饭行是project的dto是不是对project的dtos吧这个名字你起什么名字都行那然后呢是不是要把这个集合返回给前端但是不能直接返回前端我们应该像以前一样把它封装成rest response然后把它放进去这样子就
[06:48] 可以了啊这control代码也搞定那目前吧咱们第一阶段接口1这块功能咱们编码全部完成咱一会呢就要进行功能测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在项目服务层中，通过 MyBatis-Plus 的 LambdaQueryWrapper 查询项目数据，并结合 Tender 表获取剩余金额，最终封装成 DTO 返回。

2) 按时间顺序列出每张画面的要点：

画面 1:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  list.add(Long.parseLong(str));
  queryWrapper.lambda().in(Project::getId, list); // ... where id in (1,2,3,4,5)
  List<Project> projectsList = queryWrapper.list();
  List<ProjectDTO> dtos = new ArrayList<>();
  // 2. 转换为DTO对象
  for (Project project : projects) {
      ProjectDTO projectDTO = convertProjectEntityToDTO(project);
      // 3. 获取剩余额度
      getProjectRemainingAmount(project);
  }
  ```

画面 2:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  // 4. 查询出借人数
  ```

画面 3:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  tenderMapper.selectCount(Wrappers.lambdaQuery());
  ```

画面 4:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  tenderMapper.selectCount(Wrappers.lambdaQuery().eq(Tender::getProjectId, project.getId()));
  ```

画面 5:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  tenderMapper.selectCount(Wrappers.lambdaQuery().eq(Tender::getProjectId, project.getId()));
  ```

画面 6:
- 代码位置：ProjectDTO.java
- 代码内容：
  ```java
  package cn.itsent.wanningzp.api.transaction.model;

  import ...

  @Data
  public class ProjectDTO {
      // 二健
      @JsonSerialize(using = JsonLongSerializer.class)
      private Long id;
      // 发标人用户标识
      private Long consumerId;
      // 发标人用户编码
  }
  ```

画面 7:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  projectDTO.setRemainingAmount(getProjectRemainingAmount(project));
  ```

画面 8:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  projectDTO.setRemainingAmount(getProjectRemainingAmount(project));
  ```

画面 9:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  tenderMapper.selectCount(Wrappers.lambdaQuery().eq(Tender::getProjectId, project.getId()));
  ```

画面 10:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  projectDTO.setRemainingAmount(getProjectRemainingAmount(project));
  // 4. 查询出借人数
  projectDTO.setTenderCount(tenderMapper.selectCount(Wrappers.lambdaQuery().eq(Tender::getProjectId, project.getId())));
  dtos.add(projectDTO);
  ```

画面 11:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  projectDTO.setTenderCount(tenderMapper.selectCount(Wrappers.lambdaQuery().eq(Tender::getProjectId, project.getId())));
  ```

画面 12:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  if (!isResponse.isSuccessfull()) {
      throw new BusinessException(CommonErrorCode.UNKNOWN);
  }
  return response.getResult();
  ```

画面 13:
- 代码位置：TransactionController.java
- 代码内容：
  ```java
  @ApiOperation("通过ids获取多个标的")
  @GetMapping("/projects/{ids}")
  public RestResponse<List<ProjectDTO>> queryProjectsIds(@PathVariable String ids) {
      return RestResponse.success(projectService.queryProjectsIds(ids));
  }
  ```

画面 14:
- 代码位置：TransactionController.java
- 代码内容：
  ```java
  @ApiOperation("根据标的的id查询投标记录")
  @GetMapping("/tenders/projects/{id}")
  public RestResponse<List<TenderOverviewDTO>> queryTendersByProjectId(@PathVariable Long id) {
      return null;
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
- 无额外代码或配置需抄录。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 无 PPT 或架构图/流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
- 无额外内容。

