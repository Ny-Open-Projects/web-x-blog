/**
 * 根据传入的字符串计算值
 * @param str 传入的字符串
 * @returns 计算后的值
 */
export function calcValueByString(str: string) {
  let value
  if (/^\d+$/.test(str))
    value = Number(str)
  else if (['true', 'false'].includes(str))
    value = str === 'true'

  return value ?? str
}

/**
 * 根据输入的字符串计算数据类型
 * @param str 输入的字符串
 * @returns 数据类型(string, boolean, number)
 */
export function calcTypeByString(str: string) {
  if (/^\d+$/.test(str))
    return 'number'
  else if (['true', 'false'].includes(str))
    return 'boolean'

  return 'string'
}
