// 自选清单：localStorage 持久化，看板与模拟盘共用
const KEY = "quantsite-watch-v1";
const DEFAULT = ["510300", "510500", "515030", "512000", "588000"];

export function getWatch(): string[] {
  if (typeof window === "undefined") return DEFAULT;
  try {
    const a = JSON.parse(localStorage.getItem(KEY) || "null");
    return Array.isArray(a) && a.length ? a : DEFAULT;
  } catch { return DEFAULT; }
}

export function saveWatch(w: string[]): void {
  if (typeof window !== "undefined") localStorage.setItem(KEY, JSON.stringify(w));
}

// 简单代码校验：6 位数字（A 股/ETF）
export function validCode(c: string): boolean {
  return /^\d{6}$/.test(c.trim());
}
