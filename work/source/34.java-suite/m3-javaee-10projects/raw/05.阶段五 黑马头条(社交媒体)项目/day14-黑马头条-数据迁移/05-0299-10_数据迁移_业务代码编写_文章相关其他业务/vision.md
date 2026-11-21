# 画面线理解：10_数据迁移_业务代码编写_文章相关其他业务

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\10_数据迁移_业务代码编写_文章相关其他业务【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 01:13, 02:30, 03:23, 04:12, 05:29, 06:16, 07:16, 08:45, 09:49, 10:49, 12:02, 13:05, 13:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:05:45

1) 这一组画面整体在讲什么（一句话）：
演示如何为文章内容模块设计并实现 MyBatis 的 Mapper 接口、Service 接口及其实现类，并展示数据库表结构和相关 SQL。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档“7.3 文章内容接口”中的“7.3.1 mapper定义”部分，包含 Mapper 接口方法签名和对应的 XML 映射文件内容。
画面2：展示项目结构，聚焦于 `ApArticleContentMapper.java` 接口文件，其中定义了 `selectByIds` 方法。
画面3：展示 `ApArticleContentService` 接口，定义了 `queryByIds` 和 `getById` 方法。
画面4：展示 `ApArticleContentServiceImpl` 实现类，包含 `queryByIds` 和 `getById` 方法的骨架。
画面5：展示 Navicat for MySQL 界面，显示数据库 `heima-news` 中的表结构，其中包含 `ap_article_content` 表。
画面6：展示文档“7.4.2 service”部分，包含 `ApArticleService` 接口定义和 `updateSyncStatus` 方法的注释。
画面7：展示 `ApArticleMapper.xml` 文件，包含 `selectList` 和 `update` SQL 语句。
画面8：展示 `ApArticleService` 接口，正在编辑 `list` 方法。
画面9：在 `ApArticleServiceImpl` 中，选择 `Log` 类型的 Logger。
画面10：在 `ApArticleServiceImpl` 中，编辑 `newApArticleList` 方法，设置 `syncStatus` 为 false。
画面11：在 `ApArticleServiceImpl` 中，编辑 `updateSyncStatus` 方法，设置 `syncStatus` 为 true。
画面12：展示 `ApAuthorService` 接口，正在定义 `List<ApAuthor>` 返回类型。
画面13：展示 `ApAuthorService` 接口，正在编辑 `queryByIds` 方法。
画面14：展示 `ApAuthorServiceImpl` 实现类，编辑 `getById` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
List<ApArticleContent> selectByArticleIds(List<String> articleIds);
<include refid="BaseColumn_List"/>
<include refid="Blob_Column_List"/>
from ap_article_content
where article_id IN
<foreach collection="list" item="id" index="index" open="(" close=")" separator=",">
    #{id}
</foreach>
</select>

画面2：
package com.heima.migration.mappers.app;
import com.heima.model.article.po.ApArticleContent;
import java.util.List;
public interface ApArticleContentMapper {
    ApArticleContent selectById(Integer articleId);
    void insert(ApArticleContent aparticleContent);
    List<ApArticleContent> selectByArticleIds(List<String> articleIds);
}

画面3：
package com.heima.migration.service;
import com.heima.model.article.po.ApArticleContent;
import java.util.List;
public interface ApArticleContentService {
    public List<ApArticleContent> queryByIds(List<String> ids);
    public ApArticleContent getById(Long id);
}

画面4：
import org.springframework.stereotype.Service;
@Service
@SuppressWarrings("all")
public class ApArticleContentServiceImpl implements ApArticleContentService {
    private ApArticleContentMapper apArticleContentMapper;
    @Override
    public List<ApArticleContent> queryByIds(List<String> ids) {
        return null;
    }
    @Override
    public ApArticleContent getById(Long id) {
        return null;
    }
}

画面5：
（无代码，仅显示数据库表结构）

画面6：
// 更新
// @Param apArticle
void updateSyncStatus(ApArticle apArticle);
<update id="updateSyncStatus">
    UPDATE ap_article SET sync_status = #{syncStatus} WHERE id=#{id}
</update>

画面7：
<select id="selectList" resultMap="resultMap">
    select
    <include refid="Base_Column_List"/>
    <include refid="Base_Column_Where"/>
    from ap_article
</select>
<update id="updateSyncStatus">
    UPDATE ap_article SET sync_status = #{syncStatus} WHERE id=#{id}
</update>

画面8：
package com.heima.migration.service;
public interface ApArticleService {
    public ApArticle getById(Long id);
}

画面9：
import com.heima.model.article.po.ApArticle;
import org.springframework.stereotype.Service;
@Service
@SuppressWarrings("all")
public class ApArticleServiceImpl implements ApArticleService {
    private ApArticleMapper apArticleMapper;
    @Override
    public List<ApArticle> queryByIds(List<Integer> ids) {
        return null;
    }
    @Override
    public ApArticle getById(Long id) {
        return null;
    }
}

画面10：
@Override
public List<ApArticle> newApArticleList() {
    ApArticle aparticle = new ApArticle();
    aparticle.setSyncStatus(false);
    return apArticleMapper.selectList(aparticles);
}

画面11：
@Override
public void updateSyncStatus(ApArticle aparticle) {
    log.info("开始更新数据同步状态。aparticle: {}", aparticle);
    if(null != aparticle) {
        aparticle.setSyncStatus(true);
        apArticleMapper.updateSyncStatus(aparticle);
    }
}

画面12：
package com.heima.migration.service;
public List<ApAuthor> queryByIds(List<Integer> ids) {
    return null;
}
public ApAuthor getById(Long id) {
    return null;
}

画面13：
package com.heima.migration.service;
import com.heima.migration.service.ApAuthorService;
import com.heima.model.article.po.ApAuthor;
import org.springframework.stereotype.Service;
@Service
@SuppressWarrings("all")
public class ApAuthorServiceImpl implements ApAuthorService {
    private ApAuthorMapper apAuthorMapper;
    @Override
    public List<ApAuthor> queryByIds(List<Integer> ids) {
        return apAuthorMapper.selectByIds(ids);
    }
    @Override
    public ApAuthor getById(Long id) {
        if(null != id) {
            return apAuthorMapper.selectById(id);
        }
        return null;
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（无 PPT、架构图或表格）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
