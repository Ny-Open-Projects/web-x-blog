import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { allModules, getModule } from "@/lib/content";
import Markdown from "@/components/Markdown";

export function generateStaticParams() {
  return allModules().map((m) => ({ slug: m.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const mod = getModule(slug);
  if (!mod) return { title: "课程未找到" };
  return {
    title: `${mod.title} · ${mod.trackName}`,
    description: mod.summary || `${mod.trackName}课程：${mod.title}`,
    openGraph: { title: mod.title, description: mod.summary || "", type: "article" },
  };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const mod = getModule(slug);
  if (!mod) notFound();
  const all = allModules();
  const idx = all.findIndex((m) => m.slug === slug);
  const prev = idx > 0 ? all[idx - 1] : null;
  const next = idx < all.length - 1 ? all[idx + 1] : null;

  return (
    <main className="wrap">
      <div style={{ padding: "22px 0 0", fontSize: 13, color: "var(--muted)" }}>
        <Link href="/course">量化课程</Link> / <span>{mod!.trackName}</span> / <span style={{ color: "var(--text)" }}>{mod!.title}</span>
      </div>
      <article style={{ paddingBottom: 20 }}>
        <Markdown content={mod!.body} />
      </article>
      <div style={{ display: "flex", justifyContent: "space-between", gap: 12, margin: "10px 0 30px" }}>
        {prev ? <Link className="btn" href={`/course/${prev.slug}`}>← {prev.title}</Link> : <span />}
        {next ? <Link className="btn" href={`/course/${next.slug}`}>{next.title} →</Link> : <span />}
      </div>
    </main>
  );
}
