// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096059
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class ListNode {
    // 定义类型
    val: number; // 值: number;
    next: ListNode | null; // 下一个: ListNode 按位或 null;
    constructor(v: number, next: ListNode | null = null) {
      this.val = v;
      this.next = next;
    }
  }
  function build(a: number[]): ListNode | null {
    // 定义函数/方法 build
    let head: ListNode | null = null; // 把 null; 写入 let head: ListNode | null
    for (let i = a.length - 1; i >= 0; i--) head = new ListNode(a[i], head); // 让 下标 i 从 数组.长度 减 1 开始计数，下标 i 不低于 0 就继续
    return head; // 返回 头节点
  }
  function isPalindrome(head: ListNode | null): boolean {
    // 定义判定函数 isPalindrome
    const vals: number[] = []; // 把 []; 写入 const vals: number[]
    let p = head; // 把 头节点 存入 节点
    while (p) {
      vals.push(p.val);
      p = p.next;
    } // 循环，直到不满足「节点) { vals 追加 节点.值); 节点 赋值为 节点.下一个; }」
    let left = 0,
      right = vals.length - 1; // 把 0, 右边界 赋值为 vals.长度 减 1 存入 左边界
    while (left < right) {
      // 循环，直到不满足「左边界 小于 右边界」
      if (vals[left] !== vals[right]) return false; // 若 vals[左边界] 不等于 vals[右边界]，直接返回 false
      left++;
      right--; // 左边界 加一 ; 右边界 减一 ;
    }
    return true; // 返回 true
  }
  const cases: [number[] | null, boolean][] = [
    [null, true],
    [[1, 2, 2, 1], true],
    [[1, 2], false],
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const inp = c[0]; // 把 字符[0] 存入 inp
    const want = c[1]; // 把 字符[1] 存入 want
    const got = isPalindrome(inp === null ? null : build(inp)); // 把 isPalindrome(inp 全等于 null ? null : build(inp)) 存入 got
    if (got !== want) {
      fail = true;
      console.log(
        'FAIL isPalindrome(' +
          JSON.stringify(inp) +
          ')=' +
          got +
          ' want ' +
          want,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
