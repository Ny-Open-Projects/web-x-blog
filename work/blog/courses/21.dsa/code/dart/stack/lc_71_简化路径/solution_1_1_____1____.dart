// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134368624
// LeetCode 71. 简化路径 — Dart 版（方案1）
String simplifyPath(String path) {
  // 定义函数/方法 simplifyPath
  final st = <String>[]; // 把 小于 String 超过 [] 存入 st
  for (final part in path.split('/')) {
    // for (final part in 当前路径.split(' 除以 ')) {
    if (part.isEmpty || part == '.')
      continue; // 若 part.isEmpty 或 part 等于 '.') continue;
    if (part == '..') {
      // 若 part 等于 '..'
      if (st.isNotEmpty) st.removeLast(); // 若 st.isNotEmpty) st.removeLast();
    } else {
      // 否则
      st.add(part); // st 追加 part);
    }
  }
  return st.isEmpty
      ? '/'
      : '/' + st.join('/'); // 返回 st.isEmpty ? ' 除以 ' : ' 除以 ' 加 st.join(' 除以 ')
}

void main() {
  if (simplifyPath('/home/') != '/home') throw StateError('c1');
  if (simplifyPath('/../') != '/') throw StateError('c2');
  if (simplifyPath('/home//foo/') != '/home/foo') throw StateError('c3');
  if (simplifyPath('/a/./b/../../c/') != '/c') throw StateError('c4');
  print('PASS');
}
