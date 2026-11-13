// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138684407
// LeetCode 649. Dota2参议院 — Dart 版（方案2）
String predictPartyVictory(String senate) {
  // 定义函数/方法 predictPartyVictory
  final n = senate.length; // 把 senate.长度 存入 元素个数
  final radiant = <int>[]; // 把 小于 int 超过 [] 存入 radiant
  final dire = <int>[]; // 把 小于 int 超过 [] 存入 dire
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    if (senate[i] == 'R') {
      // 若 senate[下标 i] 等于 'R'
      radiant.add(i); // radiant 追加 下标 i);
    } else {
      // 否则
      dire.add(i); // dire 追加 下标 i);
    }
  }
  var rh = 0, dh = 0; // 把 0, dh 赋值为 0 存入 rh
  while (rh < radiant.length && dh < dire.length) {
    // 循环，直到不满足「rh 小于 radiant.长度 且 dh 小于 dire.长度」
    final r = radiant[rh++]; // 把 radiant[rh 加一 ] 存入 右指针
    final d = dire[dh++]; // 把 dire[dh 加一 ] 存入 d
    if (r < d) {
      // 若 右指针 小于 d
      radiant.add(r + n); // radiant 追加 右指针 加 元素个数);
    } else {
      // 否则
      dire.add(d + n); // dire 追加 d 加 元素个数);
    }
  }
  return rh >= radiant.length
      ? 'Dire'
      : 'Radiant'; // 返回 rh 不低于 radiant.长度 ? 'Dire' : 'Radiant'
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (predictPartyVictory('RD') != 'Radiant') throw StateError('c1');
  if (predictPartyVictory('DDR') != 'Dire') throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
