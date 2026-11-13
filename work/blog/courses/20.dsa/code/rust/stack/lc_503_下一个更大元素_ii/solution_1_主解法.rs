// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145045460
// LeetCode 503. 下一个更大元素 II — Rust 版（方案1）
fn next_greater_elements(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 next_greater_elements
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    let mut res = vec![-1; n]; // 把 vec取反 [ 减 1; 元素个数]; 写入 let mut res
    let mut st: Vec<usize> = Vec::new(); // 把 Vec::new(); 写入 let mut st: Vec<usize>
    for i in 0..n * 2 {
        // 逐个取出 0 的元素（下标 i）
        let ii = i % n; // 把 下标 i 对…取模 元素个数 存入 ii
        while let Some(&top) = st.last() {
            // 边取边处理，取空即停
            if nums[top] < nums[ii] {
                res[top] = nums[ii];
                st.pop();
            } else {
                break;
            }
        }
        if i < n {
            st.push(ii);
        } // 若 下标 i 小于 元素个数 { st 追加 ii); }
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(next_greater_elements(vec![1, 2, 1]), vec![2, -1, 2]); // 断言校验
    assert_eq!(next_greater_elements(vec![3, 2, 1]), vec![-1, 3, 3]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
