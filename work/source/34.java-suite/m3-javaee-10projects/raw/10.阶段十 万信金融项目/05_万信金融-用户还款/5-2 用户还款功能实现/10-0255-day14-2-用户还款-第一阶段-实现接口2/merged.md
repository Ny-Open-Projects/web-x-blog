# day14-2-用户还款-第一阶段-实现接口2

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-2-用户还款-第一阶段-实现接口2_【海量资源尽在 666java.com】.mp4
- 时长 8分26秒（音频 506s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才我们把第一阶段当中接口一这块功能已经实现过了接下来按照顺序怎样实现接口二接口二是不是根据接口一生成的或者查询到的还款计划去生成什么还款联系就是把这个还款联系的给它保存到哪个表里对保存到 repayment detail 这个表里这是不是也是数据库操作增删改查当中的增对不对
[00:29] 所以说呢我们也是像要干什么先编写数据访问我们需要再加一个什么呀接口那是接口啊这个接口呢是不是用来操作这个repayment的这个表的所以说咱这个接口的名字这么起啊一paymentrepayment的第一第一什么呀d t a i l m a p p a定义这么一个
[01:05] 然后呢这个接口跟之前一样我们也让他继承MP的这个什么呀对base那这个范形是不是就是这个表对应的那个实体类啊叫repayment detailrepayment什么呀detail对没错好这呢我加上这个注释吧这是什么呀对操作操作这个表操作这个表的什么呀
[01:43] map 接口哎那这个数据访问层的这个代码呢咱就写了目前呢这里边暂时不需要咱去自定义方法啊咱就用从这个接口里边继承的那些增长改查就满足使用啊目前啊那这个数据访问层咱们搞定之后接下来是不是该编写业务层的代码好咱找到业务层啊还是这个业务层实现类对不对那第二个接口对应的方案是不是这个方法
[02:17] 你看咱刚才已经生成了但是这个呃代码咱还没实现了那这样呢咱就要实现这个什么功能对根据什么呀还款计划去生成啊或者说保存还款明信那这里边这个逻辑呢应该是我们可以给它分成两步第一步是那先进行什么呀先进行查询然后呢查不到数据才进行什么呀
[02:52] 保存啥意思啊来看看看这个表就是这个repayment detail这是不是还款明细吗我们说了每个还款计划是不是都会对应一个还款明细那么这个表里边数据呢很有可能它有可能是已经存在就是某个还款计划它对应的还款明细有可能是已经存在这是很有可能的那我们这个时候呢在保存数据之前先查一下查查某个还款计划它的这个明细数据是不是已经有了有了的话我就
[03:22] 查出来之后我直接返回了对不对那没有的话我才拧一个对象然后调上setter方案给它复制然后保存到这个表里边啊所以要先做一个查询那根据什么来查我们说了我们查的是不是某个还款计划对应的还款明细那自然就是根据这个什么呀还款计划的ID啊但是大家注意这个可不是表里边的主件啊这个不是表里边的主件但是我们查询的确是根据还款计划的ID来进行查询的
[03:50] 所以你看我们这里边是不是分成了这两步那这个代码呢编译起来还是比较简单的咱先把这个刚才这个map接口先注进来private叫repaymentrepayment detail是什么呀map注进来之后呢我们回到在哪
[04:25] 在这对吧我们说了先进行什么样查询吧那个调用这个接口呗那我调用他哪个方法呢查询哪个方法再来个白地吗可不是啊这个方式根据主建查的我们刚才说了我们这个这个什么样缓缓计划来的可不是主见那我们应该根据谁去查呢应该用哪个方法应该这个方法是来个等不完然后呢你把这个条件给他封装用warp对不对进行封装就行这个代码咱们之前也经常写大家应该
[04:57] 还有印象那既然把这个代码写一下吧咱还用Lambda的那种写法啊那应该是WR哪个类啊WRAWARPS对不对点什么呀LambdaQuery我们需要在这儿指定一下范形范形不用说了是不是就是那个repayment detailrepayment detail因为我们操作是这个表啊
[05:26] 然后我们要封装的条件是一个相等判断嘛就是那个缓缓计划ID等于谁那这个字段名我们就应该是这么个来写的啊字段名应该是这个是不是是他不是对这就是缓缓计划ID吗直直从哪来啊直你看这个参照对象不就是一个缓缓计划吗不就是要他的ID呢来我们调他的什么给他吧搞定这个条件封装好了对吧封装好之后呢你扔给slide1方案他就进行了查询
[05:59] 那么他查出来的就是一个什么对象对还款银器我们接收一下就行了这是我们这个查询就搞定搞定完之后呢我们在这是不是要做判断啊你要做判断啊看看有没有查出来数据吗如果他干什么呀等于证明这个还款银器是不是还不存在那我应该在衣服里边就要进行什么呀保存对吧保存完之后呢我们最终是不是要
[06:31] 反回这个对象啊因为我说了嘛以后啊后边这个流程当中还要用这个对象所以说需要作为反制反而这里边代码应该很简单吧不就是一个常规的一个保存吗我们new这么一个对象是不是然后掉他的一堆在这方向往里边复制复完之之后掉没法解口就实现了保存这个代码我就不再给大家编写了啊我们拿过来用一用就行了最简单的一块代码好咱过一遍啊过一遍
[07:05] 这套路一样嘛首先我先自己拗一个这个什么实体类对象拗完之后你看开始agre down set方法往里边复制吧比如说这个什么呀这个IDrepayment plan ID还有这个什么呀本息对吧这些数据都是从哪取的你看都是从这个缓缓计划里边去这也是为什么我们这个方法要要加这么一个参数的原因吗缓缓的时间啊缓缓的时间就是这个什么当前时间啊还有什么呀我们自己又生成了一个流水号对不对
[07:40] 这个生成的流水号有啥用咱后边用到的时候再说因为我们将来要跟从管代理服打交道要发请求大家结合以往的经验我们一般跟从管代理服打交道是不是都会有一个流水号对不对这个流水号是不是还是那个request的流水号我们可以进去看看是吧还是这个流水号用了好多次还有就是这个数据的状态默认应该是什么对未同步的大概就这么几个值该给的都给过了然后掉Mapper接口
[08:12] 什么方法因此的方法就实现了这个什么呀这块功能也比较简单这是目前吧咱把第一阶段接口二这块功能呢也全部搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在还款服务中，通过 MyBatis-Plus 的 Mapper 接口和 LambdaQueryWrapper 实现对还款明细表（repayment_detail）的查询与保存功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示数据库表 repayment_plan 的查询结果，SQL 语句为 SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOLD_REPAYMENT_DATE, '%Y-%m-%d') = '2024-04-15' AND REPAYMENT_STATUS = '1'。
画面2: 展示数据库表 repayment_detail 的结构，包含字段 ID、REPAYMENT_PLAN_ID、AMOUNT、REPAYMENT_DATE、REQUEST_ID、STATUS。
画面3: 展示 RepaymentDetailMapper.java 文件，定义了接口 RepaymentDetailMapper extends BaseMapper<RepaymentDetail>。
画面4: 展示 RepaymentDetailMapper.java 文件，接口定义为 public interface RepaymentDetailMapper extends BaseMapper<RepaymentDetail>。
画面5: 展示数据库表 repayment_plan 的查询结果，SQL 语句为 SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOLD_REPAYMENT_DATE, '%Y-%m-%d') = '2024-04-15' AND REPAYMENT_STATUS = '1'。
画面6: 展示 RepaymentServiceImpl.java 文件，定义了方法 @Transactional(rollbackFor = BusinessException.class) public String startRepayment(ProjectWithTendersDTO projectDTO)。
画面7: 展示 RepaymentServiceImpl.java 文件，定义了方法 @Override private void saveReceivablePlan(RepaymentPlan repaymentPlan, TenderDTO tender, EqualInterestRepayment receipt)。
画面8: 展示 RepaymentServiceImpl.java 文件，定义了方法 @Override public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan)。
画面9: 展示 RepaymentServiceImpl.java 文件，定义了方法 @Override public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan)。
画面10: 展示 RepaymentServiceImpl.java 文件，定义了方法 @Override public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan)。
画面11: 展示 RepaymentServiceImpl.java 文件，定义了方法 @Override public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan)。
画面12: 展示 PPT 页面，标题为“3.2.2 还款服务生成还款明细接口(接口②)”，内容为在业务层 RepaymentServiceImpl 类中实现生成还款明细功能，代码为 @Override RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) { RepaymentDetail repaymentDetail = repaymentDetailMapper.selectOne( wrappers.<RepaymentDetail>lambdaQuery().eq(RepaymentDetail::getRepaymentPlanId, repaymentPlan.getId())); if (repaymentDetail != null) { ... } }。
画面13: 展示 CodePrefixCode.java 文件，定义了常量 CODE_CONSUMER_PREFIX = "USR_"，CODE_REQUEST_PREFIX = "REQ_"。
画面14: 展示 RepaymentServiceImpl.java 文件，定义了方法 @Override public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) { RepaymentDetail repaymentDetail = repaymentDetailMapper.selectOne( wrappers.<RepaymentDetail>lambdaQuery().eq(RepaymentDetail::getRepaymentPlanId, repaymentPlan.getId())); if (repaymentDetail != null) { ... } }。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOLD_REPAYMENT_DATE, '%Y-%m-%d') = '2024-04-15' AND REPAYMENT_STATUS = '1'

画面2:
Columns (6)
Field Type Comment
ID bigint(20) 主键
REPAYMENT_PLAN_ID bigint(20) 还款计划关联标识
AMOUNT decimal(10,2) 金额
REPAYMENT_DATE datetime 还款日期时间
REQUEST_ID varchar(50) 请求流水号（用于请求流水号生成器），查询时，查询多个还款计划时，需要多个还款计划的请求流水号。
STATUS tinyint(4) 可用状态

画面3:
package cn.itcast.wanxingzp.repayment.Mapper;
import com.baomidou.mybatisplus.core.Mapper.BaseMapper;
public interface RepaymentDetailMapper extends BaseMapper<RepaymentDetail> {

画面4:
package cn.itcast.wanxingzp.repayment.Mapper;
import cn.itcast.wanxingzp.repayment.entity.RepaymentDetail;
import com.baomidou.mybatisplus.core.Mapper.BaseMapper;
public interface RepaymentDetailMapper extends BaseMapper<RepaymentDetail> {

画面6:
@Override
@Transactional(rollbackFor = BusinessException.class)
public String startRepayment(ProjectWithTendersDTO projectDTO) {

画面7:
@Override
private void saveReceivablePlan(RepaymentPlan repaymentPlan, TenderDTO tender, EqualInterestRepayment receipt) {

画面8:
@Override
public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {

画面9:
@Override
public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {

画面10:
@Override
public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {

画面11:
@Override
public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {

画面12:
@Override
public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {
RepaymentDetail repaymentDetail = repaymentDetailMapper.selectOne(
wrappers.<RepaymentDetail>lambdaQuery().eq(RepaymentDetail::getRepaymentPlanId, repaymentPlan.getId()));
if (repaymentDetail != null) {

画面13:
CODE_CONSUMER_PREFIX = "USR_",
CODE_REQUEST_PREFIX = "REQ_"

画面14:
@Override
public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {
RepaymentDetail repaymentDetail = repaymentDetailMapper.selectOne(
wrappers.<RepaymentDetail>lambdaQuery().eq(RepaymentDetail::getRepaymentPlanId, repaymentPlan.getId()));
if (repaymentDetail != null) {

4) PPT 标题、架构图/流程图的结构、表格数据：
画面12:
标题：3.2.2 还款服务生成还款明细接口(接口②)
内容：在业务层 RepaymentServiceImpl 类中实现生成还款明细功能，代码为：
@Override
RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {
RepaymentDetail repaymentDetail = repaymentDetailMapper.selectOne(
wrappers.<RepaymentDetail>lambdaQuery().eq(RepaymentDetail::getRepaymentPlanId, repaymentPlan.getId()));
if (repaymentDetail != null) {
... } }。

5) 无。

