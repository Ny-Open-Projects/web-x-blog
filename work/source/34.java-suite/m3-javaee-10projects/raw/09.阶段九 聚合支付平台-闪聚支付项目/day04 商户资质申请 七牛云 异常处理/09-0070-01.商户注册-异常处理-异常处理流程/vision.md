# 画面线理解：01.商户注册-异常处理-异常处理流程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\01.商户注册-异常处理-异常处理流程【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:34, 02:03, 02:38, 03:17, 03:53, 04:12, 05:31, 05:44, 06:27, 07:54, 09:10, 10:19, 10:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:01:30

1) 这一组画面整体在讲什么（一句话）：
讲解系统异常处理的规范，包括异常信息格式、异常处理流程以及自定义异常类的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档目录，当前选中“2.4.6 校验商户手机号”章节，右侧内容为“2.4.5.1 异常信息格式”，包含状态码200（成功）、401（没有权限）、500（程序错误）的说明。
画面2：IDE中显示验证验证码的Java代码，使用RestTemplate发起POST请求，若响应body中result为null或false，则抛出RuntimeException异常。
画面3：文档页面显示“2.4.5.2 异常处理流程”标题，下方有“自定义错误体”示例JSON，其中“errorMessage”字段被高亮。
画面4：文档页面显示“2.4.5.1 异常信息格式”，内容与画面1相同。
画面5：文档页面显示“2.4.5.2 异常处理流程”标题，下方有“自定义错误体”示例JSON，其中“errorMessage”字段被高亮。
画面6：Postman工具中发送POST请求到“http://localhost:5001/merchant/merchants/register”，返回状态码500，响应体包含“error”: “Internal Server Error”。
画面7：文档页面显示“2.4.5.1 异常信息格式”，内容与画面1相同。
画面8：文档页面显示“系统规范了异常处理流程，如下：”，下方是一个流程图，包含“响应信息（errCode, errMessage）”、“取出ErrorCode”、“统一为99999异常”、“BusinessException 自定义异常”、“Exception 不可预知异常”、“异常捕获”、“Application”、“Service (Dubbo)”等节点。
画面9：文档页面显示“系统规范了异常处理流程，如下：”，下方流程图中“异常捕获”节点被鼠标悬停。
画面10：文档页面显示“系统规范了异常处理流程，如下：”，下方流程图中“异常捕获”节点被鼠标悬停。
画面11：IDE中显示发送验证码的Java代码，使用RestTemplate发起POST请求，若响应body中result为null或false，则抛出RuntimeException异常。
画面12：文档页面显示“系统规范了异常处理流程，如下：”，下方流程图中“Application”节点被鼠标悬停。
画面13：Redis客户端界面，显示连接到localhost:6379，键“sms:1310139960c34c34a5a313d91881d3de”对应的值为“586438”。
画面14：文档页面显示“系统规范了异常处理流程，如下：”，下方流程图中“Service (Dubbo)”节点被鼠标悬停。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2代码：
String url = "http://localhost:56685/saling/verify?name=sak&verificationCode=" + verifyCode;
Map bodyMap = null;
ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, new HttpEntity<>(null, headers), Map.class);
Log.info("请求验证码服务，得到响应：{}", JSON.toJSONString(exchange));
bodyMap = exchange.getBody();
if (bodyMap == null || bodyMap.get("result") == null || !(Boolean) bodyMap.get("result")) {
    throw new RuntimeException("校验验证码失败");
}
画面11代码：
httpHeaders.setContentType(MediaType.APPLICATION_JSON);
HttpEntity httpEntity = new HttpEntity(body, httpHeaders);
ResponseEntity<Map> exchange = null;
Map bodyMap = null;
try {
    exchange = restTemplate.exchange(sess_url, HttpMethod.POST, httpEntity, Map.class);
    Log.info("请求验证码服务，得到响应：{}", JSON.toJSONString(exchange));
    bodyMap = exchange.getBody();
    if (bodyMap == null || bodyMap.get("result") == null || !(Boolean) bodyMap.get("result")) {
        throw new RuntimeException("发送验证码失败");
    }
    String key = (String) bodyMap.get("key");
    Log.info("得到发送验证码对应的key：{}", key);
    return key;
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8、9、10、12、14：流程图结构如下：
- “响应信息（errCode, errMessage）”指向“取出ErrorCode”。
- “取出ErrorCode”指向“统一为99999异常”。
- “统一为99999异常”指向“BusinessException 自定义异常”和“Exception 不可预知异常”。
- “BusinessException 自定义异常”和“Exception 不可预知异常”都指向“异常捕获”。
- “异常捕获”指向“Application”。
- “Application”指向“Service (Dubbo)”。
画面12：在“Application”节点下方有文字说明：“抛出异常BusinessException”。
画面14：在“Service (Dubbo)”节点下方有文字说明：“抛出异常BusinessException”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
