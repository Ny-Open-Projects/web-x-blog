# 05.圈子功能实现之动态信息点赞（编写接口服务-取消点赞）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\05.圈子功能实现之动态信息点赞（编写接口服务-取消点赞）_【海量资源尽在 666java.com】.mp4
- 时长 4分31秒（音频 271s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下这个取消点赞的这个API那么这个API的这个名字啊叫什么呢叫做这个dislike啊也就是说这个取消这个like同样的还是去传递我们这个ID啊这样的一个参数然后呢下面我们来看一下那么在返回这个结果中啊那么依然是需要去返回这个点赞数的所以说接下来呢我们来写一下这个API
[00:29] 那么首先呢我们就可以直接来拷贝一下是不是前面所写的点赞的这个Controller修改一下就ok了对吧好那么来看一下这个首先呢改成dcdslack看一下它是小写吧这个别写错啊全小写然后呢这个我们就写一个dclike然后呢传递一个这个public id然后呢我们这个位置呢需要调用的什么呢就叫dc
[00:58] like comment把这个传递过去然后呢其他的逻辑呢是不是就都一样了这个叫什么呢叫做取消取消点赞然后呢我们来实现啊这个Service中的这个方法那么看一下这个方法如何去做一个实现那么取消点赞呢首先呢我们肯定是需要去先去拿到我们这个user对象对吧
[01:24] 等于这个user-local.get去拿到这个对象然后呢我们去调用我们圈子API里面的什么呢有个叫做remote啊contactremote这个comment然后呢user id呢来一个user.get id那第二个参数呢就是这个public id第三个参数呢就是type那么现在我们传第一那么这样的话是不是就可以去做删除了对吧拿一个这个布尔兹
[01:52] 那么接下来呢我们显然呢是需要去做一个布尔值的一个判断那么如果为force那我们就如果为force那我们就return什么呢比方说我们就return0吧应该是return什么return none对吧不应该return0然后呢下面呢我们就来看一下那么我既然已经取消点赞了对不对那我这个就是我redis中的这个点赞数就需要什么呢需要减
[02:21] 需要减少减少1对不对那么应该这个怎么去减少呢我们来看一下那么上面我们这个点证数我们来拷贝一下这个是它的一个key它的一个key然后呢我们就需要调用this.readystemplate.进行什么呢进行做一个什么呢discrement做一个我们的一个减1减少就可以了
[02:50] 那么它的返回值那么其实就是我们的一个这个count了对吧这个就是我们的一个count那我们最后呢把这个count给它做一个return就OK那么这是一个操作那么接下来是吧我们应该去删除这个该用户的一个标记点赞对吧那我应该把它删除掉那么还是拿到上面这个key
[03:19] 然后呢我们就可以去做一个删除了是不是通过this.readistemplate.delete去做一个删除这样的话是不是就OK了好那么到这里呢我们这个取消点赞是不是就搞定了那么接下来呢我们同样的也是去打一个断点然后呢我们再次呢把我们的这个服务呢跑起来好那么来等待它的一个启动好那么现在我们就重启起来了接下来我们来测试一下
[03:48] 那么我们只需要把这个加一个什么呢diss like这样的话就可以了走那么我们发起请求那么现在呢就进入到Controller了然后呢我们进入到我们这个Service往下面走走哎它呢是去然后删除然后呢这个是做一个递减然后下面去做删除啊这样的话就ok了好通过那么如果我再次去做一个取消的话看它会怎么样走
[04:16] 然后呢我们去往下面走这个呢显然看的是不是就是为浪了对吧直接就会响应什么响应这个500了OK好嘞那么到这里呢我们这个取消点赞啊是不是也就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package com.tanhua.server.Service;

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

