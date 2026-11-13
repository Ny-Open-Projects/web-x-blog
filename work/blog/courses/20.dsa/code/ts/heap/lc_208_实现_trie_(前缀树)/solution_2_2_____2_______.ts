// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145248170

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual); // 把 JSON.stringify(actual) 存入 数组
  const e = JSON.stringify(expected); // 把 JSON.stringify(expected) 存入 e
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class Trie {
  // 定义类型
  root: Record<string, any>; // 根节点: Record 小于 string, any 超过 ;
  constructor() {
    this.root = {};
  } // 把 {}; } 写入 根节点
  insert(word: string): void {
    // insert(单词: string): void {
    let node = this.root; // 把 this.根节点 存入 节点
    for (const ch of word) {
      // for (const 字符 of 单词) {
      if (!(ch in node)) node[ch] = {}; // 若 取反 (字符 in 节点)) 节点[字符] 赋值为 {};
      node = node[ch]; // 把 节点[字符] 存入 节点
    }
    node['end'] = true; // 把 true; 写入 node['end']
  }
  search(word: string): boolean {
    // search(单词: string): boolean {
    const node = this.startsWith(word); // 把 this.startsWith(单词) 存入 节点
    return node !== false && 'end' in node && node['end'] === true; // 返回 节点 不等于 false 且 '终点' in 节点 且 节点['终点'] 全等于 true
  }
  startsWith(prefix: string): any {
    // startsWith(prefix: string): any {
    let node = this.root; // 把 this.根节点 存入 节点
    for (const ch of prefix) {
      // for (const 字符 of prefix) {
      if (!(ch in node)) return false; // 若 取反 (字符 in 节点)，直接返回 false
      node = node[ch]; // 把 节点[字符] 存入 节点
    }
    return node; // 返回 节点
  }
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const trie = new Trie(); // 把 new Trie() 存入 trie
  trie.insert('apple'); // trie 插入 「apple」);
  assertEq(trie.search('apple'), true, 'search apple'); // 断言校验
  assertEq(trie.search('app'), false, 'search app'); // 断言校验
  assertEq(
    trie.startsWith('app'),
    { l: { e: { end: true } } },
    'startsWith app',
  ); // 断言校验
  trie.insert('app'); // trie 插入 「app」);
  assertEq(trie.search('app'), true, 'search app after insert'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
