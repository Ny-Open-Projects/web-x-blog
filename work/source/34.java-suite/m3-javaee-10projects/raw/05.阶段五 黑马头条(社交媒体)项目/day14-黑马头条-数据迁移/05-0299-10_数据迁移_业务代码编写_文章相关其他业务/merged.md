# 10_数据迁移_业务代码编写_文章相关其他业务

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\10_数据迁移_业务代码编写_文章相关其他业务【海量资源尽在 666java.com】.mp4
- 时长 14分9秒（音频 849s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续往下讲刚才咱们是把这个文章的这种配置就是已经做完了下面咱们再去做另外一个就是文章的内容它其实跟这个配置是类似的也是有两个方法一个是根据当前的ids去查询另外一个是当前的id去查询好吧
[00:22] 然后咱们下面就来去定义一下这个MIPR这个MIPR咱们之前也是没有的根据当前的article id去查询它的什么所有的什么当前的content这时候你需要去定义一下找到谁找到当前的搜一下ticre然后是content好吧就它然后你在这再去加一个方法然后下面咱们去找到这个MIPR
[00:58] 在这下面也去加一个方法就是根据前的文章的少一个括号啊我把这里加上啊这到时候别出错的好吧嗯行那加完之后啊那咱们这个方法就算是定义完了啊这时候呢你需要在前的Service里边再去创建一个接口这个接口呢叫啥呢叫AP articlecontent Service啊错了好这个定义完之后啊嗯我看看啊检查一遍啊
[01:33] RTICLE CONTENT 没问题然后这是一个接口改一下这边也有两个方法第一个是PUBLIC然后是返回的当前的是一个APARTICLE CONTENT 包有什么意思这是包这个方法叫QUERYPIE然后是叫ARTICLEIDS这里边装的就是所有的ID
[02:07] 这是street然后是ids好吧我还要查询一个是吧public然后是aparticlecontent就它然后是atarticleid好就这样叫s也行叫id好吧叫integer的什么id好这样完了然后下面咱们可以定义它的实现右键在这去创建一个class
[02:39] 这是impl实现刚才定义的aparticlecontentaparticlecontentservice然后呢是让他被sprint去管理加一个superwarning吧那行那这样加完之后啊咱们可以去入他的myproprivate有一个叫做什么aparticlecontentmypro好
[03:22] 关之后你可以直接去调用方法就可以比较简单然后是有一个叫做select by ids然后你把ids装进去就可以了第二个是根据一个发现一个是吧好cp articlecontent mypn.r有一个叫做select by id把id装进去这样也可以了行这个方法咱们就算是定义完了
[03:51] 定义完之后咱们接着往下看然后下面咱们还有哪些没有定义呢就是文章文章的解释文章的话咱们看一下有几个方法第一个是根据主件去查询然后第二个是要去获取未同步的数据同步和不同步其实主要是来看一下找到当前的AP articleAP article哪呢这个是吧
[04:20] 这是有一个同步的状态咱们会有一个true或者firsttrue的话就是同步了first就是没有同步所以说咱们会根据当前的这个东西根据当前的查询就是看看到底有哪些没有同步没有同步的时候咱们再去同步然后再去更改它的状态这个状态改的其实也是刚才我说的这个字段好吧那行咱们下面就来去定义它的一个这种Service
[04:48] 那这时候咱们也是要先去定义它的MIPR这个MIPR也是没有的哪个没有呢第一个是slacks list然后根据条件查询然后第二个就是根据当前的这种应该是要更新当前的这种同步状态咱们可以拷贝一下它然后是找到当前的AAPMIPR应该是这个好这边咱们可以在这去定义一些方法好
[05:20] 印完之后你可以去找到它的什么找到它的这个东西麦克风文件然后是把这两个方法给拿过来这个没有是吧没有的话这样我稍微去改改好吧稍等一下这个我是在笔记上是加了一段大家可以看一看你就把这个也拷过来这是一个条件的判断拷过来然后是你是直接扔到上面就可以了到上面
[05:53] 扔到哪呢那这吧好吧这个呢就是一个条件你看这里边呢其实就有一个当前的这个状态啊当前的同步的状态啊这样这样的话就可以作为条件当然这些条件也是可以的好吧有哪个条件他就以哪个条件啊你传哪条件他就以哪个条件查询好那加完这个网那下面应该是不做错了啊下面呢咱们就来去编写一下咱们的这种Service啊Service打开嗯把这个都关了吧
[06:24] 打开这个然后是在这去创建一个接口这个接口啊写一下APRTICLESERVICE这个接口是吧好然后呢是这里边有几个方法呀里边现在是有三个啊有三个啊哪三个呢Public首先是根据主件去查询一个AP article然后是叫什么呢叫get by ad
[07:01] 好这是第一个是lang类型的ID然后下面接着往下看然后第二个是当前的public一个list返回返回的是一个AP article然后这个插序内是它的未同步的东西这个什么意思这是好这个方法的叫at然后是sync这是同步的意思
[07:41] list这是没有参数的啊把上面标一下标一下也行啊是查询未同步的数据然后下面还有最后一个是吧要更新update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是update是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是up date是
[08:17] 好吧那这个方法这个介绍定义完之后呢咱们下面就可以去定义一下啊这去写他的实现叫impl然后是点okimplement是吧ap articleservice好,i有三个方法咱们需要去实现啊这是一个Service下个log4jlog4j2然后呢是再加一个super warning好吧
[08:51] 然后下面就可以去定义它的myproap articlemypro好先注入进来这个Service非常好写你直接去拷贝一下它然后是点有一个slack的by id把id装进去好了这是第一个第二个的话咱们需要去这里边需要去传一个参数你可以看点有一个叫做slack的list
[09:21] 这个里边需要去放一个AP article它现在是作为条件去往里边传的你有一个它然后你需要去设一个ap article.set一个叫做sync scissors这个设为firstfirst的话就是还没有被同步的咱们只查询未同步的然后你就可以去把它装进去就可以了是一个查询未同步的数据
[09:51] 下面还有一个更新是吧更新的话咱们可以这么着在这去加个4gloginfo说开始更新数据同步状态然后是有一个APCLE然后是冒号他是谁就是APR机构好吧然后下面就可以去调用了咱们这个表现还是得去判断一下
[10:24] 说none不等于前的AP article然后呢你就可以去设置AP article.有一个set它这是啥呢是为true好吧然后呢下面就可以去调用AP article myper然后是有一个叫做update通信状态的一个方法然后是把AP article装进去那这样的话这个方法就算是完了啊
[10:53] 那咱们下面继续还有一个接口咱们需要去设置一下就是当前的作者作者这块这个方法也这个类也比较简单所以说咱们也要去设置一下这里边同样我们需要去根据当前的IDDS去查询这个其实就是他的自己的主件所以说咱们还要再去设置一下打开当前的AP author mapperAP a u t h Mapper好吧
[11:21] 然后在这里边去加入一个方法然后下面就可以去把这个Maple文件拷贝一下找到他好这个Maple准备完之后就可以干嘛呢就可以去在这定义他的Service右键是创建一个接口这是APAUTH然后是Onservice这个接口是吧好然后里边有两个方法是吧第一个是干嘛呢
[11:54] public插群所有不是所有应该是一个集合ap a u t h o r然后呢把包然后是叫啥呢叫curryids然后接的就是一个listlist里边装的是integer不是shrimpinteger然后呢这是ids这是插群多个还有插群什么一个的叫ap u t h o r然后是
[12:27] at by id然后这里边装的是一个integer的浪子型的是吧浪子型的ID那这个定义完之后咱们在这去创建一个好好吧行咱们需要去实现当前的AP author servicectrl i好在这去加一个Service再加一个super warning
[12:57] 下面就可以注入当前的myproprivate然后是当前的ap-a-u-t-h-omypro先把它注入进来注入进来之后就可以调用了这也非常简单有一个叫做select by id把他id转进去这不是id我看看有一个叫做select by ids是吧这是ids
[13:31] 然后这个是个量的型刚才还不真不如去定义整台个是吧嗯行吧无所谓啊那咱们就转一下吧if放浪不等于当前的id然后呢咱们就可以干嘛呢可以去return前的apap author mypr.有一个slag的id把当前id装进去就可以了但是这个不行是吧这个interval6吧好吧这样就可以了啊
[13:59] 如果说它要是为难的话咱们就直接返回一个难就可以了好吧行那这个当前的这个作者这一块咱们也做完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何为文章内容模块设计并实现 MyBatis 的 Mapper 接口、Service 接口及其实现类，并展示数据库表结构和相关 SQL。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档“7.3 文章内容接口”中的“7.3.1 Mapper定义”部分，包含 Mapper 接口方法签名和对应的 XML 映射文件内容。
画面2：展示项目结构，聚焦于 `ApArticleContentMapper.java` 接口文件，其中定义了 `selectByIds` 方法。
画面3：展示 `ApArticleContentService` 接口，定义了 `queryByIds` 和 `getById` 方法。
画面4：展示 `ApArticleContentServiceImpl` 实现类，包含 `queryByIds` 和 `getById` 方法的骨架。
画面5：展示 Navicat for MySQL 界面，显示数据库 `heima-news` 中的表结构，其中包含 `ap_article_content` 表。
画面6：展示文档“7.4.2 Service”部分，包含 `ApArticleService` 接口定义和 `updateSyncStatus` 方法的注释。
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
package com.heima.migration.Service;
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
package com.heima.migration.Service;
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
package com.heima.migration.Service;
public List<ApAuthor> queryByIds(List<Integer> ids) {
    return null;
}
public ApAuthor getById(Long id) {
    return null;
}

画面13：
package com.heima.migration.Service;
import com.heima.migration.Service.ApAuthorService;
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

