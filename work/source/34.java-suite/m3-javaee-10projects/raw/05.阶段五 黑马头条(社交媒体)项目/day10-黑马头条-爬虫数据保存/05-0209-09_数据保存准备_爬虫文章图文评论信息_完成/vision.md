# 画面线理解：09_数据保存准备_爬虫文章图文评论信息_完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\09_数据保存准备_爬虫文章图文评论信息_完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:44, 00:58, 01:14, 01:29, 01:41, 01:56, 02:07, 02:28, 03:08, 03:38, 03:53, 04:06, 04:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:05:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis 框架实现对爬虫文章评论信息表的实体类定义、Mapper 接口与 XML 映射文件编写，以及 Service 层的业务逻辑实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程文档目录，当前章节为“1.3 爬虫文章评论信息表”，并显示实体类 CINewsComment 的 Java 代码，包含 id、newsId、username、content、commentDate、createdDate 字段。
画面 2：在 IDEA 中打开测试类 CrawlerNewsAdditionalServiceTest，右键弹出菜单，显示“Run”和“Debug”等选项，测试类中定义了测试方法 testQueryList。
画面 3：继续展示 CINewsComment 实体类的完整代码，包含所有字段及其注释。
画面 4：展示项目结构，左侧为项目目录树，右侧为 IDEA 的搜索界面，显示“Search Everywhere”等提示。
画面 5：展示 CINewsCommentMapper.xml 文件内容，包含 MyBatis 的 XML 配置，定义了 resultMap 和 sql 标签。
画面 6：展示 CNewsCommentMapper.java 接口文件，定义了 insert、selectByPrimaryKey、updateByPrimaryKeySelective 等方法。
画面 7：在项目目录树中选中 CNewsCommentMapper.xml 文件，准备进行编辑。
画面 8：在 CNewsCommentMapper.xml 文件中编辑 update 语句，使用 <if> 标签进行条件判断，设置 update 语句的参数。
画面 9：在 CNewsCommentMapper.xml 文件中编辑 sql 标签，定义了 Base_Column_list 和 Base_Column_where 两个 SQL 片段，包含多个 <if> 条件判断。
画面 10：在 CrawlerNewsCommentService.java 文件中，通过自动补全功能选择接口方法 save。
画面 11：在 CrawlerNewsCommentServiceImpl.java 文件中，定义了实现类，导入必要的包。
画面 12：在 CrawlerNewsCommentServiceImpl.java 文件中，为类添加 @Service 注解，并声明私有变量。
画面 13：在 CrawlerNewsCommentServiceImpl.java 文件中，声明私有变量 cINewsCommentMapper，并在 save 方法中调用其 insertSelective 方法。
画面 14：在 CrawlerNewsCommentServiceImpl.java 文件中，完成 save 方法的编写，调用 cINewsCommentMapper.insertSelective 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
/**
 * 文章评论
 */
@Data
public class CINewsComment implements Serializable {
    /**
     * 主键
     */
    private Integer id;
    /**
     * 文章ID
     */
    private Integer newsId;
    /**
     * 评论人
     */
    private String username;
    /**
     * 评论内容
     */
    private String content;
    /**
     * 评论日期
     */
    private Date commentDate;
    /**
     * 创建日期
     */
    private Date createdDate;
}
```

画面 2：
```java
import org.springframework.test.context.junit4.SpringRunner;
import java.util.List;
@org.junit.Test
public class CrawlerNewsAdditionalServiceTest {
    @Autowired
    private CrawlerNewsAdditionalService crawlerNewsAdditionalService;
    @Test
    public void testQueryList() {
        CNewsAdditional cNewsAdditional = new CNewsAdditional();
        cNewsAdditional.setUrl("https://blog.csdn.net/weixin_49976602");
        List<CNewsAdditional> cNewsAdditionals = crawlerNewsAdditionalService.queryList(cNewsAdditional);
        System.out.println(cNewsAdditionals);
    }
}
```

画面 3：
```java
/**
 * 文章评论
 */
@Data
public class CINewsComment implements Serializable {
    /**
     * 主键
     */
    private Integer id;
    /**
     * 文章ID
     */
    private Integer newsId;
    /**
     * 评论人
     */
    private String username;
    /**
     * 评论内容
     */
    private String content;
    /**
     * 评论日期
     */
    private Date commentDate;
    /**
     * 创建日期
     */
    private Date createdDate;
}
```

画面 5：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.heima.model.crawler.mappers.CINewsCommentMapper">
    <resultMap id="Base_Column_List" type="com.heima.model.crawler.pojos.CINewsComment">
        <result column="id" property="id"/>
        <result column="username" property="username"/>
        <result column="content" property="content"/>
        <result column="comment_date" property="commentDate"/>
        <result column="created_date" property="createdDate"/>
    </resultMap>
    <sql id="Base_Column_List">
        id,news_id,username,content,comment_date,created_date
    </sql>
```

画面 6：
```java
import ...
public interface CNewsCommentMapper {
    int deleteByPrimaryKey(Integer id);
    int insert(CINewsComment record);
    int insertSelective(CINewsComment record);
    CINewsComment selectByPrimaryKey(Integer id);
    int updateByPrimaryKeySelective(CINewsComment record);
    int updateByPrimaryKey(CINewsComment record);
}
```

画面 8：
```xml
<if test="username != null">
    #{username}
</if>
<if test="content != null">
    #{content}
</if>
<if test="commentDate != null">
    #{commentDate}
</if>
<if test="createdDate != null">
    #{createdDate}
</if>
<trim>
    updateByPrimaryKeySelective
    parameterType="com.heima.model.crawler.pojos.CINewsAdditional"
    update c_news_comments
    set
```

画面 9：
```xml
<result column="username" property="username"/>
<result column="content" property="content"/>
<result column="comment_date" property="commentDate"/>
<result column="created_date" property="createdDate"/>
</resultMap>
<sql id="Base_Column_list">
    id,news_id,username,content,comment_date,created_date
</sql>
<sql id="Base_Column_where">
    <if test="newsId != null and newsId != ''">
        news_id = #{newsId}
    </if>
    <if test="username != null and username != ''">
        username = #{username}
    </if>
    <if test="content != null and content != ''">
        content = #{content}
    </if>
</sql>
```

画面 10：
```java
package com.heima.crawler.service;
public interface CrawlerNewsCommentService {
    public void save(CINewsComment cINewsComment);
}
```

画面 11：
```java
package com.heima.crawler.service.impl;
import com.heima.crawler.service.CrawlerNewsCommentService;
import com.heima.model.crawler.pojos.CINewsComment;
public class CrawlerNewsCommentServiceImpl implements CrawlerNewsCommentService {
    @Override
    public void save(CINewsComment cINewsComment) {
    }
}
```

画面 12：
```java
@Service
@SuppressWarnings("all")
public class CrawlerNewsCommentServiceImpl implements CrawlerNewsCommentService {
    private CINewsCommentMapper cINewsCommentMapper;
    @Override
    public void save(CINewsComment cINewsComment) {
    }
}
```

画面 13：
```java
@Service
@SuppressWarnings("all")
public class CrawlerNewsCommentServiceImpl implements CrawlerNewsCommentService {
    @Autowired
    private CINewsCommentMapper cINewsCommentMapper;
    @Override
    public void save(CINewsComment cINewsComment) {
        cINewsCommentMapper.insertSelective(cINewsComment);
    }
}
```

画面 14：
```java
@Service
@SuppressWarnings("all")
public class CrawlerNewsCommentServiceImpl implements CrawlerNewsCommentService {
    @Autowired
    private CINewsCommentMapper cINewsCommentMapper;
    @Override
    public void save(CINewsComment cINewsComment) {
        cINewsCommentMapper.insertSelective(cINewsComment);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
