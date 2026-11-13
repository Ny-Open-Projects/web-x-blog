// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138684407
// LeetCode 649. Dota2参议院 — Rust 版（方案1）
fn predict_party_victory(senate: &str) -> String {
    // 定义函数/方法 predict_party_victory
    let n = senate.len() as i32; // 把 senate.长度() as i32 存入 元素个数
    let mut radiant: std::collections::VecDeque<i32> = Default::default();
    let mut dire: std::collections::VecDeque<i32> = Default::default();
    for (i, c) in senate.chars().enumerate() {
        // for (下标 i, 字符) in senate.chars().enumerate() {
        if c == 'R' {
            radiant.push_back(i as i32);
        } else {
            dire.push_back(i as i32);
        }
    }
    while !radiant.is_empty() && !dire.is_empty() {
        // while 取反 radiant 是否为空 且 取反 dire 是否为空 {
        let r = radiant.pop_front().unwrap(); // 把 radiant.pop_front().unwrap() 存入 右指针
        let d = dire.pop_front().unwrap(); // 把 dire.pop_front().unwrap() 存入 d
        if r < d {
            radiant.push_back(r + n);
        } else {
            dire.push_back(d + n);
        }
    }
    if radiant.is_empty() {
        "Dire".to_string()
    } else {
        "Radiant".to_string()
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(predict_party_victory("RD"), "Radiant"); // 断言校验
    assert_eq!(predict_party_victory("DDR"), "Dire"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
