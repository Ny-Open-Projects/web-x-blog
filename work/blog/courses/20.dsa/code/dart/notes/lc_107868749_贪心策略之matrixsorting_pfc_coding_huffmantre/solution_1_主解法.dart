// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749
// LeetCode 107868749. 贪心策略 — Dart 版（贪心策略之 matrixSort / PFC 编码 / Huffman 树）
void matrixSort(List<List<int>> matrix) {
  // 定义函数/方法 matrixSort
  final rows = matrix.length,
      cols = matrix[0].length; // 把 矩阵.长度, 列数 赋值为 矩阵[0].长度 存入 行数
  for (var c = 0; c < cols; c++) {
    // 让 字符 从 0 开始计数，字符 小于 列数 就继续
    final col = <int>[for (final r in matrix) r[c]]
      ..sort(); // 把 小于 int 超过 [for (final 右指针 in 矩阵) 右指针[字符]]. 排序 ) 存入 col
    for (var r = 0; r < rows; r++) {
      // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
      matrix[r][c] = col[r]; // 把 col[右指针]; 写入 matrix[r][c]
    }
  }
  for (var r = 0; r < rows; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
    matrix[r].sort(); // 排序
  }
}

class Huff {
  // 定义类型
  int freq; // int 频次表;
  String? sym; // String? sym;
  Huff? left, right; // Huff? 左边界, 右边界;
  bool get isLeaf => sym != null;
  Huff.leaf(this.freq, this.sym); // Huff.leaf(this.频次表, this.sym);
  Huff.internal(
    this.freq,
    this.left,
    this.right,
  ); // Huff.internal(this.频次表, this.左边界, this.右边界);
}

Huff buildHuffman(Map<String, int> freqs) {
  // 定义函数/方法 buildHuffman
  var nodes = <Huff>[for (final e in freqs.entries) Huff.leaf(e.value, e.key)]
    ..sort((a, b) => a.freq.compareTo(b.freq));
  while (nodes.length > 1) {
    // 循环，直到不满足「nodes.长度 超过 1」
    final a = nodes.removeAt(0); // 把 nodes.removeAt(0) 存入 数组
    final b = nodes.removeAt(0); // 把 nodes.removeAt(0) 存入 b
    final merged = Huff.internal(
      a.freq + b.freq,
      a,
      b,
    ); // 把 Huff.internal(数组.频次表 加 b.频次表, 数组, b) 存入 merged
    var i = 0; // 把 0 存入 下标 i
    while (i < nodes.length && nodes[i].freq < merged.freq) {
      // 循环，直到不满足「下标 i 小于 nodes.长度 且 nodes[下标 i].频次表 小于 merged.频次表」
      i++; // 下标 i 加一
    }
    nodes.insert(i, merged); // nodes 插入 下标 i, merged);
  }
  return nodes[0]; // 返回 nodes[0]
}

Map<String, String> huffmanCodes(Map<String, int> freqs) {
  final root = buildHuffman(freqs); // 把 buildHuffman(freqs) 存入 根节点
  final codes = <String, String>{}; // 把 小于 String, String 超过 {} 存入 codes
  void walk(Huff node, String prefix) {
    // 定义函数/方法 walk
    if (node.isLeaf) {
      // 若 节点.isLeaf
      codes[node.sym!] = prefix.isEmpty
          ? '0'
          : prefix; // 把 prefix.isEmpty ? '0' : prefix; 写入 codes[node.sym!]
    } else {
      // 否则
      walk(node.left!, prefix + '0'); // walk(节点.左边界取反 , prefix 加 '0');
      walk(node.right!, prefix + '1'); // walk(节点.右边界取反 , prefix 加 '1');
    }
  }

  walk(root, ''); // walk(根节点, '');
  return codes; // 返回 codes
}

void main() {
  // 程序入口：跑内嵌自测用例
  final freqs = <String, int>{
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45,
  };

  // case1: matrixSort
  final mat = <List<int>>[
    [5, 3, 4],
    [1, 6, 2],
    [7, 9, 8],
  ];
  matrixSort(mat); // matrixSort(mat);
  if (mat.toString() != '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]') {
    // 若 mat.toString() 不等于 '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]'
    throw StateError(
      'matrixSort mismatch',
    ); // throw StateError('matrixSort mismatch');
  }

  // case2: WPL
  final codes = huffmanCodes(freqs); // 把 huffmanCodes(freqs) 存入 codes
  var wpl = 0; // 把 0 存入 wpl
  final codeList = <String>[]; // 把 小于 String 超过 [] 存入 codeList
  freqs.forEach((sym, f) {
    // freqs.forEach((sym, f) {
    final c = codes[sym]!; // 把 codes[sym]取反 存入 字符
    wpl += f * c.length; // wpl累加 f 乘 字符.长度
    codeList.add(c); // codeList 追加 字符);
  }); // });
  if (wpl != 224)
    throw StateError(
      'WPL mismatch: $wpl',
    ); // 若 wpl 不等于 224) throw StateError('WPL mismatch: $wpl');

  // case3: 前缀无关
  var prefixFree = true; // 把 true 存入 prefixFree
  for (var i = 0; i < codeList.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 codeList.长度 就继续
    for (var j = 0; j < codeList.length; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 codeList.长度 就继续
      if (i != j && codeList[j].startsWith(codeList[i])) prefixFree = false;
    }
  }
  if (!prefixFree)
    throw StateError(
      'not prefix-free',
    ); // 若 取反 prefixFree) throw StateError('not prefix 减 free');

  print('PASS'); // 全部用例通过，输出 PASS
}
