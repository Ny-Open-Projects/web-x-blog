// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135533027
// LeetCode 208. 实现 Trie (前缀树) — Dart 版（方案1）
class TrieNode {
  // 定义类型
  final Map<String, TrieNode> children =
      {}; // 把 {}; 写入 final Map<String, TrieNode> children
  bool isEnd = false; // 把 false 存入 isEnd
}

class Trie {
  // 定义类型
  final TrieNode root = TrieNode(); // 把 TrieNode(); 写入 final TrieNode root
  void insert(String word) {
    // 定义函数/方法 insert
    var node = root; // 把 根节点 存入 节点
    for (final ch in word.split('')) {
      // for (final 字符 in 单词.split('')) {
      node.children[ch] ??= TrieNode(); // 把 TrieNode(); 写入 node.children[ch] ??
      node = node.children[ch]!; // 把 节点.children[字符]取反 存入 节点
    }
    node.isEnd = true; // 把 true; 写入 node.isEnd
  }

  TrieNode? _walk(String s) {
    // TrieNode? _walk(String 字符串) {
    var node = root; // 把 根节点 存入 节点
    for (final ch in s.split('')) {
      // for (final 字符 in 字符串.split('')) {
      final next = node.children[ch]; // 把 节点.children[字符] 存入 下一个
      if (next == null) return null; // 若 下一个 等于 null，直接返回 null
      node = next; // 把 下一个 存入 节点
    }
    return node; // 返回 节点
  }

  bool search(String word) {
    // 定义函数/方法 search
    final n = _walk(word); // 把 _walk(单词) 存入 元素个数
    return n != null && n.isEnd; // 返回 元素个数 不等于 null 且 元素个数.isEnd
  }

  bool startsWith(String prefix) => _walk(prefix) != null;
}

void main() {
  // 程序入口：跑内嵌自测用例
  final t = Trie(); // 把 Trie() 存入 另一字符串
  t.insert('apple'); // 另一字符串 插入 'apple');
  if (!t.search('apple'))
    throw StateError(
      'c1',
    ); // 若 取反 另一字符串.search('apple')) throw StateError('c1');
  if (t.search('app'))
    throw StateError('c2'); // 若 另一字符串.search('app')) throw StateError('c2');
  if (!t.startsWith('app'))
    throw StateError(
      'c3',
    ); // 若 取反 另一字符串.startsWith('app')) throw StateError('c3');
  if (t.search('appl'))
    throw StateError('c4'); // 若 另一字符串.search('appl')) throw StateError('c4');
  print('PASS'); // 全部用例通过，输出 PASS
}
