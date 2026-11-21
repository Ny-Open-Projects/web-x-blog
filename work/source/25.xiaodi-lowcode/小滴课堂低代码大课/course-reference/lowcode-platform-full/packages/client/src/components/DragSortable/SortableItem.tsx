import type { FC, ReactNode } from "react";
import { useSortable } from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";

interface PropsType {
  id: string;
  children: ReactNode;
}

const SortableItem: FC<PropsType> = ({ id, children }) => {
  // 使用 useSortable 钩子，获取排序项的相关属性、事件监听器和节点引用
  const { attributes, listeners, setNodeRef, transform, transition } =
    useSortable({ id });

  // 定义样式对象，包含过渡和变换效果
  const style = {
    transition,
    // 默认输出带scaleY的transform
    // 因为我们的组件Y轴大小并不一致
    // 所以用正则替换为空
    transform: CSS.Transform.toString(transform)?.replace(/scaleY\(.+\)/, ""),
  };

  // 返回带有排序项属性和事件监听器的 div 元素，以及子元素节点
  return (
    <div ref={setNodeRef} style={style} {...attributes} {...listeners}>
      {children}
    </div>
  );
};

export default SortableItem;
