# 画面线理解：15-修改员工考勤记录

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\15-修改员工考勤记录_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:27, 00:56, 01:25, 02:02, 02:32, 03:22, 04:41, 05:16, 05:38, 06:00, 06:16, 06:28, 06:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:39:29

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 系统中通过前端页面操作考勤记录，并在后端通过 IntelliJ IDEA 编辑 AttendanceController 和 AtteService 类来实现考勤数据的修改功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 IntelliJ IDEA 中 iHRM 项目的目录结构，当前选中的是 `ihrm_parent` 项目根目录。
画面 2: 展示 iHRM 系统的考勤列表页面，显示了多个员工的考勤记录，状态为“旷工”。
画面 3: 展示考勤列表页面，筛选条件为“部门”为“开发部”，显示了开发部员工的考勤记录。
画面 4: 展示考勤列表页面，点击某条记录后，弹出考勤详情弹窗，显示了该员工的考勤状态。
画面 5: 展示浏览器开发者工具的 Network 标签页，显示了对考勤记录的 PUT 请求，状态码为 404 Not Found。
画面 6: 展示 IntelliJ IDEA 中 AttendanceController.java 文件，显示了 importExcel 和 getAttDate 方法的代码。
画面 7: 展示 AttendanceController.java 文件，光标位于 editAtte 方法的注释上方，准备编辑。
画面 8: 展示浏览器开发者工具的 Network 标签页，显示了对考勤记录的 PUT 请求，请求体中包含 userId、days、deptId、attStatus 等参数。
画面 9: 展示 IntelliJ IDEA 中 AtteService.java 文件，显示了 editAtte 方法的代码，注释为“编辑考勤”。
画面 10: 展示 AtteService.java 文件，光标位于 editAtte 方法中，准备调用 attendanceDao.save 方法。
画面 11: 展示 AtteService.java 文件，光标位于 editAtte 方法中，正在输入 attendanceDao.save 方法。
画面 12: 展示 IntelliJ IDEA 中项目结构，光标位于 AttendanceController.java 文件上，准备运行。
画面 13: 展示 iHRM 系统的考勤列表页面，显示了多个员工的考勤记录，状态为“旷工”。
画面 14: 展示 iHRM 系统的考勤列表页面，显示了多个员工的考勤记录，状态为“旷工”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6:
```java
/**
 * 上传考勤数据
 */
@RequestMapping(value = "/import", method = RequestMethod.POST)
public Result importExcel(@RequestParam(name="file") MultipartFile file) throws Exception {
    excelImportService.importAttendanceExcel(file,companyId);
    return new Result(ResultCode.SUCCESS);
}

/**
 * 查询考勤数据列表
 */
@RequestMapping(value = "", method = RequestMethod.GET)
public Result importExcel(int page,int pagesize) throws Exception {
    Map map = atteService.getAttDate(companyId,page,pagesize);
    return new Result(ResultCode.SUCCESS,map);
}

/**
 * 编辑用户的考勤记录
 */
@RequestMapping(value = "/{id}", method = RequestMethod.PUT)
public Result editAtte(@RequestBody Attendance map) throws Exception {
    Map map = atteService.getAttDate(companyId,page,pagesize);
    return new Result(ResultCode.SUCCESS,map);
}
```

画面 7:
```java
/**
 * 编辑用户的考勤记录
 */
@RequestMapping(value = "/{id}", method = RequestMethod.PUT)
public Result editAtte(@RequestBody Attendance map) throws Exception {
    Map map = atteService.getAttDate(companyId,page,pagesize);
    return new Result(ResultCode.SUCCESS,map);
}
```

画面 9:
```java
//编辑考勤
public void editAtte(Attendance attendance) {
    //1.查询考勤记录是否存在，存在则更新，不存在则新增
    Attendance vo = attendanceDao.findByUserIdAndDay(attendance.getUserId(), attendance.getDay());
    if(vo == null) {
        attendance.setId(0);
    }else{
        attendance.setId(vo.getId());
    }
    attendanceDao.save(attendance);
}
```

画面 10:
```java
//编辑考勤
public void editAtte(Attendance attendance) {
    //1.查询考勤记录是否存在，存在则更新，不存在则新增
    Attendance vo = attendanceDao.findByUserIdAndDay(attendance.getUserId(), attendance.getDay());
    if(vo == null) {
        attendance.setId(0);
    }else{
        attendance.setId(vo.getId());
    }
    attendanceDao.save(attendance);
}
```

画面 11:
```java
//编辑考勤
public void editAtte(Attendance attendance) {
    //1.查询考勤记录是否存在，存在则更新，不存在则新增
    Attendance vo = attendanceDao.findByUserIdAndDay(attendance.getUserId(), attendance.getDay());
    if(vo == null) {
        attendance.setId(0);
    }else{
        attendance.setId(vo.getId());
    }
    attendanceDao.save(attendance);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
