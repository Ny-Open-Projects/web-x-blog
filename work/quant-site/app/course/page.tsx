import Link from "next/link";
import { allModules } from "@/lib/content";

export const metadata = { title: "量化课程", description: "量化基础 / 数字货币量化实战 / 数据分析（量化基石）三轨课程" };

const DESC: Record<string, string> = {
  basics: "从量化定义、交易分类、系统构成到 JQData 取数，建立完整知识地图。",
  quant: "用 Python 从零跑通数据处理、择时/选币/套利策略到自动交易。",
  data: "Excel/SQL/Python/爬虫/pandas/可视化/指标体系——量化取数与因子计算的地基。",
};

export default function Page() {
  const mods = allModules();
  const tracks = (["basics", "quant", "data"] as const).map((t) => ({
    t, name: mods.find((m) => m.track === t)?.trackName || t, list: mods.filter((m) => m.track === t),
  }));

  return (
    <main className="wrap">
      <section className="hero">
        <h1>量化课程</h1>
        <p>三大主线：<b>量化基础</b>（概念·分类·系统·取数）→ <b>数据分析</b>（工具·清洗·可视化·指标体系）→ <b>数字货币量化实战</b>（Python·策略·自动交易）。由浅入深，配可运行代码。</p>
      </section>

      <div className="course-grid">
        {tracks.map((tr) => (
          <div className="course-card" key={tr.t}>
            <h3>{tr.name}</h3>
            <div className="meta">{tr.list.length} 个模块</div>
            <p>{DESC[tr.t]}</p>
          </div>
        ))}
      </div>

      {tracks.map((tr) => (
        <section className="section" key={tr.t}>
          <div className="section-title"><span className="bar"></span>{tr.name}<span className="sub">{tr.list.length} 模块</span></div>
          {tr.list.map((m) => (
            <div className="chapter" key={m.slug}>
              <Link href={`/course/${m.slug}`} style={{ color: "inherit" }}>
                <summary style={{ display: "flex" }}>
                  <span className="n">{String(m.order).padStart(2, "0")}</span>
                  <span style={{ flex: 1 }}>{m.title}</span>
                  <span className="cnt">阅读 →</span>
                </summary>
              </Link>
              {m.summary && <div style={{ padding: "0 18px 14px", color: "var(--muted)", fontSize: 13 }}>{m.summary}</div>}
            </div>
          ))}
        </section>
      ))}
    </main>
  );
}
