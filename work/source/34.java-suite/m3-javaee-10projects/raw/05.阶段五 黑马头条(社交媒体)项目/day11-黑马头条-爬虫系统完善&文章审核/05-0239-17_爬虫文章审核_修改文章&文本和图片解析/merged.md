# 17_爬虫文章审核_修改文章&文本和图片解析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\17_爬虫文章审核_修改文章&文本和图片解析【海量资源尽在 666java.com】.mp4
- 时长 4分20秒（音频 260s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就接着往下看然后这个进度咱们先不玩了写咱们先把这两个方法给补全第一个是当前的修改的方法然后第二个是当前的处理这个当前的文本和图片的方法现在咱们先来完成第一个就是update CL News咱们找到这个方法来看一下这个怎么写呢就在这你看这有一个叫做CL NewsRset什么呢
[00:30] set status直接给一个就可以了这就是失败因为咱们现在是这里边都是干嘛了都是失败都是失败然后下面可以去再去设置它的一个名谣述点一个reset list是吧你可以把当前的message装进去就可以了中的一定要用当前的srv srvnews viper点有一个叫做update status好然后这时候你就可以把当前的srvnews装进去就可以了
[01:00] 看的话就算是修改成功好吧这是修改啊然后下面呢咱们来去完成这个方法那这个方法呢其实最主要的呢就是要找出文本和图片是吧从哪啊从当前的杰森尔瑞中是吧杰森尔瑞刚才说了其实就是当前这么个内容所以说写习也还是挺容易的啊好直接打开在这啊咱们可以直接判断一下啊如果说不等于不等于谁啊
[01:34] 不等于当前这个json array然后呢咱们下面就可以去循环json array.for然后呢它这个呢其实是一个什么呢是一个object就能叫obj吧这个obj其实是一个叫json object我们可以写json objectjson object等于obj这样的话咱们又强转一下这样操作起来比较方便啊
[02:05] 通过jsonobigroup.js打一个get,给了谁呢其实第一个咱们要给一个type然后最终就能拿到当前这个typestring type就等于,好,转一下这个就相当于拿到谁拿到于一项中的一个type因为咱们现在循环的是某一个对象OK这样拿到type之后咱们就可以去判断
[02:40] 我判断呢if如果说啊当前的imadmade啊.reqs当前的type那这时候呢不是它是一个什么它是一个图片这时候我们就可以jsonobgoobject.get谁呢这是当前的value拿到值吗这里是不是值啊不拿到一个密值拿到这个value啊
[03:13] 最终咱们要的是当前的图片的路径对吧所以说呢咱们在这啊拿到这个路径之后呢返回这它返回的也是一个Street的字母圈啊Street这个呢就是强转一下吧好强转完之后呢你就可以把它装到哪啊装到隐秘之然后是Value啊就Value啊那的话就是一个图片好咱们可以判断第二个呗
[03:43] 第二个其实跟这个类似是吧判断一下呗下面是什么呢下面是text, 说是text是文本的话这时候呢咱们拿到的也是value这时候呢你就可以干嘛呢你就可以用当前的open去按s.open然后呢就把这个value放进去就可以了这样就可以了那行那这两个方法试完之后那这个流程咱们就先洗到这
[04:12] 然后接下来呢咱们再去保存文章和图片啊不是保存文章和文章的一些其他信息好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现对文章文本和图片的审核功能，通过调用阿里云的文本和图片审核 API，并更新数据库中的文章状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了项目结构，选中了 `AliyunTextScanRequest` 类，右侧编辑器显示了 `ReviewCrawlerArticleService.java` 中的文本审核逻辑，包括日志记录、文本内容解析和审核失败时的更新操作。
画面 2: 选中了 `AliyunImageScanRequest` 类，右侧编辑器显示了图片审核的逻辑，包括调用图片审核 API 和审核失败时的更新操作。
画面 3: 在 `handlerTextAndImages` 方法中，光标位于 `cNews.setStatus(0);` 语句，显示了修改文章状态的代码。
画面 4: 在 `handlerTextAndImages` 方法中，光标位于 `cNewsMapper.updateNews(cNews);` 语句，显示了更新数据库中文章信息的代码。
画面 5: 展示了 `handlerTextAndImages` 方法的完整结构，包括参数声明和方法体。
画面 6: 在 `handlerTextAndImages` 方法中，光标位于 `if(null != jsonArray)` 语句，准备开始遍历 JSON 数组。
画面 7: 在 `handlerTextAndImages` 方法中，光标位于 `for (Object obj : jsonArray)` 语句，开始遍历 JSON 数组。
画面 8: 在 `handlerTextAndImages` 方法中，光标位于 `String type = (String) jsonObject.get("type");` 语句，获取图片或文本的类型。
画面 9: 在 `handlerTextAndImages` 方法中，光标位于 `if("image".equals(type))` 语句，判断当前对象是否为图片。
画面 10: 在 `handlerTextAndImages` 方法中，光标位于 `String value = (String) jsonObject.get("value");` 语句，获取图片或文本的值。
画面 11: 在 `handlerTextAndImages` 方法中，光标位于 `images.add(value);` 语句，将图片 URL 添加到图片列表中。
画面 12: 在 `handlerTextAndImages` 方法中，光标位于 `sb.append(value);` 语句，将文本内容追加到 StringBuilder 中。
画面 13: 在 `handlerTextAndImages` 方法中，光标位于 `cNews.setStatus(9);` 语句，将文章状态更新为审核通过。
画面 14: 在 `handlerTextAndImages` 方法中，光标位于 `cNewsMapper.updateNews(cNews);` 语句，更新数据库中的文章信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
Log.info("开始文本内容的审核");
List<String> images = new ArrayList<>();
StringBuilder sb = new StringBuilder();
JSONArray jsonArray = JSON.parseArray(content);
handlerTextAndImages(images, sb, jsonArray);
```

画面 2:
```java
String imageResponse = aliyunImageScanRequest.imageScanRequest(images);
if(null == imageResponse || imageResponse.equals("pass")) {
    updateNews(cNews, message, "图片内容审核失败");
    return;
}
```

画面 3:
```java
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    // 修改文章信息
    // 参数 cNews
    // 文章内容或标题为空
    cNews.setStatus(0);
}
```

画面 4:
```java
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    // 修改文章信息
    // 参数 cNews
    // 文章内容或标题为空
    cNewsMapper.updateNews(cNews);
}
```

画面 5:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    // 修改文章信息
    // 参数 cNews
    // 文章内容或标题为空
    cNews.setStatus(0);
    cNewsMapper.updateNews(cNews);
}
```

画面 6:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 7:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 8:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 9:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 10:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 11:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 12:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 13:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
        }
    }
}
```

画面 14:
```java
/**
 * 解析文本和图片
 * @param images
 * @param sb
 * @param jsonArray
 */
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if(null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value

