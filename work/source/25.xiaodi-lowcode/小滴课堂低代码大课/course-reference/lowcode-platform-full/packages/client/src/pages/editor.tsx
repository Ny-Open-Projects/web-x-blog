import { createRef, useEffect, useRef, useState } from "react";
import { useTitle } from "ahooks";

import EditorHeader from "./Editor/EditorHeader";
import EditorLeftPanel from "./Editor/EditorLeftPanel";
import EditorRightPanel from "./Editor/EditorRightPanel";
import EditorCanvas from "./Editor/EditorCanvas";

import { useStoreComponents } from "~/hooks";
function Editor() {
  useTitle("小滴低代码平台 - 页面编辑");
  const { store: storeComps, localStorageInStore } = useStoreComponents();

  //  创建容器用于调用子组件的函数
  const canvasRef = createRef<any>();
  // 创建容器绑定 dom 用于监听滚动事件
  const canvasContainerRef = useRef<HTMLDivElement>(null);

  const [scrolling, setScrolling] = useState(false);

  // 从本地缓存或者服务端获取上一次配置的页面组件
  useEffect(() => {
    localStorageInStore();
  }, []);

  useEffect(() => {
    let scrollTimeout: NodeJS.Timeout;

    // 定义滚动事件处理函数
    const handleScroll = () => {
      // 如果正在滚动中则清除滚动计时
      if (scrolling) clearTimeout(scrollTimeout);

      setScrolling(true);
      // 滚动时隐藏小工具栏
      canvasRef.current?.setShowToolbar(false);

      // 一个特殊的小技巧判断是否有没有滚动完毕
      // 在30ms内没有滚动则认为滚动完毕
      scrollTimeout = setTimeout(() => {
        // 滚动完毕后将状态设置回来
        setScrolling(false);
        // 滚动完毕后将小工具栏显示出来
        canvasRef.current.setShowToolbar(true);
      }, 300);
    };

    // 绑定滚动事件监听器到画布容器元素
    canvasContainerRef.current?.addEventListener("scroll", handleScroll);

    // 组件销毁时，清除滚动事件监听器和滚动超时的函数
    return () => {
      canvasContainerRef.current?.removeEventListener("scroll", handleScroll);
      clearTimeout(scrollTimeout);
    };
  }, [scrolling]);

  return (
    <div className="flex flex-col h-full bg-[#f1f2f4]">
      {/* 头部组件 */}
      <header className="shadow-sm p-4 bg-white">
        <EditorHeader />
      </header>
      <main className="flex flex-1 border overflow-x-hidden">
        {/* 左侧编辑组件 */}
        <div className={`w-80 bg-white px-4 overflow-y-auto`}>
          <EditorLeftPanel />
        </div>
        {/* 中间编辑组件 */}
        <div className="flex-auto flex items-center justify-center">
          <div
            ref={canvasContainerRef}
            className="editor-canvas-container w-[380px] h-[700px] bg-white text-left overflow-y-auto overflow-x-hidden"
          >
            <EditorCanvas store={storeComps} onRef={canvasRef} />
          </div>
        </div>
        {/* 右侧编辑组件 */}
        <div className={`w-80 bg-white px-4 overflow-y-auto`}>
          <EditorRightPanel />
        </div>
      </main>
    </div>
  );
}
export default Editor;
