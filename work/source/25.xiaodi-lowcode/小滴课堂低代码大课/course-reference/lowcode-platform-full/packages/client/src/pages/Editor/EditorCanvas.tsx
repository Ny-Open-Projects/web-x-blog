import ClassNames from "classnames";
import { toJS } from "mobx";
import { observer } from "mobx-react-lite";
import type { FC, ReactNode } from "react";
import {
  useMemo,
  useState,
  useEffect,
  useImperativeHandle,
  Ref,
  createRef,
} from "react";
import { getComponentByType } from "@lowcode/share";
import type {
  TBasicComponentConfig,
  TComponentPropsUnion,
} from "@lowcode/share";
import { useStoreComponents, useComponentKeyPress } from "~/hooks";
import type { TStoreComponents } from "~/store";
import SortableContainer from "~/components/DragSortable/SortableContainer";
import SortableItem from "~/components/DragSortable/SortableItem";
import type { DragStartEvent } from "@dnd-kit/core";
import { components } from "./LeftPanel/ComponentList";
import { DeleteOutlined, UpOutlined, DownOutlined } from "@ant-design/icons";

// 获取公共组件
export function generateComponent(conf: TBasicComponentConfig) {
  const Component = getComponentByType(conf.type);

  // toJS将mobx装饰过的对象转成普通对象
  return <Component {...toJS(conf.props)} key={conf.id} />;
}

interface ComponentWrapperProps {
  id: string;
  children: ReactNode;
  isDragable: boolean;
  onClick: () => void;
  isCurrentComponent: boolean;
}

// 公共组件的布局样式组件
const ComponentWrapper: FC<ComponentWrapperProps> = ({
  id,
  children,
  isDragable,
  isCurrentComponent,
  onClick,
}) => {
  // 设置选中的组件样式和鼠标hover的样式
  const classNames = useMemo(() => {
    return ClassNames({
      "absolute left-0 top-0 w-full h-full z-[999]": true,
      "hover:border-[3px] hover:border-blue-500":
        !isCurrentComponent && !isDragable,
      "border-[2px] border-blue-400": isCurrentComponent,
    });
  }, [isCurrentComponent, isDragable]);

  return (
    <div
      className="relative cursor-pointer component-warpper"
      onClick={onClick}
      data-id={id} // 绑定 id，方便工具栏位置的控制
    >
      <div className={classNames} />
      <div
        className="pointer-events-none" //屏蔽鼠标和键盘操作
      >
        {children}
      </div>
    </div>
  );
};

// 每个工具的样式组件
const EditorChooiseToolbarIconContainer: FC<{
  children: ReactNode;
  onClick: () => void;
}> = ({ children, onClick }) => {
  return (
    <div
      className="cursor-pointer hover:bg-gray-50/50 px-[0.5px] transition-colors"
      onClick={onClick}
    >
      {children}
    </div>
  );
};

// 组件的工具栏
const EditorChooiseToolbar: FC<{
  hidden: boolean;
  onRef: any;
}> = observer(({ hidden, onRef }) => {
  const {
    store,
    moveUpComponent,
    moveDownComponent,
    removeCurrentComponent,
    getCurrentComponentConfig,
  } = useStoreComponents();
  const [currentComponentRect, setCurrentComponentRect] =
    useState<ClientRect>();

  const [isFirst, setIsFirst] = useState(false);
  const [refrash, setRefrash] = useState(false);
  const [localHidden, setLocalHidden] = useState(false);

  // 滚动控制的 hidden 和是否可见控制的 localHidden 去控制工具栏是否展示
  const classNames = useMemo(() => {
    return ClassNames({
      hidden: hidden || localHidden,
      "absolute bg-blue-500 p-[4px] flex items-center text-sm text-white gap-2":
        true,
    });
  }, [hidden, localHidden]);

  useImperativeHandle(onRef, () => ({ setRefrash }));

  // 循环遍历所有组件的配置数组，找到当前默认组件的名字
  const componentName = useMemo(() => {
    return (
      components.find(
        (item) => item.type === getCurrentComponentConfig.get()?.type
      )?.name ?? "组件名称"
    );
  }, [getCurrentComponentConfig.get()]);

  // 获取当前默认选中的组件 DOM 元素
  function getCurrentCompConfig() {
    const componentWarppers = document.querySelectorAll(".component-warpper");
    let currentCompConfig = null;

    componentWarppers?.forEach((el) => {
      if (el.getAttribute("data-id") === store.currentCompConfig)
        currentCompConfig = el;
    });

    return currentCompConfig as HTMLDivElement | null;
  }

  // 获取默认选中的 DMO 元素在浏览器的坐标和宽高
  function resizeComponent() {
    const currentComponent = getCurrentCompConfig();
    if (currentComponent) {
      const rect = currentComponent?.getBoundingClientRect();
      setCurrentComponentRect(rect);
    }
  }

  // 来观察当前组件是否可见，去展示或者隐藏工具栏
  // 并根据可见性设置全局变量hidden的值
  useEffect(() => {
    // 获取canvas容器元素
    const oCanvasContainer = document.querySelector(".editor-canvas-container");
    // 获取当前组件的配置信息
    const currentComponent = getCurrentCompConfig();

    // 创建一个Intersection Observer实例
    // 用于观察某个组件元素是否进入或离开视口
    const _observer = new IntersectionObserver(
      (entries) => {
        console.log(111, entries);
        // 遍历entries数组
        entries.forEach((entry) => {
          // 如果当前元素不是当前组件，则直接返回
          if (entry.target !== currentComponent) return;

          // 如果元素是可见的，则将全局变量localHidden设置为false
          entry.isIntersecting ? setLocalHidden(false) : setLocalHidden(true);
        });
      },
      // Intersection Observer的配置选项
      {
        // 定义观察的可见性阈值，当元素完全进入或离开视口时触发回调
        threshold: 0.9,
        // 将根元素设置为canvas容器元素
        root: oCanvasContainer,
      }
    );

    // 如果当前组件和canvas容器元素都存在，则将当前组件添加到观察列表中
    if (currentComponent && oCanvasContainer)
      _observer.observe(currentComponent);

    // 在组件卸载时，清除Intersection Observer的监听
    return () => {
      _observer.disconnect();
    };
    // getCurrentComponentConfig.get()默认选中变化重新执行, 滚动触发hidden变化重新执行
  }, [getCurrentComponentConfig.get(), hidden]);

  // 使用useEffect钩子函数来处理一些只在组件挂载时执行的逻辑
  useEffect(() => {
    // 如果不是第一次渲染，则直接返回
    if (!isFirst) {
      // 将isFirst标记设置为true
      setIsFirst(true);
      // 因为这个时候，组件可能还没有完全挂载完成，所以需要延迟一段时间
      setTimeout(() => {
        resizeComponent();
      }, 500);
      return;
    }

    // refrash hook，用于强制刷新一次组件
    if (refrash) {
      setRefrash(false);
      return;
    }

    // 调用resizeComponent函数
    resizeComponent();
  }, [hidden, localHidden, isFirst, refrash, getCurrentComponentConfig.get()]);

  // 工具栏的按钮点击
  function handleOnClick(fn: () => void) {
    setRefrash(true);
    fn();
  }

  return (
    getCurrentComponentConfig.get() && (
      <div
        className={classNames}
        style={{
          left: `${currentComponentRect?.right}px`, // 设置工具栏定位的 left 等于当前组件的 right，左手坐标系定位
          top: `${currentComponentRect && currentComponentRect.bottom - 28}px`, // 设置工具栏定位的 top 等于当前组件的 bottom-工具栏高度，左手坐标系定位
        }}
      >
        {/* 组件名字 */}
        <span>{componentName} |</span>

        {/* 删除按钮 */}
        <EditorChooiseToolbarIconContainer
          onClick={() => handleOnClick(removeCurrentComponent)}
        >
          <DeleteOutlined />
        </EditorChooiseToolbarIconContainer>

        {/* 向上按钮 */}
        <EditorChooiseToolbarIconContainer
          onClick={() => handleOnClick(moveUpComponent)}
        >
          <UpOutlined />
        </EditorChooiseToolbarIconContainer>

        {/* 向下按钮 */}
        <EditorChooiseToolbarIconContainer
          onClick={() => handleOnClick(moveDownComponent)}
        >
          <DownOutlined />
        </EditorChooiseToolbarIconContainer>
      </div>
    )
  );
});

// 低代码视图组件
const EditorCanvas: FC<{
  store: TStoreComponents;
  onRef: any;
}> = observer(({ store, onRef }) => {
  const {
    getComponentById,
    isCurrentComponent,
    setCurrentComponent,
    getCurrentComponentConfig,
    moveComponent,
  } = useStoreComponents();

  // 控制是否有拖拽
  const [isDragable, setIsDragable] = useState(false);
  // 控制工具栏的显示隐藏，定义在当前组件，方便抛出给父组件滚动事件调用
  const [showToolbar, setShowToolbar] = useState(true);
  const toolbarRef = createRef<any>();

  // 点击组件设置成选中组件，已选中则不做操作
  function handleComponentClick(conf: TComponentPropsUnion) {
    if (isCurrentComponent(conf)) return;
    setCurrentComponent(conf.id);
  }

  // 拖拽结束 要移动的和被替换的元素下标索引，传入移动组件的函数
  function handleDragEnd(oldIndex: number, newIndex: number) {
    moveComponent({ oldIndex, newIndex });
    setIsDragable(false);
    toolbarRef.current?.setRefrash(true);
  }

  // 拖拽开始，设置当前选中的为默认组件
  function handleDragStart(event: DragStartEvent) {
    setCurrentComponent(event.active.id.toString());
    setIsDragable(true);
  }

  // 键盘操作数组的监听事件
  useComponentKeyPress();

  // 提供父组件调用自身的函数，控制工具栏的展示隐藏
  useImperativeHandle(onRef, () => ({ setShowToolbar }));

  return (
    <>
      <SortableContainer
        items={store.sortableCompConfig}
        onDragEnd={handleDragEnd}
        onDragStart={handleDragStart}
      >
        {store.sortableCompConfig
          .map((id) => getComponentById(id))
          .map((conf) => {
            return (
              <SortableItem id={conf.id} key={conf.id}>
                <ComponentWrapper
                  id={conf.id}
                  key={conf.id}
                  isDragable={isDragable}
                  onClick={() => handleComponentClick(conf)}
                  isCurrentComponent={
                    getCurrentComponentConfig.get()?.id === conf.id
                  }
                >
                  {generateComponent(conf)}
                </ComponentWrapper>
              </SortableItem>
            );
          })}
      </SortableContainer>
      <EditorChooiseToolbar hidden={!showToolbar} onRef={toolbarRef} />
    </>
  );
});

export default EditorCanvas;
