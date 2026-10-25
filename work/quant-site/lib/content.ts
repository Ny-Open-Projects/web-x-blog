import fs from "fs";
import path from "path";

export type Module = {
  slug: string; track: "basics" | "quant" | "data"; trackName: string; order: number;
  title: string; summary: string; body: string;
};

const DIR = path.join(process.cwd(), "content");
const TRACKS: Record<string, string> = { basics: "量化基础", quant: "数字货币量化实战", data: "数据分析（量化基石）" };
const pad = (n: number) => String(n).padStart(2, "0");

function parse(raw: string): { fm: Record<string, string>; body: string } {
  const m = raw.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!m) return { fm: {}, body: raw };
  const fm: Record<string, string> = {};
  for (const line of m[1].split("\n")) {
    const i = line.indexOf(":");
    if (i > 0) fm[line.slice(0, i).trim()] = line.slice(i + 1).trim();
  }
  return { fm, body: m[2] };
}

export function allModules(): Module[] {
  const mods: Module[] = [];
  for (const track of ["basics", "quant", "data"] as const) {
    const dir = path.join(DIR, track);
    if (!fs.existsSync(dir)) continue;
    for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".md"))) {
      const { fm, body } = parse(fs.readFileSync(path.join(dir, f), "utf-8"));
      const order = +(fm.order || 99);
      mods.push({ slug: `${track}-${pad(order)}`, track, trackName: TRACKS[track], order, title: fm.title || f, summary: fm.summary || "", body });
    }
  }
  return mods.sort((a, b) => (a.track === b.track ? a.order - b.order : a.track.localeCompare(b.track)));
}

export function getModule(slug: string): Module | undefined {
  return allModules().find((m) => m.slug === slug);
}
