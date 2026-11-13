// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
// LeetCode 27. 移除元素 — Rust 版（方案2）
fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
    // 定义函数/方法 remove_element
    let mut k = 0usize; // 把 0usize; 写入 let mut k
    for i in 0..nums.len() {
        // 逐个取出 0 的元素（下标 i）
        if nums[i] != val {
            nums[k] = nums[i];
            k += 1;
        } // 若 数组[下标 i] 不等于 值 { 数组[下标 k] 赋值为 数组[下标 i]; 下标 k 累加 1; }
    }
    k as i32 // 下标 k as i32
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut v = vec![3, 2, 2, 3]; // 把 vec取反 [3,2,2,3]; 写入 let mut v
    assert_eq!(remove_element(&mut v, 3), 2); // 断言校验
    assert_eq!(&v[..2], &[2, 2]); // 断言校验
    let mut v2 = vec![0, 1, 2, 2, 3, 0, 4, 2]; // 把 vec取反 [0,1,2,2,3,0,4,2]; 写入 let mut v2
    assert_eq!(remove_element(&mut v2, 2), 5); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
