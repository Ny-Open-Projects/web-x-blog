// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133911745
// LeetCode 45. 跳跃游戏II — Rust 版（方案2）
fn jump(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 jump
    let mut position = nums.len() - 1; // 把 数组.长度() 减 1; 写入 let mut position
    let mut steps = 0; // 把 0; 写入 let mut steps
    while position > 0 {
        // while position 超过 0 {
        for i in 0..position {
            // 逐个取出 0 的元素（下标 i）
            if i + nums[i] as usize >= position {
                // 若 下标 i 加 数组[下标 i] as usize 不低于 position
                position = i; // 把 下标 i; 写入 position
                steps += 1; // steps累加 1
                break; // 跳出循环
            }
        }
    }
    steps // steps
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(jump(vec![2, 3, 1, 1, 4]), 2); // 断言校验
    assert_eq!(jump(vec![2, 3, 0, 1, 4]), 2); // 断言校验
    assert_eq!(jump(vec![1]), 0); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
