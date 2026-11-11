// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134312127
// LeetCode 383. 赎金信 — Rust 版（方案1）
fn can_construct(ransom: String, magazine: String) -> bool {
    // 定义函数/方法 can_construct
    let mut cnt = [0i32; 26]; // 把 [0i32; 26]; 写入 let mut cnt
    for b in magazine.bytes() {
        cnt[(b - b'a') as usize] += 1;
    } // 逐个取出 magazine 的元素（b）
    for b in ransom.bytes() {
        // 逐个取出 ransom 的元素（b）
        let i = (b - b'a') as usize; // 把 (b 减 b'数组') as usize 存入 下标 i
        cnt[i] -= 1; // cnt[i]累减 1
        if cnt[i] < 0 {
            return false;
        } // 若 计数[下标 i] 小于 0 { return false; }
    }
    true // true
}
fn main() {
    assert!(!can_construct("a".into(), "b".into()));
    assert!(!can_construct("aa".into(), "ab".into()));
    assert!(can_construct("aa".into(), "aab".into()));
    println!("PASS");
} // 程序入口：跑内嵌自测用例
