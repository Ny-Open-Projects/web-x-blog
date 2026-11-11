// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135096603
// LeetCode 455. 分发饼干 — Dart 版（方案2）
int findContentChildren(List<int> g, List<int> s) {
  // 定义函数/方法 findContentChildren
  final gg = List<int>.from(g)..sort(); // 把 List 小于 int 超过 .from(g). 排序 ) 存入 gg
  final ss = List<int>.from(s)
    ..sort(); // 把 List 小于 int 超过 .from(字符串). 排序 ) 存入 ss
  var child = 0, cookie = 0; // 把 0, cookie 赋值为 0 存入 子节点
  while (child < gg.length && cookie < ss.length) {
    // 循环，直到不满足「子节点 小于 gg.长度 且 cookie 小于 ss.长度」
    if (ss[cookie] >= gg[child]) child++; // 若 ss[cookie] 不低于 gg[子节点]) 子节点 加一 ;
    cookie++; // cookie 加一
  }
  return child; // 返回 子节点
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (findContentChildren([1, 2, 3], [1, 1]) != 1) throw StateError('c1');
  if (findContentChildren([1, 2], [1, 2, 3]) != 2) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
