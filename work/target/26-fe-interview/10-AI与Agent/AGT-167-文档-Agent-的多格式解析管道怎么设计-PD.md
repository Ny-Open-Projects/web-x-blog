---
title: [AGT-167] 文档 Agent 的多格式解析管道怎么设计（PDF/Word/Excel/网页）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-167：文档 Agent 的多格式解析管道怎么设计（PDF/Word/Excel/网页）？
**答**：
- 管道分层：格式识别（magic bytes 而非扩展名）→ 格式适配器（PDF 走版面分析保留标题层级，Word 抽段落样式，Excel 表格转双层表示，网页去噪抽正文）→ 统一中间表示（IR：块树，每块带类型/层级/来源页码）→ 下游（chunking/嵌入）只消费 IR。
- 关键难点：PDF 双栏/表格/扫描件——扫描件 OCR 前置判断（文本层字符密度低即 OCR），表格用表格检测模型或规则修复行列；版面信息（标题层级）直接决定父子分块质量，不能在纯文本上补。
- 保真要求：每块保留 `source { page, bbox }` 支持溯源高亮（AGT-075）；图片块生成 caption 并保留原位置。
- 质量门禁：解析后跑「完整性检查」（页数对齐、字符覆盖率、乱码率），不达标走备用解析器并标记低置信。

```typescript
// 多格式文档解析管道：适配器 → 统一 IR → 质量门禁
interface Block { type: 'heading' | 'paragraph' | 'table' | 'image'; level?: number; text: string;
  source: { page: number; bbox?: number[] }; confidence: number; }
interface DocIR { docId: string; format: 'pdf' | 'docx' | 'xlsx' | 'html'; blocks: Block[]; }

type Adapter = (buf: Buffer) => Promise<Block[]>;

const adapters: Record<DocIR['format'], Adapter> = {
  pdf: async (buf) => {
    const pdf = await pdfParse(buf);
    const charDensity = pdf.text.length / pdf.numpages;
    if (charDensity < 100) return ocrPipeline(buf);            // 扫描件：字符密度低 → OCR
    return pdf.text.split('\n').map((t, i) => ({
      type: /^第?[0-9一二三四五六七八九十]+[章节]/.test(t) ? 'heading' : 'paragraph',
      level: 1, text: t, source: { page: i + 1 }, confidence: 0.9,
    }));
  },
  docx: async (buf) => parseDocxBlocks(buf),                  // Word 按样式抽标题层级
  xlsx: async (buf) => toRowSentences(await parseXlsx(buf)),  // 表格转行句子（AGT-146）
  html: async (buf) => extractReadable(buf.toString()),       // 网页去噪抽正文
};

function sniff(buf: Buffer): DocIR['format'] {
  if (buf.subarray(0, 4).toString() === '%PDF') return 'pdf';
  if (buf.subarray(0, 4).toString('hex') === '504b0304') return 'docx';
  if (buf.subarray(0, 8).toString('hex') === 'd0cf11e0a1b11ae1') return 'docx';
  return 'html';
}

export async function ingest(buf: Buffer, docId: string): Promise<DocIR> {
  const format = sniff(buf);
  let blocks = await adapters[format](buf);
  // 质量门禁：乱码率与空块率超阈值 → 标记低置信并尝试备用解析
  const garbled = blocks.filter((b) => (b.text.match(/\uFFFD/g) ?? []).length / Math.max(1, b.text.length) > 0.05).length;
  const confidence = garbled / Math.max(1, blocks.length) > 0.2 ? 0.5 : 1;
  if (confidence < 1) blocks = await adapters[format === 'pdf' ? 'html' : 'pdf'](buf).catch(() => blocks);
  audit.info({ docId, format, blocks: blocks.length, confidence });
  return { docId, format, blocks };
}
async function pdfParse(b: Buffer) { void b; return { text: '第1章 概述', numpages: 1 }; }
async function ocrPipeline(b: Buffer) { void b; return [] as Block[]; }
async function parseDocxBlocks(b: Buffer) { void b; return [] as Block[]; }
async function parseXlsx(b: Buffer) { void b; return [] as any[][]; }
function toRowSentences(rows: any[][]): Block[] { void rows; return []; }
function extractReadable(html: string): Block[] { return [{ type: 'paragraph', text: html, source: { page: 1 }, confidence: 0.8 }]; }
const audit = { info: (x: unknown) => { void x; } };
```
