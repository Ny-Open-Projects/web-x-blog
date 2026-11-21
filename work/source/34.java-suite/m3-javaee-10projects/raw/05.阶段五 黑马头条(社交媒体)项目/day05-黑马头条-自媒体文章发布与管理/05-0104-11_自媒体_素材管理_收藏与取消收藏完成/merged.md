# 11_自媒体_素材管理_收藏与取消收藏完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\11_自媒体_素材管理_收藏与取消收藏完成【海量资源尽在 666java.com】.mp4
- 时长 14分47秒（音频 888s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来完成素材管理里边的最后一个接口就是收藏与取消收藏接口咱们还是来看一下当前的这个接口的定义这里边是有两个院一个是收藏一个是取消收藏一个收藏一个取消收藏然后他请求的这种DTO呢是当前这个DTO成功之后呢咱们只需要去返回成功就可以了就那么简单
[00:28] 当然这里边是有两个方法大家一定要知道然后下面这个里边有什么参数咱们可以看一下这参数的话其实只有一个就是只是当前的一个什么素材的ID素材的ID当然如果说你拿到ID之后如果说你调用的是这个方法那就是收藏如果说调用的这个方法那就是取消收藏好吧那行那么下面就来去完成当前的MapMap里边只有这么一个方法
[00:56] 就是说你可以去修改当前的状态第一个就是你要是修改的是谁修改的是哪一条数据然后它的登录的ID是谁应该是用户ID是吧还有你到底修改成啥咱们应该是这个其实类型的话就是你是否会收藏好吧这个type就是是否会收藏你要传一个0或者1过来0就是未收藏1就是收藏那行咱们还是去找到当前的这种Maple文件
[01:26] 不是这个应该是这个反过一下然后在这去加个东西加一个方法这你看首先在这你还要注意它这个是含了多个参数所以说你在这你需要去把这个通一下到底是哪个参数区分一下好改完之后咱们就可以去写当前的什么Map文件Map文件的话只是一个修改好拷贝来看一下
[02:00] 首先这一块是你要去修改当前这个东西然后主要是修改是当前的这个e-collection它默认是0目前你刚加进去肯定就是0然后你点收藏的话它就会把这个改成1然后给你什么条件条件就是当前的用户ID跟当前的素材的ID好吧行目前的话咱们就写到这然后下面咱们就来去写Service这个Service的话咱们还是在之前的Service中去写就可以找到它
[02:28] 在这去定义一个方法public不用写publicresponse result然后是什么叫changecloser material然后是scissors好吧然后这个方法名虽然有点长但是能够看明白然后下面咱们需要去传两个参数两个参数然后第一个参数就是当前的dto当前这个dto好第二个参数其实就是谁
[03:02] 是前面一个什么叫shout type好吧这个shout好像有点问题是吗没问题这个其实就是修改状态就是收藏或取消收藏好吧下面咱们就来去写它的实现实现的话其实比较简单咱们在这写一下什么change user然后怎么写
[03:37] 我们在这直接去判断就可以了我说首先在这一幅一下BTO每一段银道或者是什么了BTO.GETID因为它只有一个参数啊BTO.GETID可以吗这个参数咱们写错了啊参数写错了找到当前的上面这个东西啊这个应该是它不应该是它WM MatterView是这个东西啊那咱们继续啊
[04:10] 这东西咱们要去换下了啊这东西啊然后那dto.getit如果说他也等于那然后呢咱们就直接return就可以了好吧return response result.irror然后怎么写啊给你的参数非法是吧app那完事了啊那行那这个设完之后啊咱们下面呢就可以去获取用户信息获取用户信息然后呢
[04:43] 我会去会去会去怎么怎么会去wm Thread local是吧点get user点然后最终是拿到一个useruser之后啊咱们就可以干嘛呢可以去调用当前的麦克风里边是有一个叫什么叫update第一个参数是谁啊这个参数是dto点get id然后第二个参数是user点get id第三个参数是type是吧能听啊最终你就能去返回一个东西但是你不返回现在没事是吧
[05:13] 好那到这其实成功了成功之后咱们就可以直接去返回了叫raisebondsok responseok为什么我们可以直接返回一个成功success好这样就算是完成了这个Service还是比较简单的然后下面咱们就来去写搭的一个什么写他的一个接口这个接口API找到他的APIAPIAPI那这API里边写几个方法想想
[05:44] 刚才说了咱们在这是不是要去写两个请求所以说咱们在这去写两个第一个是public response without然后是什么flex tlone material然后这个是叫什么收藏一会咱们再去说一个取消叫wmatterlue DTODTO 完事那行那这个咱们稍等这是收藏
[06:18] 下面还有一个取消收藏拷贝一下是取消收藏前面咱们加一个扛数好吧CNCL这是C大写好这个就是取消收藏这时候咱们就可以写它的扛出了扛出了的话这样我们在这再去加一个CONNECTON没有吗METRIL我看看
[06:57] c u l l e c t o nm i t r就这个好这是一个其实还有第二个是吧咱们把第二个给写上什么c u l l e c t o n这个好吧两个方法我们就算是解完了解完之后咱们在这先去加一个东西叫postmyping这里边是什么这是收藏是吧c t好吧取消取消的话也很简单postmyping写错了
[07:34] Bust My Ping然后怎么写啊下面是杠是Console这样的话就算是取消这时候咱们它这个取消跟收藏说错了啊收藏和取消收藏它这个参数是不太一样的参数不太一样的咱们这样咱们可以直接去调一下方法打什么打一个change一个是DTO
[08:05] 第二个呢二个的话就是当前的一个零或者一是吧比如说咱们传这个零他不是啊他是一个零直接传零就可以了啊零的话你需要去强转一下叫什么小少这样是不是可以啊他这样就没问题了然后下面这个呢下面这个也是返回他但是这个是这是零啊这是这么一个一啊这么一个一能破了啊取消的话是零设置为零这个是设置为一设置为一
[08:36] 好吧那行那这样的话咱们就算是设置完了这样写死还是不太好写死还是不太好啊据说咱们在这去定义一个什么定义一个常量咱们可以打开看一下这里边其实已经写了在这定义一个常量这个常量的话就在当前common下边这个包下边去定义一个常量咱们把它拷贝一下拷贝完之后打开当前的common在这去写然后这里边好像少一个包是吧咱们在这去加上
[09:12] 叫MediaConstants再一个帮叫MediaConstants然后呢咱们可以把这个列直接拷过来之后呢都可以大概看一眼啊咱们目前用到的就有两个一个是收藏是一一个取消收藏是零是吧所以说咱们在这啊Ctrl中就可以这么写了看这列啊WebMediaWM Media
[09:47] 我们的收藏是什么收藏是qllcollectmaterial好是一个啊第二个呢第二个是还是wmd.com.socollectmaterial这样的话参数就算是设置完了啊设置完之后啊这个咱们就算是开发完了但这个东西啊你还得再去加一个request body啊
[10:21] 好那边开发完之后呢你可以去重启一下当前的接口稍等重启一下当前的服务啊好正在重启稍等一下啊重启完之后呢咱们可以打开当前的这块这个位置啊刷新一下刷新完之后呢你可以点一下比如说我去这按钮其实就是收藏点一下收藏是不是操作成功了你可以在当前这个地儿去查看当前已经收藏的图片或者叫素材比如我再去收藏一个啊
[11:02] 我把它也给收藏了收藏完之后你可以看一下当前是不是两个呀当然我也可以取消我不要它了好吧你看点一下收藏是不是就剩一个了没问题当前这个功能是没有问题的好吧那咱们下面来看一下当前前台的代码的流程咱们还是打开当前这个MetalView.Vue.Win页这一面然后这里边其实有一个方法这个方法来看一下找到当前的哪个就这个就这个
[11:34] 这个其实就是一个按钮这个按钮的话就是当前的这个方法这个方法你可以搜一下往下搜好往下走好其实就这个方法这个方法里边你看它传的时候是这么传的它首先是拿到当前的默认值这个默认值我可以告诉你就是一个0默认值是0应该不是0应该是获取到当前图片的一个这种事物收藏因为这个应该是从数据库中去读出来的
[12:04] 好吧然后去判断如果它等于1那就是0如果说等于0那就是1它不等于1的话肯定是0所以说咱们就要设置为1正常是相反也就是说你要是0我就改成1你要是1我就改成0就这么个效果然后最终咱们会是调用了当前的一个API接口然后是把这个参数给传过来了传过来之后它是最终是调了public.js咱们可以往下看
[12:32] 找到当前收藏和取消他就会去判断当这一侧中当前这个材数到底是0还是1如果是0的话你看如果说是等于0的话其实就是当前这个URL如果说是1的话就是这个URL这个URL其实就是啥呢就是收藏这个就是取消收藏最终是把URL传过去最终就能发的抢求了据猜他其实也是区分了URL去发的抢求好那这个是不是没问题
[13:00] 行这个咱们就收藏和取消取消收藏咱们就说到这但这里边还有个东西咱们再简单说一说全部他默认是加载全部你可以点收藏点收藏的时候这个按钮它会去变一些值好代码到底是咱俩控制的可以看一下还是打开当前的view当前页面页面里边的上面其实有两个按钮一个按钮就是叫全部一个是收藏
[13:28] 它这里边是绑定了一个变量叫v-modal当你点全部的时候它是一个video看到了吗只能选一个是吧要不然就是0要不然就是1全部就是01收藏就是1就会给它复制同时呢只要一旦改变它就会触发这个方法也就是说你可以往下看它一旦触发这个方法之后就是当前的这个load date然后呢这个值它就会改变因为刚才说了它已经做了一个
[13:57] 双向的绑定是吧双向绑定啊不是零又是一你点收藏的时候他就是在这啊在这在这传的就是一那你这时候你查询的时候就是只是查询啥呀只是查询的当前已经收藏的所有的这种数据好吧当然这个麦封文件咱们之前写过可以简单的回顾一下啊打开当前的哪块的说的啊嗯打开的麦封
[14:27] 麦克风里边你看当前获取列表的时候是不是加了一个条件呢看它到底是不是等于一等于一的话就是去加上条件如果不等于一就是查询所有内容是吧行啊那目前的这个素材管理这一块啊咱们这个所有内容都已经讲完了好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现图片管理模块的收藏与取消收藏功能，包括接口定义、服务层逻辑、控制器层代码及前端交互逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示接口文档，定义收藏和取消收藏接口的请求/响应规范，包括接口名称、DTO类、响应状态码。
画面2：展示服务层代码，定义分页查询和删除图片的方法。
画面3：展示服务层代码，实现根据状态查询图片列表并返回数据。
画面4：展示服务层代码，实现根据状态修改图片状态的方法。
画面5：展示服务层代码，通过用户ID获取用户信息并更新图片状态。
画面6：展示控制器层代码，定义分页查询和删除图片的接口。
画面7：展示控制器层代码，定义删除图片、分页查询和收藏接口。
画面8：展示控制器层代码，定义收藏和取消收藏接口。
画面9：展示项目结构，定位到控制器层代码。
画面10：展示控制器层代码，为收藏和取消收藏接口添加常量。
画面11：展示前端页面，显示图片管理界面，包含收藏按钮。
画面12：展示前端Vue代码，实现收藏和取消收藏的逻辑。
画面13：展示前端Vue代码，定义收藏和删除图片的图标和数据结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
4.5 收藏、取消收藏接口
4.5.1 接口定义
(1) 基本定义
此接口用于标记系列图片收藏、取消收藏等操作。
参考标准  请参考通用接口规范
收藏接口名称  /api/v1/media/material/collect
取消收藏接口  /api/v1/media/material/cancel_collect
请求DTO  com.heima.model.media.dto.WmMaterialDto
响应DTO  {"host": null, "code": 0, "error_message": "操作成功","data": "SUCCESS"}
(2) CODE定义
PARAM_INVALID  PARAM_INVALID(501,“无效参数”)
SERVER_ERROR  SERVER_ERROR(503,“服务器内部错误”)
```

画面2：
```java
//上传图片
@Request
public ResponseResult uploadPicture(MultipartFile multipartFile);

//删除图片
@Request
public ResponseResult delPicture(WmMaterialDto dto);

//分页查询列表
@Request
public ResponseResult findList(WmMaterialListDto dto);
```

画面3：
```java
List<WmMaterial> datas = wmMaterialMapper.findListByIdAndStatus(dto, uid);
datas = datas.stream().map(item -> {
    item.setUrl(fileServerUrl + item.getUrl());
    return item;
}).collect(Collectors.toList());
int total = wmMaterialMapper.countListByIdAndStatus(dto, uid);
Map<String, Object> resDatas = new HashMap<>();
resDatas.put("curPage", dto.getPage());
resDatas.put("size", dto.getSize());
resDatas.put("list", datas);
resDatas.put("total", total);
return ResponseResult.okResult(resDatas);
```

画面4：
```java
@Override
public ResponseResult changeUserMaterialStatus(WmMaterialDto dto, Short type) {
    if (dto == null || dto.getUid() == null) {
        return ResponseResult.errorResult(501, "无效参数");
    }
    return null;
}
```

画面5：
```java
@Override
public ResponseResult changeUserMaterialStatus(WmMaterialDto dto, Short type) {
    if (dto == null || dto.getUid() == null) {
        return ResponseResult.errorResult(501, "无效参数");
    }
    //获取用户信息
    User user = WmThreadLocalUtils.getUser();
    wmMaterialMapper.updateStatusById(dto.getUid(), user.getId(), type);
    return null;
}
```

画面6：
```java
//分页查询列表
@Request
public ResponseResult findList(WmMaterialListDto dto);
```

画面7：
```java
@Override
@PostMapping("/del_picture")
public ResponseResult delPicture(WmMaterialDto dto) {
    return materialService.delPicture(dto);
}

@Override
@PostMapping("/list")
public ResponseResult list(@RequestBody WmMaterialListDto dto) {
    return materialService.findList(dto);
}

@Override
@PostMapping("/collect")
public ResponseResult collectionMaterial(WmMaterialDto dto) {
    return materialService.changeUserMaterialStatus(dto, 1);
}

@Override
@PostMapping("/cancel_collect")
public ResponseResult cancelCollectionMaterial(WmMaterialDto dto) {
    return null;
}
```

画面8：
```java
@Override
@PostMapping("/collect")
public ResponseResult collectionMaterial(WmMaterialDto dto) {
    return materialService.changeUserMaterialStatus(dto, 1);
}

@Override
@PostMapping("/cancel_collect")
public ResponseResult cancelCollectionMaterial(WmMaterialDto dto) {
    return null;
}
```

画面9：
```
src
├── main
│   └── java
│       └── com
│           └── heima
│               └── common
│                   └── media
│                       └── Controller
│                           └── MaterialManageController.java
```

画面10：
```java
@Override
@PostMapping("/collect")
public ResponseResult collectionMaterial(WmMaterialDto dto) {
    return materialService.changeUserMaterialStatus(dto, WmMediaConstants.COLLECT_MATERIAL);
}

@Override
@PostMapping("/cancel_collect")
public ResponseResult cancelCollectionMaterial(WmMaterialDto dto) {
    return materialService.changeUserMaterialStatus(dto, WmMediaConstants.CANCEL_COLLECT_MATERIAL);
}
```

画面11：
无代码或配置。

画面12：
```javascript
//收藏图片
async collectImg (img) {
    let isCollected = this.imgData.list.find(item => item.id === img.id);
    if (isCollected) {
        isCollected = false;
    } else {
        isCollected = true;
    }
    await collectOrCancel(img.id, isCollected);
    this.$forceUpdate(); //强制更新
    this.$message({type: 'success', message: '操作成功'});
}

//删除图片
async delImg (img) {
    let result = await this.$confirm('确认删除该素材？');
    if (result) {
        await delImg(img.id);
        this.$message({type: 'success', message: '删除成功'});
        this.loadData();
    }
}
```

画面13：
```javascript
export default {
    name: 'material',
    data () {
        return {
            collectIcon: require('@/assets/collect.png'), //收藏图标
            collectSelectedIcon: require('@/assets/collect_select.png'), //收藏选中图标
            delIcon: require('@/assets/del.png'), //删除图标
            total: 0,
            currentPage: 1,
            pageCount: 0,
            pageSize: 15,
            imgChange: false, //根据上传图片导致图片状态变化，此次采用来控制是否在关闭后要进行重新加载
            showPicDialog: false,
            activeSelect: '0',
            imgData: [], //存储图片数据，同时作为收藏数据和全部数据的引用
        };
    },
    components: {
        Upload
    },
    mounted () {
        this.loadData();
    }
};
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

