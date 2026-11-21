# 画面线理解：11_自媒体_素材管理_收藏与取消收藏完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\11_自媒体_素材管理_收藏与取消收藏完成【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:10, 02:28, 03:47, 04:28, 05:06, 05:54, 07:07, 08:05, 09:11, 10:11, 10:57, 11:47, 13:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:47:44

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
│                       └── controller
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
