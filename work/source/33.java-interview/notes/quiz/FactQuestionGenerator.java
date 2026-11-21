import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

/**
 * 知识点事实矩阵 → 笔试题库生成器（确定性输出，固定随机种子）。
 *
 * 输入格式（facts-*.txt，每行一个知识点，| 分隔 12 字段）：
 *   id|domain|topic|dim|term|fact|why|miscon1|miscon2|miscon3|usage|version
 * 以 # 开头的行是注释，跳过。
 *
 * 每条知识点展开为：
 *   单选·正向（fact 为正确项 + 本条/同主题的 miscon 作干扰项）
 *   判断·真（fact）  判断·假（miscon1）  判断·假（miscon2）
 *   填空（term 挖空）  简答（fact+why+usage 组合为要点）
 * 主题内 ≥3 条真知识点时额外生成：单选·反向（3 真 + 1 误，答"错误项"）
 *
 * 运行：java FactQuestionGenerator <facts文件> <输出目录>
 */
public class FactQuestionGenerator {

    record Fact(String id, String domain, String topic, String dim, String term,
                String fact, String why, List<String> miscon, String usage, String version) {}

    static final Random RNG = new Random(20261115L);
    static int seq = 1000;
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
            if (f.length < 12) {
                System.err.println("SKIP(字段不足" + f.length + "): " + f[0]);
                continue;
            }
            List<String> miscon = new ArrayList<>();
            for (int i = 7; i <= 9 && i < f.length; i++)
                if (!f[i].isBlank()) miscon.add(f[i].trim());
            facts.add(new Fact(f[0].trim(), f[1].trim(), f[2].trim(), f[3].trim(), f[4].trim(),
                    f[5].trim(), f[6].trim(), miscon, f[10].trim(), f[11].trim()));
        }

        // 按 domain 分组输出
        Map<String, List<Fact>> byDomain = new LinkedHashMap<>();
        Map<String, List<Fact>> byTopic = new LinkedHashMap<>();
        for (Fact ft : facts) {
            byDomain.computeIfAbsent(ft.domain, k -> new ArrayList<>()).add(ft);
            byTopic.computeIfAbsent(ft.domain + "::" + ft.topic, k -> new ArrayList<>()).add(ft);
        }

        StringBuilder bank = new StringBuilder();
        int[] counts = new int[8];   // 单正/单反/判真/判假/填空/简答/其他
        for (var e : byDomain.entrySet()) {
            String domain = e.getKey();
            List<Fact> list = e.getValue();
            bank.append("# 笔试题库 · ").append(domain).append("（知识点 ")
                .append(list.size()).append(" 条）\n\n");

            // 主题内排序保证反向题选材稳定
            for (Fact ft : list) {
                appendSingleChoice(bank, counts, ft, byTopic);
                appendJudgeTrue(bank, counts, ft);
                appendJudgeFalse(bank, counts, ft);
                appendScenarioChoice(bank, counts, ft);
                appendScenarioJudge(bank, counts, ft);
                appendFill(bank, counts, ft);
                appendShort(bank, counts, ft);
            }
            // 反向单选：按主题（≥3 条真知识点的主题）
            for (var te : byTopic.entrySet()) {
                if (!te.getKey().startsWith(domain + "::")) continue;
                List<Fact> tf = te.getValue();
                if (tf.size() < 3) continue;
                Fact misconOwner = tf.stream().filter(f -> !f.miscon.isEmpty()).findFirst().orElse(null);
                if (misconOwner == null) continue;
                appendReverseChoice(bank, counts, te.getKey().split("::")[1], tf, misconOwner);
            }
        }

        Path out = Paths.get(outDir, "quiz-bank.md");
        Files.writeString(out, bank.toString(), StandardCharsets.UTF_8);
        System.out.println("知识点矩阵: " + facts.size() + " 条");
        System.out.println("生成题目: " + (counts[0]+counts[1]+counts[2]+counts[3]+counts[4]+counts[5]+counts[6]+counts[7]));
        System.out.println("  单选正向=" + counts[0] + " 单选反向=" + counts[1]
                + " 判断真=" + counts[2] + " 判断假=" + counts[3]
                + " 场景单选=" + counts[6] + " 场景判断=" + counts[7]
                + " 填空=" + counts[4] + " 简答=" + counts[5]);
        System.out.println("输出: " + out.toAbsolutePath());
    }

    // ---------- 各题型 ----------

    static void appendSingleChoice(StringBuilder b, int[] c, Fact f, Map<String, List<Fact>> byTopic) {
        List<String> wrongs = new ArrayList<>(f.miscon);
        // 同主题借调干扰项
        for (Fact o : byTopic.getOrDefault(f.domain + "::" + f.topic, List.of())) {
            if (wrongs.size() >= 3) break;
            if (o == f) continue;
            for (String m : o.miscon)
                if (wrongs.size() < 3 && !m.equals(f.fact) && !wrongs.contains(m)) wrongs.add(m);
        }
        if (wrongs.size() < 3) return;                 // 干扰项不足 3 个则不出单选（质量守门）
        List<String> opts = new ArrayList<>(List.of(f.fact));
        opts.addAll(wrongs.subList(0, 3));
        shuffleStable(opts, f.id + "sc");

        int ans = opts.indexOf(f.fact) + 1;
        char letter = (char) ('A' + ans - 1);
        c[0]++;
        b.append("**Q").append(TAG).append(seq++).append("（单选·正向·").append(f.dim).append("）** 关于「")
          .append(f.topic).append("」的说法，正确的是？\n");
        for (int i = 0; i < 4; i++)
            b.append("- ").append((char)('A'+i)).append(". ").append(opts.get(i)).append("\n");
        b.append("**答案：").append(letter).append("**\n");
        b.append("**解析：** ").append(f.fact).append("。原因：").append(f.why).append("。\n");
        b.append("**来源：** ").append(f.id).append(" · ").append(f.topic);
        if (!f.version.isEmpty()) b.append("（").append(f.version).append("）");
        b.append("\n\n");
    }

    static void appendReverseChoice(StringBuilder b, int[] c, String topic, List<Fact> truths, Fact misconOwner) {
        List<String> opts = new ArrayList<>();
        for (int i = 0; i < 3 && i < truths.size(); i++) opts.add(truths.get(i).fact);
        opts.add(misconOwner.miscon.get(0));
        shuffleStable(opts, topic + "rev" + misconOwner.id);

        int ans = opts.indexOf(misconOwner.miscon.get(0)) + 1;
        char letter = (char) ('A' + ans - 1);
        c[1]++;
        b.append("**Q").append(TAG).append(seq++).append("（单选·反向·").append(topic).append("）** 以下关于「")
          .append(topic).append("」的说法，**错误**的是？\n");
        for (int i = 0; i < 4; i++)
            b.append("- ").append((char)('A'+i)).append(". ").append(opts.get(i)).append("\n");
        b.append("**答案：").append(letter).append("**\n");
        b.append("**解析：** 正确表述应为——").append(misconOwner.fact).append("。原因：").append(misconOwner.why).append("。\n\n");
    }

    static void appendJudgeTrue(StringBuilder b, int[] c, Fact f) {
        c[2]++;
        b.append("**Q").append(TAG).append(seq++).append("（判断·").append(f.dim).append("）** ").append(f.fact).append("\n");
        b.append("**答案：对。** 解析：").append(f.why).append("\n\n");
    }

    static void appendJudgeFalse(StringBuilder b, int[] c, Fact f) {
        List<String> ms = f.miscon;
        if (!ms.isEmpty()) {
            c[3]++;
            b.append("**Q").append(TAG).append(seq++).append("（判断·").append(f.dim).append("）** ").append(ms.get(0)).append("\n");
            b.append("**答案：错。** 正确表述：").append(f.fact).append("。原因：").append(f.why).append("\n\n");
        }
        if (ms.size() > 1) {
            c[3]++;
            b.append("**Q").append(TAG).append(seq++).append("（判断·").append(f.dim).append("）** ").append(ms.get(1)).append("\n");
            b.append("**答案：错。** 正确表述：").append(f.fact).append("。原因：").append(f.why).append("\n\n");
        }
        if (ms.size() > 2) {
            c[3]++;
            b.append("**Q").append(TAG).append(seq++).append("（判断·").append(f.dim).append("）** ").append(ms.get(2)).append("\n");
            b.append("**答案：错。** 正确表述：").append(f.fact).append("。原因：").append(f.why).append("\n\n");
        }
    }

    static void appendFill(StringBuilder b, int[] c, Fact f) {
        if (f.term.isEmpty()) return;
        // 空白容忍匹配：允许 term 各字符间夹空白（如"B+树"匹配"B+ 树"）
        StringBuilder rx = new StringBuilder();
        for (int i = 0; i < f.term.length(); i++) {
            if (i > 0) rx.append("\\s*");
            rx.append(java.util.regex.Pattern.quote(String.valueOf(f.term.charAt(i))));
        }
        java.util.regex.Matcher m = java.util.regex.Pattern.compile(rx.toString())
                .matcher(f.fact);
        if (!m.find()) return;                          // 守门：挖不准就不出填空
        c[4]++;
        b.append("**Q").append(TAG).append(seq++).append("（填空·").append(f.dim).append("）** ")
          .append(m.replaceFirst("______")).append("\n");
        b.append("**答案：").append(f.term).append("**。解析：").append(f.why).append("\n\n");
    }

    static void appendShort(StringBuilder b, int[] c, Fact f) {
        c[5]++;
        b.append("**Q").append(TAG).append(seq++).append("（简答·").append(f.dim).append("）** 请说明「")
          .append(f.topic).append("」中").append(f.term.isEmpty() ? "该知识点" : f.term)
          .append("的机制与使用要点。\n");
        b.append("**要点（标准答案）**：① ").append(f.fact).append("；② 原理：").append(f.why);
        if (!f.usage.isEmpty()) b.append("；③ 使用要点：").append(f.usage);
        if (!f.version.isEmpty()) b.append("。版本锚点：").append(f.version);
        b.append("。\n\n");
    }

    /** 场景单选：以 usage 为正确项、miscon 为干扰项 */
    static void appendScenarioChoice(StringBuilder b, int[] c, Fact f) {
        if (f.usage.isEmpty() || f.miscon.size() < 3) return;
        List<String> opts = new ArrayList<>(List.of(f.usage));
        opts.addAll(f.miscon.subList(0, 3));
        shuffleStable(opts, f.id + "sc2");
        int ans = opts.indexOf(f.usage) + 1;
        char letter = (char) ('A' + ans - 1);
        c[6]++;
        b.append("**Q").append(TAG).append(seq++).append("（场景单选·").append(f.dim).append("）** 在工程实践中关于「")
          .append(f.term.isEmpty() ? f.topic : f.term).append("」，下列做法符合推荐实践的是？\n");
        for (int i = 0; i < 4; i++)
            b.append("- ").append((char)('A'+i)).append(". ").append(opts.get(i)).append("\n");
        b.append("**答案：").append(letter).append("**\n");
        b.append("**解析：** 推荐实践：").append(f.usage).append("。事实依据：").append(f.fact).append("。\n\n");
    }

    /** 场景判断：推荐实践陈述为真 */
    static void appendScenarioJudge(StringBuilder b, int[] c, Fact f) {
        if (f.usage.isEmpty()) return;
        c[7]++;
        b.append("**Q").append(TAG).append(seq++).append("（场景判断·").append(f.dim).append("）** 推荐实践：").append(f.usage).append("\n");
        b.append("**答案：对。** 解析：").append(f.fact).append("。原因：").append(f.why).append("\n\n");
    }

    /** 稳定洗牌：以题源 id 为种子，保证每次生成结果一致 */
    static void shuffleStable(List<String> opts, String seedText) {
        Random r = new Random(seedText.hashCode() * 31L + 7L);
        Collections.shuffle(opts, r);
    }
}
