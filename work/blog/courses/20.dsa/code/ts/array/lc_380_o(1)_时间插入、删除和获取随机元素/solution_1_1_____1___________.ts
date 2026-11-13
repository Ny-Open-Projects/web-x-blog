// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345735
/**
 ** LeetCode 380. O(1) 时间插入、删除和获取随机元素
 ** 方案1: 变长数组 + 哈希表
 */

class RandomizedSet {
  // 定义类型
  private vals: number[]; // private vals: number[];
  private valMap: Map<number, number>; // private valMap: Map 小于 number, number 超过 ;

  constructor() {
    // constructor() {
    this.vals = []; // 把 []; 写入 this.vals
    this.valMap = new Map(); // 把 new Map(); 写入 this.valMap
  }

  insert(val: number): boolean {
    // insert(值: number): boolean {
    if (this.valMap.has(val)) return false; // 若 this.valMap.has(值)，直接返回 false
    this.valMap.set(val, this.vals.length); // this.valMap.set(值, this.vals.长度);
    this.vals.push(val); // 把 值 压入栈/数组尾部
    return true; // 返回 true
  }

  remove(val: number): boolean {
    // remove(值: number): boolean {
    if (!this.valMap.has(val)) return false; // 若 取反 this.valMap.has(值)，直接返回 false
    const idx = this.valMap.get(val)!; // 把 this.valMap 查找 值)取反 存入 idx
    const last = this.vals[this.vals.length - 1]; // 把 this.vals[this.vals.长度 减 1] 存入 last
    this.vals[idx] = last; // 把 last; 写入 this.vals[idx]
    this.valMap.set(last, idx); // this.valMap.set(last, idx);
    this.vals.pop(); // 弹出栈顶元素
    this.valMap.delete(val); // this.valMap.delete(值);
    return true; // 返回 true
  }

  getRandom(): number {
    // getRandom(): number {
    return this.vals[Math.floor(Math.random() * this.vals.length)]; // 返回 this.vals[向下取整(Math.random() 乘 this.vals.长度)]
  }
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  let fail = false; // 把 false 存入 fail
  const rs = new RandomizedSet(); // 把 new RandomizedSet() 存入 rs
  if (rs.insert(1) !== true) {
    fail = true;
    console.log('FAIL insert(1) should be true');
  }
  if (rs.remove(2) !== false) {
    fail = true;
    console.log('FAIL remove(2) should be false');
  }
  if (rs.insert(2) !== true) {
    fail = true;
    console.log('FAIL insert(2) should be true');
  }
  const r1 = rs.getRandom(); // 把 rs.getRandom() 存入 r1
  if (r1 !== 1 && r1 !== 2) {
    fail = true;
    console.log('FAIL getRandom=' + r1 + ' not in {1,2}');
  }
  if (rs.remove(1) !== true) {
    fail = true;
    console.log('FAIL remove(1) should be true');
  }
  if (rs.insert(2) !== false) {
    fail = true;
    console.log('FAIL insert(2) again should be false');
  }
  const r2 = rs.getRandom(); // 把 rs.getRandom() 存入 r2
  if (r2 !== 2) {
    fail = true;
    console.log('FAIL getRandom=' + r2 + ' want 2');
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
