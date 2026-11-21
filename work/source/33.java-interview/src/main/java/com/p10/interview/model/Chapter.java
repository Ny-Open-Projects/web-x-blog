package com.p10.interview.model;

/**
 * 一章面试内容的统计模型。
 *
 * <p>由 {@link com.p10.interview.generator.InterviewGuideGenerator} 在扫描 docs/ 目录时填充，
 * 最终用于渲染总索引 INDEX.md。</p>
 */
public class Chapter {

    /** 目录名，如 01-java-fundamentals */
    private final String dirName;

    /** 章节标题，取自 README.md 的一级标题 */
    private String title;

    /** 正文文件路径 */
    private String filePath;

    /** 题目数量（统计 "### 题" 开头的小节） */
    private int questionCount;

    /** 中文字符数（近似字数） */
    private int chineseCharCount;

    /** 非空行数 */
    private int lineCount;

    public Chapter(String dirName) {
        this.dirName = dirName;
    }

    public String getDirName() {
        return dirName;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getFilePath() {
        return filePath;
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }

    public int getQuestionCount() {
        return questionCount;
    }

    public void setQuestionCount(int questionCount) {
        this.questionCount = questionCount;
    }

    public int getChineseCharCount() {
        return chineseCharCount;
    }

    public void setChineseCharCount(int chineseCharCount) {
        this.chineseCharCount = chineseCharCount;
    }

    public int getLineCount() {
        return lineCount;
    }

    public void setLineCount(int lineCount) {
        this.lineCount = lineCount;
    }

    @Override
    public String toString() {
        return "Chapter{" + dirName + ", title=" + title
                + ", questions=" + questionCount
                + ", chars=" + chineseCharCount + "}";
    }
}
