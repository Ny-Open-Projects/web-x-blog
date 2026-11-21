# 21_自媒体文章管理_文章删除后台接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\21_自媒体文章管理_文章删除后台接口开发【海量资源尽在 666java.com】.mp4
- 时长 10分40秒（音频 641s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们来说一下当前文章里边的最后一个接口就是删除文章后台啊删除文章啊那删除文章的话呢咱们还是来去看一下这个接口定义啊这个接口定义现在会比较简单一些啊主要说他们现在是可以去删除那参数呢大家也能想到就是根据某一个ID啊就是当前的文章的ID去删除最终你操作成功的时候你直接返回数据就可以了好吧
[00:26] 那这个MIPR文件里边咱们首先是要定义两个方法第一个方法就是要去查先查查出来之后如果说没有问题那么咱们再去删除再去删除这里边还有一个隐藏的东西就是说咱们需要去删除它的什么当前文章当前文章对应的素材的关系就哪个你不仅要删除这个表
[00:51] 不仅要删除这个表还要删除啥呢还要删除它的一个素材引用的关系表这个表的数据咱们也要删好吧行那咱们下面呢就来去实现这个代码啊首先呢还是要写这个Map这个Map的话咱们这两个方法还要再去诶是去写一下啊开当前的Map接口好放到这之后呢一个是查询啊一个是删除行那这个
[01:17] 查询完之后,咱们下面就可以去稍等,我看看这两方好像是一样的是不是都一样的这个咱们就不用去拼那么多了,拼一个就可以了好吧好,来看一下这个其实就是返回的某一个对象,是吧?
[01:36] 我们就不用管了咱们就用这一个就可以了咱们只需要去订一个删除就可以好吧把它给拷贝一下
[01:47] 这个有了当前的删除的方法咱们就算是定义好了定义好之后咱们下面就写Service那这Service该怎么去写还是打开当前的news Service这里边咱们再定义一个方法这个方法就是删除文章response result然后是dlnews好吧然后参数的话就是刚才说的wmnews.dq
[02:18] 这个是根据主件删除根据主件删除删除文章信息好那这个加完之后啊加完之后呢咱们下面就来写他的实现啊在这再去写放DEL News好拿拿到这个方法之后呢咱们现在就可以去写他的一个方法了这里边啊这边咱们要去简单说一说啊首先咱们要去去查询
[02:52] 查询完之后呢先看一下这个文章到底存在不存在如果说存在啊这样查询文章好第二个呢就是要去判断那啥呢判断文章是否存在文章是否存在存在的话就删除不存在就不删除就是你如果说存在的话咱们还要去判断一个东西啊这个大家可能想不到就是啥呢说中前文章是否审核通过那审核通过的话呢就说明已经在APP上了啊
[03:26] 能够让用户去查看了能够让用户查看的文章咱们也不让他干嘛了也不让他去删除好吧这一个就是要删除文章与素材的关系然后最后呢还是审查文章好吧那咱们一块一块去做在查明之前咱们还是老套路还是得先去判断一下前的参数DTO等于或者是什么DTO
[04:01] 他如果说等一等一难的话他就直接return然后点这写错了是吧这写错了是吧这不要request body这叫response-redout好这个行是吧往上走把这个也改了完之后再回来好
[04:34] 这就没事了啊这时候你可以直接返回responseresult.ir说你参数有问题啊好那这样的话咱们就可以了啊然后接着往下看啊下面咱们就可以去查询了查询的话呢目前这里边已经有二级了所以说这个没问题直接用wmsnewsmapper然后呢是点咱们有一个selectselect news detail就它
[05:08] 你就可以通过tto的getid然后拿到当前的一个文章信息然后呢然后干嘛呢然后的话你就看一下这个文章是否存在就可以那是否存在啊wmnews等于等于那的话啊咱们就还是说你这个啊有问题有问题呢就说你的文章不存在是啊嗯说数据不存在啊文章不存在在这写吧文章不存在好吧
[05:43] 如果说他都没事,没事的话呢,咱们还要再去判断啊判断什么呢,判断当前的这个状态有一个叫什么来着Status, that status该Status是亮啊,咱们还是打开这个表啊,来看一下今天的文章呢,你看审核审核通过呢是8审核通过是8那这个的话咱们就那啥了啊如果说你要审核通过的话呢,咱们就不会那啥了就不会再让他去删除了
[06:13] 不让他再以下图那这是怎么写呢就这个咱们在这个当前的有一个东西WM News Constance里边有一个有一个常量叫WM News我看啥是哪个呢就是Status没有是吧有有这个是8如果说是8的话就是审核通过的话
[06:52] 这会儿还用写不行是吧这样啊这样咱们把它给考出来考出来之后呢.EqualsEquals啊把当前的状态装进去不说是已经审核通过的话呢咱们就提示一句话说你这个东西啊你不能删除不能删除啊大家在这写啊写这什么呢当前的DisponseResult.Era是吧是App
[07:23] 算数有问题然后呢是什么当前文章通过审核不可删除通过审核不可删除好吧就结束了啊行那这个好像逻辑上还不太不太严谨啊这里边咱们还要再去多判断一个东西啊嗯这里边还有个算数啊还是当前的然后是有一个WM
[07:56] news哪个呢这里边是有一个pubpublish已经发布的已经发布的这个这个呢其实它是一个已经发布的话呢他们也应该删除啊所以说咱们还要再去判断一下还是谁呀还是wnews.getstaters好吧两个八或者九的话呢你看啊那个表里边八或者九这是再发布这已经审核通过了啊
[08:25] 还有一个再发布的状态都已经审核通过的这种状态那这时候那这个文章就不应该被删除所以说啊这两个你要盘的两次好吧嗯行那这个啊这个是上面好然后下面的话如果说都没事那咱们现在就可以删除关系了啊WM News然后他东西啊然后打二有一个列表这是谁呀这个就是news id我们就可以把你谁呀WM News的什么it id
[08:56] 传过去这个就是文章ID好吧那最终呢咱们可以再去删除wm-news-map.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github.github
[09:25] 这个Service咱们就算是写完了写完之后这时候咱们还要再去写它的接口这个接口打开再去加一个方法public response without然后是blnews然后这里是什么WMNewsDQ加上之后咱们在这加注释注释叫删除文章这时候咱们可以开这
[09:55] 再去把这个列把这个方法给重写一下dl news他好呃全吧嗯这里边叫怎么着是pulse他卖屏然后怎么着这是叫dlnewws啊好那在这去加一个什么request body完事啊最终呢嗯错了啊request body然后呢是调用当前的Service方法就可以了啊elite然后把这个u装进去
[10:30] 最终咱们这个机口就算是解完了一会咱们来整合前端一会把这三个机口统一测试一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import com.heima.model.media.Mapper.WmNewsMapper;
import com.heima.model.media.Service.WmNewsService;
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

