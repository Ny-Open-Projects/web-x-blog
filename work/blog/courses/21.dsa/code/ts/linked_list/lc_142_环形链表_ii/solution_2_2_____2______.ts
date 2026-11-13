// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094299
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class ListNode {
    val: number;
    next: ListNode | null;
    constructor(v = 0, n: ListNode | null = null) {
      this.val = v;
      this.next = n;
    }
  } // 定义类型
  function hasCycleAt(head: ListNode | null): number {
    // 定义函数/方法 hasCycleAt
    let slow: ListNode | null = head,
      fast: ListNode | null = head;
    let has = false; // 把 false 存入 has
    while (fast && fast.next) {
      slow = slow!.next;
      fast = fast.next.next;
      if (slow === fast) {
        has = true;
        break;
      }
    }
    if (!has) return -1; // 若 取反 has，直接返回 减 1
    slow = head;
    while (slow !== fast) {
      slow = slow!.next;
      fast = fast!.next;
    }
    let idx = 0;
    let cur = head;
    while (cur !== slow) {
      cur = cur!.next;
      idx++;
    }
    return idx; // 返回 idx
  }
  // acyclic
  const a = new ListNode(1);
  a.next = new ListNode(2);
  a.next.next = new ListNode(3);
  if (hasCycleAt(a) !== -1) {
    console.log('FAIL acyclic');
    throw new Error('FAILED');
  }
  // cycle at index 1 (value 2)
  const b = new ListNode(3);
  b.next = new ListNode(2);
  b.next.next = new ListNode(0);
  b.next.next.next = b.next;
  if (hasCycleAt(b) !== 1) {
    console.log('FAIL cycle got ' + hasCycleAt(b));
    throw new Error('FAILED');
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
