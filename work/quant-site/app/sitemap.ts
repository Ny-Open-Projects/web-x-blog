import type { MetadataRoute } from "next";
import { allModules } from "@/lib/content";

const BASE = "https://quant.webfault.com";

export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();
  const mods = allModules().map((m) => ({
    url: `${BASE}/course/${m.slug}`,
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.7,
  }));
  return [
    { url: BASE, lastModified: now, changeFrequency: "daily" as const, priority: 1 },
    { url: `${BASE}/course`, lastModified: now, changeFrequency: "weekly" as const, priority: 0.9 },
    { url: `${BASE}/sim`, lastModified: now, changeFrequency: "weekly" as const, priority: 0.8 },
    ...mods,
  ];
}
