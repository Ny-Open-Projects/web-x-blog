import { action } from "mobx";
import { createStorePage } from "~/store";
import type { TStorePage } from "~/store";

const storePage = createStorePage();

export function useStorePage() {
  /**
   * 设置页面标题
   * @param title - 页面标题
   */
  const setPageTitle = action((title: string) => {
    storePage.title = title;
  });

  /**
   * 更新页面信息
   * @param page - 部分页面信息
   */
  const updatePage = action((page: Partial<TStorePage>) => {
    if (!page) return;
    for (const [key, value] of Object.entries(page))
      storePage[key as keyof TStorePage] = value;
  });

  return {
    updatePage,
    setPageTitle,
    store: storePage,
  };
}
