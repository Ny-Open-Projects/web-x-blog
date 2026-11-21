# 画面线理解：07_自媒体_素材管理_图片上传功能完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\07_自媒体_素材管理_图片上传功能完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:16, 02:00, 02:52, 04:03, 04:46, 05:15, 05:48, 06:39, 07:02, 08:02, 09:00, 10:16, 10:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:44:27

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的图片上传功能的前后端实现，包括控制器、服务层代码、文件上传逻辑、前端 Vue 组件以及调试过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 项目结构：`heima-leadnews-media` 模块被选中。
- 代码内容：`MaterialServiceImpl.java` 中的 `uploadPicture` 方法，包含创建 `wmMaterial` 对象、设置属性、插入数据库并返回结果的逻辑。
- 代码片段：
  ```java
  //上传成功后，保存一条数据wm_material
  wmMaterial wmMaterial = new WmMaterial();
  wmMaterial.setCreatedTime(new Date());
  wmMaterial.setTypeId((short)0);
  wmMaterial.setUserId(wbUser.getId());
  wmMaterial.setCollection((short)0);
  wmMaterialMapper.insert(wmMaterial);
  wmMaterial.setUrl(fileServerUrl + fileId);
  return ResponseResult.okResult(wmMaterial);
  ```

画面 2：
- 代码内容：`MaterialManageControllerApi.java` 接口定义。
- 代码片段：
  ```java
  package com.heima.media.api;

  import com.heima.model.common.dto.ResponseResult;
  import org.springframework.web.multipart.MultipartFile;

  public interface MaterialManageControllerApi {
      //上传图片
      @PostMapping
      @Return
      public ResponseResult uploadPicture(MultipartFile file);
  }
  ```

画面 3：
- 代码内容：`MaterialManageController.java` 中的 `uploadPicture` 方法，初始状态为空。
- 代码片段：
  ```java
  public ResponseResult uploadPicture(MultipartFile file) {
      return null;
  }
  ```

画面 4：
- 代码内容：`MaterialManageController.java` 中的 `@RestController` 注解和 `@RequestMapping` 注解。
- 代码片段：
  ```java
  @RestController
  @RequestMapping("/api/v1/media/material")
  public class MaterialManageController implements MaterialManageControllerApi {
      @Autowired
      private MaterialService materialService;

      @Override
      @PostMapping("/upload_picture")
      public ResponseResult uploadPicture(MultipartFile file) {
          return materialService.uploadPicture(file);
      }
  }
  ```

画面 5：
- 网页内容：登录页面，显示“正在等待导入用户”。
- 页面地址：`localhost:8080/#/login`

画面 6：
- 网页内容：登录成功后，进入“图片管理”页面，弹出“上传图片”对话框。
- 页面地址：`localhost:8080/#/material/list`

画面 7：
- 代码内容：`MaterialServiceImpl.java` 中的文件上传逻辑，包含文件格式校验和 FastDFS 上传。
- 代码片段：
  ```java
  //验证参数
  if (multipartFile == null) {
      return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
  }
  //上传图片到fastdfs
  String originalFilename = multipartFile.getOriginalFilename();
  if (originalFilename.matches(".*(gif|jpg|jpeg).*")) {
      return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_IMAGE_FORMAT_ERROR);
  }
  String fileId = null;
  try {
      fileId = fastDfsClient.uploadFile(multipartFile.getBytes(), extName);
  } catch (Exception e) {
      e.printStackTrace();
  }
  ```

画面 8：
- 代码内容：`MaterialServiceImpl.java` 中的文件上传逻辑，包含创建 `wmMaterial` 对象、设置属性、插入数据库并返回结果的逻辑。
- 代码片段：
  ```java
  //上传成功后，保存一条数据wm_material
  wmMaterial wmMaterial = new WmMaterial();
  wmMaterial.setCreatedTime(new Date());
  wmMaterial.setTypeId((short)0);
  wmMaterial.setUserId(wbUser.getId());
  wmMaterial.setCollection((short)0);
  wmMaterialMapper.insert(wmMaterial);
  wmMaterial.setUrl(fileServerUrl + fileId);
  return ResponseResult.okResult(wmMaterial);
  ```

画面 9：
- 代码内容：Vue 组件中 `el-pagination` 分页组件的代码。
- 代码片段：
  ```html
  <el-pagination
      background
      layout="prev, pager, next, jumper"
      :total="imgPage.total"
      :page-count="imgPage.pageCount"
      :page-size="imgPage.pageSize"
      :current-page="imgPage.currentPage"
      @current-change="pageChange"
  />
  ```

画面 10：
- 代码内容：Vue 组件中 `el-dialog` 弹窗和 `upload` 组件的代码。
- 代码片段：
  ```html
  <el-dialog
      :visible.sync="showPicDialog"
      width="56%"
      :show-close="false"
      :center="true"
      :before-close="closeModal"
  >
      <upload v-if="showPicDialog" :imgChange="imgChange" />
      <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="closeModal">关闭</el-button>
      </span>
  </el-dialog>
  ```

画面 11：
- 代码内容：`MaterialManageController.java` 中的 `@PostMapping` 注解和 `uploadPicture` 方法。
- 代码片段：
  ```java
  @Override
  @PostMapping("/upload_picture")
  public ResponseResult uploadPicture(MultipartFile file) {
      return materialService.uploadPicture(file);
  }
  ```

画面 12：
- 代码内容：Vue 组件中 `el-upload` 上传组件的代码。
- 代码片段：
  ```html
  <el-upload
      action="http://localhost:8080/api/v1/media/upload"
      :on-success="handleSuccess"
      :before-upload="beforeUpload"
      :on-error="handleError"
      :file-list="fileList"
      :auto-upload="false"
  >
      <el-button size="small" type="primary">点击上传</el-button>
  </el-upload>
  ```

画面 13：
- 代码内容：`MaterialManageController.java` 中的 `@PostMapping` 注解和 `uploadPicture` 方法。
- 代码片段：
  ```java
  @Override
  @PostMapping("/upload_picture")
  public ResponseResult uploadPicture(MultipartFile file) {
      return materialService.uploadPicture(file);
  }
  ```

画面 14：
- 代码内容：Vue 组件中 `el-upload` 上传组件的代码。
- 代码片段：
  ```html
  <el-upload
      action="http://localhost:8080/api/v1/media/upload"
      :on-success="handleSuccess"
      :before-upload="beforeUpload"
      :on-error="handleError"
      :file-list="fileList"
      :auto-upload="false"
  >
      <el-button size="small" type="primary">点击上传</el-button>
  </el-upload>
  ```
