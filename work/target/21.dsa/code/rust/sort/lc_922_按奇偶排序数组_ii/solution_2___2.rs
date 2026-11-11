// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
// LeetCode 922. 按奇偶排序数组II — Rust 版（方案2）
fn sort_array_by_parity_ii(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 sort_array_by_parity_ii
    let mut sorted = nums; // 把 数组; 写入 let mut sorted
    sorted.sort(); // 排序
    let mut res = vec![0; sorted.len()]; // 把 vec取反 [0; sorted.长度()]; 写入 let mut res
    let (mut odd, mut even) = (1usize, 0usize); // 把 (1usize, 0usize); 写入 let (mut odd, mut even)
    for &item in &sorted {
        // for 按位与 item in 按位与 sorted {
        if item % 2 != 0 {
            res[odd] = item;
            odd += 2;
        }
        // 若 item 对…取模 2 不等于 0 { 结果[odd] 赋值为 item; odd 累加 2; }
        else {
            res[even] = item;
            even += 2;
        } // 否则
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(sort_array_by_parity_ii(vec![4, 2, 5, 7]), vec![2, 5, 4, 7]); // 断言校验
    assert_eq!(sort_array_by_parity_ii(vec![2, 3]), vec![2, 3]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
