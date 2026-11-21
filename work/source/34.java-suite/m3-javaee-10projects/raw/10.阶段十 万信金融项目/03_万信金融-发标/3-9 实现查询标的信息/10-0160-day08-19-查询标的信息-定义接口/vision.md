# 画面线理解：day08-19-查询标的信息-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-9 实现查询标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-9 实现查询标的信息\day08-19-查询标的信息-定义接口_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:07, 01:10, 02:41, 03:04, 03:11, 03:57, 04:21, 04:50, 05:29, 05:49, 06:30, 06:46, 07:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:56:58

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
