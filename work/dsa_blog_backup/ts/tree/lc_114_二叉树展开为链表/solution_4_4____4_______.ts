// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145007192
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  interface TreeNode {
    // 定义类型
    val: number; // 值: number;
    left: TreeNode | null; // 左边界: TreeNode 按位或 null;
    right: TreeNode | null; // 右边界: TreeNode 按位或 null;
  }
  function tn(val: number): TreeNode {
    // 定义函数/方法 tn
    return { val: val, left: null, right: null }; // 返回 { 值: 值, 左边界: null, 右边界: null }
  }
  // 忠实翻译 python build_tree（层序，null 表示空缺）
  function buildTree(vals: (number | null)[]): TreeNode | null {
    // 定义函数/方法 buildTree
    if (vals.length === 0) {
      // 若 vals.长度 全等于 0
      return null; // 返回 null
    }
    const root = tn(vals[0] as number); // 把 tn(vals[0] as number) 存入 根节点
    const q: TreeNode[] = [root]; // 把 [根节点]; 写入 const q: TreeNode[]
    let i = 1; // 把 1 存入 下标 i
    while (i < vals.length) {
      // 循环，直到不满足「下标 i 小于 vals.长度」
      const node = q.shift() as TreeNode; // 把 节点.shift() as TreeNode 存入 节点
      if (vals[i] !== null) {
        // 若 vals[下标 i] 不等于 null
        node.left = tn(vals[i] as number); // 把 tn(vals[下标 i] as number); 写入 左边界
        q.push(node.left); // 把 节点.左边界 压入栈/数组尾部
      }
      i += 1; // 下标 i累加 1
      if (i < vals.length) {
        // 若 下标 i 小于 vals.长度
        if (vals[i] !== null) {
          // 若 vals[下标 i] 不等于 null
          node.right = tn(vals[i] as number); // 把 tn(vals[下标 i] as number); 写入 右边界
          q.push(node.right); // 把 节点.右边界 压入栈/数组尾部
        }
        i += 1; // 下标 i累加 1
      }
    }
    return root; // 返回 根节点
  }
  // 忠实翻译 python solution_4：原地把左子树最右节点接到当前 right 之后，清空 left，沿 right 前进
  function flatten(root: TreeNode | null): TreeNode | null {
    // 定义函数/方法 flatten
    let curr = root; // 把 根节点 存入 当前值
    while (curr !== null) {
      // 循环，直到不满足「当前值 不等于 null」
      if (curr.left !== null) {
        // 若 当前值.左边界 不等于 null
        const next = curr.left; // 把 当前值.左边界 存入 下一个
        let predecessor = next; // 把 下一个 存入 predecessor
        while (predecessor.right !== null) {
          // 循环，直到不满足「predecessor.右边界 不等于 null」
          predecessor = predecessor.right; // 把 predecessor.右边界 存入 predecessor
        }
        predecessor.right = curr.right; // 把 当前值.右边界; 写入 右边界
        curr.left = null; // 把 null; 写入 左边界
        curr.right = next; // 把 下一个; 写入 右边界
      }
      curr = curr.right; // 把 当前值.右边界 存入 当前值
    }
    return root; // 返回 根节点
  }
  function readChain(root: TreeNode | null): {
    vals: number[];
    allLeftNull: boolean;
  } {
    // 定义函数/方法 readChain
    const vals: number[] = []; // 把 []; 写入 const vals: number[]
    let allLeftNull = true; // 把 true 存入 allLeftNull
    let n = root; // 把 根节点 存入 元素个数
    while (n !== null) {
      // 循环，直到不满足「元素个数 不等于 null」
      vals.push(n.val); // 把 元素个数.值 压入栈/数组尾部
      if (n.left !== null) {
        // 若 元素个数.左边界 不等于 null
        allLeftNull = false; // 把 false 存入 allLeftNull
      }
      n = n.right; // 把 元素个数.右边界 存入 元素个数
    }
    return { vals: vals, allLeftNull: allLeftNull }; // 返回 { vals: vals, allLeftNull: allLeftNull }
  }
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) {
      // 若 数组.长度 不等于 b.长度
      return false; // 返回 false
    }
    for (let i = 0; i < a.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i] !== b[i]) {
        // 若 数组[下标 i] 不等于 b[下标 i]
        return false; // 返回 false
      }
    }
    return true; // 返回 true
  }
  const cases: { vals: (number | null)[]; want: number[] }[] = [
    { vals: [1, 2, 5, 3, 4, null, 6], want: [1, 2, 3, 4, 5, 6] },
    { vals: [7], want: [7] },
    { vals: [], want: [] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const root = buildTree(c.vals); // 把 buildTree(字符.vals) 存入 根节点
    const out = readChain(flatten(root)); // 把 readChain(flatten(根节点)) 存入 out
    if (!eqArr(out.vals, c.want) || !out.allLeftNull) {
      // 若 取反 eqArr(out.vals, 字符.want) 或 取反 out.allLeftNull
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL flatten(' +
          JSON.stringify(c.vals) +
          ')=' +
          JSON.stringify(out.vals) +
          ' want ' +
          JSON.stringify(c.want) +
          ' allLeftNull=' +
          out.allLeftNull,
      ); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
