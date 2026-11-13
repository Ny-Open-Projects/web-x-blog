// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134773756
// LeetCode 75. 颜色分类 — Rust 版（方案2）
fn sort_colors(nums: &mut Vec<i32>) {
    // 定义函数/方法 sort_colors
    let (mut p0, mut cur, mut p2) = (0usize, 0usize, nums.len() - 1);
    while cur <= p2 {
        // 把 p2 { 写入 while cur <
        if nums[cur] == 0 {
            nums.swap(p0, cur);
            p0 += 1;
            cur += 1;
        }
        // 若 数组[当前值] 等于 0 { 数组.交换 p0, 当前值); p0 累加 1; 当前值 累加 1; }
        else if nums[cur] == 2 {
            nums.swap(cur, p2);
            if p2 == 0 {
                break;
            }
            p2 -= 1;
        } else {
            cur += 1;
        } // 否则
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut v = vec![2, 0, 2, 1, 1, 0];
    sort_colors(&mut v); // 把 vec取反 [2,0,2,1,1,0]; sort_colors( 按位与 mut 值); 写入 let mut v
    assert_eq!(v, vec![0, 0, 1, 1, 2, 2]); // 断言校验
    let mut v2 = vec![2, 0, 1];
    sort_colors(&mut v2); // 把 vec取反 [2,0,1]; sort_colors( 按位与 mut v2); 写入 let mut v2
    assert_eq!(v2, vec![0, 1, 2]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
