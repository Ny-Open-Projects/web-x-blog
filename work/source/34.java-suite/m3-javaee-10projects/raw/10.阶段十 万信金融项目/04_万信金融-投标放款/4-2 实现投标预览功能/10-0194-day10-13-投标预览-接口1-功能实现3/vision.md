# 画面线理解：day10-13-投标预览-接口1-功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-2 实现投标预览功能
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-2 实现投标预览功能\day10-13-投标预览-接口1-功能实现3_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:07, 01:35, 01:53, 02:14, 02:55, 03:16, 03:37, 04:25, 04:53, 05:21, 05:51, 06:12, 06:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:24:46

1) 这一组画面整体在讲如何在项目服务层中，通过 MyBatis-Plus 的 LambdaQueryWrapper 查询项目数据，并结合 Tender 表获取剩余金额，最终封装成 DTO 返回。

2) 按时间顺序列出每张画面的要点：

画面 1:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  list.add(Long.parseLong(str));
  queryWrapper.lambda().in(Project::getId, list); // ... where id in (1,2,3,4,5)
  List<Project> projectsList = queryWrapper.list();
  List<ProjectDTO> dtos = new ArrayList<>();
  // 2. 转换为DTO对象
  for (Project project : projects) {
      ProjectDTO projectDTO = convertProjectEntityToDTO(project);
      // 3. 获取剩余额度
      getProjectRemainingAmount(project);
  }
  ```

画面 2:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  // 4. 查询出借人数
  ```

画面 3:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  tenderMapper.selectCount(Wrappers.lambdaQuery());
  ```

画面 4:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  tenderMapper.selectCount(Wrappers.lambdaQuery().eq(Tender::getProjectId, project.getId()));
  ```

画面 5:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  tenderMapper.selectCount(Wrappers.lambdaQuery().eq(Tender::getProjectId, project.getId()));
  ```

画面 6:
- 代码位置：ProjectDTO.java
- 代码内容：
  ```java
  package cn.itsent.wanningzp.api.transaction.model;

  import ...

  @Data
  public class ProjectDTO {
      // 二健
      @JsonSerialize(using = JsonLongSerializer.class)
      private Long id;
      // 发标人用户标识
      private Long consumerId;
      // 发标人用户编码
  }
  ```

画面 7:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  projectDTO.setRemainingAmount(getProjectRemainingAmount(project));
  ```

画面 8:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  projectDTO.setRemainingAmount(getProjectRemainingAmount(project));
  ```

画面 9:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  tenderMapper.selectCount(Wrappers.lambdaQuery().eq(Tender::getProjectId, project.getId()));
  ```

画面 10:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  projectDTO.setRemainingAmount(getProjectRemainingAmount(project));
  // 4. 查询出借人数
  projectDTO.setTenderCount(tenderMapper.selectCount(Wrappers.lambdaQuery().eq(Tender::getProjectId, project.getId())));
  dtos.add(projectDTO);
  ```

画面 11:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  projectDTO.setTenderCount(tenderMapper.selectCount(Wrappers.lambdaQuery().eq(Tender::getProjectId, project.getId())));
  ```

画面 12:
- 代码位置：ProjectServiceImpl.java
- 代码内容：
  ```java
  if (!isResponse.isSuccessfull()) {
      throw new BusinessException(CommonErrorCode.UNKNOWN);
  }
  return response.getResult();
  ```

画面 13:
- 代码位置：TransactionController.java
- 代码内容：
  ```java
  @ApiOperation("通过ids获取多个标的")
  @GetMapping("/projects/{ids}")
  public RestResponse<List<ProjectDTO>> queryProjectsIds(@PathVariable String ids) {
      return RestResponse.success(projectService.queryProjectsIds(ids));
  }
  ```

画面 14:
- 代码位置：TransactionController.java
- 代码内容：
  ```java
  @ApiOperation("根据标的的id查询投标记录")
  @GetMapping("/tenders/projects/{id}")
  public RestResponse<List<TenderOverviewDTO>> queryTendersByProjectId(@PathVariable Long id) {
      return null;
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
- 无额外代码或配置需抄录。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 无 PPT 或架构图/流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
- 无额外内容。
