# 13-HATEOAS介绍-HATEOAS股票服务工程搭建 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们接着创建股票服务

上一讲咱们已经实现了复级工程

PaidOS Demo的搭建和配置

接下来我们就要实现订单服务和股票服务

我们先把股票服务做搭建和配置

打开我们的资料股服务工程

在这里面我们创建一个新的模块

这个模块我们给它一个名称

叫Bus Talk

因为它是PaidOS下面

我们给它名称统一前缀

PaidOS

然后叫Stalks

这个就是实现股票服务

点击Next

叫名称修改一下

注意它的成绩是在PaidOS Demo下面

点击Finish

打入Maven

在这里面就已经创建好了

PaidOS Stocks

接着的话

我们再来看看

它在创建它的工程包结构

New Package

come-add-cast.PaidOS Demo.Stock

这个就是它的一个工程包结构

创建完成之后

我们要给它做什么事情

我们必须要提供一个对应解孔

能够让它去修改股票的价格

接着的话

我们就做对应的实现

在这里面的话

是它整体的一个代码的编写和实现流程

我们带领着大家去做具体的实现

接着的话

要去修改股票服务

股票价格

我们就必须先给它创建一个股票的实体

然后再创建一个包

package

叫Nt

创建完成之后

我们再给它创建一个抽箱

抽箱的实体

复类

Cast

然后是BaseNt

这个复类的话

是一些

实体里面所公用的属性

比如像它的虚拟化

ID等等

Implains

然后

像虚拟化这一块

接口做个实现

这个的话

我们要给它定义

公用的属性

比如说

ID对不对

然后还有什么

Direct

比如说创建时间

还有呢

修改实现

Update time对不对

我们将这个包引入进来

加网 YouTube

给它加上对应的注键

ID的唯一标识

然后呢

ID的生成策略

Generate

Value

它的策略的话

我们就让它自动生成

Change

这里呢

就采用那个Generate Type

然后呢

给它

唯一的标识

然后呢

就会生成自动唯一的注键

这个呢

是它的ID的一个

注键

我们接下来呢

还必须要提供什么

它对应的映射对不对

Cluet Time也要给它映射

Update Time也要给它数据库

自动的一个映射

好

我们呢

编写一下Update

这个的话呢

那它呢

不能进行一个修改对不对

因为你这个是创建时间

Updateable

也就是创建完成之后的话呢

这个数据

按道理的话呢

你不可以

再去重新调整

因为这个是创建时间

然后呢

我们就给它一个

Releases

Time Step

就是

生成一个时间缩

这个呢是创建时间

再往下面呢

是修改时间

修改时间呢

在这里面

给它一个

修改的时间缩

然后呢

最上面还要给它什么

Get Set方法对不对

我们就通过Longboard的

Date数据

把我们实现就可以了

然后呢

Map

Shift Cast

说明呢

你是一个负类

好

接着的话呢

我们还要创建什么

股票的

实体

创建一个Class

这个Class呢

叫Stocks

N体

我们呢

也给它生成一下

在这里面呢

要给它N体的标注

因为成为JPA实现了

对不对

也要你一个Longboard的注解

还有呢

Table的映射

要给它一个表名

给它定义

Table名称

Table名称的话呢

我们叫T

Stocks

然后呢

再给它定义

对应的属性

有两个属性

一个属性呢

是叫股票名称

另外一个属性呢

是叫

股票的价格

因为到时候我们也提供一个

价格的修改接口

这个呢是

股票名称

下面的话呢

是股票价格

股票价格加上对应的注射

这里我们就不给Glue面

Glue面的话呢

是要做质地的映射

因为如果是不给的话呢

就按默认方式进行一个映射匹配

接着的话呢

我们要给它什么

构造参数

增加呢

对应的构造

方法

NoArgs

Control

这是无参的

这个呢是支持所有参数的构造方法

这样呢

我们就完成了

股票实体的创建

接下来的话呢

再创建一个数据层

Open in terminal

然后呢

cd 点点

Make dir

before citri

这样呢

就已经创建完成

我们刷新项

我们呢

给它一个JP的

实现方法

创建一个类

这个类的话呢

这个应该是个接口

JP的接口

要stocks

report citri

好

这个的话呢主要是负责呢

股票的

数据层服务接口

我们让它呢

去继承

JP的接口

JP

report citri

然后呢

要传递

它的实体

就是我们刚才所创建的

stock

NT

还有呢

它的主线类型

是long的类型

然后我们呢给它提供一个数据层接口

叫stocks

NT

根据呢

股票名称

来查找呢

股票对象对不对

那么呢我们要传递它的

一个参数

这个参数呢就是股票名称

Stream name

这个方法呢加上注释说明

根据

名称查

查询

查询信息

好

翻到 by name

这样呢我们玩的JPA的实验

我们还在增加一个什么

启动类

startup

创建一个

对应的启动包

在这里面的话呢

放入启动类

new class

然后呢是

date

OS

stocks

application

负责呢

等股的启动

这个话呢

我们不需要单一模式

PSVM

Spring

application.run

然后呢

dateOS

就是指向呢

本

指向的当前类对不对

然后在这里面的话呢是

class

传递了

参数

我们呢还给它做对应的配置

要做什么配置呢

做Habitat的初始化配置

因为我们用到的是JPA对不对

Habitat5

Mode

然后呢

Habitat

给这个bin呢做一个配置

让它呢

加入到那个Spring容器管理当中

return new

habitat

Mode

直接创建一个新的对象

然后呢

给它一个诸解

纳入容器管理

并

做声明

这个呢是Habitat的初始化

然后呢

我们还要给它呢

再创建对应的

配置

因为的话呢我们HabitatOS的话呢

它传输是通过json数据做一个封装传递

所以呢我们还对一个

json的

主件呢做一个处理

这里json主件呢是采用那个json实现的

JS

JSON

然后这里面的话呢

我们选择的是json to object

map-build

map-build

后面的话呢还有custom

JSON

让它呢

做一个

初始化

用Numble表示

out to

好这样呢就创建完成

这个呢是用于什么

json

数据

的封装处理

我们上面呢还在增加对应的

主件

slim-boot-application

必要的主件对不对

然后呢

compand-skin

这个的话呢等于base

packages

然后呢要扫描我们的

基础包

compt-id-cast

然后呢我们还别忘了另外一个主件是anti-skin

扫描我们所定义的实体

在这里面base-packages

要等于什么

同样

也是做

相关的

compt-id-cast

扫描

最后呢我们还要开启jpa的

主件

Enable jpa

C2 base

然后呢

要扫描jpa的数据省机口

base-packages

要等于什么

compt-id-cast

好这里面的话呢它扫描的就是这个

那接下来的话呢

我们还去实现了工程的配置

工程配置这块呢我们在resource下面创建一个配置文件

叫application

foroblis

然后呢给它一个server

点port

8080

然后拿spleen

jpa

点hyphenate

这个呢给你

none

不用每次起功的时候呢都进行一个更新

然后拿spleen点jpa点foroblis

这个呢点

就是hyphenate的属性的一些配置

点co.circle

我们让它呢打印出来

然后呢

spleen.jp

点problis

这里面的话呢我们让它做一个格式化

并用我们呢直观的跟踪

测试

circle.enqueue

这也不用不让它结束

再接着的话呢我们还创建一个表的结构

这表的结构呢我们就叫

she-mai-schema.circle

在结构里面的话呢

job

table

只要一个表对不对

togs.ext

如果它存在呢就进行一个删除

然后呢我们要去创建

table.togs

然后呢

给它一个id呢

一个

int

mod2

这个跟我们的那个mycircle的语法呢都差不多

然后呢name

64

这个是名称对不对

price

这个呢是价格

然后呢credit time

time.sdmp

这它的时间

时间戳

然后呢update的

time

我们要插入的链

update

看

values

比如说我们插入几只股票信息

一个是中国平安

然后呢

是它的

价格

86

86.6

时间呢就取当前时间

这些话都是一样的

好然后的话呢我们再创建两条记录

这个的话呢一个是

另外的股票

工商银行

那么这个是

6.6价格呢我们就随便填写

招商银行

然后这个价格呢我们就给他26.6

好这样呢就创建了表结构以及呢

数据的初始化

在这里呢

我们就完成了

股票服务的

创建

和它的

配置

那这一讲呢咱们先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于如何在 Spring Boot 项目中集成 HATEOAS（Hypermedia as the Engine of Application State）规范，以实现 RESTful API 的自描述和可发现性。课程通过一个“订单服务”和“股票服务”的双服务架构进行演示，重点讲解了如何使用 Spring Data REST 自动为实体类生成包含链接关系的超媒体资源。讲师通过 IntelliJ IDEA 开发环境，逐步展示了从创建基础实体类、配置 Spring Boot 应用、到编写数据访问层和启动服务的完整开发流程，并强调了 HATEOAS 的核心思想是让客户端能够通过资源的响应中包含的链接，自动发现和调用后续操作。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程开场，展示课程大纲，介绍本节将讲解 HATEOAS 的概念和实现。
*   **00:15 - 00:30**: 展示系统架构图，说明订单服务和股票服务如何通过 HATEOAS 风格进行交互。
*   **00:30 - 00:45**: 介绍 HATEOAS 的核心步骤，包括查询股票信息、更新价格、生成订单。
*   **00:45 - 01:00**: 进入工程目录，展示项目结构，包括 `hateoas-stocks` 和 `hateoas-order` 两个模块。
*   **01:00 - 01:15**: 创建 `BaseEntity` 基础实体类，添加 `@Entity` 和 `@Table` 注解。
*   **01:15 - 01:30**: 在 `BaseEntity` 中添加 `@CreationTimestamp` 和 `@UpdateTimestamp` 注解，用于自动管理创建和更新时间。
*   **01:30 - 01:45**: 创建 `StocksEntity` 实体类，继承 `BaseEntity`，并添加 `@Entity`、`@Data`、`@NoArgsConstructor`、`@AllArgsConstructor` 等注解。
*   **01:45 - 02:00**: 在 `StocksEntity` 中定义 `name` 和 `price` 字段，并添加 `@Column` 注解。
*   **02:00 - 02:15**: 创建 `HateoasStocksApplication` 主类，配置 `@SpringBootApplication` 和 `@ComponentScan`。
*   **02:15 - 02:30**: 在主类中配置 `@Bean`，注册 `HibernateModule` 和 `Jackson2ObjectMapperBuilder` 等 Bean。
*   **02:30 - 02:45**: 配置 `application.properties` 文件，设置数据库连接和 Hibernate 属性。
*   **02:45 - 03:00**: 创建 `schema.sql` 文件，编写创建 `t_stocks` 表的 SQL 语句。
*   **03:00 - 03:15**: 创建 `data.sql` 文件，编写插入测试数据的 SQL 语句。
*   **03:15 - 03:30**: 完成所有配置，准备启动服务。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **系统架构图**: 展示了“客户”、“订单服务”和“股票服务”之间的交互流程。
    *   **HATEOAS 步骤**: 详细列出了四个步骤：查询股票信息、更新股票价格、重新查询、生成订单信息。
    *   **工程目录结构**: 展示了 `hateoas-stocks` 和 `hateoas-order` 模块的目录结构。

*   **代码**:
    *   **`BaseEntity.java`**:
        ```java
        @Entity
        @Table(name = "t_base")
        public class BaseEntity implements Serializable {
            @Id
            @GeneratedValue(strategy = GenerationType.IDENTITY)
            private Long id;
            @Column(name = "create_time")
            @CreationTimestamp
            private Date createTime;
            @Column(name = "update_time")
            @UpdateTimestamp
            private Date updateTime;
        }
        ```
    *   **`StocksEntity.java`**:
        ```java
        @Entity
        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        @Table(name = "t_stocks")
        public class StocksEntity extends BaseEntity {
            @Column(name = "name")
            private String name;
            @Column(name = "price")
            private Double price;
        }
        ```
    *   **`HateoasStocksApplication.java`**:
        ```java
        @SpringBootApplication
        @ComponentScan(basePackages = "com.iteast")
        public class HateoasStocksApplication {
            private static HateoasStocksApplication ourInstance = new HateoasStocksApplication();
            public static HateoasStocksApplication getInstance() {
                return ourInstance;
            }
            private HateoasStocksApplication() {
                // 初始化配置
            }
            @Bean
            public HibernateModule hibernateModule() {
                return new HibernateModule();
            }
            @Bean
            public Jackson2ObjectMapperBuilder jackson2ObjectMapperBuilder() {
                return new Jackson2ObjectMapperBuilder();
            }
        }
        ```
    *   **`application.properties`**:
        ```properties
        server.port=8080
        spring.jpa.hibernate.ddl-auto=auto
        spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect
        spring.jpa.show-sql=true
        spring.jpa.properties.hibernate.format_sql=true
        ```
    *   **`schema.sql`**:
        ```sql
        drop table t_stocks if exists;
        create table t_stocks (
            id bigint auto_increment,
            name varchar(64),
            price double,
            create_time timestamp,
            update_time timestamp,
            primary key (id)
        );
        ```
    *   **`data.sql`**:
        ```sql
        insert into t_stocks(name, price, create_time, update_time) values ('中国平安', 100.0, now(), now());
        insert into t_stocks(name, price, create_time, update_time) values ('工商银行', 80.0, now(), now());
        ```

---

### 4) 关键场景与演示描述

*   **场景一：系统架构演示 (00:15-00:30)**:
    讲师在屏幕上展示了一个流程图，图中包含“客户”、“订单服务”和“股票服务”三个角色。通过箭头和步骤标签，清晰地说明了 HATEOAS 的工作流程：客户首先通过订单服务查询股票信息，然后订单服务通过 HTTP PUT 更新股票价格，最后订单服务生成订单信息。这个图帮助观众理解了 HATEOAS 的核心思想——资源驱动的交互。

*   **场景二：工程结构与实体类创建 (00:45-01:45)**:
    讲师在 IntelliJ IDEA 中展示了项目的目录结构，并逐步创建了 `BaseEntity` 和 `StocksEntity` 两个实体类。在创建 `BaseEntity` 时，讲师强调了 `@CreationTimestamp` 和 `@UpdateTimestamp` 注解的重要性，它们可以自动为实体添加创建和更新时间戳。在创建 `StocksEntity` 时，讲师使用了 Lombok 的 `@Data`、`@NoArgsConstructor` 和 `@AllArgsConstructor` 注解，简化了代码编写。

*   **场景三：主类配置与数据库初始化 (02:00-03:15)**:
    讲师在 `HateoasStocksApplication` 主类中配置了 `@SpringBootApplication` 和 `@ComponentScan`，并添加了 `@Bean` 注解来注册 `HibernateModule` 和 `Jackson2ObjectMapperBuilder`。接着，讲师在 `application.properties` 文件中配置了数据库连接和 Hibernate 属性，并在 `schema.sql` 和 `data.sql` 文件中编写了创建表和插入测试数据的 SQL 语句。最后，讲师准备启动服务，为后续的 API 测试做准备。

---

以上是根据视频画面整理出的技术课程结构化分析。
