import type { IRichTextComponentProps } from "@lowcode/share";
import {
  fillComponentPropsByConfig,
  richTextComponentDefaultConfig,
} from "@lowcode/share";
import { useMemo, useRef } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";

import { useStoreComponents } from "~/hooks";

export default function RichTextComponentProps(
  _props: IRichTextComponentProps
) {
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, richTextComponentDefaultConfig);
  }, [_props]);
  const { updateCurrentComponent } = useStoreComponents();

  // 创建 React Quill 编辑器的实例
  const editorRef = useRef<ReactQuill>(null);

  return (
    <div className="flex items-center justify-center">
      <ReactQuill
        theme="snow"
        value={props.content.value}
        onChange={(_value, _delta, _source, editor) =>
          updateCurrentComponent({ content: editor.getHTML() })
        }
        ref={editorRef}
        modules={{
          toolbar: [
            [
              { header: [1, 2, 3, 4, false] },
              "bold",
              "italic",
              "underline",
              { color: [] },
              { background: [] },
              { align: [] },
              { list: "ordered" },
              { list: "bullet" },
              { font: [] },
            ],
            ["code-block"],
          ],
        }}
        placeholder="请输入内容"
      />
    </div>
  );
}
