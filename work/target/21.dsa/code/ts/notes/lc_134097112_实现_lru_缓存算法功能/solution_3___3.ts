// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class LRUCache {
    // 定义类型
    length: number;
    data: Map<number, number>; // 长度:number; data:Map 小于 number,number 超过 ;
    constructor(length: number) {
      this.length = length;
      this.data = new Map();
    } // 把 长度; this.data 赋值为 new Map(); } 写入 长度
    set(key: number, value: number) {
      // set(key:number,value:number){
      if (this.data.has(key)) this.data.delete(key); // 若 this.data.has(key)) this.data.delete(key);
      this.data.set(key, value); // this.data.set(key,value);
      if (this.data.size > this.length) {
        // 若 this.data.大小 超过 this.长度
        const k = this.data.keys().next().value; // 把 this.data.keys().下一个().value 存入 下标 k
        this.data.delete(k); // this.data.delete(下标 k);
      }
    }
    get(key: number): number | null {
      // get(key:number):number 按位或 null{
      if (!this.data.has(key)) return null; // 若 取反 this.data.has(key)，直接返回 null
      const v = this.data.get(key)!; // 把 this.data 查找 key)取反 存入 值
      this.data.delete(key);
      this.data.set(key, v); // this.data.delete(key); this.data.set(key,值);
      return v; // 返回 值
    }
  }
  const c = new LRUCache(2); // 把 new LRUCache(2) 存入 字符
  let fail = false; // 把 false 存入 fail
  c.set(1, 1);
  c.set(2, 2); // 字符.set(1,1); 字符.set(2,2);
  if (c.get(1) !== 1) {
    fail = true;
    console.log('FAIL1');
  } // 若 字符 查找 1) 不等于 1){fail 赋值为 true;输出(「FAIL1」);}
  c.set(3, 3); // 字符.set(3,3);
  if (c.get(2) !== null) {
    fail = true;
    console.log('FAIL2');
  } // 若 字符 查找 2) 不等于 null){fail 赋值为 true;输出(「FAIL2」);}
  c.set(4, 4); // 字符.set(4,4);
  if (c.get(1) !== null) {
    fail = true;
    console.log('FAIL3');
  } // 若 字符 查找 1) 不等于 null){fail 赋值为 true;输出(「FAIL3」);}
  if (c.get(3) !== 3) {
    fail = true;
    console.log('FAIL4');
  } // 若 字符 查找 3) 不等于 3){fail 赋值为 true;输出(「FAIL4」);}
  if (c.get(4) !== 4) {
    fail = true;
    console.log('FAIL5');
  } // 若 字符 查找 4) 不等于 4){fail 赋值为 true;输出(「FAIL5」);}
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
