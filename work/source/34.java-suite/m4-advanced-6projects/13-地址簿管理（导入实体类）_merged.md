# 13-地址簿管理（导入实体类） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来呢,继续来看咱们地址簿管理

刚才呢,我们这个业务需求,产品原型,还有数据模型呢都已经说完了

接下来呢,我们就需要来导入实体类,对吧

那么,我们这个表其实已经有了,对吧

前面我们已经看到了,这个就是这个地址簿这张表

那么要开发之前呢,咱们需要把对应的这个实体类呢,把它导到我们项目当中来

它这里边的属性呢,跟咱们表里面的字段呢,都是一一对应的

我们先把这个entity这个包呢,来创建一下

在这个品达下边,来创建这么一个包,就叫做entity,对吧

然后呢,把这个类呢,先来创建一下

咱们这个类就叫做address book

整个代码呢,都考过来

这个呢,这就是我们这个地址簿实体类,对吧

地址簿实体类,然后呢,大家可以看到table name

通过这个注解映射的是这张表,对吧

跟这个表有对应关系,好

然后具体这里边的属性,对吧

有ID,user ID,还有什么name

for name

number等等这些啊

跟我们看到的这个表都是一一对应的

前面来看一下

就是跟这个表

都是有对应关系的啊

所以我们直接导进来,直接使用就可以了

这是关于这个实体类,就已经导入完了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是“品达物流TMS项目”第三章“用户服务开发”中的“地址簿管理”模块的教学内容。讲师正在演示如何根据数据库表结构 `pd_address_book` 创建对应的 Java 实体类 `AddressBook`。核心内容包括：
- **数据模型分析**：展示 `pd_address_book` 表的字段结构，包括 `id`, `user_id`, `name`, `phone_number`, `extension_number`, `province_id`, `city_id`, `county_id`, `address`, `company_name`, `is_default`, `create_time` 等字段及其数据类型和约束。
- **实体类开发**：在 IntelliJ IDEA 中创建 `AddressBook` 类，并使用 MyBatis-Plus 的注解（如 `@TableName`, `@TableId`, `@TableField`）和 Lombok 注解（如 `@Data`, `@EqualsAndHashCode`, `@Accessors`）来映射数据库表结构。
- **开发流程**：从分析数据库表结构，到编写 Java 实体类，再到后续的接口开发（如 `AddressBookController`），为后续的用户服务开发奠定基础。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:10**：开场，展示课程大纲，定位到“第3章 用户服务开发”下的“4.3 导入实体类”。
- **00:10 - 00:30**：展示数据库表结构。讲师在 Typora 中打开 `TMS项目讲义_第1章.md`，并展示 `pd_address_book` 表的字段结构图，包括字段名、类型、长度、是否可为空等信息。
- **00:30 - 01:00**：进入实体类开发。讲师在 IntelliJ IDEA 中打开 `AddressBook.java` 文件，开始编写实体类代码。
- **01:00 - 01:30**：编写实体类代码。讲师逐步添加注解和字段，包括 `@Data`, `@EqualsAndHashCode`, `@Accessors`, `@TableName`, `@TableId`, `@TableField` 等，并定义 `id`, `userId`, `name`, `phoneNumber` 等字段。
- **01:30 - 02:00**：继续编写实体类。讲师继续添加剩余字段，如 `extensionNumber`, `provinceId`, `cityId`, `countyId`, `address`, `companyName`, `isDefault`, `createTime`。
- **02:00 - 02:30**：展示实体类完成。讲师高亮显示完整的 `AddressBook` 类，并说明其与数据库表的映射关系。
- **02:30 - 03:00**：过渡到下一节。讲师在 Typora 中切换到“4.4 服务接口开发”章节，预告下一步将创建控制器。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 图表

- **数据模型表**：在 Typora 文档中展示的 `pd_address_book` 表结构，包含以下字段：
  - `id` (varchar, 50, 主键)
  - `user_id` (varchar, 50)
  - `name` (varchar, 50)
  - `phone_number` (varchar, 20)
  - `extension_number` (varchar, 10)
  - `province_id` (bigint, 20)
  - `city_id` (bigint, 20)
  - `county_id` (bigint, 20)
  - `address` (varchar, 255)
  - `company_name` (varchar, 100)
  - `is_default` (tinyint, 1, 是否默认)
  - `create_time` (datetime, 创建时间)

#### 代码

- **实体类 `AddressBook`**：
  ```java
  package com.itehima.pinda.entity;

  import com.baomidou.mybatisplus.annotation.IdType;
  import com.baomidou.mybatisplus.annotation.TableField;
  import com.baomidou.mybatisplus.annotation.TableId;
  import com.fasterxml.jackson.annotation.JsonFormat;
  import lombok.Data;
  import lombok.EqualsAndHashCode;
  import lombok.experimental.Accessors;
  import org.springframework.format.annotation.DateTimeFormat;
  import java.time.LocalDateTime;

  /**
   * 地址簿
   */
  @Data
  @EqualsAndHashCode(callSuper = false)
  @Accessors(chain = true)
  @TableName("pd_address_book")
  public class AddressBook {

      @TableId(value = "id", type = IdType.ASSIGN_UUID)
      private String id;

      @TableField("user_id")
      private String userId;

      @TableField("name")
      private String name;

      @TableField("phone_number")
      private String phoneNumber;

      @TableField("extension_number")
      private String extensionNumber;

      @TableField("province_id")
      private Long provinceId;

      @TableField("city_id")
      private Long cityId;

      @TableField("county_id")
      private Long countyId;

      @TableField("address")
      private String address;

      @TableField("company_name")
      private String companyName;

      @TableField("is_default")
      private Integer isDefault;

      @TableField("create_time")
      @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
      @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
      private LocalDateTime createTime;
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：数据库表结构分析**（00:10-00:30）
  - 讲师在 Typora 中打开讲义文档，高亮显示“4.2 数据模型”部分。
  - 展示 `pd_address_book` 表的结构图，通过鼠标点击和滚动，逐一介绍每个字段的含义和数据类型。
  - 强调 `id` 字段是主键，`user_id` 字段关联用户表，`is_default` 字段用于标识默认地址。

- **场景二：实体类创建与注解应用**（00:30-01:30）
  - 讲师在 IntelliJ IDEA 中打开项目结构，导航到 `entity` 包。
  - 创建新的 Java 文件 `AddressBook.java`，并设置包名 `com.itehima.pinda.entity`。
  - 逐步添加注解：
    - `@Data`：自动生成 getter、setter、toString 等方法。
    - `@EqualsAndHashCode(callSuper = false)`：用于生成 equals 和 hashCode 方法。
    - `@Accessors(chain = true)`：启用链式调用。
    - `@TableName("pd_address_book")`：指定数据库表名。
    - `@TableId(value = "id", type = IdType.ASSIGN_UUID)`：指定主键字段和生成策略。
    - `@TableField("字段名")`：指定非主键字段的映射关系。
  - 为每个字段添加注释，说明其业务含义。

- **场景三：字段定义与数据类型映射**（01:30-02:30）
  - 讲师逐行添加字段，如 `userId`, `name`, `phoneNumber` 等。
  - 对于 `createTime` 字段，同时添加 `@DateTimeFormat` 和 `@JsonFormat` 注解，确保在 Java 和 JSON 序列化时格式一致。
  - 高亮显示 `@TableField("create_time")` 注解，说明其作用是将 Java 字段映射到数据库字段。
  - 展示完整的实体类代码，强调其与数据库表结构的完全对应。

- **场景四：过渡与预告**（02:30-03:00）
  - 讲师在 Typora 中切换到“4.4 服务接口开发”章节。
  - 预告下一步将创建 `AddressBookController` 控制器，并提供 `save` 方法。
  - 展示控制器类的初步代码结构，为后续开发做准备。
