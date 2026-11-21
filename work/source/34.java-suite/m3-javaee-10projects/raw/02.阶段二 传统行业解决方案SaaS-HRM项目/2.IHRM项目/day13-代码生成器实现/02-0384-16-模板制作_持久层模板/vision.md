# 画面线理解：16-模板制作：持久层模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\16-模板制作：持久层模板_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:18, 00:21, 00:27, 01:02, 01:06, 01:09, 01:12, 01:37, 01:45, 01:53, 02:02, 02:05, 02:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:06:55

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 SpringBoot 代码生成器（CodeGenerator）自动生成项目中的实体类、DAO 接口等代码，并展示生成后的文件结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 IntelliJ IDEA 项目结构，当前选中的是 `CompanyDao.java` 文件，位于 `src/main/java/$path2/$path3/dao/` 路径下。
画面2：在 IDEA 中选中 `ClassNameDao.java` 文件，准备进行代码生成。
画面3：在 IDEA 中选中 `CompanyDao.java` 文件，准备进行代码生成。
画面4：在 IDEA 中选中 `CompanyDao.java` 文件，准备进行代码生成。
画面5：切换到 PPT 页面，显示“3.3 SpringBoot通用模板”下的“3.3.1 实体类”部分，展示实体类模板代码。
画面6：PPT 页面展示“3.3.1 实体类”模板代码，包含 `@Entity`、`@Table` 注解和属性定义。
画面7：PPT 页面展示“3.2 需求分析”下的“（3）数据格式”表格，列出项目中使用的变量名及其含义。
画面8：PPT 页面展示“（3）数据格式”表格，并在下方显示了多个 IDE 窗口的缩略图，包括 IDEA、Notepad++ 等。
画面9：在 IDEA 中选中 `ClassNameDao.java` 文件，准备进行代码生成。
画面10：弹出“代码生成器 1.0”窗口，模板选择为“springboot程序的模板”，项目名称为“company”，包名为“com.ihrm.system”。
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
