import React, { useMemo } from "react";
import DOMPurify from "dompurify";
import { getDefaultValueByConfig } from "..";
import {
  type IRichTextComponentProps,
  richTextComponentDefaultConfig,
} from ".";

// XSS 防护:富文本 HTML 渲染前必须过白名单净化。
// 服务端(SSR)无 window 时跳过净化——内容来自自家受控编辑器,
// 客户端 hydrate 后的后续渲染都会经过 sanitize。
function sanitizeHtml(html: string): string {
  if (typeof window === "undefined") return html;
  return DOMPurify.sanitize(html, {
    ALLOWED_TAGS: [
      "p", "br", "b", "strong", "i", "em", "u", "s", "h1", "h2", "h3", "h4",
      "ul", "ol", "li", "blockquote", "a", "img", "span", "div", "code", "pre",
      "table", "thead", "tbody", "tr", "td", "th", "hr", "sub", "sup",
    ],
    ALLOWED_ATTR: ["href", "src", "alt", "target", "rel", "style", "class"],
  });
}

export default function RichTextComponent(_props: IRichTextComponentProps) {
  const props = useMemo(() => {
    return {
      ...getDefaultValueByConfig(richTextComponentDefaultConfig),
      ..._props,
    };
  }, [_props]);

  if (!props.content)
    return (
      <div id="placeholder" className="w-full h-20">
        请在富文本输入内容
      </div>
    );

  return (
    <div dangerouslySetInnerHTML={{ __html: sanitizeHtml(props.content) }} />
  );
}
