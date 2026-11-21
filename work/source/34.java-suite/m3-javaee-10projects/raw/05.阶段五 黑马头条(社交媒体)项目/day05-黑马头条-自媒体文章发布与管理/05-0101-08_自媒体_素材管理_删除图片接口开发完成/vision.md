# 画面线理解：08_自媒体_素材管理_删除图片接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\08_自媒体_素材管理_删除图片接口开发完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:30, 03:11, 03:58, 04:55, 06:16, 08:01, 08:45, 10:01, 11:09, 13:07, 13:44, 14:40, 15:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:45:24

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
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0.0" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.heima.model.mappers.wemedia.WmNewsMaterialMapper">
</mapper>
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
