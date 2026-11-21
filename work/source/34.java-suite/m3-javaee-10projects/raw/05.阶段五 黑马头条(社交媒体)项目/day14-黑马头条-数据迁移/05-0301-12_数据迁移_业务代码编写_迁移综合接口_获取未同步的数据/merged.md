# 12_数据迁移_业务代码编写_迁移综合接口_获取未同步的数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\12_数据迁移_业务代码编写_迁移综合接口_获取未同步的数据【海量资源尽在 666java.com】.mp4
- 时长 19分20秒（音频 1160s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 来继续啊咱们就来去写它的实现类啊好背一下它然后是在这去创建一个类叫impl然后呢去是让它去实现当前的这个接口是吧是在这去加一个Service加一个log4接触好那我现在先问一下啊这些类啊这些方法咱们需要哪些Service呢那我说是Service啊因为这些Service啊
[00:29] Service刚才说了就是为当前的这个Service去什么服务的是吧所以说你需要把这4个Service统一的都要注入进来来加一个然后是private是第一个是AP articlearticleconfig就它其实这个出哪个无所谓顺序无所谓然后咱们接着往下看咱们直接拷贝一下config content一个private
[01:04] 好我们就速度稍微快点然后是public private然后是第三个是AP article Service然后呢是接着往下啊也是author好那这个四个方法四个类啊咱们注入进来了那你说还需要注入吗刚才说了这里边呢其实有一个东西咱们需要从HBase中去查是吧还有是
[01:45] 同步到HBase所以说咱们是不是得去注入一个HBase相关的操作类哪个呢咱们之前其实做过测试private里边是有一个叫做什么呢叫HBaseStorage Client用的是它我们叫Storage Client就可以了把它给注入进来一会儿咱们就可以用它去插入数据也可以去获取数据
[02:13] 好那这个咱们该注入的这种接口都已经注入完了然后下面咱们就可以干嘛呢就可以去编写类编写方法咱们首先要编写的是第一个那这个呢那这个是获取当前的什么Article Quantity List那这个到底该怎么去获取呢就这样咱们其实在当前的这种Article Service中其实定义了一个方法就是查询什么未同步的数据
[02:40] 首先呢你要去查询为什么的数据然后呢再去把它给综合起来就可以了当然查询它呢只是第一步因为你还要关联的查询什么呢config content author而这些数据咱们都需要好吧呃最终呢咱们就是把它呢给封装成这么一个粒子集合就可以了那好那这个思路啊有了之后呢那咱们下面呢就来去干嘛呢就来去写一下啊我现在在这打印日啊说生成
[03:13] 当前的这个东西列表然后下面呢咱们就可以去查询了啊查询的话就是用当前的APArticleService而有一个叫做get是吧这个第二个方法是不是查询的是被什么被审核的列表好拿到这个列表之后呢我们接着往下看然后下面该怎么做呢好拿到它之后呢下面该怎么去写呢大家想一想这样啊咱们这样啊
[03:46] 首先呢你要去先获取啊先获取什么呢获取文章列表文章ID列表吧应该是这样说啊文章ID列表然后呢要获取文章中的什么作者ID作者ID列表好吧然后呢是列表啊然后呢你就可以去查阅什么呢
[04:19] 就根据当前的文章ID列表上去查询什么根据啊查询当前的什么配置文章配置列表和文章内容列表好然后还有一个是吧根据当前的作者IDID列表查询列表啊查询什么作者信息
[05:00] 坐在那边吧然后呢然后呢你再去综合一下然后再去综合然后是综合谁啊综合他就把这些数据啊通通都塞到这里边当然他这个呢应该是一个利此集合最终把这利此集合返回就可以了那咱们下面思路说好之后呢下面呢咱们就来去实现一下啊那首先呢咱们要获取文章的D啊怎么怎么去设置呢我们可以用这个流啊比如说
[05:32] 先这个历史机和点有一个stream然后呢是点mapmap啊我们可以找一下说ap article啊这里边啊咱们首先呢是找到一个叫嗯streamvolley off啊volley offvolley off那咱们可以去把当前这个啊转成当前的一个stream啊stream啊ap article点get id嗯然后呢
[06:03] 然后呢你就可以完了啊就to like这样的话呢就能去找到一个集合这个集合呢就是什么呢aparti cled类似吧好吧因为加id啊比较明显些好那这个就算是给你完了啊这个就是文章的ad列表啊这里边找的不就是当前的id吗id最终的找到之后呢把它封装到了一个集合中是吧
[06:33] 好那这是一个啊那这个找的其实也是类似啊也是通过当前这个集合点有一个叫做stream.map还是当前的什么那这样咱们可以去定义当前的AParticle然后呢是找谁呢当前的get有一个叫做authorid知道了吧那咱们可以去分段下啊没等于none吗不等于none的话呢咱们就
[07:04] 这样你反回那我不等于那呢我们就返回当前的getAuth ID这样的话呢咱们就算是定完了定完之后呢这时候呢你说等于那咱们还要吗不要了是吧所以说咱们在这再去加一个过滤然后是X好然后是怎么写呢X不等于什么呢然后呢咱们再去用connect
[07:35] 这样的话就能去返回一个什么返回一个当前的和这个机盒其实就是什么当前的一个什么东西就是一个作者的ID列表怎么叫APAUTHORlist IDlist行那这样设置完了其实咱们还要去设置一个东西是一个东西最终的这个东西咱们可以让他去这样有一个int value
[08:05] 这样咱们就返回的就不是浪了是个intex好吧这样就不用再去转换了好吧那这样那就能获取到已经获取到了作者的ID既然这两个都拿到之后那咱们获取列表呗列表怎么拿首先是AAP首先拿这个config点儿有一个slack的articleids他装的这个列表是吧那就是AAParticleidlist好他返回的就是今天的一个
[08:35] 叫这个AAP article config list好再来一个啊叫AAP content.有一个也是像这个是吧也是这个AAP article id list然后最终它反复的是一个文章的那边文章的那边啊那这两个拿到之后呢还有第三个嗯双击一下啊那第三个呢就是什么呢发行作者的那边那这个也很简单啊AAP author
[09:05] 啊,Service,而有一个Select,啊,Curie,啊,CurieByIDs那这个就是当前的AP Author ID List啊,返回的就是作者的列表信息好吧,行,那这样的话,咱们就算是完了啊那做完之后啊,那最终呢,还要去干嘛呢还要去整合它,是吧,还要整合啊那整合该怎么整合呢,咱们呢,同样的可以用一个这种方式去做啊
[09:32] 那这样咱们可以这么写啊咱们首先呢在这定义一个当前的这种集合啊集合就是他就是他啊然后呢是咱们叫什么呢叫article list等于啥呢等于一个AP啊等于啊AP article list哎没有AP article list吗找找啊那是ID啊ID处理啊我看看啊应该是这个啊这个当前未同步的数据啊
[10:13] 还是用当前的StreamStreamStreamSt好,这里有一个叫什么有一个map咱们还可以去做循环叫AP article好,就这么写然后就可以去设置这里边该怎么去设置这个先这么写不行是吧先这么写我们就可以去拿到里边去NU一个当前的这种数据那NU谁呢
[10:43] new的就是return new一个new一个叫做article就它往里边去设置那怎么设置呢我们先做个封号那怎么设置呢比如说set一个article那这个就是之前的jp article这个就设置完了往里边去设了一个值然后这个还没有完是吧还没有完这只是设了第一个
[11:12] 然后下面咱们还要还会去设置第二个第二个怎么设置可以看咱们要去根据什么根据文章的ID过滤过滤出符合要求的什么内容对象是对象是列表这个怎么办你就是可以这么着你可以去设置一个叫做AP article
[11:45] cp content list咱们还是用一个spam还是用field用它去过滤然后咱们就可以去s.getArticleId然后它等于谁呢等于Article中的getId然后如果说它相等的话这时候咱们就可以去把它通到一个集合中
[12:16] 好那这个集合有可能会有多条数据不可能只有一条数据怎么叫好吧这时候你可以去判断下不可能有多条数据它只能有一条要不然没有要不然只有一条怎么可以去判断下不等于当前的AEP这是S然后呢非什么知道了吧哪个意思
[12:47] 如果它不为空那这时候呢我们就获取一点数据setAP article content那这个呢就是当前的这个集合中的一条数据set0那就可以了那这个呢内容啊咱们就算是设置完了好设置完了啊这个思路啊大家要捋一捋啊然后下面呢咱们会有类似的方式去写不是这么去写的啊第二个呢就是谁啊就是AP放这个
[13:17] 然后点死店然后是点卖破不是卖吧是 filter filter要过滤的呢是一个还是叫s吧我稍微啊然后他然后是他s点get article id点 equals ap article点get id然后呢如果说他是一样的话啊是一样的话啊这时候呢你就可以去让他去找成一个集合那个集合啊这集合呢怎么叫啊
[13:47] 然后你再去判断这个集合到底是否为空啊是空的话肯定是有对象的啊然后不为是他他不为难认得呢是非呗好吧啊AP article configs.isempting它不为空那这时候呢你就可以去set一个叫做config这个就是当前集合中的一条数据啊AP rget0是吧
[14:19] 这样的话咱们就设置完了还有一个还有一个这个还有应该还是最后一个这是第一个第二个这是第三个是吧还有一个那个是啥呢那个就是当前的author list点有一个stream然后点filter这个是应该是一模一样的然后是怎么着s然后是怎么着s.getid
[14:50] 这是文章这是作者的ID然后他要等于谁等于当前的APArticle中的getPost ID加intvalue最好是加intvalue要不然的话他就不是那啥了行这个咱们可以再加intvalue要稍等我看看先前这个东西他首先是当前的APArticle的ID他好没有问题
[15:26] 然后最终的是点 connect 结合好这个集合咱们叫做 AP Authors然后咱们再去判断上面的一样说是 non 不等于当前的什么AP AuthorsAP Authors 按的非不为空是吧AP Authors 变量性多大家一定要区分而意思 Ampli然后就可以去拿到一条数据
[15:58] Z有一个叫做AP Author然后呢就是完了就是把这个数据捞就可以了啊就是他他啊get0好这样数据就算是设置完了啊设置完之后啊那里边你说感觉还少数据吗其实呢还少一个还少一个啊还少哪个呢还可以看一下啊这边呢咱们可以再去设置另外一个啊这边还是可以可以剩下一个就是设置回调
[16:32] 设置回调方法为什么要设置回调方法呢是用户啊方法的回调用于啥呢用于修改同步的然后是插入哪HBase成功之后啊成功后同步状态修改啊好下面呢咱们就可以写写啊我写呢是set一个叫做callback有一个HBase in work
[17:10] 就这个方法我们可以new一个当前的article这个方法一个参数就是aparticle然后第二个你就可以去设立一个参数x-最终的是aparticle serviceaparticle serviceaparticle太多了Service.有一个叫做update把这个s传进去就可以了那这个通路咱们就设置完了
[17:42] 这个咱们先这个分号最终的他要去转成一个集合好这样的话就可以了这个集合有没有咱们还要再去做一个判断好吧判断的意义还是得去查看当前集合里边有没有值不等于当前的集合然后是什么的推现在集合是意思安不得说它不为空这时候我们就可以去打印计划
[18:14] 生成当前的叫什么article quantity是吧然后是列表完成然后是size好size就是当前集合的queryqusqr有一个叫做size好吧不然咱们就微空就微空好 微向还是size
[18:59] 这是生成那边完成也是size但这个size是0啊0啊行最终呢你就把这个集合呢给它返回就可以了行那这样呢这个方法那就算是解完了啊还是挺多还是挺长啊变量涉及的特别多大家呢一定要一定的是细心一些不要把这个变量搞混了好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中使用 Stream API 和服务层方法，将文章、作者、配置等数据聚合为 ArticleQuantity 对象。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 IDEA 中 ArticleQuantityService 接口定义，包含 getArticleQuantityList 和 getArticleQuantityById 方法。
画面 2: 展示 ArticleQuantityServiceImpl 类，定义了私有服务依赖和 getArticleQuantityList 方法。
画面 3: 展示 ApArticleService 类，包含 getSyncArticleList 和 updateSyncStatus 方法。
画面 4: 展示 ArticleQuantityServiceImpl 中的 getArticleQuantityList 方法，使用 Stream API 处理数据。
画面 5: 展示 ArticleQuantityServiceImpl 中的 getArticleQuantityList 方法，使用 Stream API 处理数据，弹出 Lambda 表达式建议。
画面 6: 展示 ArticleQuantityServiceImpl 中的 getArticleQuantityById 方法，弹出方法建议。
画面 7: 展示 ArticleQuantityServiceImpl 中的 getArticleQuantityList 方法，弹出 List<ArticleConfig> 类型的建议。
画面 8: 展示 ArticleQuantityServiceImpl 中的 getArticleQuantityList 方法，弹出 List<ArticleConfig> 类型的建议。
画面 9: 展示 ArticleQuantityServiceImpl 中的 getArticleQuantityList 方法，弹出 List<ArticleConfig> 类型的建议。
画面 10: 展示 ArticleQuantityServiceImpl 中的 getArticleQuantityList 方法，弹出 List<ArticleConfig> 类型的建议。
画面 11: 展示 ArticleQuantityServiceImpl 中的 getArticleQuantityList 方法，弹出 List<ArticleConfig> 类型的建议。
画面 12: 展示 ArticleQuantityServiceImpl 中的 getArticleQuantityList 方法，弹出 List<ArticleConfig> 类型的建议。
画面 13: 展示 ArticleQuantityServiceImpl 中的 getArticleQuantityList 方法，弹出 List<ArticleConfig> 类型的建议。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public interface ArticleQuantityService {
    List<ArticleQuantity> getArticleQuantityList();
    ArticleQuantity getArticleQuantityById(Long id);
}
```

画面 2:
```java
import com.heima.migration.Service.ArticleQuantityService;
import lombok.extern.log4j.Log4j2;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Log4j2
public class ArticleQuantityServiceImpl implements ArticleQuantityService {
    @Autowired
    private ApArticleConfigService apArticleConfigService,
            apArticleContentService;
    private HBaseStorageClient storageClient;

    @Override
    public List<ArticleQuantity> getArticleQuantityList() {
        log.info("生成ArticleQuantity列表");
        List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
        return null;
    }

    @Override
    public ArticleQuantity getArticleQuantityById(Long id) {
        return null;
    }
}
```

画面 3:
```java
public List<Article> getSyncArticleList() {
    return null;
}

public void updateSyncStatus(Article aparticle) {
}
```

画面 4:
```java
@Override
public List<ArticleQuantity> getArticleQuantityList() {
    log.info("生成ArticleQuantity列表");
    List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
    List<String> aparticleIdList = aparticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
    return null;
}
```

画面 5:
```java
List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
List<String> aparticleIdList = aparticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
aparticleList.stream().map(article -> article.getAuthorId() != null ? article.getAuthorId().intValue() : null).filter(Predicate.isEqual(article.getAuthorId())).collect(Collectors.toList());
```

画面 6:
```java
private HBaseStorageClient storageClient

@Override
public List<ArticleQuantity> getArticleQuantityList() {
    log.info("生成ArticleQuantity列表");
    List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
    List<String> aparticleIdList = aparticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
    return null;
}

@Override
public ArticleQuantity getArticleQuantityById(Long id) {
    return null;
}
```

画面 7:
```java
List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
List<String> aparticleIdList = aparticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
List<ArticleConfig> aparticleConfigList = apArticleConfigService.queryByArticleIds(aparticleIdList);
List<ArticleContent> aparticleContentList = apArticleContentService.queryByArticleIds(aparticleIdList);
List<Author> apauthorList = apAuthorService.queryByIds(aparticleIdList);
```

画面 8:
```java
List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
List<String> aparticleIdList = aparticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
List<ArticleConfig> aparticleConfigList = apArticleConfigService.queryByArticleIds(aparticleIdList);
List<ArticleContent> aparticleContentList = apArticleContentService.queryByArticleIds(aparticleIdList);
List<Author> apauthorList = apAuthorService.queryByIds(aparticleIdList);
```

画面 9:
```java
List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
List<String> aparticleIdList = aparticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
List<ArticleConfig> aparticleConfigList = apArticleConfigService.queryByArticleIds(aparticleIdList);
List<ArticleContent> aparticleContentList = apArticleContentService.queryByArticleIds(aparticleIdList);
List<Author> apauthorList = apAuthorService.queryByIds(aparticleIdList);
```

画面 10:
```java
List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
List<String> aparticleIdList = aparticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
List<ArticleConfig> aparticleConfigList = apArticleConfigService.queryByArticleIds(aparticleIdList);
List<ArticleContent> aparticleContentList = apArticleContentService.queryByArticleIds(aparticleIdList);
List<Author> apauthorList = apAuthorService.queryByIds(aparticleIdList);
```

画面 11:
```java
List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
List<String> aparticleIdList = aparticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
List<ArticleConfig> aparticleConfigList = apArticleConfigService.queryByArticleIds(aparticleIdList);
List<ArticleContent> aparticleContentList = apArticleContentService.queryByArticleIds(aparticleIdList);
List<Author> apauthorList = apAuthorService.queryByIds(aparticleIdList);
```

画面 12:
```java
List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
List<String> aparticleIdList = aparticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
List<ArticleConfig> aparticleConfigList = apArticleConfigService.queryByArticleIds(aparticleIdList);
List<ArticleContent> aparticleContentList = apArticleContentService.queryByArticleIds(aparticleIdList);
List<Author> apauthorList = apAuthorService.queryByIds(aparticleIdList);
```

画面 13:
```java
List<ArticleQuantity> articleQuantityList = apArticleService.getSyncArticleList();
List<String> aparticleIdList = aparticleList.stream().map(article -> String.valueOf(article.getId())).collect(Collectors.toList());
List<ArticleConfig> aparticleConfigList = apArticleConfigService.queryByArticleIds(aparticleIdList);
List<ArticleContent> aparticleContentList = apArticleContentService.queryByArticleIds(aparticleIdList);
List<Author> apauthorList = apAuthorService.queryByIds(aparticleIdList);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

