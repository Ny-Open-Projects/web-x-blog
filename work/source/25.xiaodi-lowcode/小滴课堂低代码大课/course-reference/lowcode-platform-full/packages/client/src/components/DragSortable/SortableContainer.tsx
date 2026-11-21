import type { FC, ReactNode } from "react";
import type { DragEndEvent, DragStartEvent } from "@dnd-kit/core";
import {
  DndContext,
  MouseSensor,
  closestCenter,
  useSensor,
  useSensors,
} from "@dnd-kit/core";
import {
  SortableContext,
  verticalListSortingStrategy,
} from "@dnd-kit/sortable";

interface PropsType {
  items: string[]; //可排序项的数组
  children: ReactNode; //子元素节点
  onDragStart: (event: DragStartEvent) => void; //拖拽开始时的回调函数
  onDragEnd: (oldIndex: number, newIndex: number) => void; //拖拽结束时的回调函数
}

const SortableContainer: FC<PropsType> = ({
  children,
  items,
  onDragEnd,
  onDragStart,
}) => {
  // 使用 useSensors 钩子，创建一个鼠标传感器，设置拖动监听像素为每2px执行一次
  const sensors = useSensors(
    useSensor(MouseSensor, {
      activationConstraint: {
        distance: 2,
      },
    })
  );

  // 拖拽结束时的处理函数
  function handleDragEnd(event: DragEndEvent) {
    // 获取拖拽的激活和目标元素
    const { active, over } = event;
    if (over == null) return;

    /**
     * 对比交换后的id变化
     * 如果id不对等则就是交换过了，获取交换的顺序
     * 然后抛出onDragEnd，在具体的视图内处理数据
     */
    if (active.id !== over.id) {
      const newIndex = items.findIndex((c) => c === over.id);
      const oldIndex = items.findIndex((c) => c === active.id);
      onDragEnd(oldIndex, newIndex);
    }
  }

  return (
    <DndContext
      sensors={sensors}
      collisionDetection={closestCenter} // 最接近中心算法 碰撞检测算法
      onDragEnd={handleDragEnd}
      onDragStart={onDragStart}
    >
      {/* 使用 SortableContext 包裹子元素，设置排序的策略为垂直列表 */}
      <SortableContext items={items} strategy={verticalListSortingStrategy}>
        {children}
      </SortableContext>
    </DndContext>
  );
};

export default SortableContainer;
