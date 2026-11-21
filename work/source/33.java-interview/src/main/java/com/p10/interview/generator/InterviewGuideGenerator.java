package com.p10.interview.generator;

import com.p10.interview.model.Chapter;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * 面试指南生成器。
 *
 * <p>扫描项目根目录的 docs/ 下所有章节（每个章节一个目录，内含 README.md），
 * 统计题目数量与中文字数，并在项目根目录生成：</p>
 * <ul>
 *     <li>INDEX.md —— 总索引：章节目录、题目数、字数、预计学习时长</li>
 *     <li>STUDY-TRACKER.md —— 学习进度打卡表（30/60/90 天计划对照）</li>
 * </ul>
 *
 * <p>运行方式（任选其一）：</p>
 * <pre>
 *   mvn compile exec:java                  # Maven
 *   java -cp target/classes com.p10.interview.generator.InterviewGuideGenerator   # 手动
 * </pre>
 */
public class InterviewGuideGenerator {

    private static final String DOCS_DIR = "docs";
    private static final String INDEX_FILE = "INDEX.md";
    private static final String TRACKER_FILE = "STUDY-TRACKER.md";

    public static void main(String[] args) throws IOException {
        Path root = Paths.get("").toAbsolutePath();
        Path docs = root.resolve(DOCS_DIR);
        if (!Files.isDirectory(docs)) {
            System.err.println("未找到 docs 目录: " + docs);
            System.exit(1);
        }

        List<Chapter> chapters = scanChapters(docs);
        renderIndex(root, chapters);
        renderTracker(root, chapters);

        int totalQuestions = 0;
        int totalChars = 0;
        for (Chapter c : chapters) {
            totalQuestions += c.getQuestionCount();
            totalChars += c.getChineseCharCount();
        }
        System.out.println("扫描章节: " + chapters.size());
        System.out.println("题目总数: " + totalQuestions);
        System.out.println("中文字数: " + totalChars);
        System.out.println("已生成: " + root.resolve(INDEX_FILE));
        System.out.println("已生成: " + root.resolve(TRACKER_FILE));
    }

    /** 按目录名排序扫描 docs 下的章节目录 */
    static List<Chapter> scanChapters(Path docs) throws IOException {
        List<String> dirNames = new ArrayList<>();
        try (DirectoryStream<Path> stream = Files.newDirectoryStream(docs)) {
            for (Path p : stream) {
                if (Files.isDirectory(p) && Files.isRegularFile(p.resolve("README.md"))) {
                    dirNames.add(p.getFileName().toString());
                }
            }
        }
        Collections.sort(dirNames);

        List<Chapter> result = new ArrayList<>();
        for (String dir : dirNames) {
            Path md = docs.resolve(dir).resolve("README.md");
            Chapter chapter = new Chapter(dir);
            chapter.setFilePath(docs.resolve(dir).resolve("README.md").toString());
            for (String line : Files.readAllLines(md, StandardCharsets.UTF_8)) {
                if (chapter.getTitle() == null && line.startsWith("# ")) {
                    chapter.setTitle(line.substring(2).trim());
                }
                if (isQuestionLine(line)) {
                    chapter.setQuestionCount(chapter.getQuestionCount() + 1);
                }
                chapter.setChineseCharCount(chapter.getChineseCharCount() + countChinese(line));
                if (!line.trim().isEmpty()) {
                    chapter.setLineCount(chapter.getLineCount() + 1);
                }
            }
            result.add(chapter);
        }
        return result;
    }

    /** 统计一行内的中文字符数（CJK 统一表意文字区间） */
    static int countChinese(String line) {
        int count = 0;
        for (int i = 0; i < line.length(); i++) {
            char ch = line.charAt(i);
            if (ch >= 0x4E00 && ch <= 0x9FFF) {
                count++;
            }
        }
        return count;
    }

    /**
     * 判断一行是否为题目标题。兼容三种格式：
     * 1. "### 题 1.2.1：..."（主体章节）与 "## 题 1：..."（手写册）
     * 2. "## 9.1 题一：..."（场景册的中文序号）
     * 3. "**Q1：..."（附录软实力题）
     */
    static boolean isQuestionLine(String line) {
        String t = line.trim();
        if (t.startsWith("### 题") || t.startsWith("## 题")) {
            return true;
        }
        if (t.matches("(#+\\s+)?[^*]*题[一二三四五六七八九十]+：.*")) {
            return true;
        }
        return t.startsWith("**Q") && t.contains("：");
    }

    private static void renderIndex(Path root, List<Chapter> chapters) throws IOException {
        StringBuilder sb = new StringBuilder();
        sb.append("# Java 后端面试全景 · 总索引（对标阿里 P10）\n\n");
        sb.append("> 本文件由 `InterviewGuideGenerator` 自动生成，重新运行 `mvn compile exec:java` 可刷新统计。\n\n");
        sb.append("| 章节 | 题目数 | 中文字数(约) | 预计学习时长 |\n");
        sb.append("|------|--------|--------------|--------------|\n");

        int totalQuestions = 0;
        int totalChars = 0;
        for (Chapter c : chapters) {
            totalQuestions += c.getQuestionCount();
            totalChars += c.getChineseCharCount();
            int hours = Math.max(1, Math.round(c.getChineseCharCount() / 1500f));
            String shortTitle = (c.getTitle() == null || c.getTitle().isEmpty())
                    ? c.getDirName() : c.getTitle().split(" —— ")[0];
            sb.append("| [").append(shortTitle).append("](")
              .append(DOCS_DIR).append("/").append(c.getDirName()).append("/README.md) | ")
              .append(c.getQuestionCount()).append(" | ")
              .append(c.getChineseCharCount()).append(" | ")
              .append(hours).append(" 小时 |\n");
        }

        sb.append("\n**合计**：").append(chapters.size()).append(" 个章节，")
          .append(totalQuestions).append(" 道题，正文约 ")
          .append(String.format("%.1f 万字", totalChars / 10000.0)).append("。\n\n");
        sb.append("- [大纲与章节结构](docs/00-outline.md)\n");
        sb.append("- **[全卷速记卡合订本（考前一小时专用）](SPEED-CARDS.md)**\n");
        sb.append("- [学习进度打卡表](STUDY-TRACKER.md)\n");
        sb.append("- [Arthas 实战沙盘](notes/arthas-practice/README.md)（需 JDK，安装见 tools/）\n\n");
        sb.append("## 学习路径建议\n\n");
        sb.append("1. **零基础起步**：先读每章的“零基础卡片”小节，配合第 16 册 30/60/90 天打卡计划；\n");
        sb.append("2. **主线推进**：第 1→2→3 章是 Java 内功，第 4→5→6→7 章是中间件，第 8→9 章是架构，第 10 章是差异化加分；\n");
        sb.append("3. **冲刺背诵**：只用各章“一页速记卡”+ 合订本滚动复习；\n");
        sb.append("4. **模拟实战**：第 9 章五步法 + 附录 A 软实力题 + 第 18/19/21 册实录范文对照演练。\n");

        Files.write(root.resolve(INDEX_FILE), sb.toString().getBytes(StandardCharsets.UTF_8));
    }

    private static void renderTracker(Path root, List<Chapter> chapters) throws IOException {
        StringBuilder sb = new StringBuilder();
        sb.append("# 学习进度打卡表\n\n");
        sb.append("> 每读完一章，在状态列把 [ ] 改为 [x]，并在“能脱稿讲吗”一栏诚实打分（1-5）。\n\n");
        sb.append("| 章节 | 状态 | 能脱稿讲吗(1-5) | 复盘笔记 |\n");
        sb.append("|------|------|-----------------|----------|\n");
        for (Chapter c : chapters) {
            sb.append("| ").append(c.getTitle()).append(" | [ ] | | |\n");
        }
        sb.append("\n## 追问链自测记录\n\n");
        sb.append("- 日期：\n- 自问题目：\n- 卡住的追问：\n- 明日重背清单：\n");
        Files.write(root.resolve(TRACKER_FILE), sb.toString().getBytes(StandardCharsets.UTF_8));
    }
}
