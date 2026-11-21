# 画面线理解：15-模板制作：实体类模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\15-模板制作：实体类模板_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:46, 01:56, 02:28, 04:31, 06:13, 08:53, 09:24, 10:02, 10:20, 11:04, 11:49, 12:45, 13:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:05:59

1) 这一组画面整体在讲什么（一句话）：
演示如何使用代码生成器（如Freemarker模板）自动生成SpringBoot项目的实体类（POJO）代码，包括配置数据格式、模板编写、调试和最终生成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了“SaaS HRM”文档的第7页，标题为“(3) 数据格式”。
- 表格列出了数据格式字段：author（作者）、project（工程名）、path1（包名1）、path2（包名2）、path3（包名3）、pPackage（完整包名）、projectComment（工程描述）、ClassName（类名）、table（数据库信息）。
- 表格下方有“table中数据内容”子表，包含：name（表名）、comment（表注释）、key（表主键）、columns（所有列信息）、columnName（字段名列名）、columnName2（属性名）。

画面2：
- 展示了IntelliJ IDEA中`$ClassName.java`文件的内容，是生成的实体类模板的一部分。
- 代码片段显示了`private String mailbox;`、`private String companySize;`、`private String industry;`等字段定义，以及对应的注释。

画面3：
- 展示了IntelliJ IDEA中`$ClassName.java`文件的内容，是生成的实体类模板的一部分。
- 代码片段显示了`private String legalRepresentative;`、`private String companyPhone;`、`private String mailbox;`、`private String companySize;`、`private String industry;`等字段定义，以及对应的注释。

画面4：
- 展示了“SaaS HRM”文档的第7页，标题为“(3) 数据格式”。
- 表格列出了数据格式字段：path1（包名1）、path2（包名2）、path3（包名3）、pPackage（完整包名）、projectComment（工程描述）、ClassName（类名）、table（数据库信息）。
- 表格下方有“table中数据内容”子表，包含：name（表名）、comment（表注释）、key（表主键）、columns（所有列信息）、columnName（字段名列名）、columnName2（属性名）。

画面5：
- 展示了“SaaS HRM”文档的第7页，标题为“3.2 需求分析”。
- 内容包括“制作适用的SpringBoot程序的通用模板”，子项为“实体类”，并列出“类路径、类名、属性列表（getter, setter方法）”。

画面6：
- 展示了IntelliJ IDEA中`$ClassName.java`文件的内容，是生成的实体类模板的一部分。
- 代码片段显示了`@Entity`、`@Table(name = "${table.name}")`注解，以及`public class ${ClassName} implements Serializable {`类定义。
- 代码中包含`<list table.columns as column>`、`<if column.columnKey??>`、`private ${column.columnType} ${column.columnName};`等Freemarker模板语法。

画面7：
- 展示了Windows资源管理器中的文件夹结构。
- 路径为：`.../ihrm/day13/资源/生成代码路径/ihrm_company`。
- 当前选中文件为`pom.xml`（XML文档，2 KB）。

画面8：
- 展示了IntelliJ IDEA中`$ClassName.java`文件的内容，是生成的实体类模板的一部分。
- 代码片段显示了`@Entity`、`@Table(name = "${table.name}")`注解，以及`public class ${ClassName} implements Serializable {`类定义。
- 代码中包含`<list table.columns as column>`、`<if column.columnKey??>`、`private ${column.columnType} ${column.columnName};`等Freemarker模板语法。
- 底部显示了错误信息：`freemarker.core.InvalidReferenceException: ...`，提示`$column.columnType`在模板中未定义。

画面9：
- 展示了Notepad++中`Permission.java`文件的内容。
- 代码片段显示了`@Entity`、`@Table(name = "bs_permission")`注解，以及`public class Permission implements Serializable {`类定义。
- 代码中包含`private String id;`、`private String userId;`、`private String companyId;`、`private String administratorName;`、`private String managementModule;`等字段定义，以及对应的getter/setter方法。

画面10：
- 展示了Notepad++中`User.java`文件的内容。
- 代码片段显示了`private String mobile;`、`private String username;`、`private String password;`、`private Integer enableState;`、`private java.util.Date createTime;`等字段定义，以及对应的getter/setter方法。
- 画面中还显示了多个窗口的缩略图，包括IntelliJ IDEA、Notepad++、PDF文档等。

画面11：
- 展示了IntelliJ IDEA中`$ClassName.java`文件的内容，是生成的实体类模板的一部分。
- 代码片段显示了`@Entity`、`@Table(name = "${table.name}")`注解，以及`public class ${ClassName} implements Serializable {`类定义。
- 代码中包含`<list table.columns as column>`、`<if column.columnKey??>`、`private ${column.columnType} ${column.columnName};`等Freemarker模板语法。
- 底部显示了错误信息：`freemarker.core.InvalidReferenceException: ...`，提示`$column.columnType`在模板中未定义。

画面12：
- 展示了IntelliJ IDEA中“代码生成器 1.0”对话框。
- 对话框中“模板”下拉框选中“springboot程序的模板”。
- “项目名（英文）”为“company”。
- “包名”为“com.ihrm.system”。
- “项目中文名称”为“人力资源”。
- “作者”为“Root”。
- “用户名”为“root”，“密码”为“111111”。
- “生成代码”按钮被点击。

画面13：
- 展示了IntelliJ IDEA中“代码生成器 1.0”对话框。
- 对话框中“模板”下拉框选中“springboot程序的模板”。
- “项目名（英文）”为“company”。
- “包名”为“com.ihrm.system”。
- “项目中文名称”为“人力资源”。
- “作者”为“Root”。
- “用户名”为“root”，“密码”为“111111”。
- “生成代码”按钮被点击。

画面14：
- 展示了Notepad++中`City.java`文件的内容。
- 代码片段显示了`@Entity`、`@Table(name = "bs_city")`注解，以及`public class City implements Serializable {`类定义。
- 代码中包含`private String id;`、`private String name;`、`private java.util.Date createTime;`等字段定义，以及对应的getter/setter方法。
- 代码中包含`public void setId(String value) { this.id = value; }`、`public String getId() { return this.id; }`、`public void setName(String value) { this.name = value; }`、`public String getName() { return this.name; }`、`public void setCreateTime(java.util.Date value) { this.createTime = value; }`、`public java.util.Date getCreateTime() { return this.createTime; }`等方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面6代码：
```java
@Entity
@Table(name = "${table.name}")
public class ${ClassName} implements Serializable {
    <list table.columns as column>
    <if column.columnKey??>
    @Id
    </if>
    private ${column.columnType} ${column.columnName};
    </list>

    <list table.columns as column>
    <if column.columnKey??>
    @Id
    </if>
    private ${column.columnType} ${column.columnName};
    </list>
}
```

画面8代码：
```java
@Entity
@Table(name = "${table.name}")
public class ${ClassName} implements Serializable {
    <list table.columns as column>
    <if column.columnKey??>
    @Id
    </if>
    private ${column.columnType} ${column.columnName};
    </list>

    <list table.columns as column>
    <if column.columnKey??>
    @Id
    </if>
    private ${column.columnType} ${column.columnName};
    </list>
}
```

画面9代码：
```java
package com.ihrm.system.pojo;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.io.Serializable;

@Entity
@Table(name = "bs_permission")
public class Permission implements Serializable {

    @Id
    private String id;
    @Id
    private String userId;
    private String companyId;
    private String administratorName;
    private String managementModule;

    public void setId(String
