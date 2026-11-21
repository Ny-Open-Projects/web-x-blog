# day08-19-查询标的信息-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-9 实现查询标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-9 实现查询标的信息\day08-19-查询标的信息-定义接口_【海量资源尽在 666java.com】.mp4
- 时长 7分19秒（音频 440s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢我们把管理平台的前端工程给部署好也能运行起来是不是那咱接下来就可以实现审核标底的这个业务功能那在这个业务功能当中我们首先要实现的就是查询标底信息大家看这个图我放大一些这个图咱前面见过了是不是大家看一下啊这个我们前面说了P2P公司的管理员是不是要进行
[00:31] 标的信息的审核是不是他想审核是不是首先你看很自然是不是得先把标的信息给先干什么查一下这应该是一个分页列表查询是不是查出来之后呢哎每个标的后边都有审核这个按钮然后就可以进行操作所以说我们要想进行审核标的首先要先实现标的的一个什么呀对分页查询啊这功能实现完之后呢在管理平台的这个页面就会把这个标的信息给查出来
[01:01] 查出来之后呢这个P2P公司的管理员在这就可以看到这些信息然后进行什么呀审核操作所以说咱首先在审核标题的时候首先要实现的就是标题信息的一个带条件的分页查询咱这个查询尽量给它实现的这个功能完整一些那跟以前一样咱先定义接口这个其实就是增删改良当中的一个查询嘛只不过我们想把这个功能做的完善一些还是一个查询
[01:31] 先定一个接口吧咱去这个应该是哪交易中心是吧交易中心我们要去API工程里边找到transaction这个包这是交易中心的这个接口吧在这里边我们需要在这里边新增方法我们新增的方法大家看这个讲义吧它只是一个查询就是条件可能会比较多吧还带着分页排序大家看一下我们定义了一个方法叫query什么呀projects证明是查询
[02:05] 很多这个什么样标的信息然后呢我们再看看这个方法呢有一堆参数咱一起了解一下啊第一个参数叫queryprojectquerydq这个我们见名之意基本上能猜出来它是用来封装这个什么样查询条件你看我们可以根据什么呀根据利率进行查询还可以根据根据这个借款金额进行查询根据你借款的年限就是这个期数
[02:32] 经营查询等等的我们会有很多条件啊这个条件呢我们将来会封装到project query DQ这个对象里面这个对象的话我们看看咱们有没有这个类啊这里边给大家提供的就是他咱看应该考到哪个包里边啊API工程是吧model好我们先把它考进来然后打开看一下就是在这里边粘过来
[03:03] 好咱看一下这里边可以根据标的类型查询标的标的的什么名称这个期指的这个期限对吧利率还款方式标的状态等等等等啊反正能查询的这个条件非常多这是第一个参数第二个参数啊大家都比较熟悉了就是什么呀升旭还是降旭接下来配一囊吧配一赛子就是分业的条件吧配一囊吧表示第几页配一赛子表示一页显示多少行
[03:32] 这个sort by就是根据哪个字段进行查询啊sort by跟这个order他俩应该是一起使用的配计number跟配计size是一起使用的而他呢就是专门封装对查询条件这是这一堆参数咱先搞明白呃这个搞完之后呢我们看看啊我们查出来数据怎么进行封装我们是封装成了一个配给VO对象配给VO配给VO呢我们打开让大家看一看搜一下吧PAGE
[04:00] 配置view大家看一下是不是在恐慢工程里面已经给大家提供好了我们打开配件view他是支持饭行的啊支持饭行的你看咱这里边最终查出来的数据每一行的数据是用什么来封装的呀project的dto对象来封装那我们先了解一下配给view这个对象他里边都有啥那这里边咱就看属性就行了第一个content大家看是一个集合这个大家能猜到我比如说我要查第一页的数据
[04:32] 一页显示十行那么这个集合不就是存在那十行数据吗是不是这十行数据呢我们都是封装成了这个project的dto这个类型的对象存进去然后还有这个是什么呀总页数这个就是第几页这个就是每页显示多少行我们把这个分页查询相关的这些数据全部封装到pageview对象里查出来的数据呢是放到content这个记号里面这个你一定要熟悉整个这个
[05:00] 分析查询他都有哪些参数以及这个查出来数据是怎么进行封装了这个了解完之后呢这个代码我就不再给大家写了我就直接粘过来就行了我们应该是粘到对这个地方这是我们的接口就定好接到定好之后咱跟之前一样顺手呢在Controller里边来个空实现那我们就去这个谁啊交易中心找到Controller他现在应该是报错是吧
[05:35] 我们打开这该报错了然后我们把刚才街口里边定义的那个方法给他生成一下就是这个方法对不对来让我一下看那这里边呢必要的一些注解咱们要补一下比如说这个sweat ui的这一堆注解挺多的啊这里边就是每个参数都是什么意思等等相关的一些注意这个我觉得你不用敲了你从简易里边粘过去就行了知道这里边这都是什么意思就ok了然后呢还有就是smart mvc的这个一个注解
[06:08] post map 访入进对不对projects key包括这个地方这些注解request body也说证明了查询条件呢我们是不是将来是通过jason数据传过来然后在这进行封装了这是整个这一块吧这个大家也都知道是咋回事我就把它直接粘过来啊我给他粘过来直接啊但是粘过来估计这个格式会比较乱啊因为从pdf粘过来的这个看着都很头疼是不是
[06:43] 那这个我们只能是暂时手工先调一下缺少大果号这个小果号小果号小果号多个小果号啊生一个多一个小果号刚才啊然后这这就没错反正这个格式从pdf粘过来比较乱啊你下去自己再给他调整调整就行了这是我们把查询标底信息的接口这块就定义好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在万信金融项目中，实现标的查询的分页接口，包括定义查询DTO、接口方法及控制器实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT第14页，标题“3.4 查询标的信息”，内容说明审核标需先实现标的分页查询，查询信息在管理平台展示，仅P2P公司管理员可见。
画面2：PPT第14页，展示“万信金融”登录界面，强调业务需先实现标的分页查询。
画面3：PPT第14页，展示“3.4.1 定义接口”小节，说明需在TransactionApi接口中新增queryProjects方法，实现带条件的分页查询。
画面4：文件资源管理器，显示“万信金融-第3章-讲义-发标v1.0.pdf”文件。
画面5：IDE中打开“ProjectQueryDTO.java”，展示该DTO类定义，包含type、name、startPeriod、endPeriod、startAnnualRate等字段。
画面6：IDE中“ProjectQueryDTO.java”文件，高亮显示“private BigDecimal endAnnualRate;”字段。
画面7：IDE中“TransactionApi.java”文件，展示接口定义，包含createProject和queryProjects方法。
画面8：IDE中“ProjectQueryDTO.java”文件，高亮显示“private BigDecimal borrowerAnnualRate;”字段。
画面9：IDE中“PageVO.java”文件，展示分页对象的定义，包含content、total、pageNo、pageSize字段。
画面10：IDE中“TransactionApi.java”文件，展示queryProjects方法的定义，参数包括ProjectQueryDTO、order、pageNo、pageSize、sortBy。
画面11：PPT第19页，展示“TransactionController.java”中@ApiOperation注解，定义“检标的信”接口，参数包括projectQueryDTO、order、pageNo、pageSize、sortBy。
画面12：PPT第19页，展示“TransactionController.java”中@ApiOperation注解，参数定义与画面11相同。
画面13：IDE中“TransactionController.java”文件，展示queryProjects方法的实现，包含@RestController注解和@PostMapping("/projects")。
画面14：IDE中“TransactionController.java”文件，展示queryProjects方法的完整实现，包含@ApiOperation注解和参数定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
1. 在TransactionApi接口中新增查询方法queryProjects，实现带条件的分页查询：
/**
 * 检索标的
 * @param projectQueryDTO
 * @return
 */
```

画面5：
```java
@Data
@ApiModel(value = "ProjectQueryDTO", description = "标的的信息查询对象")
public class ProjectQueryDTO {
    @ApiModelProperty("标的的类型")
    private String type;
    @ApiModelProperty("名称")
    private String name;
    @ApiModelProperty("起止标的期限(单位:天)")
    private Integer startPeriod;
    @ApiModelProperty("起止标的期限(单位:天)")
    private Integer endPeriod;
    @ApiModelProperty("起止年化利率(投资人视图)")
    private BigDecimal startAnnualRate;
    @ApiModelProperty("起止年化利率(投资人视图)")
    private BigDecimal endAnnualRate;
    @ApiModelProperty("年化利率(借款人视图)")
    private BigDecimal borrowerAnnualRate;
    @ApiModelProperty("还款方式")
    private String repaymentWay;
    @ApiModelProperty("标的的状态")
    private String projectStatus;
}
```

画面7：
```java
public interface TransactionApi {
    /**
     * 创建标的
     * @param projectDTO
     * @return
     */
    RestResponse<ProjectDTO> createProject(ProjectDTO projectDTO);

    /**
     * 检索标的
     * @param projectQueryDTO
     * @param order
     * @param pageNo
     * @param pageSize
     * @param sortBy
     * @return
     */
    RestResponse<PageVO<ProjectDTO>> queryProjects(ProjectQueryDTO projectQueryDTO,
            String order, Integer pageNo, Integer pageSize, String sortBy);
}
```

画面9：
```java
package cn.itcast.wanxingzp.common.domain;

import java.io.Serializable;

public class PageVO<T> implements Serializable {
    private List<T> content = new ArrayList<>();
    private long total;
    private int pageNo;
    private int pageSize;

    public PageVO() {
    }

    public PageVO(List<T> content, long total, int pageNo, int pageSize) {
        this.content = content;
        this.total = total;
        this.pageNo = pageNo;
        this.pageSize = pageSize;
    }
}
```

画面11：
```java
@ApiOperation("检标的信")
@ApiImplicitParams({
    @ApiImplicitParam(name = "projectQueryDTO", value = "标的的信息查询对象",
            required = true, dataType = "ProjectQueryDTO", paramType = "body"),
    @ApiImplicitParam(name = "order", value = "顺序", required = false,
            dataType = "string", paramType = "query"),
    @ApiImplicitParam(name = "pageNo", value = "页码", required = true,
            dataType = "int", paramType = "query"),
    @ApiImplicitParam(name = "pageSize", value = "每页记录数", required = true,
            dataType = "int", paramType = "query"),
    @ApiImplicitParam(name = "sortBy", value = "排序字段", required = true,
            dataType = "string", paramType = "query")
})
```

画面13：
```java
@RestController
@PostMapping("/projects")
public RestResponse<PageVO<ProjectDTO>> queryProjects(@RequestBody ProjectQueryDTO projectQueryDTO,
        String order, Integer pageNo, Integer pageSize, String sortBy) {
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：PPT标题“3.4 查询标的信息”，副标题“审核标的业务需要首先实现标的的分页查询，查询出来的标的的信息会在管理平台中展示出来，只有P2P公司的管理员看到这些标的信息了，才能进行审核操作。”
画面11：PPT标题“TransactionController.java”，副标题“2. 在TransactionController类中实现该方法：”，下方展示@ApiOperation注解内容。
画面13：PPT标题“TransactionController.java”，副标题“@Override”，下方展示@ApiOperation注解内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

