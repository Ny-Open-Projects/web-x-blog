// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133844403
// LeetCode 55. 跳跃游戏 — Rust 版（方案1）
fn can_jump(nums: Vec<i32>) -> bool {
    // 定义函数/方法 can_jump
    let mut max_reach = 0usize; // 把 0usize; 写入 let mut max_reach
    for i in 0..nums.len() {
        // 逐个取出 0 的元素（下标 i）
        if i > max_reach {
            return false;
        } // 若 下标 i 超过 max_reach { return false; }
        let r = i + nums[i] as usize; // 把 下标 i 加 数组[下标 i] as usize 存入 右指针
        if r > max_reach {
            max_reach = r;
        } // 若 右指针 超过 max_reach { max_reach 赋值为 右指针; }
    }
    true // true
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(can_jump(vec![2, 3, 1, 1, 4])); // 断言校验
    assert!(!can_jump(vec![3, 2, 1, 0, 4])); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
