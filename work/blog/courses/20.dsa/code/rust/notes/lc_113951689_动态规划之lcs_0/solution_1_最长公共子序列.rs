// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
// LeetCode 113951689. 动态规划之 LCS — Rust 版（最长公共子序列：DP 填表 + 回溯构造）

fn lcs_table(a: &str, b: &str) -> Vec<Vec<usize>> {
    // 定义函数/方法 lcs_table
    let ab = a.as_bytes(); // 把 数组.as_bytes() 存入 ab
    let bb = b.as_bytes(); // 把 b.as_bytes() 存入 bb
    let (m, n) = (ab.len(), bb.len()); // 把 (ab.长度(), bb.长度()); 写入 let (m, n)
    let mut dp = vec![vec![0usize; n + 1]; m + 1]; // 把 vec取反 [vec取反 [0usize; 元素个数 加 1]; 映射表 加 1]; 写入 let mut dp
    for i in 1..=m {
        // 逐个取出 1 的元素（下标 i）
        for j in 1..=n {
            // 逐个取出 1 的元素（下标 j）
            dp[i][j] = if ab[i - 1] == bb[j - 1] {
                // 把 if ab[下标 i 减 1] 等于 bb[下标 j 减 1] { 写入 dp[i][j]
                dp[i - 1][j - 1] + 1 // DP 表[下标 i 减 1][下标 j 减 1] 加 1
            } else {
                // 否则
                dp[i - 1][j].max(dp[i][j - 1]) // DP 表[下标 i 减 1][下标 j].取较大值 DP 表[下标 i][下标 j 减 1])
            };
        }
    }
    dp // DP 表
}

fn lcs_length(a: &str, b: &str) -> usize {
    // 定义函数/方法 lcs_length
    let dp = lcs_table(a, b); // 把 lcs_table(数组, b) 存入 DP 表
    dp[a.len()][b.len()] // DP 表[数组.长度()][b.长度()]
}

fn lcs_string(a: &str, b: &str) -> String {
    // 定义函数/方法 lcs_string
    let ab = a.as_bytes(); // 把 数组.as_bytes() 存入 ab
    let bb = b.as_bytes(); // 把 b.as_bytes() 存入 bb
    let dp = lcs_table(a, b); // 把 lcs_table(数组, b) 存入 DP 表
    let (mut i, mut j) = (ab.len(), bb.len()); // 把 (ab.长度(), bb.长度()); 写入 let (mut i, mut j)
    let mut out = Vec::with_capacity(dp[i][j]); // 把 Vec::with_capacity(DP 表[下标 i][下标 j]); 写入 let mut out
    while i > 0 && j > 0 {
        // while 下标 i 超过 0 且 下标 j 超过 0 {
        if ab[i - 1] == bb[j - 1] {
            // 若 ab[下标 i 减 1] 等于 bb[下标 j 减 1]
            out.push(ab[i - 1]); // 把 ab[下标 i 减 1] 压入栈/数组尾部
            i -= 1; // 下标 i累减 1
            j -= 1; // 下标 j累减 1
        } else if dp[i - 1][j] >= dp[i][j - 1] {
            // 否则，若 DP 表[下标 i 减 1][下标 j] 不低于 DP 表[下标 i][下标 j 减 1]
            i -= 1; // 下标 i累减 1
        } else {
            // 否则
            j -= 1; // 下标 j累减 1
        }
    }
    out.reverse(); // 反转
    String::from_utf8(out).unwrap() // String::from_utf8(out).unwrap()
}

fn is_common_sub(a: &str, b: &str, s: &str) -> bool {
    // 定义判定函数 is_common_sub
    let ab = a.as_bytes(); // 把 数组.as_bytes() 存入 ab
    let bb = b.as_bytes(); // 把 b.as_bytes() 存入 bb
    let (mut ia, mut ib) = (0usize, 0usize); // 把 (0usize, 0usize); 写入 let (mut ia, mut ib)
    for &ch in s.as_bytes() {
        // for 按位与 字符 in 字符串.as_bytes() {
        while ia < ab.len() && ab[ia] != ch {
            // 把 字符 { 写入 while ia < ab.len() && ab[ia] !
            ia += 1; // ia累加 1
        }
        while ib < bb.len() && bb[ib] != ch {
            // 把 字符 { 写入 while ib < bb.len() && bb[ib] !
            ib += 1; // ib累加 1
        }
        if ia >= ab.len() || ib >= bb.len() {
            // 若 ia 不低于 ab.长度() 或 ib 不低于 bb.长度(
            return false; // 返回 false
        }
        ia += 1; // ia累加 1
        ib += 1; // ib累加 1
    }
    true // true
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: Vec<(&str, &str, usize)> = vec![
        ("ABCBDAB", "BDCABA", 4),
        ("AGGTAB", "GXTXAYB", 4),
        ("abc", "abc", 3),
        ("", "abc", 0),
        ("abc", "xyz", 0),
    ];
    for (idx, (a, b, want)) in cases.iter().enumerate() {
        // for (idx, (数组, b, want)) in cases.iter().enumerate() {
        let got = lcs_length(a, b); // 把 lcs_length(数组, b) 存入 got
        assert_eq!(got, *want, "case {} failed: lcs_length({},{})", idx, a, b); // 断言校验
    }
    for (a, b) in [("ABCBDAB", "BDCABA"), ("AGGTAB", "GXTXAYB")] {
        let s = lcs_string(a, b); // 把 lcs_string(数组, b) 存入 字符串
        assert_eq!(
            s.len(),
            lcs_length(a, b),
            "lcs_string length mismatch: {}",
            s
        ); // 断言校验
        assert!(is_common_sub(a, b, &s), "not a common subsequence: {}", s); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
