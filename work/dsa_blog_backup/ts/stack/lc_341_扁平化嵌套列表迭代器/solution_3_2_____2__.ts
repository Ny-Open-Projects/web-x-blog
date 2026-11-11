// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345560
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class NestedInteger {
    // 定义类型
    private _int: number | null = null; // 把 null; 写入 private _int: number | null
    private _list: NestedInteger[] | null = null; // 把 null; 写入 private _list: NestedInteger[] | null
    constructor(value?: any) {
      // constructor(value?: any) {
      if (value === undefined || value === null) {
        // 若 value 全等于 undefined 或 value 全等于 null
        this._list = []; // 把 []; 写入 this._list
      } else if (Array.isArray(value)) {
        // 否则，若 Array.isArray(value
        this._list = value.map((v: any) => new NestedInteger(v));
      } else {
        // 否则
        this._int = value; // 把 value; 写入 this._int
      }
    }
    isInteger(): boolean {
      return this._int !== null;
    } // 把 赋值为 null; } 写入 isInteger(): boolean { return this._int !
    getInteger(): number {
      return this._int as number;
    } // getInteger(): number { return this._int as number; }
    getList(): NestedInteger[] {
      return this._list as NestedInteger[];
    }
  }
  class NestedIterator {
    // 定义类型
    private stack: NestedInteger[] = []; // 把 []; 写入 private stack: NestedInteger[]
    constructor(nestedList: NestedInteger[]) {
      // constructor(nestedList: NestedInteger[]) {
      this.stack = nestedList.slice(); // 把 nestedList 截取 ); 写入 栈
    }
    hasNext(): boolean {
      // hasNext(): boolean {
      while (this.stack.length > 0) {
        // 循环，直到不满足「this.栈.长度 超过 0」
        if (this.stack[0].isInteger())
          return true; // 若 this.栈[0].isInteger()，直接返回 true
        else {
          // 否则
          const cur = this.stack[0].getList(); // 把 this.栈[0].getList() 存入 当前值
          this.stack.shift(); // 取出队首元素
          this.stack.unshift(...cur); // this.栈.unshift(...当前值);
        }
      }
      return false; // 返回 false
    }
    next(): number {
      return this.stack.shift()!.getInteger();
    } // 取出队首元素
  }
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const cases = [
    { inp: [1, [2, 3]], want: [1, 2, 3] },
    { inp: [[1], 2, [3, [4]]], want: [1, 2, 3, 4] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const nested = new NestedInteger(c.inp).getList(); // 把 new NestedInteger(字符.inp).getList() 存入 nested
    const it = new NestedIterator(nested); // 把 new NestedIterator(nested) 存入 it
    const out: number[] = []; // 把 []; 写入 const out: number[]
    while (it.hasNext()) out.push(it.next()); // 循环，直到不满足「it.hasNext()) out 追加 it.下一个());」
    if (!eqArr(out, c.want)) {
      fail = true;
      console.log('FAIL', c, 'got', out);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
