# 16-模板制作：持久层模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\16-模板制作：持久层模板_【海量资源尽在 ubkz.com】.mp4
- 时长 2分25秒（音频 145s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那实体类相关的我们已经搞好了那接下来呢我们关注的就变成了DU好了那接下来找到DU我们一起来看一下如何去做首先呢就是DU这个它的类的名称好了对类的名称呢咱们都知道一般是使用类名加DU的形式来进行匹配所以在这边我把这个类名呢Ctrl C Copy到这边做一个简单的修改OK那好了接下来呢这边同样的Comedy也要修改
[00:33] OK修改好了之后注意那我们这边用的是SpringDataJPA的形式来进行数据库操作那这边呢需要我们有JPARepository以及JPASpecialCaseExecutor那其中的这个范形是不是也是跟我们的实体类匹配的是一致的OK那这样一来我们的方法我们的实体类的相应的声明已经搞定了那接下来就是这边包名包名了$我们开始进行配置
[01:01] 那配置呢同样咱们就可以借助我们刚才做模板分析数据的这么一个列表咱们一起来找一下包名P packageP package那接下来注意那这边呢我们要用到实体类那这个实体类呢咱们是不是已经把它放到了当前这个包的POJO这边啊所以我们这边做一个简单的替换工作package打点POJO好了那接下来
[01:32] company那company就是我们的类名好了做一个替换OK那各位来看这样一来我这个do档其实也已经替换好了它替换好了之后我们再去生成一下现在同样的代码生成里面的所有内容全部都删掉那好了我们一起走好了生成成功我们一起来看一下首先咱们关注一下POJO全部都在
[02:03] 那接着关注一下do你会发现do全部也都已经生成了我们可以以比如说company这个举例来看一下companysystem.do这个包下没问题com.hmsystem.pojo这个包下叫company也没问题好了companycompanycompanyOK那这样一来我们的do也就已经生成好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 代码生成器（CodeGenerator）自动生成项目中的实体类、DAO 接口等代码，并展示生成后的文件结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 IntelliJ IDEA 项目结构，当前选中的是 `CompanyDao.java` 文件，位于 `src/main/java/$path2/$path3/dao/` 路径下。
画面2：在 IDEA 中选中 `ClassNameDao.java` 文件，准备进行代码生成。
画面3：在 IDEA 中选中 `CompanyDao.java` 文件，准备进行代码生成。
画面4：在 IDEA 中选中 `CompanyDao.java` 文件，准备进行代码生成。
画面5：切换到 PPT 页面，显示“3.3 Spring Boot通用模板”下的“3.3.1 实体类”部分，展示实体类模板代码。
画面6：PPT 页面展示“3.3.1 实体类”模板代码，包含 `@Entity`、`@Table` 注解和属性定义。
画面7：PPT 页面展示“3.2 需求分析”下的“（3）数据格式”表格，列出项目中使用的变量名及其含义。
画面8：PPT 页面展示“（3）数据格式”表格，并在下方显示了多个 IDE 窗口的缩略图，包括 IDEA、Notepad++ 等。
画面9：在 IDEA 中选中 `ClassNameDao.java` 文件，准备进行代码生成。
画面10：弹出“代码生成器 1.0”窗口，模板选择为“Spring Boot程序的模板”，项目名称为“company”，包名为“com.ihrm.system”。
画面11：在“代码生成器 1.0”窗口中，项目名称为“company”，包名为“com.ihrm.system”，项目中文名称为“人力资源”，作者为“itcast”，数据库为“hrm”，用户名为“root”，密码为“111111”。
画面12：在文件资源管理器中，显示生成的 `pojo` 目录下的 Java 文件列表，包括 `Company.java`、`Department.java` 等。
画面13：在文件资源管理器中，显示生成的 `dao` 目录下的 Java 文件列表，包括 `CompanyDao.java`、`DepartmentDao.java` 等。
画面14：在 Notepad++ 中打开 `CompanyDao.java` 文件，页面为空白。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```java
package ${package}.pojo;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 * ${comment} 最多层
 * @Author ${author}"itcast"
 */
@Entity
@Table(name="${table.name}")
public class ${ClassName} implements Serializable {
    //定义私有属性
    @List table.columns as column
    @if column.columnKey??
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey == "PRI"
    @if column.columnKey ==

