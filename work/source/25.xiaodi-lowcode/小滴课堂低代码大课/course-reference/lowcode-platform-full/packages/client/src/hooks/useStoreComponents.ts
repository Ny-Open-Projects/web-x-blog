import { ulid } from "ulid";
import { action, computed, toJS } from "mobx";
import type { TComponentPropsUnion, TComponentTypes } from "@lowcode/share";
import { calcValueByString } from "@lowcode/share";
import { createStoreComponents } from "~/store";
import { arrayMove } from "@dnd-kit/sortable";
import { trackUndo } from "mobx-shallow-undo";
import { message } from "antd";
import type { TStoreComponents } from "~/store";
import { getLowCodePage } from "~/api/low-code";
import { useStorePage } from ".";

const storeComponents = createStoreComponents();

// 撤销前进的插件
const sotreComponentsUndoer = trackUndo(
  () => toJS(storeComponents),
  (value) => {
    const { _replace } = useStoreComponents();
    _replace(value);
  }
);

export function useStoreComponents() {
  // 默认选中的组件
  const setCurrentComponent = action((id: string) => {
    storeComponents.currentCompConfig = id;
  });

  // 定义添加组件的函数
  const push = action((type: TComponentTypes) => {
    // 创建一个新的组件配置
    // @ts-ignore
    const comp: TComponentPropsUnion = { id: ulid(), type, props: {} };
    storeComponents.compConfigs[comp.id] = comp;
    storeComponents.sortableCompConfig.push(comp.id);
    // 设置默认选中的组件
    setCurrentComponent(comp.id);
  });

  // 定义根据id获取组件配置的函数
  const getComponentById = action((id: string) => {
    return storeComponents.compConfigs[id];
  });

  // 判断是否为当前组件
  const isCurrentComponent = action((compConfig: TComponentPropsUnion) => {
    return getCurrentComponentConfig.get()?.id === compConfig.id;
  });

  // 返回默认选中组件属性信息
  const getCurrentComponentConfig = computed(() => {
    return storeComponents.currentCompConfig
      ? storeComponents.compConfigs[storeComponents.currentCompConfig]
      : null;
  });

  // 定义根据props更新当前组件的函数
  const updateCurrentComponent = action(
    (compConfig: TComponentPropsUnion["props"]) => {
      // 遍历传入的compConfig对象，更新当前组件配置的props属性
      const curCompConfig = getCurrentComponentConfig.get();
      if (!curCompConfig) return;

      for (const [key, value] of Object.entries(compConfig)) {
        // 更新当前组件配置的props属性
        // @ts-expect-error ignore type
        curCompConfig.props[key] = calcValueByString(value);
      }
    }
  );

  // 定义带有数组参数的更新当前组件配置的函数
  type TUpdateCurrentCompConfigWithArray = (args: {
    key: string;
    index: number;
    field: string;
    value: string;
  }) => void;
  const updateCurrentCompConfigWithArray: TUpdateCurrentCompConfigWithArray =
    action(({ key, index, field, value }) => {
      // 获取当前组件配置
      const curCompConfig = getCurrentComponentConfig.get();
      if (!curCompConfig) return;

      // 更新当前组件配置的props属性
      // @ts-expect-error typescript无法正确推断可选类型
      curCompConfig.props[key][index][field] = value;
    });

  // 定义展开或者折叠组件列表的函数
  const setItemsExpandIndex = action((index: number) => {
    storeComponents.itemsExpandIndex = index;
  });

  // 定义撤销操作的函数
  const undo = action(() => {
    // 判断有无上一步
    if (!sotreComponentsUndoer.hasUndo) {
      message.warning("没有可撤销的操作");
      return;
    }
    // 执行撤销操作
    sotreComponentsUndoer.undo();
  });

  // 定义重做操作的函数
  const redo = action(() => {
    //  判断有无下一步
    if (!sotreComponentsUndoer.hasRedo) {
      message.warning("没有可重做的操作");
      return;
    }
    // 执行重做操作
    sotreComponentsUndoer.redo();
  });

  // 定义移动组件的函数
  const moveComponent: (pos: { oldIndex: number; newIndex: number }) => void =
    action(({ oldIndex, newIndex }) => {
      // arrayMove根据两个索引子排序数组，返回排序后的数组
      storeComponents.sortableCompConfig = arrayMove(
        storeComponents.sortableCompConfig,
        oldIndex,
        newIndex
      );
    });

  // 定义向上移动组件的函数
  const moveUpComponent = action(() => {
    // 获取当前组件在数组中的旧索引
    const oldIndex = getCurrentComponentIndex.get();
    // 如果当前组件不是第一个组件，则执行移动操作
    if (getCurrentComponentIndex.get() !== 0) {
      moveComponent({
        oldIndex,
        newIndex: oldIndex - 1,
      });
    } else {
      message.warning("此组件已经是第一个了");
    }
  });

  // 定义向下移动组件的函数
  const moveDownComponent = action(() => {
    // 获取当前组件在数组中的旧索引
    const oldIndex = getCurrentComponentIndex.get();
    // 如果当前组件不是最后一个组件，则执行移动操作
    if (
      getCurrentComponentIndex.get() !==
      storeComponents.sortableCompConfig.length - 1
    ) {
      moveComponent({
        oldIndex,
        newIndex: oldIndex + 1,
      });
    } else {
      message.warning("此组件已经是最后一个了");
    }
  });

  // 定义复制当前组件的函数
  const copyCurrentComponent = action(() => {
    // 获取当前组件配置，在复制前先转换为JS对象
    const curCompConfig = getCurrentComponentConfig.get();
    if (!curCompConfig) return;

    // 复制当前组件配置，并保存到storeComponents.copyedCompConig中
    storeComponents.copyedCompConig = toJS(curCompConfig);
  });

  // 定义粘贴组件的函数
  const pasteCopyedComponent = action(() => {
    // 如果不存在复制的组件配置，则返回
    if (!storeComponents.copyedCompConig) return;

    // 创建新的组件配置，深拷贝复制的对象，重新分配 id，否3则 id 跟复制前的yi'zhi
    const comp = {
      ...JSON.parse(JSON.stringify(storeComponents.copyedCompConig)),
      id: ulid(),
    };

    // 将新的组件配置添加到storeComponents.compConfigs中
    storeComponents.compConfigs[comp.id] = comp;
    // 将新的组件配置id添加到storeComponents.sortableCompConfig中
    storeComponents.sortableCompConfig.push(comp.id);
    // 设置当前组件配置为新添加的组件配置
    setCurrentComponent(comp.id);
  });

  // 定义删除当前组件的函数
  const removeCurrentComponent = action(() => {
    // 获取当前组件配置的id在storeComponents.sortableCompConfig中的索引
    const curCompConfig = getCurrentComponentConfig.get();
    if (!curCompConfig) return;

    const index = getCurrentComponentIndex.get();
    // 从storeComponents.sortableCompConfig中删除当前组件
    storeComponents.sortableCompConfig.splice(index, 1);
    // 从storeComponents.compConfigs中删除当前组件配置
    delete storeComponents.compConfigs[curCompConfig.id];

    // 如果当前组件被删除，则将当前组件配置设置为上一个组件的配置，如果不存在则设置为第一个组件的配置
    const rollbackIndex = index - 1 > 0 ? index - 1 : 0;
    storeComponents.currentCompConfig =
      storeComponents.sortableCompConfig[rollbackIndex] || null;
  });

  // 定义替换组件配置的函数
  const _replace = action((value: TStoreComponents) => {
    storeComponents.compConfigs = value.compConfigs;
    storeComponents.currentCompConfig = value.currentCompConfig;
    storeComponents.sortableCompConfig = value.sortableCompConfig;
  });

  // 获取当前组件在数组中的索引的 computed property
  const getCurrentComponentIndex = computed(() => {
    // 返回storeComponents.sortableCompConfig中当前组件配置的id所在的位置
    return storeComponents.sortableCompConfig.indexOf(
      getCurrentComponentConfig.get()!.id
    );
  });

  // 定义将组件存储到本地存储的函数
  const storeInLocalStorage = action(() => {
    // 将组件配置、可排序组件配置、当前组件配置和存储时间保存到本地存储
    const compConfig = JSON.stringify(toJS(storeComponents.compConfigs));
    const sortableCompConfig = JSON.stringify(
      toJS(storeComponents.sortableCompConfig)
    );
    const currentCompConfig = JSON.stringify(
      toJS(storeComponents.currentCompConfig)
    );

    localStorage.setItem("compConfig", compConfig);
    localStorage.setItem("sortableCompConfig", sortableCompConfig);
    localStorage.setItem("currentCompConfig", currentCompConfig);
    // 保存当前操作的时间
    localStorage.setItem("store_time", String(Date.now()));

    message.success("保存成功");
  });

  // 定义从本地存储中读取组件的函数
  const localStorageInStore = action(async () => {
    // 从本地存储中读取组件配置相关数据
    const compConfig = localStorage.getItem("compConfig");
    const sortableCompConfig = localStorage.getItem("sortableCompConfig");
    const currentCompConfig = localStorage.getItem("currentCompConfig");

    const storeTime = localStorage.getItem("store_time");
    const releaseTime = localStorage.getItem("release_time");

    // 如果存在组件配置数据，则根据存储时间判断是否可以读取数据
    if (compConfig && compConfig !== "{}") {
      if (
        storeTime &&
        Number(storeTime) > (releaseTime ? Number(releaseTime) : 0)
      ) {
        // 从JSON字符串转换为组件配置对象
        storeComponents.compConfigs = JSON.parse(compConfig);
        storeComponents.sortableCompConfig = JSON.parse(sortableCompConfig!);
        storeComponents.currentCompConfig = JSON.parse(currentCompConfig!);
        message.success("已自动从草稿中读取数据");
      } else {
        // 服务端获取页面组件
        readDataFromServer();
      }
    } else {
      // 服务端获取页面组件
      readDataFromServer();
    }
  });

  const { updatePage } = useStorePage();
  // 定义从服务器读取数据的函数
  const readDataFromServer = action(async () => {
    // 获取组件数据和页面信息，并转换为组件配置对象
    const { data } = await getLowCodePage();
    storeComponents.compConfigs = data?.components
      ?.map((comp: any) => {
        return {
          ...comp,
          id: ulid(),
        };
      })
      .reduce((acc: any, cur: any) => {
        // 将组件配置id添加到可排序组件配置中
        acc[cur.id] = {
          id: cur.id,
          type: cur.type,
          props: cur.options ?? {},
        };
        return acc;
      }, {});
    storeComponents.sortableCompConfig = Object.keys(
      storeComponents.compConfigs
    );
    // 设置当前组件配置为可排序组件配置的第一个组件配置
    storeComponents.currentCompConfig = storeComponents.sortableCompConfig[0];
    // 更新页面信息
    updatePage({
      tdk: data.tdk,
      title: data.page_name,
      description: data.desc,
    });

    message.success("已自动从服务器读取数据");
  });

  return {
    _replace,
    push,
    getComponentById,
    isCurrentComponent,
    getCurrentComponentConfig,
    setCurrentComponent,
    store: storeComponents,
    updateCurrentComponent,
    updateCurrentCompConfigWithArray,
    setItemsExpandIndex,
    undo,
    redo,
    moveComponent,
    moveUpComponent,
    moveDownComponent,
    copyCurrentComponent,
    pasteCopyedComponent,
    removeCurrentComponent,
    getCurrentComponentIndex,
    storeInLocalStorage,
    localStorageInStore,
  };
}
