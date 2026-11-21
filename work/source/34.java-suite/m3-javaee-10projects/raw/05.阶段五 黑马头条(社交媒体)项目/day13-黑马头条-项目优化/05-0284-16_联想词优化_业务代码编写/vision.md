# 画面线理解：16_联想词优化_业务代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\16_联想词优化_业务代码编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:03, 01:34, 02:52, 04:09, 05:01, 06:05, 06:56, 07:54, 08:55, 10:28, 11:26, 12:30, 13:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:56:24

1) 这一组画面整体在讲如何使用 Trie 树数据结构实现关联词搜索功能，并结合 Redis 缓存进行优化。

2) 按时间顺序列出每张画面的要点：
画面1：展示文档中“3.3.6 工具类说明”部分，包含 TrieNode 类的 Java 代码定义和 Trie 工具类的声明。
画面2：展示数据库 SQL 查询语句，用于从关联词表中模糊查询。
画面3：展示 TrieNode 类中插入单词的 Java 代码实现。
画面4：展示文档中“3.3.7 代码实现”部分，包含 ApArticleSearchService 接口定义。
画面5：展示项目结构，突出 ApArticleSearchService 接口和相关实现类。
画面6：展示 ApArticleSearchServiceImpl 类中 findUserSearch 方法的代码，包含参数校验和数据库查询。
画面7：展示 findUserSearch 方法中对分页大小的校验逻辑。
画面8：展示 searchAssociationV2 方法中使用 RedisTemplate 的代码。
画面9：展示 searchAssociationV2 方法中声明的多个 Mapper 接口。
画面10：展示 searchAssociationV2 方法中使用 JSON 序列化和 Redis 存储的代码。
画面11：展示 searchAssociationV2 方法中使用 try-catch 块处理异常。
画面12：展示 searchAssociationV2 方法中创建 Trie 树并插入关联词的代码。
画面13：展示 searchAssociationV2 方法中使用 Trie 树进行前缀匹配并返回结果的代码。
画面14：展示 searchAssociationV2 方法中将匹配结果封装并返回的代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
```java
public class TrieNode {
    public char var;
    public boolean isword;
    public Map<Character, TrieNode> children = new HashMap<>();
    public boolean containLongTail = false;
    public TrieNode() {
    }
    public TrieNode(char c) {
        TrieNode node = new TrieNode();
        node.var = c;
    }
}
```
```java
public class Trie {
    private TrieNode root;
}
```
画面2：
```sql
select id=selectB/associateWords resultMap="BaseResultMap"
select
    include refid="Base_column_list" />
from sp_associate_words
where associate_words like #{searchWords} limit #{limit}
```
画面3：
```java
private TrieNode root;
public Trie() {
    root = new TrieNode();
    root.var = '';
}
//插入trie树
public void insert(String word) {
    TrieNode ws = root;
    for(int i = 0; i < word.length(); i++){
        char c = word.charAt(i);
        if(!ws.children.keySet().contains(c)) {
            ws.children.put(c, new TrieNode());
        }
        ws = ws.children.get(c);
    }
}
```
画面4：
```java
(1) ApArticleSearchService
//  联想词V2
@param userSearchDto
@return
ResponseResult searchAssociateV2(UserSearchDto userSearchDto);
```
画面5：
```java
ResponseResult searchUserSearch(UserSearchDto dto);
// 保存搜索记录
@Param entryId
@Param searchWords
@return
ResponseResult saveUserSearch(Integer entryId, String searchWords);
ResponseResult searchAssociationV2(UserSearchDto dto);
```
画面6：
```java
@Autowired
private ApUserSearchMapper apUserSearchMapper;
@Override
public ResponseResult findUserSearch(UserSearchDto dto) {
    if(dto.getPageSize() > 30 || dto.getPageSize() < 1) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //完成业务实体id
    ResponseResult result = apUserSearchMapper.selectById(dto.getEntryId());
    if(result.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    //查询搜索记录
    List<ApUserSearch> list = apUserSearchMapper.selectByEntryId(int result.getData(), dto.getPageSize());
    return ResponseResult.okResult(list);
}
```
画面7：
```java
@Override
public ResponseResult findUserSearch(UserSearchDto dto) {
    if(dto.getPageSize() > 30 || dto.getPageSize() < 1) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //完成业务实体id
    ResponseResult result = apUserSearchMapper.selectById(dto.getEntryId());
    if(result.getCode() == AppHttpCodeEnum.SUCCESS.getCode()) {
        return result;
    }
    //查询搜索记录
    List<ApUserSearch> list = apUserSearchMapper.selectByEntryId(int result.getData(), dto.getPageSize());
    return ResponseResult.okResult(list);
}
```
画面8：
```java
@Autowired
private StringRedisTemplate redisTemplate;
@Override
public ResponseResult searchAssociationV2(UserSearchDto dto) {
    if(dto==null || dto.getPageSize() > 50) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    redisTemplate.opsForValue().get("associate_list");
    return null;
}
```
画面9：
```java
@Autowired
private StringRedisTemplate redisTemplate;
@Override
public ResponseResult searchAssociationV2(UserSearchDto dto) {
    if(dto==null || dto.getPageSize() > 50) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    String assoStr = redisTemplate.opsForValue().get("associate_list");
    List<String> aw = null;
    if(StringUtils.isBlank(assoStr)) {
        aw = JSON.parseArray(assoStr, ApAssociateWords.class);
    } else {
        aw = apAssociateWordsMapper.selectAllAssociateWords();
        redisTemplate.opsForValue().set("associate_list", JSON.toJSONString(aw));
    }
    return null;
}
```
画面10：
```java
@Override
public ResponseResult searchAssociationV2(UserSearchDto dto) {
    if(dto==null || dto.getPageSize() > 50) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    String assoStr = redisTemplate.opsForValue().get("associate_list");
    List<String> aw = null;
    if(StringUtils.isBlank(assoStr)) {
        aw = JSON.parseArray(assoStr, ApAssociateWords.class);
    } else {
        aw = apAssociateWordsMapper.selectAllAssociateWords();
        redisTemplate.opsForValue().set("associate_list", JSON.toJSONString(aw));
    }
    return null;
}
```
画面11：
```java
@Override
public ResponseResult searchAssociationV2(UserSearchDto dto) {
    if(dto==null || dto.getPageSize() > 50) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    String assoStr = redisTemplate.opsForValue().get("associate_list");
    List<String> aw = null;
    if(StringUtils.isBlank(assoStr)) {
        aw = JSON.parseArray(assoStr, ApAssociateWords.class);
    } else {
        aw = apAssociateWordsMapper.selectAllAssociateWords();
        redisTemplate.opsForValue().set("associate_list", JSON.toJSONString(aw));
    }
    return null;
}
```
画面12：
```java
@Override
public ResponseResult searchAssociationV2(UserSearchDto dto) {
    if(dto==null || dto.getPageSize() > 50) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    String assoStr = redisTemplate.opsForValue().get("associate_list");
    List<String> aw = null;
    if(StringUtils.isBlank(assoStr)) {
        aw = JSON.parseArray(assoStr, ApAssociateWords.class);
    } else {
        aw = apAssociateWordsMapper.selectAllAssociateWords();
        redisTemplate.opsForValue().set("associate_list", JSON.toJSONString(aw));
    }
    //使用trie树进行管理词
    Trie t = new Trie();
    for (ApAssociateWords a : aw) {
        t.insert(a.getAssociateWords());
    }
    return null;
}
```
画面13：
```java
@Override
public ResponseResult searchAssociationV2(UserSearchDto dto) {
    if(dto==null || dto.getPageSize() > 50) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    String assoStr = redisTemplate.opsForValue().get("associate_list");
    List<String> aw = null;
    if(StringUtils.isBlank(assoStr)) {
        aw = JSON.parseArray(assoStr, ApAssociateWords.class);
    } else {
        aw = apAssociateWordsMapper.selectAllAssociateWords();
        redisTemplate.opsForValue().set("associate_list", JSON.toJSONString(aw));
    }
    //使用trie树进行管理词
    Trie t = new Trie();
    for (ApAssociateWords a : aw) {
        t.insert(a.getAssociateWords());
    }
    List<String> ret = t.startWith(dto.getSearchWords());
    for (String s : ret) {
        ApAssociateWords apassociateWords = new ApAssociateWords();
        apassociateWords.setAssociateWords(s);
        list.add(apassociateWords);
    }
    return null;
}
```
画面14：
```java
@Override
public ResponseResult searchAssociationV2(UserSearchDto dto) {
    if(dto==null || dto.getPageSize() > 50) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    String assoStr = redisTemplate.opsForValue().get("associate_list");
    List<String> aw = null
