"use client";
import { marked } from "marked";

marked.setOptions({ gfm: true, breaks: false });

export default function Markdown({ content }: { content: string }) {
  const html = marked.parse(content, { async: false }) as string;
  return <div className="md" dangerouslySetInnerHTML={{ __html: html }} />;
}
