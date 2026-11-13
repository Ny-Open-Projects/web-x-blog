// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133772625
// LeetCode 131. 分割回文串 — Rust 版（方案1）
fn is_pal(s: &[char]) -> bool {
    // 定义判定函数 is_pal
    let (mut i, mut j) = (0usize, s.len() - 1); // 把 (0usize, 字符串.长度() 减 1); 写入 let (mut i, mut j)
    while i < j {
        // while 下标 i 小于 下标 j {
        if s[i] != s[j] {
            return false;
        } // 若 字符串[下标 i] 不等于 字符串[下标 j] { return false; }
        i += 1; // 下标 i累加 1
        j -= 1; // 下标 j累减 1
    }
    true // true
}
fn partition(s: &str) -> Vec<Vec<String>> {
    // 定义函数/方法 partition
    let chars: Vec<char> = s.chars().collect(); // 把 字符串.chars().collect(); 写入 let chars: Vec<char>
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    let mut path: Vec<String> = Vec::new(); // 把 Vec::new(); 写入 let mut path: Vec<String>
    fn dfs(chars: &[char], start: usize, path: &mut Vec<String>, res: &mut Vec<Vec<String>>) {
        // 定义函数/方法 dfs
        if start == chars.len() {
            res.push(path.clone());
            return;
        } // 若 起点 等于 chars.长度() { 结果 追加 当前路径.clone()); return; }
        for end in start + 1..=chars.len() {
            // 逐个取出 起点 的元素（终点）
            if is_pal(&chars[start..end]) {
                // 定义判定函数 is_pal
                path.push(chars[start..end].iter().collect()); // 把 chars[起点..终点].iter( 压入栈/数组尾部
                dfs(chars, end, path, res); // dfs(chars, 终点, 当前路径, 结果);
                path.pop(); // 弹出栈顶元素
            }
        }
    }
    dfs(&chars, 0, &mut path, &mut res); // dfs( 按位与 chars, 0, 按位与 mut 当前路径, 按位与 mut 结果);
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = partition("aab"); // 把 partition(「aab」) 存入 got
    let want = vec![
        vec!["a".to_string(), "a".to_string(), "b".to_string()],
        vec!["aa".to_string(), "b".to_string()],
    ];
    assert_eq!(got, want); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
