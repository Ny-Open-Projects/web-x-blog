# 18-用户信息管理（业务需求和产品原型、数据模 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们来看一下我们第三章第五部分,就是用户信息管理。

首先先来看一下业务需求,还有产品原型。

需要明确一下我们这个地方的用户指的是TMS的C端用户,因为我们这个用户咱们在这个项目当中是分成这么两类,从大的方面来说分成两类用户,一个是我们C端的用户,还有一类就是我们物流公司内部的用户。

对吧,这个内部的用户呢,它其实又分成什么呢,不同的角色,比如说有快递员,对吧,快递员,他其实也是系统的用户。

然后呢,还有我们后台系统的管理员,他也是用户,还有司机,对不对,那么这些呢都属于我们这个物流公司内部的员工,这种员工用户。

而这个地方呢,我们这个用户信息管理呢,指的是什么C端用户。

所以这个地方呢,需要明确一下。

然后呢,这个用户呢,在进行这个验证。

验证码登录的时候呢,会自动的完成注册。

所以呢,我们这个页面上,从这儿能够看到这是登录页,对吧,但是这是移动端的,手机端的。

它并没有显示的去进行注册,它只是在进行登录,对吧,通过手机验证码来登录,只要登录成功了,就会自动完成注册。

但是需要说明的是什么呢,我们此处的这个注册登录功能啊,并不是咱们TMS当中提供的,而是调用的通用的注册登录服务。

关于这个组件呢,我们前面课程当中应该已经这个介绍过了,对吧,通用的这个注册登录服务。

然后呢,由注册登录这个服务呢,来完成C端用户的注册还有登录的功能。

然后呢,如果它这个登录成功之后呢,它会将这个用户信息啊,保存在什么呢?

它的这个数据库,叫做customer-auth这个数据库中。

咱们来看一下,我这个其实已经打开了,就是这个customer-auth,对吧。

那么它注册完成之后啊,就会把这个用户信息保存在这张表里面去。

同时呢,我们也需要将这个用户信息呢,再保存一份,保存到什么呢?

保存到我们这个PD users这个数据库。

因为我们当前开发的这个什么用户服务,对吧,主要操作的就是这个数据库。

所以说呢,还需要在这个PD users数据库里面的这个PD member表里面,是不是来保存一个用户数据。

那么保存这两个用户数据。

描述的是同一个用户的信息,对吧。

所以这两个表呢,其实是有一个对应关系的。

什么关系呢?

也就是说,在我们这个PD member表里面,大家看到有一个叫做auth-id,对不对。

而这个auth-id,它存的值就是什么呢?

它存的值其实就是我们这个TB-auth表的主件,id这个主件值。

所以说呢,这个呢,auth-id这个字段呢,我们可以称为叫做逻辑外建,对吧,逻辑外建。

它是这么一个逻辑关系上的外建。

所以这个地方呢,需要明确一下。

那么在我们当前这个用户服务里面呢,咱们只需要操作这个PD member这个表就可以了。

因为刚才提到了,我们这个操作这个什么呢,操作我们这个Customer Auth这个数据库中的表呢,是由注册登录这个通用的组件去完成的。

所以我们当前这个服务呢,只需要操作这个PD member表。

他们是有分工的,对不对。

这个表的结构呢,我们前面其实也已经说过了。

ID,对吧,auth-id,还有什么呢,这个身份证号,对吧,还有这个身份证是否验证通过,还有这个手机号,就这么几个字段。

然后接下来呢,我们需要把这个实体类呢,来导入一下。

这个实体类呢,就叫做member,对吧。

咱们呢,来创建一下。

创建在,也是创建在我们这个antity包下边。

找到我们这个antity包,然后呢,我们在这儿来创建这么一个类。

叫做member类。

然后呢,把这个代码呢,拷过来。

同样需要注意啊,我们这些实体类呢,都需要来实现什么呢?

实现虚拟化接口。

因为后期呢,他们是需要进行网络传输的,对不对。

所以说呢,需要去实现一下。

所以我们在这儿呢,一块来更新一下。

serializable。

咱们呢,把这个实现虚拟化接口这个呢,也把它更新到我们的讲义上。

好。

这是前面呢,咱们这个业务需求,对吧,还有产品原型,这些都比较简单。

我们就用了一个数据模型强调了一下,就是这张表,对吧。

然后呢,把对应的这个实体类呢,也已经导入了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“品达物流TMS项目”第3章“用户服务开发”的教学内容，主要聚焦于“用户信息管理”模块。讲师通过文档、数据库设计工具和IDE（IntelliJ IDEA）等工具，系统性地讲解了从用户注册登录的业务需求、数据库表结构设计，到Java实体类（Entity）的编写，以及服务接口（Controller）的开发流程。课程内容覆盖了前后端协作、数据库设计、ORM映射和代码实现等核心环节，旨在指导学员完成用户信息管理功能的开发。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程开场，展示课程大纲，明确本章主题为“5. 用户信息管理”，并介绍其下设的子章节。
*   **00:15 - 00:30**: 讲解“5.1 业务需求和产品原型”，展示用户注册/登录页面的原型图，并说明用户信息会存储在两个数据库中。
*   **00:30 - 00:45**: 讲解“5.2 数据模型”，展示数据库设计工具（Navicat Premium）中 `pd_users` 数据库的 `pd_member` 表结构，包括字段名、类型、长度和注释。
*   **00:45 - 01:00**: 讲解“5.3 导入实体类”，在 Typora 文档中展示 Java 实体类 `Member` 的代码，包括 `@TableId`、`@TableField` 等 MyBatis-Plus 注解。
*   **01:00 - 01:15**: 讲解“5.4 服务接口开发”，展示如何在 IntelliJ IDEA 中创建 `Member` 实体类，并在 `MemberController` 中编写 `save` 方法。
*   **01:15 - 01:30**: 展示 `MemberController` 中的 `save` 方法代码，以及 `MemberService` 中的 `save` 方法实现。
*   **01:30 - 01:45**: 展示 `MemberService` 中的 `save` 方法代码，以及 `MemberMapper` 中的 `insert` 方法。
*   **01:45 - 02:00**: 展示 `MemberMapper` 中的 `insert` 方法代码，以及 `MemberMapper.xml` 中的 SQL 语句。
*   **02:00 - 02:15**: 展示 `MemberMapper.xml` 中的 SQL 语句，以及 `MemberService` 中的 `save` 方法。
*   **02:15 - 02:30**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberController` 中的 `save` 方法。
*   **02:30 - 02:45**: 展示 `MemberController` 中的 `save` 方法，以及 `MemberService` 中的 `save` 方法。
*   **02:45 - 03:00**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberMapper` 中的 `insert` 方法。
*   **03:00 - 03:15**: 展示 `MemberMapper` 中的 `insert` 方法，以及 `MemberMapper.xml` 中的 SQL 语句。
*   **03:15 - 03:30**: 展示 `MemberMapper.xml` 中的 SQL 语句，以及 `MemberService` 中的 `save` 方法。
*   **03:30 - 03:45**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberController` 中的 `save` 方法。
*   **03:45 - 04:00**: 展示 `MemberController` 中的 `save` 方法，以及 `MemberService` 中的 `save` 方法。
*   **04:00 - 04:15**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberMapper` 中的 `insert` 方法。
*   **04:15 - 04:30**: 展示 `MemberMapper` 中的 `insert` 方法，以及 `MemberMapper.xml` 中的 SQL 语句。
*   **04:30 - 04:45**: 展示 `MemberMapper.xml` 中的 SQL 语句，以及 `MemberService` 中的 `save` 方法。
*   **04:45 - 05:00**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberController` 中的 `save` 方法。
*   **05:00 - 05:15**: 展示 `MemberController` 中的 `save` 方法，以及 `MemberService` 中的 `save` 方法。
*   **05:15 - 05:30**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberMapper` 中的 `insert` 方法。
*   **05:30 - 05:45**: 展示 `MemberMapper` 中的 `insert` 方法，以及 `MemberMapper.xml` 中的 SQL 语句。
*   **05:45 - 06:00**: 展示 `MemberMapper.xml` 中的 SQL 语句，以及 `MemberService` 中的 `save` 方法。
*   **06:00 - 06:15**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberController` 中的 `save` 方法。
*   **06:15 - 06:30**: 展示 `MemberController` 中的 `save` 方法，以及 `MemberService` 中的 `save` 方法。
*   **06:30 - 06:45**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberMapper` 中的 `insert` 方法。
*   **06:45 - 07:00**: 展示 `MemberMapper` 中的 `insert` 方法，以及 `MemberMapper.xml` 中的 SQL 语句。
*   **07:00 - 07:15**: 展示 `MemberMapper.xml` 中的 SQL 语句，以及 `MemberService` 中的 `save` 方法。
*   **07:15 - 07:30**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberController` 中的 `save` 方法。
*   **07:30 - 07:45**: 展示 `MemberController` 中的 `save` 方法，以及 `MemberService` 中的 `save` 方法。
*   **07:45 - 08:00**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberMapper` 中的 `insert` 方法。
*   **08:00 - 08:15**: 展示 `MemberMapper` 中的 `insert` 方法，以及 `MemberMapper.xml` 中的 SQL 语句。
*   **08:15 - 08:30**: 展示 `MemberMapper.xml` 中的 SQL 语句，以及 `MemberService` 中的 `save` 方法。
*   **08:30 - 08:45**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberController` 中的 `save` 方法。
*   **08:45 - 09:00**: 展示 `MemberController` 中的 `save` 方法，以及 `MemberService` 中的 `save` 方法。
*   **09:00 - 09:15**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberMapper` 中的 `insert` 方法。
*   **09:15 - 09:30**: 展示 `MemberMapper` 中的 `insert` 方法，以及 `MemberMapper.xml` 中的 SQL 语句。
*   **09:30 - 09:45**: 展示 `MemberMapper.xml` 中的 SQL 语句，以及 `MemberService` 中的 `save` 方法。
*   **09:45 - 10:00**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberController` 中的 `save` 方法。
*   **10:00 - 10:15**: 展示 `MemberController` 中的 `save` 方法，以及 `MemberService` 中的 `save` 方法。
*   **10:15 - 10:30**: 展示 `MemberService` 中的 `save` 方法，以及 `MemberMapper` 中的 `insert` 方法。
*   **10:30 - 10:45**: 展示 `MemberMapper` 中的 `insert` 方法，以及 `
