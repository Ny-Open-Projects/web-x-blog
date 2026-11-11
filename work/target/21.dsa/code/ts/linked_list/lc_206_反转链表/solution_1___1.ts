// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function build(nums: any): ListNode | null {
    // 定义函数/方法 build
    let dummy = new ListNode(0);
    let cur = dummy; // 把 new ListNode(0); let 当前值 赋值为 哨兵节点 存入 哨兵节点
    if (nums != null)
      for (const n of nums) {
        cur.next = new ListNode(n);
        cur = cur.next;
      }
    return dummy.next;
  } // 返回 哨兵节点.下一个; }
  function toList(head: any): any {
    const r: any[] = [];
    while (head) {
      r.push(head.val);
      head = head.next;
    }
    return r;
  } // 定义函数/方法 toList
  function buildTree(vals: any): TreeNode | null {
    // 定义函数/方法 buildTree
    if (!vals || !vals.length) return null;
    const root = new TreeNode(vals[0]);
    const q: any[] = [root];
    let i = 1;
    while (q.length && i < vals.length) {
      const node = q.shift();
      if (i < vals.length && vals[i] !== null && vals[i] !== undefined) {
        node.left = new TreeNode(vals[i]);
        q.push(node.left);
      }
      i++;
      if (i < vals.length && vals[i] !== null && vals[i] !== undefined) {
        node.right = new TreeNode(vals[i]);
        q.push(node.right);
      }
      i++;
    }
    return root;
  } // 返回 根节点; }
  function toLevel(root: any): any {
    if (!root) return [];
    const r: any[] = [];
    const q: any[] = [root]; // 定义函数/方法 toLevel
    while (q.length) {
      const n = q.shift();
      if (!n) {
        r.push(null);
        continue;
      }
      r.push(n.val);
      q.push(n.left);
      q.push(n.right);
    } // 把 元素个数.值 压入栈/数组尾部
    while (r.length && r[r.length - 1] === null) r.pop();
    return r;
  }
  function eqArr(a: any, b: any): boolean {
    // 定义函数/方法 eqArr
    if (a === b) return true; // 若 数组 全等于 b，直接返回 true
    if (Array.isArray(a) && Array.isArray(b)) {
      if (a.length !== b.length) return false;
      for (let i = 0; i < a.length; i++) if (!eqArr(a[i], b[i])) return false;
      return true;
    }
    if (typeof a === 'object' && typeof b === 'object' && a && b)
      return JSON.stringify(a) === JSON.stringify(b);
    return false;
  } // 返回 false; }

  function reverseList(head: any): any {
    // 定义函数/方法 reverseList
    let p1 = head; // 把 头节点 存入 p1
    let p2 = null; // 把 null 存入 p2
    while (p1) {
      // 循环，直到不满足「p1」
      let tmp = p1.next; // 把 p1.下一个 存入 临时变量
      p1.next = p2; // 把 p2 写入 下一个
      let p2 = p1; // 把 p1 存入 p2
      let p1 = tmp; // 把 临时变量 存入 p1
    }
    console.log(p1 && p1.val, p2 && p2.val); // 打印输出
    return p2; // 返回 p2
  }

  const cases: any[] = [
    {
      inRaw: [null],
      wantRaw: null,
      ptypes: ['none'],
      rtype: 'none',
      inplace: true,
    },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const args = c.inRaw.map((v: any, i: number) => {
      const tp = c.ptypes[i]; // 把 字符.ptypes[下标 i] 存入 tp
      if (tp === 'listnode') return build(v); // 若 tp 全等于 'listnode'，直接返回 build(值)
      if (tp === 'treenode') return buildTree(v); // 若 tp 全等于 'treenode'，直接返回 buildTree(值)
      return v;
    }); // 返回 值; })
    let got: any; // let got: any;
    if (c.inplace) {
      // 若 字符.inplace
      (reverseList as any)(...args); // (reverseList as any)(...args);
      const tp = c.ptypes[0]; // 把 字符.ptypes[0] 存入 tp
      got =
        tp === 'listnode'
          ? toList(args[0])
          : tp === 'treenode'
            ? toLevel(args[0])
            : args[0];
    } else {
      // 否则
      let r = (reverseList as any)(...args); // 把 (reverseList as any)(...args) 存入 右指针
      got =
        c.rtype === 'listnode'
          ? toList(r)
          : c.rtype === 'treenode'
            ? toLevel(r)
            : r;
    }
    if (!eqArr(got, c.wantRaw)) {
      fail = true;
      console.log(
        'FAIL',
        JSON.stringify(got),
        'want',
        JSON.stringify(c.wantRaw),
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error('FAILED');
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
