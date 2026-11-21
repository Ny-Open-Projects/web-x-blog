# 09_自媒体_素材管理_素材列表接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\09_自媒体_素材管理_素材列表接口开发【海量资源尽在 666java.com】.mp4
- 时长 13分32秒（音频 812s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 来咱们下面去完成素材列表这个接口先来看一下接口定义这个定义来首先还是当前的这种URL是吧这个没啥可说的它是一个list咱们要查询列表然后第二个是有一个参数这个参数是wm material然后是list DTO然后第三个咱们看一下显示的DTO里边有一个东西就是啥有一个date
[00:26] 这里边有个size和total还有一个例子集合这个很显然就是咱们在去查询列表的时候分页是不是需要这是分页需要的内容好那咱们下面就依次来去看一下当前这个东西这里边到底有啥好咱们可以找到当前那个类control然后是找到这已经定义好的这个类这里边你看这目前只有一个参数是查询是否收藏的一个参数
[00:55] 这里边你看还有个内容叫一个sense是不是继承了一个配置request DTO这个例子咱们在前段时候先讲过但是一直没有用过到今天用到了这个是分页的时候需要请求要获取的参数应该是参数第一个是size第二是配置是不是就是当前页和当前的条数当前页的条数还有一个这种方法叫check param
[01:24] 其实就是来检验当前这个参数到底合理不合理如果说它配置等于等于0或者小于0的时候咱们就给一个默认值下面也有默认值如果说size等于0或者小于0或者大于100的时候咱们也会默认值是10OK那这个都能看明白吧OK那这个其实就是参数就是参数好再往下看最终咱们要去返回一个列表这个列表的话列表返回的数据其实就是你要去查询当前这个表的所有的数据
[01:53] 要去返回但这个条件是啥呢这个条件当然第一个条件肯定是要进行分业是吧第二条件其实你要根据某一个用户某一个用户去查询这个一定要清晰好吧这是一块还有吗还有一个其实这个等到下一个节目会去讲到就是收藏收藏是否收藏这里边是有一个意思collection这个就是你要是0就是不收藏1的话就是收藏
[02:23] OK那这个也是作为条件进行查询的好吧那行那咱们下面就来去定义MapMap里边你可以看一下这里边就有两个方法一个是查询集合第二个就是Count就是查询总条数好吧当前用户的总条数这里边做用户好吧行把两个方法拷贝一下跑到咱们的MapMap介绍里边然后呢然后再说一下因为这里边是有两个条件两个条件怎么办
[02:55] 有的人家是不是在这去加什么发热吗你在这去一定一下或者定义一下到时候他找不着这个参数啊谁说在这写一下好在这上面也写一下啊是uid好这是uid那行啊那这个加完之后啊咱们就可以去写当前的mypro文件来把下面东西也拷贝一下啊好然后呢咱们就可以看一下当前这个mypro文件啊
[03:31] 首先这个是一个查询列表的一个方法是吧然后是查询它然后根据的一个条件就是当前的某一个用户下面的所有的媒体资源就是图片资源然后下面还有一个就是它是否等一等一是否等一等一那是否等一等一就是看是否收藏了收藏的话咱们就加上收藏就加上不收藏就不加了其实下面条件是一样的
[03:56] 那为什么要加这东西呢就这样啊如果说你要没收藏的话呢咱们应该查询所有的内容没收藏的时候查询所有内容如果你收藏的话咱们只查询收藏的内容那这个呢其实是两个两个信息啊我再去说一下啊大家注意听你要是收藏的话我只查询啥呢如果你有条件是一我只查询收藏那边如果说你要不是一我要查询全部的信息这个呢其实跟咱们数据展示是有关系的
[04:24] 好吧咱们一会再去讲啊这个如今大家先去理解一下好吧这个看看的时候也是一样啊也是等于一的时候有收藏的收藏的话呢我目前就只查收藏的没收藏的话呢咱们就查询所有的好吧行那下面还有一个啊下面非常简单的一个参数就是这块内容的前面第一个是你要查询葱的还是茶是吧还有就是你要查询多少条啊要查询多少条好吧
[04:52] 那行那这个这个麦克文件咱们就说完了说完之后咱们下面就来去写Service写咱们那个咱们的Service这个Service其实你还是在这写还是在咱们之前的那个Service去写就可以了好吧来打开找到当前的Service就它在这你再去加一个方法就是产品里边还是response result然后是find list好吧猜数是谁
[05:20] 参数就是wm-ulisttto,listtto就它,tto,完了啊,嗯,停,分页查询列表,好,那这个啊,咱们加完之后呢,咱们就可以去写它的Service,然后在这,再找到当前的Service,然后findlist就它,好吧,那首先呢,你还是要就想要写啊,这里边第一步呢,干嘛呢,要验证参数,
[05:57] 这个才说啊第二个呢咱们又就可以去进行查询那查询之前呢咱们需要去有些条件是吧这条件啥呢获取用户因为这个条件里边是不是有个用户啊然后呢你就可以查询了啊查询查询最后是返回啊这个返回的时候啊你一定要注意返回的时候要根据当前的接口的定义去进行返回好吧它返回的部分其实有很多好吧
[06:32] 那行 那们继续往下看啊那咱们就来去把这个单位写一写首先验证参数的话呢怎么办呢这里边其实这个配置主要快速DTO里边其实已经验证完了你直接到下当前这个方法就可以打开当前的这个Service呢好在这啊你DTO讲什么直接去验证一下可以这样的话就算是完成了好吧那行下面呢咱们去拿到用户啊
[07:04] 就拿到最终的是拿到用户的呃懂什么拿到用户的ID是吧好这个呢其实就是谁啊就是UIDUID啊拿到UID之后呢咱们就现在呢就可以进行他寻了啊WMMetalMetalViewMap.slack的应该是他find list UID按照status也不对是吧是是那是这个吗啊是这个啊是这个啊
[07:36] 然后第一个参数谁啊第一个参数DTO二个参数呢就是UID是吧最终你可以去返回一个列表返回一个列表啊叫DAT4好吧DAT4之后啊咱们下面就还要去做一个事这个什么事呢大家都知道啊目前的话呢像这个是不是都是文件ID啊你要文件ID你在浏览器上直接能访问吗是不是强调很多次了你在这直接访问吧那怎么访问呢
[08:05] 在前面需要干嘛呢要去加上你的地址原HTTP我这是192.168.25.133那这样你是可以访问的所以说我们在这需要去循环需要去循环当前的数据进行把这URL给它改变了改变成啥呢给它加上谁的加上当前的这个地址好吧加这个地址那行那这个怎么加怎么写
[08:34] 其实很简单就是直接做一个分心环直接去遍历每一端数据重新set一下URL数据就可以了好咱们写下咱们可以这么写用流去写好吧Stream流gates.stream. 点啥呢点一个map好吧然后咱们就可以去写了然后是item然后是杠好写啊然后是item.setURL
[09:09] 然后就可以去加上当前的User URL然后是加谁加上当前的item.set URL是吧这样的话就算是写出了最终咱们就可以returnitem下面还没有完是吧没有完但这个好像是ID是吧这写错了set URL又是大写那设完之后咱们就算是删了
[09:42] 最终咱们就可以去装到重新装到当前的机壳connect然后就完了当然这个机壳你可以再重新用它去接收一下就完事了这样的话就算地址里边其实这个URL就是已经改变了已经改变了改变完之后咱们现在就可以去返回了但是返回之后咱们还少一个东西这是啥去是不是还少一个count是吧所以说你在这再去找一下
[10:13] 点,conc,还是dtu还是uat是吧最终就可以拿到一个种角数啊这种种角数啊你也可以去设一个total叫total吧好吧好最终你返回啊那返回怎么返回啊刚才说了你需要去返回很多数据所以说咱们在这创建一个mapstrain然后是project然后怎么叫啥呢叫resdata
[10:47] 等于6一个hashmap然后往里边去装数据res.setput一个咱们可以去把当前页给装进去当前页vr gauge然后怎么写dto中的get第二个咱们可以去res.setput咱们可以把size装进去size是谁
[11:23] 也是GTO中的什么get size下面还有往下看res.put我们可以装一个listlist的话其实就是咱们真正的数据是吧就是谁啊就是当前的datasok 没问题吧然后再往下咱们还要把这个总条数给装进去res.put这个是谁啊这个是叫total
[11:55] 最终咱们可以把当前resdate返回就可以了怎么写responseresult.ok把当前的resdata是装进去最终咱们的Service就算是也完了好吧写完之后咱们下面就来去写当前的接口接口的话咱们还是这样还是在当前的Controller中去定义找到当前的API在这写一个方法
[12:23] public response result然后是list参数啥呢wm material list.dtu分一二查询最终咱们可以去找到当前具体的Controller去写list加上之后咱们在这就可以直接去调用Service了
[13:02] find list DTO装进去完事了最终你要在这补全在这补全拷贝一个上面的吧这样咱们就叫啥呢叫list好吧这个呢你需要去加一个什么request保底好吧这个加完了咱们在这加个杠最好是加杠行不加杠其实也没有事啊这样是最好的好吧行那目前的话咱们这个接口就算是开发完了这个测试咱们一会也再测好吧稍等稍等一下咱们再测

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现一个图片素材管理接口，包括上传、删除和列表查询功能，涉及数据库表结构、Mapper接口定义、Service层逻辑和Controller层接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示接口文档，定义了素材列表接口的请求/响应DTO结构和错误码。
画面2：展示数据库表wm_material的数据，包含图片路径、用户ID、创建时间等字段。
画面3：展示Mapper接口WnMaterialMapper，定义了插入、根据ID查询、根据状态和用户ID查询等方法。
画面4：展示Service层代码，定义了上传、删除、查询方法的返回类型和参数。
画面5：展示Service层代码，删除方法中处理文件删除失败的异常并返回错误码。
画面6：展示Service层代码，查询方法中获取当前用户ID。
画面7：展示Service层代码，查询方法中调用Mapper的findByUidAndStatus方法。
画面8：展示Service层代码，使用Stream对查询结果进行处理。
画面9：展示Service层代码，为每个图片对象设置服务器URL。
画面10：展示Service层代码，使用Collectors.toList()收集处理后的结果。
画面11：展示Service层代码，创建Map用于返回分页数据。
画面12：展示Service层代码，向Map中添加分页数据。
画面13：展示Controller层代码，定义了上传、删除、列表接口的注解和方法。
画面14：展示Controller层代码，定义了列表接口的请求参数和返回值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
import com.heima.model.media.dto.WnMaterialListDto;
import com.heima.model.media.po.WnMaterial;
import org.apache.ibatis.annotations.Param;

import java.util.List;

public interface WnMaterialMapper {
    int insert(WnMaterial record);

    WnMaterial selectByPrimaryKey(Integer id);

    int deleteByPrimaryKey(Integer id);

    List<WnMaterial> findListByUidAndStatus(WnMaterialListDto dto, Long uid);

    int countListByUidAndStatus(WnMaterialListDto dto, Long uid);
}
```

画面4：
```java
//上传图片
@Param("multipartFile")
@Return
ResponseResult upList(WnMaterialListDto dto, MultipartFile multipartFile) {
    //删除图片
    @Param("dto")
    @Return
    ResponseResult delList(WnMaterialListDto dto) {
        //查询图片
        @Param("dto")
        @Return
        ResponseResult findList(WnMaterialListDto dto) {
```

画面5：
```java
Log.error("user {} delete file {} from fastFs error,error info: {}", user, fileId, e.getMessage());
return ResponseResult.errorResult(AppHttpCodeEnum.SERVER_ERROR);
//删除 wm_material 中的记录
wmMaterialMapper.deleteByPrimaryKey(dto.getId());
return ResponseResult.okResult(AppHttpCodeEnum.SUCCESS);
```

画面6：
```java
Long uid = WnThreadLocalUtils.getUid();
```

画面7：
```java
List<WnMaterial> datas = wmMaterialMapper.findListByUidAndStatus(dto, uid);
```

画面8：
```java
datas.stream().map(item -> {
    item.setUrl(fileServerUrl + item.getOriginalUrl());
    return item;
})
```

画面9：
```java
item.setUserId(fileServerUrl + item.getUserId());
```

画面10：
```java
.collect(Collectors.toList());
```

画面11：
```java
Map<String, Object> resData = new HashMap<>();
```

画面12：
```java
resData.put("curPage", dto.getPage());
resData.put("size", dto.getSize());
resData.put("list", datas);
```

画面13：
```java
public class MaterialManageControllerApi {
    @Autowired
    private MaterialService materialService;

    @PostMapping("/upload_picture")
    public ResponseResult uploadPicture(MultipartFile file) {
        return materialService.uploadPicture(file);
    }

    @PostMapping("/del_picture")
    public ResponseResult delPicture(@RequestBody WnMaterialDto dto) {
        return materialService.delPicture(dto);
    }

    @PostMapping("/list")
    public ResponseResult list(@RequestBody WnMaterialListDto dto) {
        return materialService.findList(dto);
    }
}
```

画面14：
```java
@PostMapping("/list")
public ResponseResult list(@RequestBody WnMaterialListDto dto) {
    return materialService.findList(dto);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

