// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355207
// LeetCode LCR 152. 验证二叉搜索树的后序遍历序列 — Rust 版（方案1）
fn verify_postorder(postorder: &[i32]) -> bool {
    // 定义函数/方法 verify_postorder
    fn check(seq: &[i32]) -> bool {
        // 定义判定函数 check
        if seq.len() <= 2 {
            return true;
        } // 若 seq.长度() 不超过 2 { return true; }
        let root = seq[seq.len() - 1]; // 把 seq[seq.长度() 减 1] 存入 根节点
        let mut i = 0usize; // 把 0usize; 写入 let mut i
        while i < seq.len() - 1 && seq[i] < root {
            i += 1;
        } // 把 1; } 写入 while i < seq.len() - 1 && seq[i] < root { i +
        for &v in &seq[i..seq.len() - 1] {
            // for 按位与 值 in 按位与 seq[下标 i..seq.长度() 减 1] {
            if v < root {
                return false;
            } // 若 值 小于 根节点 { return false; }
        }
        check(&seq[..i]) && check(&seq[i..seq.len() - 1])
    }
    check(postorder) // check(postorder)
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(!verify_postorder(&[1, 6, 3, 2, 5])); // 断言校验
    assert!(verify_postorder(&[1, 3, 2, 4, 5])); // 断言校验
    assert!(verify_postorder(&[4, 6, 5, 9, 8, 7])); // 断言校验
    assert!(verify_postorder(&[1, 2, 3])); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
