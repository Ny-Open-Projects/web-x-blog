# 画面线理解：06_自媒体_素材管理_图片上传接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\06_自媒体_素材管理_图片上传接口开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 02:25, 03:46, 04:48, 06:03, 07:52, 08:51, 11:15, 13:01, 14:12, 15:19, 16:34, 18:16, 19:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:43:39

1) 这一组画面整体在讲什么（一句话）：
实现图片上传接口的后端代码，包括接口定义、Mapper接口、XML映射文件、Service实现类及配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档中“4.2.2 接口定义”部分，包含接口名称 /api/v1/media/material/upload_picture、请求DTO WmMaterial、以及参数错误码定义。
画面2：展示IDEA中WmMaterialMapper.java文件，定义了insert方法。
画面3：展示文件资源管理器中conf目录下的配置文件列表，包括schema、sequence、partition-range等配置文件。
画面4：展示IDEA中创建XML文件的弹窗，正在创建WmMaterialMapper.xml文件。
画面5：展示IDEA中MaterialServiceImpl.java文件，定义了uploadPicture方法。
画面6：展示IDEA中MaterialServiceImpl.java文件，开始编写uploadPicture方法的实现。
画面7：展示IDEA中MaterialServiceImpl.java文件，添加了获取当前登录用户和参数校验逻辑。
画面8：展示IDEA中MaterialServiceImpl.java文件，添加了文件格式校验逻辑。
画面9：展示IDEA中MaterialServiceImpl.java文件，添加了文件上传到FastDFS的逻辑。
画面10：展示IDEA中MaterialServiceImpl.java文件，添加了创建WmMaterial对象并设置属性的逻辑。
画面11：展示IDEA中MaterialServiceImpl.java文件，完成WmMaterial对象的属性设置。
画面12：展示IDEA中MaterialServiceImpl.java文件，添加了将WmMaterial对象插入数据库的逻辑。
画面13：展示IDEA中MaterialServiceImpl.java文件，完成将WmMaterial对象插入数据库的逻辑。
画面14：展示IDEA中MaterialServiceImpl.java文件，完成将WmMaterial对象插入数据库并返回结果的逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
接口名称 /api/v1/media/material/upload_picture
请求DTO WmMaterial
响应DTO WmMaterial
(2) CODE定义
PARAM_INVALID PARAM_INVALID(501,"无效参数")。
PARAM_IMAGE_FORMAT_ERROR PARAM_IMAGE_FORMAT_ERROR(502,"图片格式有误")
SERVER_ERROR SERVER_ERROR(503,"服务器内部错误")。

画面2：
package com.heima.model.mappers.wmedia;
import com.heima.model.media.pojos.WmMaterial;
public interface WmMaterialMapper {
int insert(WmMaterial record);
}

画面4：
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.heima.model.mappers.wmedia.WmMaterialMapper">
<resultMap id="BaseResultMap" type="com.heima.model.mappers.wmedia.WmMaterial">
<id column="id" property="id" />
<result column="user_id" property="userId" />
<result column="created_time" property="createdTime" />
<result column="type" property="type" />
<result column="collection" property="collection" />
<result column="url" property="url" />
<result column="title" property="title" />
<result column="description" property="description" />
<result column="file_size" property="fileSize" />
<result column="file_type" property="fileType" />
<result column="file_name" property="fileName" />
<result column="file_ext" property="fileExt" />
<result column="file_md5" property="fileMd5" />
<result column="file_sha1" property="fileSha1" />
<result column="file_sha256" property="fileSha256" />
<result column="file_sha512" property="fileSha512" />
<result column="file_crc32" property="fileCrc32" />
<result column="file_crc64" property="fileCrc64" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64c" property="fileCrc64c" />
<result column="file_crc32c" property="fileCrc32c" />
<result column="file_crc64
