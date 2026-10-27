import Link from "next/link";

export default function NotFound() {
  return (
    <div className="wrap" style={{ padding: "90px 20px 60px", textAlign: "center" }}>
      <div style={{ fontSize: 72, fontWeight: 800, lineHeight: 1, color: "var(--accent)" }}>404</div>
      <h1 style={{ fontSize: 22, fontWeight: 800, margin: "14px 0 8px" }}>页面走丢了</h1>
      <p style={{ color: "var(--muted)", fontSize: 14, marginBottom: 26 }}>
        你访问的页面不存在或已下线。可以从下面继续：
      </p>
      <div style={{ display: "flex", gap: 12, justifyContent: "center", flexWrap: "wrap" }}>
        <Link className="btn primary" href="/">回到看板</Link>
        <Link className="btn" href="/course">量化课程</Link>
        <Link className="btn" href="/sim">模拟盘</Link>
      </div>
    </div>
  );
}
