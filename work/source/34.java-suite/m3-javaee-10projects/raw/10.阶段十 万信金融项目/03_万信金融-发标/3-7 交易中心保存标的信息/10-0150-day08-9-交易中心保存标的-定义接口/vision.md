# 画面线理解：day08-9-交易中心保存标的-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-9-交易中心保存标的-定义接口_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:52, 01:23, 01:51, 02:21, 03:07, 03:25, 03:45, 03:56, 04:05, 04:14, 04:29, 05:03, 05:16, 05:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:49:00

1) 这一组画面整体在讲：在万向2P项目中，定义交易中心服务的接口和数据传输对象（DTO），并实现其控制器。

2) 按时间顺序列出每张画面的要点：
画面1：展示PPT内容，标题为“3.2 交易中心保存标的的信息”，下方有“3.2.1 定义接口”小节，内容为“在wanning2p-api工程中新建一个transaction包，在该包中定义一个TransactionApi接口，在该接口中定义一个标的方法：”，并附带代码示例。
画面2：IDEA界面，显示项目结构，当前选中“wanning2p-api”工程。
画面3：在IDEA中，弹出“Create New Class”对话框，Name为“TransactionApi”，Type选择“Class”。
画面4：IDEA中打开“TransactionApi.java”，显示接口定义代码。
画面5：Notepad++中打开“ProjectDTO.java”，显示类的开头部分，包含包声明和导入语句。
画面6：IDEA中“TransactionApi.java”文件，光标在接口方法定义处。
画面7：IDEA中“ProjectDTO.java”文件，显示类的字段定义，包括“consumerId”、“userNo”、“projectNo”等。
画面8：IDEA中“ProjectDTO.java”文件，光标在“type”字段上。
画面9：IDEA中“ProjectDTO.java”文件，光标在“repaymentWay”字段上。
画面10：IDEA中“ProjectDTO.java”文件，光标在“isAssignment”字段上。
画面11：IDEA中“TransactionApi.java”文件，光标在接口方法定义处。
画面12：PPT内容，标题为“3.2.1 定义接口”，内容与画面1相同。
画面13：IDEA中打开“TransactionController.java”，显示类的开头部分。
画面14：PPT内容，标题为“3.2.2 功能实现”，内容为“在Mapper包中定义ProjectMapper接口，并继承MP的BaseMapper接口：”，并附带代码示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//API
//交易中心服务API
public interface TransactionApi {
    /**
     * 借款人发起
     * @param projectDTO
     * @return
     */
    RestResponse<ProjectDTO> createProject(ProjectDTO projectDTO);
}
```
画面4：
```java
package cn.itcast.wanning2p.api.transaction;

/**
 * 交易中心服务API
 */
public interface TransactionApi {
    /**
     * 借款人发起
     * @param projectDTO
     * @return
     */
    RestResponse<ProjectDTO> createProject(ProjectDTO projectDTO);
}
```
画面5：
```java
package cn.itcast.wanning2p.api.transaction.model;

import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.ser.std.ToStringSerializer;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDate;

public class ProjectDTO {
```
画面7：
```java
private long consumerId;
/**
 * 借款人用户编码
 */
private String userNo;
/**
 * 标的编码
 */
private String projectNo;
/**
 * 标的名称
 */
private String name;
```
画面8：
```java
/**
 * 标的类型
 */
private String type;
```
画面9：
```java
/**
 * 还款方式 0.1
 */
private String repaymentWay;
```
画面10：
```java
/**
 * 是否是债权转让
 */
private Integer isAssignment;
```
画面13：
```java
package cn.itcast.wanning2p.transaction.controller;

import cn.itcast.wanning2p.transaction.service.TransactionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/transaction")
public class TransactionController {
```
画面14：
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
public class TransactionController implements TransactionApi {

    @Autowired
    private TransactionService transactionService;

    @ApiOperation("借款人发起")
    @ApiImplicitParam(name = "project", value = "标的的信息", required = true,
            dataType = "Project", paramType = "body")
    @PostMapping("/my/projects")
    public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
        return null;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3.2 交易中心保存标的的信息”，小节标题为“3.2.1 定义接口”，内容为“在wanning2p-api工程中新建一个transaction包，在该包中定义一个TransactionApi接口，在该接口中定义一个标的方法：”，并附带代码示例。
画面12：PPT标题为“3.2.1 定义接口”，内容与画面1相同。
画面14：PPT标题为“3.2.2 功能实现”，内容为“在Mapper包中定义ProjectMapper接口，并继承MP的BaseMapper接口：”，并附带代码示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
