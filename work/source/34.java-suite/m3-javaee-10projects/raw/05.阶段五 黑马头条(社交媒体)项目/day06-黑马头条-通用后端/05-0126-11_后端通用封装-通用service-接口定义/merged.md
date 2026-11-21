# 11_后端通用封装-通用service-接口定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\11_后端通用封装-通用service-接口定义【海量资源尽在 666java.com】.mp4
- 时长 6分2秒（音频 362s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才呢咱们是把这个通用的DAO说完了之后啊下面咱们就来去下一块啊下一块咱们要干嘛咱们要去做一个通用的Service通用的Service这个Service只写一次啊那行那下面咱们先看这个接口这个接口里边呢才有三个方法第一个是list第二是update第三个是delete那有同学就说了那为什么没有新增啊新增跟修改用的是同一个方法那查询呢当前的
[00:29] 当前这个例子呢它是可以适用于四种比如说咱们查询所有是吧没有条件啊分页查询所有分页还有什么统计这个说的是不在条件啊还有分别是两种再条件的都是用当前那个例子就能完成好吧行那咱们下面就来去写一写啊在当前的Service里边在这去创建一个common的接口这是common Service好来这是个接口创建
[01:11] 然后呢这里边是有几个方法public response without然后呢是第一个是list 参数是谁呀参数的话是不是当前那个叫什么叫common do啊common pto 是吧pto啊好 看你完了这个就简单说一说啊查询 列本查询是吧其实呢它包含了几种方式包含了比如说咱们的
[01:45] 无条件查询什么无条件的什么统计好然后下面呢这边是分别是有条件的查询就是你带了无条件啊还有条件的什么有条件的统计发行这些东西啊然后下面还有个什么publicresponseresponseresult然后这是update这个呢也是common
[02:20] 然后DTO完了当然这个这个作用也有两个是吧两个呀咱们呢咱们这个通过当前DTO有一个MODELMODEL啊再写吧好吧通过这个什么DTO通过这个MODEL来判断然后最终的是决定到底是决定什么呢这样是吧判断
[02:57] 选择使用什么新增或者修改新增新增或修改好吧行那这个啊他有两个功能啊刚才说了一个是修改第二个是新增然后下面还有一个啊是public删除是吧public response result是delete这个功能比较占一啊功能比较占一common view这个呢只是删除啊
[03:29] 是通用的删除吧好那这个啊咱们就写完了写完之后啊咱们可以再去创建它的实现内在这打开然后叫什么来着叫commonserviceimpl是吧impl啊然后呢这去哎就是个列啊老店ok好这里边啊咱们要去实现当前的commonservice没有吗是这个啊ctrl i好
[04:06] 这个这个的话就是他的方法是吧咱们有点说这里边啥呢Service然后呢你要在这要去注入谁要去注入的是不是common.co是吧因为咱们肯定要去调数据库在这所以说好吧那这个报酬省得看着是有问题是吧怎么着在这加一个这样就可以了
[04:37] 这个算是准备完了准备完之后也可以看一下然后最终咱们会去创建这么一个Service类这个类是咱们核心的一个类它是有这三个方法delete updateupdate的话有两种情况第一个是什么addit还有什么update就是说你可以新增你也可以修改然后list专门的是可以去查询的就是在说但这里边这是介入方法其实里边还有一些辅助的方法
[05:06] 有很多看到了吗第一个是什么帕斯86哎他这个呢就是方法过滤和替换引起思考注入的关键字符一会呢咱们也会去那个写这个方法啊还有do filter这个呢就是来去调制后调用后置增强的那个bin后置增强那个bin啊一会呢咱们也会去说还有获取条件条件的话目前的话这个就是拼击sorcerer啊这个sorcerer的方式呢咱们就可以干嘛呢就可以说支持like
[05:36] 比定还有档号就是EQ就是档域啊还有是可以获取当前的set域的值还有可以获取当前插入serve域的值好吧像这个这几个方法咱们都要在当前的Service中去实现或者说去编写处理当前的业务好吧那行那这个咱们先说到这啊一会咱们再去来写一下当前这个实现类

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何创建通用的 DAO 和 Service 接口及其实现类，用于处理 CRUD 操作，并集成分页、条件查询等通用功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 CommonDao 接口的定义，包含分页查询、统计、条件查询等方法，使用 MyBatis 的动态 SQL。
画面 2: 展示了 CommonService 接口的定义，包含 list、update、delete 方法，用于业务逻辑处理。
画面 3: 展示了 CommonDao.java 文件中的完整方法定义，包括查询、统计、更新、删除等 SQL 模板。
画面 4: 展示了 CommonService.java 文件的开头部分，包含包声明和接口定义。
画面 5: 展示了 CommonService.java 文件中 list 方法的定义，注释说明其功能。
画面 6: 展示了 CommonService.java 文件中 update 方法的定义，注释说明其功能。
画面 7: 展示了 CommonService.java 文件中 delete 方法的定义，注释说明其功能。
画面 8: 展示了 CommonService.java 文件中 delete 方法的定义，注释说明其功能。
画面 9: 展示了在 IDEA 中创建 CommonServiceImpl 类的对话框。
画面 10: 展示了 CommonServiceImpl.java 文件的初始结构，包含 list、update、delete 方法的空实现。
画面 11: 展示了 CommonServiceImpl.java 文件中注入 CommonDao 的代码。
画面 12: 展示了课程 PPT 中关于辅助方法和接口方法的说明，包括 parseValue、doFilter、getWhere、getSets、getInsertSql 等方法。
画面 13: 展示了 CommonServiceImpl.java 文件中添加了 @Service 注解和 ApplicationContext 的代码。
画面 14: 展示了 CommonServiceImpl.java 文件中 list 方法的实现，返回 null。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
// 如果在mycat分库分表的情况下，可以使用多个方法完成不同分片策略的链接kuoo，这里展示为常用的查询，即非复合分片的SQL实现
// Mapper
public interface CommonDao {
    @Select("select * from ${tableName} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> list(@Param("tableName") String tableName, @Param("start") int start, @Param("size") int size);

    @Select("select count(*) from ${tableName}")
    @ResultType(Integer.class)
    int listCount(@Param("tableName") String tableName);

    @Select("select * from ${tableName} where 1=1 ${where} limit #{start},#{size}")
    @ResultType(HashMap.class)
    List<HashMap> listWhere(@Param("tableName") String tableName, @Param("where") String where);

    @Select("select count(*) from ${tableName} where 1=1 ${where}")
    @ResultType(Integer.class)
    int listCountWhere(@Param("tableName") String tableName, @Param("where") String where);
}
```

画面 3:
```java
@Select("select * from ${tableName} where 1=1 ${where} limit #{start},#{size}")
@ResultType(HashMap.class)
List<HashMap> listWhere(@Param("tableName") String tableName, @Param("where") String where);

@Select("select * from ${tableName} where 1=1 ${where}")
@ResultType(Integer.class)
int listCountWhere(@Param("tableName") String tableName, @Param("where") String where);

@Select("update ${tableName} set ${sets} where 1=1 ${where}")
@ResultType(Integer.class)
int update(@Param("tableName") String tableName, @Param("sets") String sets, @Param("where") String where);

@Select("insert into ${tableName} (${fields}) values (${values})")
@ResultType(Integer.class)
int insert(@Param("tableName") String tableName, @Param("fields") String fields, @Param("values") String values);

@Select("delete from ${tableName} where 1=1 ${where} limit 1")
@ResultType(Integer.class)
int delete(@Param("tableName") String tableName, @Param("where") String where);
```

画面 4:
```java
package com.heima.admin.Service;
```

画面 5:
```java
public ResponseResult list(CommonDto dto);
```

画面 6:
```java
public ResponseResult update(CommonDto dto);
```

画面 7:
```java
public ResponseResult delete(CommonDto dto);
```

画面 10:
```java
public class CommonServiceImpl implements CommonService {
    @Override
    public ResponseResult list(CommonDto dto) {
        return null;
    }

    @Override
    public ResponseResult update(CommonDto dto) {
        return null;
    }

    @Override
    public ResponseResult delete(CommonDto dto) {
        return null;
    }
}
```

画面 11:
```java
@Service
public class CommonServiceImpl implements CommonService {
    @Autowired
    private CommonDao commonDao;
```

画面 12:
```java
// 辅助方法
- parseValue: 方法通过字段和值注入到SQL中，注释的value都需要过滤
- doFilter: 用于根据name查找对应后置处理器，如果查询，则执行对应处理器的处理
- getWhere: 拼接where子句字符串，支持like、between、等条件拼接
- getSets: 拼接修改的set子句的值
- getInsertSql: 拼接新增的sql的字段和值字符串

// 接口方法
- delete: 方法必须有查询条件，删除成功之后执行doFilter方法后置处理
- update: 方法通过mode参数判断是新增还是修改，并检查对应的必要参数后调用对应方法
    - addData: 判断数据后，调用数据插入方法，插入成功之后再调用后置处理
    - updateData: 判断数据后，调用更新方法，修改成功后，再调用后置处理方法
- list: 方法判断权限后，计算分页参数和查询条件，并获取列表和总的条数，最后调用后置方法
```

画面 13:
```java
@Service
public class CommonServiceImpl implements CommonService {
    @Autowired
    private CommonDao commonDao;
    ApplicationContext context;
```

画面 14:
```java
@Override
public ResponseResult list(CommonDto dto) {
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 12: PPT 标题为“【辅助方法】”和“【接口方法】”，内容包括 parseValue、doFilter、getWhere、getSets、getInsertSql 等辅助方法的说明，以及 delete、update、list 等接口方法的说明。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

