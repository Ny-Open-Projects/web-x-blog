# 08_自媒体_素材管理_删除图片接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\08_自媒体_素材管理_删除图片接口开发完成【海量资源尽在 666java.com】.mp4
- 时长 16分7秒（音频 967s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来完成这个接口就是叫删除图片的接口那这接口感觉还挺简单的是吧咱们根据当前的ID去删除图片就可以了但这里边还有一个东西咱们要说一说啊看一看啊前呢是有一个什么此接口用于删除无关联图片的无关联的图片然后这时候里边呢是有一个关联的一个操作啊这个来看一下这个接口吧
[00:27] 首先是有一个地址是吧没啥可说的然后下面 DTO DTO 的路径有问题拷贝一下直接去搜一下就是他里边只有一个 ID咱们可以把当前的路径给拷贝一下把它给替换了好这里边是咱们有说了就只有一个图片的 ID当前应该是 material里边的 ID
[01:00] 然后最终呢咱们是可以响应一个成功的字幕块如果说删除成功了但里边有一个说了是一个无关联那到底关联谁呢咱们呢可以再看一下这个表啊来打开这个表这个表呢其实就是咱们存图片的这个表是吧比如这个表啊这就是一个图文的资源表是吧但这里边还有一个表啊这个表呢是这个表里边有个WM News Material就它打开它打开它之后呢你会发现啊这里边有几个字段我们来
[01:31] 过一下啊首先ID没啥可说的是吧然后好你看这儿啊这有一个material ID还有一个news ID那这啥意思呢咱们重点去说说这个东西啊首先呢那这块内容啊这块内容呢其实就是某一个文章的ID某一个发布的文章的ID然后这个呢就是当前文章引用的图片当前文章引用的图片信息所以说呢如果说当前这个图片啊
[01:57] 图文信息图文图图片的被一个文章引用了那你说这个图片还能删除吗是不是就不能删除了对吧所以说啊咱们在这删除当前这个这个某一个ID之前呢你得先去到这个表中去查看看有没有数据如果说有数据那就说明啥呢就说明已经被文章所引用那所引用的文章那所引用的这种图片还能删除吗就不能删除了当然这里边要是找不着的话呢咱们可以随便删
[02:27] 好吧行那就是这么个思路啊那咱们下面呢就来去完成当前的这个接口啊首先啊咱们还是要去呃先去那啥先去写咱们的麦克文件啊那这里边呢咱们这又加两个方法第一个呢是查询啊查询就根据主页查询这这个查询谁啊这个先查询的是这个表啊先查询的这个表啊然后第二个呢是要根据当前的主页去删除啊这两个表啊这两个方法先加进来
[02:56] 好找到当前的这种model下边当前的方法啊那Map文件打开Mapos下边VMedia然后是哪个第一个是吧好把它两个方法加进来啊加进来之后呢咱们下面呢就可以去把这Map文件给写下啊好拷贝一下啊这有一个Radio的Map咱们先把这个Radio的Map和Circle先拷过来啊拷到最上边
[03:26] 考过来之后咱们现在就可以把这两个方法给考过来一个是查询一个是删除比较简单一个就是根据当前的主件去查询某一个对象第二个是根据主件去删除好吧就是两个方法但这里边还有一个就是你是不是这个表也得有一个Map文件是不是要根据当前的资源的ID去查询是吧所以说咱们在这要再去创建一个
[03:57] 另外一个麦克风啊往下走怎么还需要去再创建另外一个麦克风啊只是需要一个插序就可以了打开当前的麦克风然后在这去拷贝一个啊那这个你看这个的话就是根据当前的MID就是MATRIOID就是刚才我选中的这一列然后去count去count啊看看有没有值如果说有值的话就不能删除了啊所以说啊咱们这个呢主要就是根据当前的条件去去查询就可以好吧来咱们把这个麦克风文件写一写找到这
[04:31] 保贝一份然后是网上下面是什么在这只需要去加一个什么加一个news完事了好吧点ok把内容给它干掉wm news material好吧下面咱们就来去把这个东西给回过来里边只是一个count你看就是当前的是这个表因为当前的条件是material id
[05:03] 然后呢是看到0如果说它大于0的话肯定是有值有值的话咱们就不能删除了好吧这个思路大家一定要知道啊行那咱们下面呢就来去写咱们的Service代码啊Service的话咱们在这啊还是在咱们之前的这个Service中去写就可以好吧还是打开当前的哪个呀当前的media找到Service来还是它啊咱们在这再加个方法
[05:34] 因为现在咱们都是一些素材管理啊所以说直接在这写就可以了这删除图片啊response result然后是dlpicture好吧根据啥呢根据刚才说了当前的什么wmmetriccto这里边只有一个字段啊字段呢就只有一个id的字段啊那这个呢是一个删除图片啊写下
[06:05] 删除图片好吧行那咱们下面就来去写它的直线这个DELEPICTURE就它好吧首先呢你要在这注入进来一个东西注入进来谁呀WMNEWSMATRIU先把它给注进来因为咱们需要先去查一次别错了什么罗阳是吧行那这个注进来之后咱们下面呢就可以去写咱们的右逻辑代码了
[06:40] 那这代码怎么写呢套路还是一样的首先呢你还是得先去判断一下当前有没有登录对吧咱们在这先去拿到当前的用户名wm-sri.local.get-user然后呢在这写啊然后这就是user这就是user啊然后下面呢咱们就可以直接去写了那写啥呢咱们还是先去判断当然咱们可以先写个思路啊那首先呢咱们要去干嘛呢
[07:11] 删除fast dfs中的什么图片删除之前呢你要先干嘛呢先去判断汤田图片有没有什么分联往下走啊如果说你删除成功之后呢你还要删除谁啊要删除一个wm看什么mattery小充的什么数据如果说它没有关联这时候呢咱们都可以去往下去删除了啊
[07:43] 首先还是得先去判断一下到底有没有关联好吧那咱们下面就写下首先还是透露首先还是得去判断当前的参数do.getid如果说他等于等一样的话或者是do.getid等一等一样那这时候咱们就直接返回参数错误就可以了好吧response response.error
[08:18] 你的参数有问题参数非法就可以了好吧然后再往下再往下的话咱们就可以真正删除了那上述之前说了先去判断是吧判断之前呢咱们先去查一次wm.mapleslag先去根据主件去发寻dto.getid好拿到这个对象之后呢咱们就可以判断了如果说啊它等于等于呢就是没查着怎么办呢没查着肯定是有问题是吧咱们可以直接去对称
[08:50] 还是当前什么还是当前你的参数你的参数根本就没有查着当前的一个素材啊好说你能查着没问题再去查看当前有没有过年那有没有过年怎么查呀跟他说了就是wmnewsmyper吧他是吧darkconkid记住他就是谁呀就是当前的他什么ID是吧
[09:21] 你用它是不是也行啊用它是不是也可以啊都可以啊行最终的就能拿到一个count好咱们去判断啊如果说count大于0大于0是不是有值啊有值还能删除吗有值是不是就不能删除了是吧所以说咱们在这直接去返回就可以了说return还是这个东西是咱们这要去提醒一句话是吧在这可以直接去提醒一下提醒啥呢
[09:55] 说你的当前图片被引用你不能删除然后再往下如果说你这块都没事他也没查着是吧这时候咱们就可以去获取或者说真正的到FastDBS中去删除那这个你看有一个咱们之前是不是注入了一个FastClientFastClient REL是不是可以根据当前的文件ID去删除没问题那文件ID是谁
[10:25] 文件ID是不是就是当前的getURL吧当然这个咱们报纸也可以这个URL是不是就是当前的一个某一个上传文件ID你可以看一下比方说你看这里边是不是有URLURL是不是这个就是文件IDOK那这个就是文件ID所以说你这么写是没有问题的好吧当然咱们为了防止出问题所以说咱们在这可以直接去这么写比如说
[10:59] 报错先看一下先穿一下好吧咱们就在这去定义一下String的什么FillID等于啥呢等于然后咱们可以直接去在这写ReplaceAll然后第一个要替换谁呢要替换的是比如说你万一有你写了你在存的时候你写了一个
[11:30] 服务器的地址前面写的服务器的地址最终你要是删除发色D144的时候删除文件的时候调用它去删除的时候你不能带这个当前的图片的服务器地址所以说怎么在这先去替换一下防止出问题是吧在这写怎么写非要有R替换成谁替换成空替换成空最终的这个文件ID其实就是
[11:56] 真正的文件ID好吧当然现在目前的话你替换也没有问题因为咱们目前的数据没有在当前的什么图图片服务器的地址是吧万一你要是弄错了那这时候你删除的时候有可能会删除删除失败所以说咱们在这严谨一些在这去加了这么个东西好吧然后再往下看如果说你这时候都已经删除了都已经删除成功了如果说要是删除不成功的话咱们在这还可以再去披露一下日志
[12:23] 这个制度咱们还是按照之前的方式去记录啊log error然后呢咱们直接写user加一号啊user那个user啊好往下走然后呢是delete然后view哪个view啊咱们可以在这写然后下面说啥呢flom fast fast dfs好吧然后呢是错误然后再往下啊就是error infer
[13:00] 冒号恩还可以去把日志给打印把异常信息打印一下这三个是什么user.getid第二个呢是当前的fewid好吧第三个呢你可以直接写一点getmythed好吧这样的话就把这个信息给打印了一下最终的如果说还是出问题咱们可以直接去returnreturn一个server一长是吧记得吧response.什么
[13:29] 然后是app http然后这怎么写啊写一个server error是不是服务器内部异常啊OK啊OK那这样的话就可以了啊最终啊你这个说你现在目前已经在fastdms中删除了所以说你在这怎么着你是不是也得在表中去删除啊我到当前这个表方式delete你谁啊你dto.getid是不是就你他去删除就完事了你直接返回谁啊
[14:00] RaceBounceWithoutOK分KD可以写一个APPHTTP它有一个success说是操作成功咱们这么写也可以最终咱们这个代码就写完了写完之后咱们下面就可以去写一下咱们的controllercontroller还是老套路咱们还是先在这定义它的一个什么
[14:31] 接口打开桑琴的media然后再这个什么他桑琴队的一种啊再去写一个啥呢叫response写全网publicresponse然后是dlpict这是啥意思wm matter roomdto好dto完了这个呢就是叫他这个呢就是删除图片
[15:09] 这个设置完之后啊咱们在这啊这个control中顺便写完来打开它打开它然后在这去写什么dl一个车是吧好完之后呢咱们在这去写个路径路径是谁啊pulse的买品然后呢怎么写啊这是dlp i c d u r e最终啊这个这边啊你要注意了
[15:38] 上面你不加request body是可以的但这时候你要接收参数的话你得去加什么request body好吧就别忘了然后加完之后咱们就可以去调用Service了这个Service咱们已经有了直接去拷贝一下RDL把当前DTO装进去就完事了好吧目前这个接口就算是解完了咱们一会再测一会把这个写完之后咱们统一到前台去集成连条再去测试好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现删除图片功能，包括接口定义、Mapper层、Service层和Controller层的代码编写与逻辑处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示删除图片接口的文档定义，包含接口名称、请求/响应DTO结构，以及参数错误码定义。
画面2：在数据库中查看 wm_news_material 表的数据，用于验证删除操作。
画面3：展示 WmMaterialMapper 接口定义，包含 selectByPrimaryKey 和 deleteByPrimaryKey 方法。
画面4：展示 WmNewsMaterialMapper.xml 映射文件，包含 selectById 和 deleteById 的 SQL 语句。
画面5：展示项目结构，确认 WmNewsMaterialMapper.xml 文件位于 resources/mappers/wemedia 目录下。
画面6：展示 MaterialService 接口定义，包含 uploadPicture 方法。
画面7：展示 MaterialServiceImpl.java 文件，定义了 uploadPicture 方法的实现。
画面8：展示 MaterialServiceImpl.java 文件，定义了 delPicture 方法的实现。
画面9：展示 MaterialServiceImpl.java 文件，编写 delPicture 方法的业务逻辑，包括校验和删除操作。
画面10：展示 MaterialServiceImpl.java 文件，编写 delPicture 方法的业务逻辑，包括校验和删除操作。
画面11：展示 MaterialServiceImpl.java 文件，编写 delPicture 方法的业务逻辑，包括校验和删除操作。
画面12：展示 MaterialServiceImpl.java 文件，编写 delPicture 方法的业务逻辑，包括校验和删除操作。
画面13：展示 MaterialManageControllerApi.java 文件，定义了上传图片和删除图片的接口。
画面14：展示 MaterialManageController.java 文件，实现上传图片和删除图片的接口。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
4.3 删除图片接口
4.3.1 接口定义
(1) 基本定义
此接口用于删除相关的图片。
参考标准 请参考通用接口1规范
接口名称 /api/v1/media/material/del_picture
请求DTO com.heima.mysql.material.core.model.dtos.WmMaterialDto
响应DTO { "host": null, "code": 0, "error_message": "操作成功", "data": "SUCCESS" }
(2) CODE定义
PARAM_INVALID
PARAM_INVALID(501,"无效参数")
SERVER_ERROR
SERVER_ERROR(503,"服务器内部错误");
```

画面3：
```
package com.heima.model.mappers.wemedia;
import com.heima.model.media.pojo.WmMaterial;
public interface WmMaterialMapper {
    int insert(WmMaterial record);
    WmMaterial selectByPrimaryKey(Integer id);
    int deleteByPrimaryKey(Integer id);
}
```

画面4：
```
<resultMap id="Base_Column_List" type="com.heima.model.media.pojos.WmMaterial">
    <id column="id" property="id" />
    <result column="user_id" property="userId" />
    <result column="type" property="type" />
    <result column="is_collection" property="isCollection" />
    <result column="created_time" property="createdTime" />
</resultMap>
<select id="selectByPrimaryKey" resultMap="Base_Column_List" parameterType="java.lang.Integer">
    select * from wm_material where id = #{id}
</select>
<delete id="deleteByPrimaryKey" parameterType="java.lang.Integer">
    delete from wm_material where id = #{id}
</delete>
```

画面5：
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0.0" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="com.heima.model.mappers.wemedia.WmNewsMaterialMapper">
</Mapper>
```

画面6：
```
public interface MaterialService {
    ResponseResult uploadPicture(MultipartFile file);
}
```

画面7：
```
@Override
public ResponseResult delPicture(WmMaterialDto dto) {
    if(dto == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    WmMaterial wmMaterial = wmMaterialMapper.selectByPrimaryKey(dto.getId());
    if(wmMaterial == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    int count = wmNewsMaterialMapper.countById(wmMaterial.getId());
    if(count > 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "当前图片被引用");
    }
    return ResponseResult.okResult(wmMaterial);
}
```

画面8：
```
@Override
public ResponseResult delPicture(WmMaterialDto dto) {
    if(dto == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    WmMaterial wmMaterial = wmMaterialMapper.selectByPrimaryKey(dto.getId());
    if(wmMaterial == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    int count = wmNewsMaterialMapper.countById(wmMaterial.getId());
    if(count > 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "当前图片被引用");
    }
    return ResponseResult.okResult(wmMaterial);
}
```

画面9：
```
@Override
public ResponseResult delPicture(WmMaterialDto dto) {
    if(dto == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    WmMaterial wmMaterial = wmMaterialMapper.selectByPrimaryKey(dto.getId());
    if(wmMaterial == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    int count = wmNewsMaterialMapper.countById(wmMaterial.getId());
    if(count > 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "当前图片被引用");
    }
    return ResponseResult.okResult(wmMaterial);
}
```

画面10：
```
@Override
public ResponseResult delPicture(WmMaterialDto dto) {
    if(dto == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    WmMaterial wmMaterial = wmMaterialMapper.selectByPrimaryKey(dto.getId());
    if(wmMaterial == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    int count = wmNewsMaterialMapper.countById(wmMaterial.getId());
    if(count > 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "当前图片被引用");
    }
    return ResponseResult.okResult(wmMaterial);
}
```

画面11：
```
@Override
public ResponseResult delPicture(WmMaterialDto dto) {
    if(dto == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    WmMaterial wmMaterial = wmMaterialMapper.selectByPrimaryKey(dto.getId());
    if(wmMaterial == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    int count = wmNewsMaterialMapper.countById(wmMaterial.getId());
    if(count > 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "当前图片被引用");
    }
    return ResponseResult.okResult(wmMaterial);
}
```

画面12：
```
@Override
public ResponseResult delPicture(WmMaterialDto dto) {
    if(dto == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    WmMaterial wmMaterial = wmMaterialMapper.selectByPrimaryKey(dto.getId());
    if(wmMaterial == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    int count = wmNewsMaterialMapper.countById(wmMaterial.getId());
    if(count > 0) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "当前图片被引用");
    }
    return ResponseResult.okResult(wmMaterial);
}
```

画面13：
```
public interface MaterialManageControllerApi {
    /**
     * 上传图片
     */
    @PostMapping("/upload_picture")
    public ResponseResult uploadPicture(MultipartFile file);
}
```

画面14：
```
@Controller
@RequestMapping("/media")
public class MaterialManageController {
    @Autowired
    private MaterialService materialService;

    @PostMapping("/upload_picture")
    public ResponseResult uploadPicture(MultipartFile file) {
        return materialService.uploadPicture(file);
    }

    @PostMapping("/del_picture")
    public ResponseResult delPicture(@RequestBody WmMaterialDto dto) {
        return materialService.delPicture(dto);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

