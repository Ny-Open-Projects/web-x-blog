/**
 ** LeetCode 2166. 设计位集
 ** 方案：2 ) 方案2：按字存储实现
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145370422
 */

export class Bitset {
  // export class Bitset {
  private n: number; // private 元素个数: number;
  private words: number[]; // private 单词列表: number[];
  private ones: number; // private ones: number;
  private reverse: number; // private reverse: number;
  constructor(size: number) {
    // constructor(大小: number) {
    this.n = size; // 把 大小; 写入 元素个数
    this.words = new Array(Math.floor((size + 31) / 32)).fill(0); // 把 new Array(向下取整((大小 加 31) 除以 32)).fill(0); 写入 单词列表
    this.ones = 0; // 把 0; 写入 this.ones
    this.reverse = 0; // 把 0; 写入 this.reverse
  }
  private realFlag(idx: number): number {
    // private realFlag(idx: number): number {
    const index = Math.floor(idx / 32); // 把 向下取整(idx 除以 32) 存入 index
    const bit = idx % 32; // 把 idx 对…取模 32 存入 bit
    return ((this.words[index] >> bit) & 1) ^ this.reverse; // 返回 ((this.单词列表[index] 超过 超过 bit) 按位与 1) 按位异或 this.reverse
  }
  private setFlag(idx: number, v: number): void {
    // private setFlag(idx: number, 值: number): void {
    const index = Math.floor(idx / 32); // 把 向下取整(idx 除以 32) 存入 index
    const bit = idx % 32; // 把 idx 对…取模 32 存入 bit
    const old = this.realFlag(idx); // 把 this.realFlag(idx) 存入 old
    if (old !== v) {
      // 若 old 不等于 值
      this.ones += v - old; // this.ones累加 (值 减 old)
      const physical = v ^ this.reverse; // 把 值 按位异或 this.reverse 存入 physical
      if (physical === 1)
        this.words[index] |= 1 << bit; // 若 physical 全等于 1) this.单词列表[index] 按位或 赋值为 (1 小于 小于 bit);
      else this.words[index] &= ~(1 << bit); // 否则
    }
  }
  fix(idx: number): void {
    this.setFlag(idx, 1);
  } // fix(idx: number): void { this.setFlag(idx, 1); }
  unfix(idx: number): void {
    this.setFlag(idx, 0);
  } // unfix(idx: number): void { this.setFlag(idx, 0); }
  flip(): void {
    this.reverse ^= 1;
    this.ones = this.n - this.ones;
  }
  all(): boolean {
    return this.ones === this.n;
  } // 把 等于 this.元素个数; } 写入 all(): boolean { return this.ones
  one(): boolean {
    return this.ones > 0;
  } // one(): boolean { return this.ones 超过 0; }
  count(): number {
    return this.ones;
  } // 计数(): number { return this.ones; }
  toString(): string {
    // toString(): string {
    let s = ''; // 把 「」 存入 字符串
    for (let i = 0; i < this.n; i++) s += this.realFlag(i).toString(); // 让 下标 i 从 0 开始计数，下标 i 小于 this.元素个数 就继续
    return s; // 返回 字符串
  }
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const bs = new Bitset(5); // 把 new Bitset(5) 存入 bs
  bs.fix(0); // bs.fix(0);
  bs.fix(3); // bs.fix(3);
  if (bs.toString() !== '10010')
    throw new Error('FAILED toString1: ' + bs.toString());
  if (bs.count() !== 2) throw new Error('FAILED count1'); // 若 bs.计数() 不等于 2) throw new Error(「FAILED count1」);
  bs.flip(); // bs.flip();
  if (bs.toString() !== '01101')
    throw new Error('FAILED toString2: ' + bs.toString());
  if (bs.count() !== 3) throw new Error('FAILED count2'); // 若 bs.计数() 不等于 3) throw new Error(「FAILED count2」);
  bs.unfix(0); // bs.unfix(0);
  if (bs.toString() !== '01101')
    throw new Error('FAILED toString3: ' + bs.toString());
  if (bs.all() || !bs.one()) throw new Error('FAILED all/one');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
