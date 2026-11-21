import { useKeyPress } from "ahooks";
import { message } from "antd";
import { useStoreComponents } from "./";

/**
 * 使用组件按键事件
 */
export function useComponentKeyPress() {
  const {
    undo, // 撤销
    redo, // 重做
    moveUpComponent, // 上移组件
    moveDownComponent, // 下移组件
    pasteCopyedComponent, // 粘贴已复制组件
    copyCurrentComponent, // 复制当前组件
    removeCurrentComponent, // 移除当前组件
    getCurrentComponentConfig, // 获取当前组件配置
  } = useStoreComponents();

  /**
   * 验证组件
   * @returns {boolean} 组件是否存在且焦点在按钮元素上
   */
  function validateComponent() {
    const isCompExist = getCurrentComponentConfig.get() !== null;
    const isActive =
      document.activeElement === document.body ||
      document.activeElement?.matches('div[role="button"]'); // 兼容拖拽插件

    if (!isCompExist) {
      message.warning("请先选择组件");
      return false;
    }
    return isActive;
  }

  /**
   * 上移组件
   */
  useKeyPress("uparrow", () => {
    if (!validateComponent()) return;
    moveUpComponent();
  });

  /**
   * 下移组件
   */
  useKeyPress("downarrow", () => {
    if (!validateComponent()) return;
    moveDownComponent();
  });

  /**
   * 移除当前组件
   */
  useKeyPress(["delete", "backspace"], () => {
    if (!validateComponent()) return;
    removeCurrentComponent();
  });

  /**
   * 复制当前组件
   */
  useKeyPress(["ctrl.c", "meta.c"], () => {
    if (!validateComponent()) return;
    copyCurrentComponent();
  });

  /**
   * 粘贴已复制组件
   */
  useKeyPress(["ctrl.v", "meta.v"], () => {
    if (!validateComponent()) return;
    pasteCopyedComponent();
  });

  /**
   * 重做
   */
  useKeyPress(["ctrl.shift.z", "meta.shift.z"], () => {
    redo();
  });

  /**
   * 撤销
   */
  useKeyPress(
    ["ctrl.z", "meta.z"],
    () => {
      if (!validateComponent()) return;
      undo();
    },
    {
      // 不严格匹配的话会和redo一次再undo
      exactMatch: true,
    }
  );
}
