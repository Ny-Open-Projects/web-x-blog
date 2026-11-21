import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

/**
 * 知识点事实矩阵 → 面试题库生成器（面试官问法 + 标准回答话术 + 评分点 + P 级别）。
 *
 * 输入与 FactQuestionGenerator 相同的 facts 文件（12 字段管道分隔）。
 * 每条知识点产出 5 道面试题：
 *   1. 概念考察（P1-P4）  2. 误用纠错（P4-P7）  3. 原理深挖（P5-P8）
 *   4. 工程落地（P6-P9）  5. 版本演进（P8-P10）
 * P 级别按 dim 关键词自动分级，题目带【面试官】【标准回答话术】【评分点】三段。
 *
 * 运行：java InterviewQuestionGenerator <facts文件> <输出目录>
 */
public class InterviewQuestionGenerator {

    record Fact(String id, String domain, String topic, String dim, String term,
                String fact, String why, List<String> miscon, String usage, String version) {}

    static final Random RNG = new Random(20261116L);
    static int seq = 1;
    static String TAG = "";   // 域前缀，避免跨文件题号冲突

    public static void main(String[] args) throws Exception {
        String factsPath = args.length > 0 ? args[0] : "facts-java-basics.txt";
        String outDir = args.length > 1 ? args[1] : ".";
        TAG = java.nio.file.Paths.get(outDir).getFileName().toString() + "-";
        Files.createDirectories(Paths.get(outDir));

        List<Fact> facts = new ArrayList<>();
        for (String line : Files.readAllLines(Paths.get(factsPath), StandardCharsets.UTF_8)) {
            String t = line.trim();
            if (t.isEmpty() || t.startsWith("#")) continue;
            String[] f = t.split("\\|", -1);
            if (f.length < 12) continue;
            List<String> miscon = new ArrayList<>();
            for (int i = 7; i <= 9 && i < f.length; i++)
                if (!f[i].isBlank()) miscon.add(f[i].trim());
            facts.add(new Fact(f[0].trim(), f[1].trim(), f[2].trim(), f[3].trim(), f[4].trim(),
                    f[5].trim(), f[6].trim(), miscon, f[10].trim(), f[11].trim()));
        }

        Map<String, List<Fact>> byDomain = new LinkedHashMap<>();
        for (Fact ft : facts) byDomain.computeIfAbsent(ft.domain, k -> new ArrayList<>()).add(ft);

        StringBuilder bank = new StringBuilder();
        bank.append("> 面试题库由知识点事实矩阵生成：每题含【面试官】问法、【标准回答话术】、【评分点】；\n")
            .append("> P 级别按题型分层：概念 P1-P4 / 误用纠错 P4-P7 / 原理深挖 P5-P7 / 工程落地 P7-P9 / 版本演进 P8-P10，P1-P10 全覆盖。\n\n");

        int[] counts = new int[7];  // 概念/纠错/原理/落地/版本/边界/追问
        Map<String, Integer> pCount = new LinkedHashMap<>();
        for (var e : byDomain.entrySet()) {
            String domain = e.getKey();
            List<Fact> list = e.getValue();
            bank.append("# 面试题库 · ").append(domain).append("（知识点 ").append(list.size())
                .append(" 条 × 5 题型）\n\n");
            for (Fact ft : list) {
                pCount.merge(pLevel(ft.dim), 1, Integer::sum);
                appendConcept(bank, counts, ft);
                appendMiscon(bank, counts, ft);
                appendWhy(bank, counts, ft);
                appendUsage(bank, counts, ft);
                appendVersion(bank, counts, ft);
                appendBoundary(bank, counts, ft);
                appendChain(bank, counts, ft);
            }
        }

        Path out = Paths.get(outDir, "interview-bank.md");
        Files.writeString(out, bank.toString(), StandardCharsets.UTF_8);
        int total = counts[0] + counts[1] + counts[2] + counts[3] + counts[4] + counts[5] + counts[6];
        System.out.println("知识点矩阵: " + facts.size() + " 条");
        System.out.println("生成面试题: " + total);
        System.out.println("  概念考察=" + counts[0] + " 误用纠错=" + counts[1]
                + " 原理深挖=" + counts[2] + " 工程落地=" + counts[3] + " 版本演进=" + counts[4]
                + " 边界追问=" + counts[5] + " 追问链=" + counts[6]);
        System.out.println("P 级别分布: " + pCount);
        System.out.println("输出: " + out.toAbsolutePath());
    }

    /** 按 dim 关键词映射 P 级别 */
    static String pLevel(String dim) {
        String d = dim == null ? "" : dim;
        if (contains(d, "方法论", "选型", "演进", "架构", "版本", "治理", "规划")) return "P8-P10";
        if (contains(d, "误用", "性能", "调优", "排查", "实战", "运维", "参数", "隐患", "教训", "工程", "优化")) return "P6-P8";
        if (contains(d, "原理", "内存", "原子", "锁", "实现", "机制", "语义", "可见", "扩展点", "模型", "流程", "结构")) return "P4-P6";
        return "P1-P3";
    }

    static boolean contains(String s, String... keys) {
        for (String k : keys) if (s.contains(k)) return true;
        return false;
    }

    // ---------- 五种面试题型 ----------

    static void head(StringBuilder b, String tag, String p, Fact f) {
        b.append("**Q").append(TAG).append(seq++).append("（").append(tag).append("·").append(p).append("）**\n");
        b.append("【面试官】");
        b.append("来源 ").append(f.id).append(" · ").append(f.dim).append("\n");
    }

    static void appendConcept(StringBuilder b, int[] c, Fact f) { String p = pLevel(f.dim);
        c[0]++;
        b.append("**Q").append(TAG).append(seq++).append("（概念考察·").append(p).append("）**\n");
        b.append("【面试官】请谈谈你对「").append(f.topic).append("」中")
          .append(f.term.isEmpty() ? "这个知识点" : "「" + f.term + "」").append("的理解。\n");
        b.append("【标准回答话术】").append(f.fact).append("。背后的原理是：").append(f.why).append("。\n");
        b.append("【评分点】① 准确说出核心机制").append(f.term.isEmpty() ? "" : "（" + f.term + "）")
          .append("；② 能带出原理层而非背结论。");
        if (!f.version.isEmpty()) b.append(" ③ 版本锚点：").append(f.version);
        b.append("\n\n");
    }

    static void appendMiscon(StringBuilder b, int[] c, Fact f) { String p = "P4-P7";
        if (f.miscon.isEmpty()) return;
        c[1]++;
        b.append("**Q").append(TAG).append(seq++).append("（误用纠错·").append(p).append("）**\n");
        b.append("【面试官】我在别的团队见过这样的说法：「").append(f.miscon.get(0)).append("」。你觉得对吗？\n");
        b.append("【标准回答话术】这个说法不正确。准确的表述是：").append(f.fact)
          .append("。原因是：").append(f.why).append("。\n");
        b.append("【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（").append(f.version.isEmpty() ? "经验级" : f.version).append("）。\n\n");
    }

    static void appendWhy(StringBuilder b, int[] c, Fact f) { String p = "P5-P7";
        c[2]++;
        b.append("**Q").append(TAG).append(seq++).append("（原理深挖·").append(p).append("）**\n");
        b.append("【面试官】「").append(f.term.isEmpty() ? f.topic : f.term)
          .append("」为什么会这样设计？背后的机制是什么？\n");
        b.append("【标准回答话术】机制层面：").append(f.why).append("。落到结论：").append(f.fact).append("。\n");
        b.append("【评分点】① 讲出").append(f.dim).append("层面的机制；② 结论与机制对应不脱节。\n\n");
    }

    static void appendUsage(StringBuilder b, int[] c, Fact f) { String p = "P7-P9";
        if (f.usage.isEmpty()) return;
        c[3]++;
        b.append("**Q").append(TAG).append(seq++).append("（工程落地·").append(p).append("）**\n");
        b.append("【面试官】在你带过的项目里，「").append(f.term.isEmpty() ? f.topic : f.term)
          .append("」你是怎么用的？踩过什么坑？\n");
        boolean usageLong = f.usage.length() >= 12;
        String core = usageLong ? f.usage : f.fact;
        String sup = usageLong ? "事实依据：" + f.fact : (f.usage.isEmpty() ? "" : "补充要点：" + f.usage + "。");
        b.append("【标准回答话术】使用要点：").append(core).append("。").append(sup)
          .append("常见误区要规避：").append(f.miscon.isEmpty() ? "见上一题" : f.miscon.get(0)).append("。\n");
        b.append("【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。\n\n");
    }

    static void appendVersion(StringBuilder b, int[] c, Fact f) { String p = "P8-P10";
        if (f.version.isEmpty()) return;
        c[4]++;
        boolean hasVerNum = f.version.chars().anyMatch(Character::isDigit);
        if (hasVerNum) {
            b.append("**Q").append(TAG).append(seq++).append("（版本演进·").append(p).append("）**\n");
            b.append("【面试官】关于「").append(f.term.isEmpty() ? f.topic : f.term)
              .append("」，版本上有什么需要特别注意的？\n");
            b.append("【标准回答话术】版本锚点：").append(f.version).append("。事实层面：").append(f.fact).append("。\n");
            b.append("【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。\n\n");
        } else {
            b.append("**Q").append(TAG).append(seq++).append("（结论依据·").append(p).append("）**\n");
            b.append("【面试官】关于「").append(f.term.isEmpty() ? f.topic : f.term)
              .append("」，你的结论依据什么出处？回答时怎么限定而不说绝对？\n");
            b.append("【标准回答话术】来源锚点：").append(f.version).append("。事实与结论：").append(f.fact)
              .append("。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。\n");
            b.append("【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。\n\n");
        }
    }

    /** 边界追问：适用边界与误区规避 */
    static void appendBoundary(StringBuilder b, int[] c, Fact f) {
        if (f.miscon.isEmpty()) return;
        c[5]++;
        b.append("**Q").append(TAG).append(seq++).append("（边界追问·P6-P9）**\n");
        b.append("【面试官】「").append(f.term.isEmpty() ? f.topic : f.term)
          .append("」有没有不适用或需要特别小心的边界场景？\n");
        b.append("【标准回答话术】边界提示：认为「").append(f.miscon.get(0))
          .append("」是常见误区。正确的边界：").append(f.fact);
        if (!f.usage.isEmpty()) b.append("。使用要点：").append(f.usage);
        b.append("。\n");
        b.append("【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。\n\n");
    }

    /** 追问链：错误实施的后果推演 */
    static void appendChain(StringBuilder b, int[] c, Fact f) {
        if (f.miscon.size() < 2) return;
        c[6]++;
        b.append("**Q").append(TAG).append(seq++).append("（追问链·P5-P8）**\n");
        b.append("【面试官】追问：如果有人按「").append(f.miscon.get(1)).append("」来实施，会发生什么？\n");
        b.append("【标准回答话术】该说法不成立，正确机制：").append(f.fact).append("。原理：").append(f.why).append("。\n");
        b.append("【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。\n\n");
    }
}
