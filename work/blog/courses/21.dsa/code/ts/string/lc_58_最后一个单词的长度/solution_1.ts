/**
 ** LeetCode 58. 最后一个单词的长度
 ** 方案：1 ) 方案1：从尾部扫描
 */

// 忠实翻译 Python 参考实现 ref_lengthOfLastWord：len(s.split()[-1]) if s.split() else 0
function lengthOfLastWord(s: string): number {
  // 定义函数/方法 lengthOfLastWord
  const trimmed = s.trim(); // 把 字符串.trim() 存入 trimmed
  if (trimmed === '') {
    // 若 trimmed 全等于 「」
    return 0; // 返回 0
  }
  const parts = trimmed.split(/\s+/); // 把 trimmed.split( 除以 \字符串 加 除以 ) 存入 parts
  return parts[parts.length - 1].length; // 返回 parts[parts.长度 减 1].长度
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 用例来自 _tools/correctness_check.py PROBLEMS["lc_58_最后一个单词的长度"]
  const cases: [string, number][] = [
    ['Hello World', 5],
    ['   fly me   to   the moon  ', 4],
    ['luffy is still joyboy', 6],
  ];
  for (const [input, want] of cases) {
    // for (const [input, want] of cases) {
    const got = lengthOfLastWord(input); // 把 lengthOfLastWord(input) 存入 got
    if (got !== want) {
      // 若 got 不等于 want
      throw new Error(
        `FAIL lengthOfLastWord(${JSON.stringify(input)}) = ${got}, want ${want}`,
      );
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
