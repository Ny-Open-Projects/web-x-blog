# 画面线理解：09_自媒体_素材管理_素材列表接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\09_自媒体_素材管理_素材列表接口开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:52, 02:58, 05:25, 06:34, 07:11, 07:42, 08:42, 09:17, 10:18, 10:57, 11:43, 12:24, 13:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:46:01

1) 这一组画面整体在讲什么（一句话）：
实现一个图片素材管理接口，包括上传、删除和列表查询功能，涉及数据库表结构、Mapper接口定义、Service层逻辑和Controller层接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示接口文档，定义了素材列表接口的请求/响应DTO结构和错误码。
画面2：展示数据库表wm_material的数据，包含图片路径、用户ID、创建时间等字段。
画面3：展示Mapper接口WnMaterialMapper，定义了插入、根据ID查询、根据状态和用户ID查询等方法。
画面4：展示Service层代码，定义了上传、删除、查询方法的返回类型和参数。
画面5：展示Service层代码，删除方法中处理文件删除失败的异常并返回错误码。
画面6：展示Service层代码，查询方法中获取当前用户ID。
画面7：展示Service层代码，查询方法中调用mapper的findByUidAndStatus方法。
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
