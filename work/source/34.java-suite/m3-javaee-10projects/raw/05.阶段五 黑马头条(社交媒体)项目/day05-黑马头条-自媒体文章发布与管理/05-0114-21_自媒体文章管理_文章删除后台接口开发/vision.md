# 画面线理解：21_自媒体文章管理_文章删除后台接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\21_自媒体文章管理_文章删除后台接口开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:32, 02:06, 03:58, 04:21, 04:58, 05:47, 06:26, 07:13, 08:11, 08:48, 09:09, 09:43, 10:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:56:48

1) 这一组画面整体在讲什么（一句话）：
实现文章删除功能的完整后端代码，包括接口定义、Mapper层SQL、Service层业务逻辑和Controller层接口调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示接口文档，定义了删除文章的接口规范，包括请求DTO、响应DTO和参数校验码。
画面2：展示Mapper层的XML文件，定义了根据主键查询文章详情的SQL语句。
画面3：展示Service层的Java代码，导入了Elasticsearch相关依赖和异常处理类。
画面4：展示Controller层的Java代码，定义了删除文章的接口方法，包含参数校验和异常处理。
画面5：展示Controller层的Java代码，添加了参数校验逻辑，使用了@Valid注解。
画面6：展示Controller层的Java代码，添加了业务逻辑，检查文章是否存在。
画面7：展示Controller层的Java代码，添加了业务逻辑，检查文章是否通过审核。
画面8：展示Controller层的Java代码，添加了业务逻辑，检查文章是否被关联。
画面9：展示Controller层的Java代码，添加了业务逻辑，检查文章是否被关联。
画面10：展示Controller层的Java代码，添加了业务逻辑，检查文章是否被关联。
画面11：展示Controller层的Java代码，添加了业务逻辑，检查文章是否被关联。
画面12：展示Controller层的Java代码，添加了业务逻辑，检查文章是否被关联。
画面13：展示Controller层的Java代码，添加了业务逻辑，检查文章是否被关联。
画面14：展示Controller层的Java代码，添加了业务逻辑，检查文章是否被关联。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
5.5 删除文章后台接口
5.5.1 接口定义
(1) 基本定义
自从对于未发布的文章进行删除操作。
参考标准 请参考通用接口规范
发布接口名称 /api/v1/media/news/del_news
请求DTO com.heima.model.media.dto.WmNewsDto
响应DTO { "host": "", "code": 0, "error_message": "操作成功", "data": {} }
(2) CODE定义
PARAM_INVALID PARAM_INVALID(501,"无效参数")。
```

画面2：
```xml
<select id="selectNewsDetailByPrimarykey"
        resultType="com.heima.model.media.pojos.WmNews">
    select <include refid="Base_Column_list"/>
    from wm_news
    where id = #{id}
</select>
```

画面3：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.*;
import com.heima.model.media.dto.WmNewsDto;
import com.heima.model.media.entity.WmNews;
import com.heima.model.media.mapper.WmNewsMapper;
import com.heima.model.media.service.WmNewsService;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com.heima.model.media.vo.WmNewsVo;
import com
