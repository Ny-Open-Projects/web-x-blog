// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function reverseWords(s: string): string {
    // 定义函数/方法 reverseWords
    return s
      .split(' ')
      .map((w) => w.split('').reverse().join(''))
      .join(' ');
  }
  let fail = false; // 把 false 存入 fail
  if (
    reverseWords("Let's take LeetCode contest") !==
    "s'teL ekat edoCteeL tsetnoc"
  ) {
    fail = true;
    console.log('FAIL1');
  }
  if (reverseWords('God Ding') !== 'doG gniD') {
    fail = true;
    console.log('FAIL2');
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
