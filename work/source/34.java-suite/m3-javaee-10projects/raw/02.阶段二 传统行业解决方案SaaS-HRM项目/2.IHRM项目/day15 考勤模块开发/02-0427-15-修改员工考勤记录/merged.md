# 15-修改员工考勤记录

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\15-修改员工考勤记录_【海量资源尽在 ubkz.com】.mp4
- 时长 6分50秒（音频 410s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们把这个查询列表的这个方法呢已经写好了那接下来我们就可以一起来试一下这个究竟怎么样了那我已经把我们这个微服呢重新启动了一下回到我们的页面刷新一把一起来看一下能不能有这个考勤数据那找到我们的考勤来进来好了各位发现当前的这些数这些是考勤的记录已经有了只不过呢都是矿工啊
[00:31] 为啥呢是因为各位发现这边请求的是不是都是8月份8月份的一些数据那8月份的数据在我们的系统当中呢各位来看考勤表里一条都没有因为刚才我做测试的时候都删了咱们这边是不是只有7月份啊没错吧所以呢这边都是一个矿工的这么一个情况啊OK好了那到目前为止呢咱们这个列表已经搞定了那列表搞定之后呢接下来咱们就开始继续做其他岛那比如说呢咱们
[01:02] 这个员工叫ITcast那这个员工呢他这个8月1号这个数据有点问题他记得是矿工但是呢我们可以把它修改成其他的这种状态那这个我们又该怎么做呢那其实这个也很简单那注意这是页面前端的效果点击过来之后勾选上正常点击确定他会向后台发送一个请求向后台发送这么一个请求
[01:32] 那这个请求发送过来之后我们就需要对当前的这个请求完成相应的业务处理这个就是我们接下来要做的就是考勤修改那对于这个考勤修改相对来说比较简单我们快速的把它实现出来好了找到我们这个代码找到我们这个代码好了那各位来看那考勤修改过来进入的这个方法后面加了一个参数注意这个参数代表的是用户的ID
[02:11] 就是代表的是当前的这个用户的ID当了它还会传递过来这么一个对象那注意这个对象呢其实就是我们要保存到数据库里面的这个烤琴相应对象所以呢我们要做的事情呢很简单注意发送的是一个put请求回到我们这边Ctrl C Ctrl V来一份编辑用户的烤琴记录OK好了那这边它请求的这个路径啊ID
[02:49] 这边是put请求方式没错吧好了接下来呢我们就是编辑editadde好了编辑考勤记录那这边呢它会给我们传递过来一个对象那注意我说过了这个对象其实就是我们需要的考勤对象所以来个at request body那把你这个对象呢转化成我们的考勤对象就可以了att考勤对象
[03:22] 好了没问题考勤对象好了那接下来呢咱们这边呢保存成功直接告他成功就可以了那我们要做的这边事呢就调用Service进行保存Service点好了我们就叫保存吧也就叫edit吧edit好了把这对象呢传递到我们的Service层当中好了Service人少方法在Service当中补充一个方法这边就是我们的编辑考勤
[03:53] 好了那对于咱们要实现的这个方法呢这个就比较简单了这个就比较简单了那这边呢需要各位要注意就是说啊你传递过来这个参数呢传递过来这个考勤有可能数据库存在有可能数据库不存在所以我需要第一个查询一下考勤是否存在好了接着如果不存在我们需要设置这个对象ID这个叫对设置
[04:21] 对象ID这个就是保存那上面这个其实就是更新嘛这个应该各位都能够理解好了那接下来呢咱们就开始把这个代码呢给它实现出来那查询考勤是否存在那各位来看页面前端输入给我们的记录呢输入给我们的数据有什么第一个部门ID第二个user ID第三个就是这个时间对没错吧
[04:48] 所以我们要查询它这个拷群是否存在其实很简单把优惠ID放进去把day放进去是不是就能查了所以这边呢我们可以来查询一下do点好了这都是我们之前写好的点get有的ID好了这个点get叫day哎叫vo这个应该都能理解好了那接下来呢咱们继续再来看那这边呢有可能if vo就是不存在
[05:25] V o等于等于那如果这玩意儿为空的话我们就需要对要保存的记录呢设置一下IDset id id worker.next好了那接下来如果这玩意儿存在存在的话我们需要给它设置上ID同样设置ID那只不过这个ID就是你查询出来的V o.getID能记住吧好了如果这个ID给它设置上之后其实这回就变成了更新了
[05:56] 所以我们接下来做最后一步操作点save别更新错传递过来是哪个我们就更新哪个OK好了这样一来代码咱们就已经写好了我这边重新启动一下我们来验证一下它最终的效果好了这边咱们服务已经重新启动成功了回到我们的页面一起来试一下刷新一下刷新一下网关还没有反应过来好接下来8月1号
[06:30] 好了给它改成正常走好了会发现它已经正常了当然可以给它改成迟到变成迟到状态了所以这样一来呢我们现在已经完成了烤琴列表烤琴设置当然还有烤琴的录入已经对应的这个烤琴修改OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

