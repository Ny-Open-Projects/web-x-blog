// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513247
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class ListNode {
    val: number;
    next: ListNode | null;
    constructor(v: number, n: ListNode | null = null) {
      this.val = v;
      this.next = n;
    }
  } // 定义类型
  function build(vals: number[]): ListNode | null {
    // 定义函数/方法 build
    const d = new ListNode(0);
    let cur = d; // 把 new ListNode(0); let 当前值 赋值为 d 存入 d
    for (const v of vals) {
      cur.next = new ListNode(v);
      cur = cur.next;
    } // 把 new ListNode(值); 当前值 赋值为 当前值.下一个; } 写入 下一个
    return d.next; // 返回 d.下一个
  }
  function toStr(head: ListNode | null): string {
    // 定义函数/方法 toStr
    const parts: string[] = []; // 把 []; 写入 const parts:string[]
    while (head) {
      parts.push(String(head.val));
      head = head.next;
    } // 循环，直到不满足「头节点){ parts 追加 String(头节点.值)); 头节点 赋值为 头节点.下一个; }」
    return parts.join('->'); // 返回 parts.join(「 减 超过 」)
  }
  function addTwoNumbers(
    l1: ListNode | null,
    l2: ListNode | null,
  ): ListNode | null {
    // 定义函数/方法 addTwoNumbers
    const d = new ListNode(0);
    let cur = d;
    let carry = 0; // 把 new ListNode(0); let 当前值 赋值为 d; let carry 赋值为 0 存入 d
    while (l1 || l2) {
      // 循环，直到不满足「l1 或 l2」
      const v1 = l1 ? l1.val : 0,
        v2 = l2 ? l2.val : 0; // 把 l1?l1.值:0, v2 赋值为 l2?l2.值:0 存入 v1
      const total = v1 + v2 + carry;
      carry = Math.floor(total / 10); // 把 v1 加 v2 加 carry; carry 赋值为 向下取整(总和 除以 10) 存入 总和
      cur.next = new ListNode(total % 10);
      cur = cur.next; // 把 new ListNode(总和 对…取模 10); 当前值 赋值为 当前值.下一个; 写入 下一个
      if (l1) l1 = l1.next;
      if (l2) l2 = l2.next; // 若 l1) l1 赋值为 l1.下一个; if(l2) l2 赋值为 l2.下一个;
    }
    if (carry) cur.next = new ListNode(carry); // 若 carry) 当前值.下一个 赋值为 new ListNode(carry);
    return d.next; // 返回 d.下一个
  }
  let fail = false; // 把 false 存入 fail
  if (toStr(addTwoNumbers(build([2, 4, 3]), build([5, 6, 4]))) !== '7->0->8') {
    fail = true;
    console.log('FAIL1');
  }
  if (toStr(addTwoNumbers(build([0]), build([0]))) !== '0') {
    fail = true;
    console.log('FAIL2');
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
