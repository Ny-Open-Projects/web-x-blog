# day08-9-交易中心保存标的-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-9-交易中心保存标的-定义接口_【海量资源尽在 666java.com】.mp4
- 时长 6分7秒（音频 367s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢咱们一起了解了一下用户发标这个业务的需求以及具体的交互流程其实主要都体现在这个实习图里边那咱接下来的话就要动手实现发标这个功能那怎么实现呢咱看这个图啊它整体呢这个流程比较多也比较复杂咱还像以前一样化整为零一个一个的进行实现那咱先实现的就是第一块吧1.1到
[00:31] 1.3就是借款人发标这一块这块咱单独看一下这块是不是只涉及到一个什么微服啊对交易中心这功能呢也非常简单其实就是增删改查当中的增就是保存数据所以咱接下来首先把这块功能给实现了呃还跟以前一样咱需要先定义什么呀接口对先定义接口就交易中心保存标底信息的接口啊
[00:58] 我们先定义接口这接口呢大家应该有印象去哪定义啊对大家应该都比较熟悉咱P2P里边所有的接口都定义在哪个地方对API这个工程当中定义在这那我们在这是不是需要单独再建一个包吗是不是Translation包跟以前套路一模一样建一个包交易是不是然后呢在包里边是不是该定义这个接口就是用于我们交易中心呢
[01:31] 这块的接口只不过我目前实现的功能是保存这个接口呢叫transaction API这个命名方式跟之前也都是一样的你看来随便打开一个看这个是不是都是一样的啊在这新建一个什么样接口这是名字啊那里边的话咱目前只需要定一个方法就是什么呀保存标的信息是不是这里边呢我们
[02:01] 这个发明叫可阅他project大家注意了啊project就是标的的意思啊project就是一个投资项目嘛一个项目啊我们在这把它称之为是标的啊标的信息那这个呢比较简单我就整体直接把这块给粘过来好大家看一下啊这是一个接口接口里边目前就定义了一个方案这个方案实现的功能就是借款员干什么呀发标然后呢我们一起了解一下这个方法呢有一个参数还有一个对反位置
[02:34] 参数的话就是一个DTO对象大家比较熟悉了这个将来一定是什么呀前端对吧他应该会填写一些信息啊然后发请求的时候把这个信息传过来我们会封装成对Project的DTO这个类型的对象那么这个类呢现在不存在我们在呃这个地方给大家提供的有在这就是他了我们直接粘过来粘到什么地方哎真到什么地方这个你看一下吧
[03:06] 如果你忘记的话啊DTO我们看一下这个包是不是在API包里吧是不是那我们就去API包那不就是这里边吗这里边他有没有建子宝啊啊modl啊跟以前套路一模一样咱再建一个什么呀子包就行了然后呢我们就把它给control c给它粘过来然后我们打开大概看一下啊这里边封装都有什么呀标底的id呀
[03:39] 发表人就是那consumer的ID呀还有他的用户编码呀标底的一个编码呀你要注意啊这是ID对吧这是编码还还不一样啊那他们都可以作为唯一标识去去使用啊名字呀标底的名字对吧描述呀标底的类型啊标底的期限啊就是你借钱借多少时间吧利率啊等等好几个利率呢是不是还款方式啊
[04:06] 这个这个是你准备借多少钱呀标底的状态呀创建的时间呀很多很多债权呀这个咱还不涉及到呢请求到流水号啊剩余额度啊对不对风险等级出借人数啊等等等等这个信息是比较多因为咱一涉及到具体的交易啊这里边数据还是非常非常多非常非常复杂的这是参数啊返回值的话这个大家都比较熟了我们
[04:34] 这个Controller这一块了返回的一般都是用什么来封装的rest response对不对我们把这个project的dto这个对象给返回了这是这个接口那么按照咱以前套的接口定义完之后咱会顺手把什么呀Controller里边这个来个空时线是不是咱去哪去交易中心这个微服务我们找一找找到谁啊Controller我们现在是不是这个Controller还不存在呢是不是
[05:02] 那你看咱接下来就顺手把这个什么呀对扛出了这个类给他见了然后把刚才那个方法给他来一个空时线先放了上好咱接下来先把这个扛抽类先创建一下呃然后呢这个代码也比较简单咱整体过一遍了他一定要实现刚才那个接口是不是这个不再说了啊要重写这个createproject这个方法然后上面呢是不是有一些sweager ui的一些什么呀注解对不对
[05:33] 还有呢就是这个防路径这个注解这个我就不再过头说了吧大家都知道然后这个注解千万别忘at request body对吧因为这里边就是return到一个空时线啊不再说了非常简单啊我直接转过来呃这是什么呀这是我们把注意看啊我们把交易中心保存标底信息这个功能的接口这一块已经全部定义好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package cn.itcast.wanning2p.transaction.Controller;

import cn.itcast.wanning2p.transaction.Service.TransactionService;
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

