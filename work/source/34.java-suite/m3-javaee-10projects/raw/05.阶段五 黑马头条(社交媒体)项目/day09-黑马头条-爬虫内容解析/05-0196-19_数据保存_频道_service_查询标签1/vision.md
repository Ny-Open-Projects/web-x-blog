# 画面线理解：19_数据保存_频道_service_查询标签1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\19_数据保存_频道_service_查询标签1【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:08, 01:02, 03:32, 04:00, 04:35, 06:00, 07:01, 08:03, 08:45, 09:34, 11:22, 12:37, 13:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:56:03

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 Service 层调用 MyBatis Mapper 实现对广告标签数据的查询与处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 MyBatis Mapper 文件（AdChannelLabelMapper.xml）中定义的 SQL 查询语句和 resultMap 映射配置。
画面 2: 展示 Service 接口文件（AdLabelService.java）的定义，包含一个 getLabelIds 方法。
画面 3: 展示 Service 接口的实现类（AdLabelServiceImpl.java）的初始骨架，包含两个方法的占位实现。
画面 4: 在实现类中，通过 IDEA 的智能提示功能，为方法添加必要的导入依赖。
画面 5: 在实现类中，通过 @Autowired 注解注入 AdLabelMapper 和 AdChannelLabelMapper。
画面 6: 为 getLabelIds 方法添加日志记录和方法体的初步结构。
画面 7: 在 getLabelIds 方法中，使用 adLabelMapper.queryAdLabels 查询数据库。
画面 8: 在 getLabelIds 方法中，对查询结果进行处理，将字符串数组转换为 List<String>。
画面 9: 在 getLabelIds 方法中，对查询结果进行空值判断。
画面 10: 在 getLabelIds 方法中，对查询结果进行非空处理，调用 adLabelList.add 方法。
画面 11: 在 getLabelIds 方法中，使用 Stream API 对 List<String> 进行处理，转换为字符串。
画面 12: 在 getLabelIds 方法中，使用 Stream API 对 List<String> 进行处理，转换为字符串。
画面 13: 在 getLabelIds 方法中，使用 Stream API 对 List<String> 进行处理，转换为字符串。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.heima.crawler.mappers.AdChannelLabelMapper">
    <resultMap id="BaseResultMap" type="com.heima.crawler.admin.pojos.AdChannelLabel">
        <result column="channel_id" property="channelId"/>
        <result column="label_id" property="labelId"/>
        <result column="ord" property="ord"/>
    </resultMap>

    <sql id="Base_Column_List">
        id, channel_id, label_id, ord
    </sql>

    <select id="selectByPrimaryKey" resultMap="BaseResultMap" parameterType="java.lang.Integer">
        select
        <include refid="Base_Column_List"/>
        from ad_channel_label
        where id = #{id}
    </select>

    <select id="selectByIdLabelId" resultMap="BaseResultMap" parameterType="java.lang.Integer">
        select
        <include refid="Base_Column_List"/>
        from ad_channel_label
        where label_id = #{labelId}
    </select>
</mapper>
```

画面 2:
```java
package com.heima.crawler.service;

public class AdLabelService {
    public String getLabelIds(String labels);
}
```

画面 3:
```java
package com.heima.crawler.service.impl;

public class AdLabelServiceImpl implements AdLabelService {
    @Override
    public String getLabelIds(String labels) {
        return null;
    }

    @Override
    public Integer getAdChannelByIds(String labels) {
        return null;
    }
}
```

画面 4:
```java
import com.heima.crawler.service.AdLabelService;
import lombok.extern.log4j.Log4j;
import org.springframework.stereotype.Service;

@Service
@Log4j
public class AdLabelServiceImpl implements AdLabelService {
    private AdLabelMapper adLabelMapper;
    private AdChannelLabelMapper adChannelLabelMapper;
}
```

画面 5:
```java
@Service
@Log4j
@SuppressWarnings("all")
public class AdLabelServiceImpl implements AdLabelService {
    @Autowired
    private AdLabelMapper adLabelMapper;
    @Autowired
    private AdChannelLabelMapper adChannelLabelMapper;

    @Override
    public String getLabelIds(String labels) {
        return null;
    }

    @Override
    public Integer getAdChannelByIds(String labels) {
        return null;
    }
}
```

画面 6:
```java
import com.heima.crawler.service.AdLabelService;
import lombok.extern.log4j.Log4j;
import org.springframework.stereotype.Service;

@Service
@Log4j
@SuppressWarnings("all")
public class AdLabelServiceImpl implements AdLabelService {
    @Autowired
    private AdLabelMapper adLabelMapper;
    @Autowired
    private AdChannelLabelMapper adChannelLabelMapper;

    @Override
    public String getLabelIds(String labels) {
        long currentTimeMillis = System.currentTimeMillis();
        log.info("获取Channel信息，标签:labels:0", labels);
        List<AdLabel> adlabelList = new ArrayList<>();
        if (StringUtils.isBlank(labels)) {
            return null;
        }
        labels = labels.toLowerCase();
        List<String> tmplabels = Arrays.asList(labels.split(regex: " "));
        adLabelMapper.queryAdLabels(labels, tmplabels);
        if (null == adlabelList && adlabelList.isEmpty()) {
            return null;
        }
    }
}
```

画面 7:
```java
import com.heima.crawler.service.AdLabelService;
import lombok.extern.log4j.Log4j;
import org.springframework.stereotype.Service;

@Service
@Log4j
@SuppressWarnings("all")
public class AdLabelServiceImpl implements AdLabelService {
    @Autowired
    private AdLabelMapper adLabelMapper;
    @Autowired
    private AdChannelLabelMapper adChannelLabelMapper;

    @Override
    public String getLabelIds(String labels) {
        long currentTimeMillis = System.currentTimeMillis();
        log.info("获取Channel信息，标签:labels:0", labels);
        List<AdLabel> adlabelList = new ArrayList<>();
        if (StringUtils.isBlank(labels)) {
            return null;
        }
        labels = labels.toLowerCase();
        List<String> tmplabels = Arrays.asList(labels.split(regex: " "));
        adLabelMapper.queryAdLabels(labels, tmplabels);
        if (null == adlabelList && adlabelList.isEmpty()) {
            return null;
        }
    }
}
```

画面 8:
```java
import com.heima.crawler.service.AdLabelService;
import lombok.extern.log4j.Log4j;
import org.springframework.stereotype.Service;

@Service
@Log4j
@SuppressWarnings("all")
public class AdLabelServiceImpl implements AdLabelService {
    @Autowired
    private AdLabelMapper adLabelMapper;
    @Autowired
    private AdChannelLabelMapper adChannelLabelMapper;

    @Override
    public String getLabelIds(String labels) {
        long currentTimeMillis = System.currentTimeMillis();
        log.info("获取Channel信息，标签:labels:0", labels);
        List<AdLabel> adlabelList = new ArrayList<>();
        if (StringUtils.isBlank(labels)) {
            return null;
        }
        labels = labels.toLowerCase();
        List<String> tmplabels = Arrays.asList(labels.split(regex: " "));
        adLabelMapper.queryAdLabels(labels, tmplabels);
        if (null == adlabelList && adlabelList.isEmpty()) {
            return null;
        }
    }
}
```

画面 9:
```java
import com.heima.crawler.service.AdLabelService;
import lombok.extern.log4j.Log4j;
import org.springframework.stereotype.Service;

@Service
@Log4j
@SuppressWarnings("all")
public class AdLabelServiceImpl implements AdLabelService {
    @Autowired
    private AdLabelMapper adLabelMapper;
    @Autowired
    private AdChannelLabelMapper adChannelLabelMapper;

    @Override
    public String getLabelIds(String labels) {
        long currentTimeMillis = System.currentTimeMillis();
        log.info("获取Channel信息，标签:labels:0", labels);
        List<AdLabel> adlabelList = new ArrayList<>();
        if (StringUtils.isBlank(labels)) {
            return null;
        }
        labels = labels.toLowerCase();
        List<String> tmplabels = Arrays.asList(labels.split(regex: " "));
        adLabelMapper.queryAdLabels(labels, tmplabels);
        if (null == adlabelList && adlabelList.isEmpty()) {
            return null;
        }
    }
}
```

画面 10:
```java
import com.heima.crawler.service.AdLabelService;
import lombok.extern.log4j.Log4j;
import org.springframework.stereotype.Service;

@Service
@Log4j
@SuppressWarnings("all")
public class AdLabelServiceImpl implements AdLabelService {
    @Autowired
    private AdLabelMapper adLabelMapper;
    @Autowired
    private AdChannelLabelMapper adChannelLabelMapper;

    @Override
    public String getLabelIds(String labels) {
        long currentTimeMillis = System.currentTimeMillis();
        log.info("获取Channel信息，标签:labels:0", labels);
        List<AdLabel> adlabelList = new ArrayList<>();
        if (StringUtils.isBlank(labels)) {
            return null;
        }
        labels = labels.toLowerCase();
        List<String> tmplabels = Arrays.asList(labels.split(regex: " "));
        adLabelMapper.queryAdLabels(labels, tmplabels);
        if (null == adlabelList && ad
