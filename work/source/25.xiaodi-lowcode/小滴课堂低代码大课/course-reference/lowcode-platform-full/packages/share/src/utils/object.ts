/**
 * 从对象中删除指定的属性
 *
 * @template T - 对象类型
 * @template K - 属性键类型
 * @param {T} obj - 要处理的对象
 * @param {K[]} keys - 要删除的属性键的数组
 * @returns {Omit<T, K>} - 删除属性后的对象
 */
export function objectOmit<T extends object, K extends keyof T>(
  obj: T,
  keys: K[]
): Omit<T, K> {
  const result = {} as any;
  for (const key in obj) {
    // 要剔除的key不插入result新对象
    if (!keys.includes(key as unknown as K)) result[key] = obj[key];
  }
  return result;
}

/**
 * 从对象中选择指定的属性并返回新的对象
 * @param obj - 要选择属性的对象
 * @param keys - 要选择的属性键
 * @returns - 包含选择属性的新对象
 */
export function objectPick<T extends object, K extends keyof T>(
  obj: T,
  keys: K[]
): Pick<T, K> {
  const result = {} as any;
  // 要拿到的key插入result新对象
  for (const key of keys) result[key] = obj[key];
  return result;
}
