// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
// LCP 117. 填充每个节点的下一个右侧节点指针 II — 方案3：已建立的 next 链做层序遍历（O(1) 额外空间）
class Nd {
  val: number;
  left: any;
  right: any;
  next: any;
  constructor(v: number) {
    this.val = v;
    this.left = null;
    this.right = null;
    this.next = null;
  }
}
function buildTree(vals: (number | null)[]): Nd | null {
  // 层序数组建树
  if (!vals.length || vals[0] === null) return null;
  const root = new Nd(vals[0]);
  const q: Nd[] = [root];
  let i = 1;
  while (q.length && i < vals.length) {
    const node = q.shift()!;
    if (i < vals.length && vals[i] !== null) {
      node.left = new Nd(vals[i] as number);
      q.push(node.left);
    }
    i++;
    if (i < vals.length && vals[i] !== null) {
      node.right = new Nd(vals[i] as number);
      q.push(node.right);
    }
    i++;
  }
  return root;
}
function connect(root: Nd | null): Nd | null {
  // 用上一层的 next 链串起下一层
  let head = root;
  while (head) {
    const dummy = new Nd(0);
    let tail = dummy;
    for (let p = head; p; p = p.next) {
      // 沿 next 链遍历当前层
      if (p.left) {
        tail.next = p.left;
        tail = tail.next;
      }
      if (p.right) {
        tail.next = p.right;
        tail = tail.next;
      }
    }
    head = dummy.next; // 下一层的头
  }
  return root;
}
function levelsByNext(root: Nd | null): number[][] {
  // 按 next 链读出各层
  const res: number[][] = [];
  let head = root;
  while (head) {
    const lvl: number[] = [];
    let firstChild: Nd | null = null;
    let tail: Nd | null = null;
    for (let p = head; p; p = p.next) {
      lvl.push(p.val);
      for (const ch of [p.left, p.right]) {
        if (ch) {
          if (tail) {
            tail.next = ch;
          } else {
            firstChild = ch;
          }
          tail = ch;
        }
      }
    }
    res.push(lvl);
    head = firstChild;
  }
  return res;
}
export function demo(): void {
  const root = buildTree([1, 2, 3, 4, 5, null, 7]);
  connect(root);
  const want = [[1], [2, 3], [4, 5, 7]];
  const got = levelsByNext(root);
  if (JSON.stringify(got) !== JSON.stringify(want)) {
    throw new Error('FAILED ' + JSON.stringify(got));
  }
  console.log('PASS');
}
demo();
