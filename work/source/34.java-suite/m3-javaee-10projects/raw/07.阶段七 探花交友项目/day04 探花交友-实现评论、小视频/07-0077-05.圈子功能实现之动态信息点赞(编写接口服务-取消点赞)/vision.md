# 画面线理解：05.圈子功能实现之动态信息点赞（编写接口服务-取消点赞）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\05.圈子功能实现之动态信息点赞（编写接口服务-取消点赞）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:27, 00:37, 01:15, 01:29, 01:43, 02:26, 02:41, 03:19, 03:31, 03:44, 04:00, 04:10, 04:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:50:55

1) 这一组画面整体在讲如何实现点赞和取消点赞功能，包括接口定义、Controller层代码和Service层代码的编写与调试。

2) 按时间顺序列出每张画面的要点：
画面1：展示接口文档，接口名称为“动态-取消点赞”，状态为“已完成”，接口路径为“GET /movements/{id}/dislike”，Mock地址为“https://mock.boxuegu.com/mock/164/movements/{id}/dislike”，请求参数为“id”（示例：动态id）。
画面2：展示IntelliJ IDEA中MovementsController.java文件，代码为点赞接口的实现，包含@GetMapping("/id/like")注解和try-catch块，返回ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build()。
画面3：展示IntelliJ IDEA中MovementsController.java文件，代码为点赞接口的实现，包含try-catch块，返回ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build()。
画面4：展示IntelliJ IDEA中MovementsService.java文件，代码为dislikeComment方法的定义，参数为String publishId。
画面5：展示IntelliJ IDEA中MovementsService.java文件，代码为dislikeComment方法的定义，参数为String publishId。
画面6：展示IntelliJ IDEA中MovementsService.java文件，代码为dislikeComment方法的定义，参数为String publishId。
画面7：展示IntelliJ IDEA中MovementsService.java文件，代码为dislikeComment方法的定义，参数为String publishId。
画面8：展示IntelliJ IDEA中MovementsService.java文件，代码为dislikeComment方法的定义，参数为String publishId。
画面9：展示IntelliJ IDEA中MovementsService.java文件，代码为dislikeComment方法的定义，参数为String publishId。
画面10：展示IntelliJ IDEA中MovementsService.java文件，代码为dislikeComment方法的定义，参数为String publishId。
画面11：展示IntelliJ IDEA中MovementsController.java文件，代码为取消点赞接口的实现，包含@GetMapping("/id/dislike")注解和try-catch块，返回ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build()。
画面12：展示IntelliJ IDEA中MovementsService.java文件，代码为dislikeComment方法的定义，参数为String publishId。
画面13：展示IntelliJ IDEA中MovementsService.java文件，代码为dislikeComment方法的定义，参数为String publishId。
画面14：展示Typora中day04.评论.md文件，内容为“1.1.4. 编写服务实现”部分，包含package语句和import语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
接口名称：动态-取消点赞
状态：已完成
接口路径：GET /movements/{id}/dislike
Mock地址：https://mock.boxuegu.com/mock/164/movements/{id}/dislike
请求参数：
参数名称	示例	备注
id		动态id
Headers：

画面2：
@GetMapping("/id/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String publishId) {
    try {
        Long count = this.movementsService.likeComment(publishId);
        if (null != count) {
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}

画面3：
@GetMapping("/id/like")
public ResponseEntity<Long> likeComment(@PathVariable("id") String publishId) {
    try {
        Long count = this.movementsService.likeComment(publishId);
        if (null != count) {
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}

画面4：
public Long dislikeComment(String publishId) {

画面5：
public Long dislikeComment(String publishId) {

画面6：
public Long dislikeComment(String publishId) {

画面7：
public Long dislikeComment(String publishId) {

画面8：
public Long dislikeComment(String publishId) {

画面9：
public Long dislikeComment(String publishId) {

画面10：
public Long dislikeComment(String publishId) {

画面11：
@GetMapping("/id/dislike")
public ResponseEntity<Long> dislikeComment(@PathVariable("id") String publishId) {
    try {
        Long count = this.movementsService.disLikeComment(publishId);
        if (null != count) {
            return ResponseEntity.ok(count);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}

画面12：
public Long dislikeComment(String publishId) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanZiApi.removeComment(user.getId(), publishId, commentType:1);
    if(!bool){
        return null;
    }

画面13：
public Long dislikeComment(String publishId) {
    User user = UserThreadLocal.get();
    boolean bool = this.quanZiApi.removeComment(user.getId(), publishId, commentType:1);
    if(!bool){
        return null;
    }

画面14：
package com.tanhua.server.service;

import com.alibaba.dubbo.common.utils.CollectionUtils;
import com.alibaba.dubbo.config.annotation.Reference;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.tanhua.server.pojo.Publish;
import com.tanhua.server.pojo.User;
import com.tanhua.server.utils.UserThreadLocal;
import com.tanhua.server.vo.Movements;
import com.tanhua.server.vo.PageInfo;
import com.tanhua.server.vo.PicUploadResult;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
