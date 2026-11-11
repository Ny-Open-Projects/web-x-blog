// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138771574
// LeetCode 93. 复原IP地址 — Rust 版（方案1）
fn valid_seg(s: &str) -> bool {
    // 定义函数/方法 valid_seg
    if s.len() == 0 || s.len() > 3 {
        return false;
    } // 若 字符串.长度() 等于 0 或 字符串.长度() 超过 3 { return false; }
    if s.len() > 1 && s.starts_with('0') {
        return false;
    } // 若 字符串.长度() 超过 1 且 字符串.starts_with('0') { return false; }
    s.parse::<i32>().map(|v| v <= 255).unwrap_or(false) // 把 255).unwrap_or(false) 写入 s.parse::<i32>().map(|v| v <
}
fn restore_ip_addresses(s: String) -> Vec<String> {
    // 定义函数/方法 restore_ip_addresses
    let chars: Vec<char> = s.chars().collect(); // 把 字符串.chars().collect(); 写入 let chars: Vec<char>
    let n = chars.len(); // 把 chars.长度() 存入 元素个数
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    if n < 4 || n > 12 {
        return res;
    } // 若 元素个数 小于 4 或 元素个数 超过 12 { return 结果; }
    for a in 1..=3 {
        // 逐个取出 1 的元素（数组）
        for b in 1..=3 {
            // 逐个取出 1 的元素（b）
            for c in 1..=3 {
                // 逐个取出 1 的元素（字符）
                let d = n - a - b - c; // 把 元素个数 减 数组 减 b 减 字符 存入 d
                if d < 1 || d > 3 {
                    continue;
                } // 若 d 小于 1 或 d 超过 3 { continue; }
                let s1: String = chars[0..a].iter().collect(); // 把 chars[0..数组].iter().collect(); 写入 let s1: String
                let s2: String = chars[a..a + b].iter().collect(); // 把 chars[数组..数组 加 b].iter().collect(); 写入 let s2: String
                let s3: String = chars[a + b..a + b + c].iter().collect();
                let s4: String = chars[a + b + c..].iter().collect(); // 把 chars[数组 加 b 加 字符..].iter().collect(); 写入 let s4: String
                if valid_seg(&s1) && valid_seg(&s2) && valid_seg(&s3) && valid_seg(&s4) {
                    // 定义函数/方法 valid_seg
                    res.push(format!("{}.{}.{}.{}", s1, s2, s3, s4)); // 把 format取反 (「{}.{}.{}.{}」, s1, s2, s3, s4 压入栈/数组尾部
                }
            }
        }
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = restore_ip_addresses("25525511135".to_string()); // 把 restore_ip_addresses(「25525511135」.to_string()) 存入 got
    assert_eq!(got, vec!["255.255.11.135", "255.255.111.35"]); // 断言校验
    assert_eq!(restore_ip_addresses("0000".to_string()), vec!["0.0.0.0"]); // 断言校验
    assert!(restore_ip_addresses("abc".to_string()).is_empty()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
