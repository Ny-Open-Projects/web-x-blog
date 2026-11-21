# 画面线理解：day08-21-查询标的信息-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-9 实现查询标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-9 实现查询标的信息\day08-21-查询标的信息-功能实现2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:20, 02:00, 03:26, 04:35, 06:06, 06:58, 07:57, 09:07, 10:48, 11:53, 13:53, 15:30, 16:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:58:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中使用 MyBatis-Plus 的 QueryWrapper 进行条件查询，并结合 Page 分页功能，最终将数据库查询结果转换为 DTO 对象并返回。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 ProjectServiceImpl.java 中的 Page 接口调用，使用 QueryWrapper 进行条件查询，包含对项目名称、年化利率、期限、状态等字段的非空判断。
画面 2: 展示 QueryWrapper 的构造，使用 lambda 表达式设置查询条件，包括项目名称、年化利率、期限等。
画面 3: 展示 QueryWrapper 的构造，使用 lambda 表达式设置查询条件，包括项目状态。
画面 4: 展示 QueryWrapper 的构造，使用 lambda 表达式设置查询条件，包括项目状态。
画面 5: 展示 QueryWrapper 的构造，使用 lambda 表达式设置查询条件，包括项目状态。
画面 6: 展示 QueryWrapper 的构造，使用 lambda 表达式设置查询条件，包括项目状态。
画面 7: 展示 QueryWrapper 的构造，使用 lambda 表达式设置查询条件，包括项目状态。
画面 8: 展示 QueryWrapper 的构造，使用 lambda 表达式设置查询条件，包括项目状态。
画面 9: 展示 QueryWrapper 的构造，使用 lambda 表达式设置查询条件，包括项目状态。
画面 10: 展示 MyBatis-Plus 的 Page 分页类源码，查看其内部结构和属性。
画面 11: 展示 Page 类的 getPages() 方法，用于获取分页信息。
画面 12: 展示将查询到的实体列表转换为 DTO 列表的代码，使用 BeanUtils.copyProperties 方法。
画面 13: 展示 PageVO 类的构造函数和 hasPrevious() 方法，用于分页信息的封装。
画面 14: 展示最终返回 PageVO 对象，包含转换后的 DTO 列表和分页信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Override
public PageVO<ProjectDTO> queryProjectByQueryDTO(ProjectQueryDTO projectQueryDTO, String order, Integer pageNo, Integer pageSize, String sort) {
    //带条件
    QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
    //动态类型
    if (StringUtils.isNotBlank(projectQueryDTO.getProjectName())) {
        queryWrapper.lambda().eq(Project::getProjectName, projectQueryDTO.getProjectName());
    }
    if (null != projectQueryDTO.getStartAnnualRate()) {
        queryWrapper.lambda().ge(Project::getStartAnnualRate, projectQueryDTO.getStartAnnualRate());
    }
    if (null != projectQueryDTO.getEndAnnualRate()) {
        queryWrapper.lambda().le(Project::getEndAnnualRate, projectQueryDTO.getEndAnnualRate());
    }
    if (null != projectQueryDTO.getStartPeriod()) {
        queryWrapper.lambda().ge(Project::getStartPeriod, projectQueryDTO.getStartPeriod());
    }
    if (null != projectQueryDTO.getEndPeriod()) {
        queryWrapper.lambda().le(Project::getEndPeriod, projectQueryDTO.getEndPeriod());
    }
    //状态
    if (StringUtils.isNotBlank(projectQueryDTO.getProjectStatus())) {
        queryWrapper.lambda().eq(Project::getProjectStatus, projectQueryDTO.getProjectStatus());
    }
    //分页
    Page<Project> page = new Page<>(pageNo, pageSize);
    //排序
    if (StringUtils.isNotBlank(order) && StringUtils.isNotBlank(sort)) {
        if (order.toLowerCase().equals("asc")) {
            queryWrapper.orderByAsc(sort);
        } else if (order.toLowerCase().equals("desc")) {
            queryWrapper.orderByDesc(sort);
        } else {
            queryWrapper.orderByDesc(Project::getCreateDate);
        }
    }
    //执行查询
    IPage<Project> iPage = page.query(queryWrapper);
    //封装结果
    private List<ProjectDTO> convertProjectEntityListToDTOList(java.util.List<Project> projectList) {
        if (projectList == null) {
            return null;
        }
        List<ProjectDTO> dtoList = new ArrayList<>();
        projectList.forEach(project -> {
            ProjectDTO projectDTO = new ProjectDTO();
            BeanUtils.copyProperties(project, projectDTO);
            dtoList.add(projectDTO);
        });
        return new PageVO<>(dtoList, iPage.getTotal(), pageNo, pageSize);
    }
```

画面 2:
```java
//带条件
QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
//动态类型
if (StringUtils.isNotBlank(projectQueryDTO.getProjectName())) {
    queryWrapper.lambda().eq(Project::getProjectName, projectQueryDTO.getProjectName());
}
if (null != projectQueryDTO.getStartAnnualRate()) {
    queryWrapper.lambda().ge(Project::getStartAnnualRate, projectQueryDTO.getStartAnnualRate());
}
if (null != projectQueryDTO.getEndAnnualRate()) {
    queryWrapper.lambda().le(Project::getEndAnnualRate, projectQueryDTO.getEndAnnualRate());
}
if (null != projectQueryDTO.getStartPeriod()) {
    queryWrapper.lambda().ge(Project::getStartPeriod, projectQueryDTO.getStartPeriod());
}
if (null != projectQueryDTO.getEndPeriod()) {
    queryWrapper.lambda().le(Project::getEndPeriod, projectQueryDTO.getEndPeriod());
}
//状态
if (StringUtils.isNotBlank(projectQueryDTO.getProjectStatus())) {
    queryWrapper.lambda().eq(Project::getProjectStatus, projectQueryDTO.getProjectStatus());
}
//分页
Page<Project> page = new Page<>(pageNo, pageSize);
//排序
if (StringUtils.isNotBlank(order) && StringUtils.isNotBlank(sort)) {
    if (order.toLowerCase().equals("asc")) {
        queryWrapper.orderByAsc(sort);
    } else if (order.toLowerCase().equals("desc")) {
        queryWrapper.orderByDesc(sort);
    } else {
        queryWrapper.orderByDesc(Project::getCreateDate);
    }
}
//执行查询
IPage<Project> iPage = page.query(queryWrapper);
//封装结果
private List<ProjectDTO> convertProjectEntityListToDTOList(java.util.List<Project> projectList) {
    if (projectList == null) {
        return null;
    }
    List<ProjectDTO> dtoList = new ArrayList<>();
    projectList.forEach(project -> {
        ProjectDTO projectDTO = new ProjectDTO();
        BeanUtils.copyProperties(project, projectDTO);
        dtoList.add(projectDTO);
    });
    return new PageVO<>(dtoList, iPage.getTotal(), pageNo, pageSize);
}
```

画面 3:
```java
//带条件
QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
//动态类型
if (StringUtils.isNotBlank(projectQueryDTO.getProjectName())) {
    queryWrapper.lambda().eq(Project::getProjectName, projectQueryDTO.getProjectName());
}
if (null != projectQueryDTO.getStartAnnualRate()) {
    queryWrapper.lambda().ge(Project::getStartAnnualRate, projectQueryDTO.getStartAnnualRate());
}
if (null != projectQueryDTO.getEndAnnualRate()) {
    queryWrapper.lambda().le(Project::getEndAnnualRate, projectQueryDTO.getEndAnnualRate());
}
if (null != projectQueryDTO.getStartPeriod()) {
    queryWrapper.lambda().ge(Project::getStartPeriod, projectQueryDTO.getStartPeriod());
}
if (null != projectQueryDTO.getEndPeriod()) {
    queryWrapper.lambda().le(Project::getEndPeriod, projectQueryDTO.getEndPeriod());
}
//状态
if (StringUtils.isNotBlank(projectQueryDTO.getProjectStatus())) {
    queryWrapper.lambda().eq(Project::getProjectStatus, projectQueryDTO.getProjectStatus());
}
//分页
Page<Project> page = new Page<>(pageNo, pageSize);
//排序
if (StringUtils.isNotBlank(order) && StringUtils.isNotBlank(sort)) {
    if (order.toLowerCase().equals("asc")) {
        queryWrapper.orderByAsc(sort);
    } else if (order.toLowerCase().equals("desc")) {
        queryWrapper.orderByDesc(sort);
    } else {
        queryWrapper.orderByDesc(Project::getCreateDate);
    }
}
//执行查询
IPage<Project> iPage = page.query(queryWrapper);
//封装结果
private List<ProjectDTO> convertProjectEntityListToDTOList(java.util.List<Project> projectList) {
    if (projectList == null) {
        return null;
    }
    List<ProjectDTO> dtoList = new ArrayList<>();
    projectList.forEach(project -> {
        ProjectDTO projectDTO = new ProjectDTO();
        BeanUtils.copyProperties(project, projectDTO);
        dtoList.add(projectDTO);
    });
    return new PageVO<>(dtoList, iPage.getTotal(), pageNo, pageSize);
}
```

画面 4:
```java
//带条件
QueryWrapper<Project> queryWrapper = new QueryWrapper<>();
//动态类型
if (StringUtils.isNotBlank(projectQueryDTO.getProjectName())) {
    queryWrapper.lambda().eq(Project::getProjectName, projectQueryDTO.getProjectName());
}
if (null != projectQueryDTO.getStartAnnualRate()) {
    queryWrapper.lambda().ge(Project::getStartAnnualRate, projectQueryDTO.getStartAnnualRate());
}
if (null != projectQueryDTO.getEndAnnualRate()) {
    queryWrapper.lambda().le(Project::getEndAnnualRate, projectQueryDTO.getEndAnnualRate());
}
if (null != projectQueryDTO.getStartPeriod()) {
    queryWrapper.lambda().ge(Project::getStartPeriod, projectQueryDTO.getStartPeriod());
}
if (null != projectQueryDTO.getEndPeriod()) {
    queryWrapper.lambda().le(Project::getEndPeriod, projectQueryDTO.getEndPeriod());
}
//状态
if (StringUtils.isNotBlank(projectQuery
