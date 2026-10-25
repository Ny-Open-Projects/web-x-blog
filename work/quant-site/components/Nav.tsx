"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const LINKS = [
  { href: "/", label: "数据看板" },
  { href: "/course", label: "量化课程" },
  { href: "/sim", label: "模拟盘" },
];

export default function Nav() {
  const path = usePathname();
  return (
    <nav className="nav">
      <div className="wrap nav-inner">
        <div className="brand">
          <span className="logo">锋</span>网锋量化
          <span style={{ color: "var(--faint)", fontWeight: 600, fontSize: 13 }}>QuantSite</span>
        </div>
        <div className="nav-links">
          {LINKS.map((l) => {
            const active = l.href === "/" ? path === "/" : path.startsWith(l.href);
            return (
              <Link key={l.href} href={l.href} className={active ? "active" : ""}>
                {l.label}
              </Link>
            );
          })}
        </div>
      </div>
    </nav>
  );
}
