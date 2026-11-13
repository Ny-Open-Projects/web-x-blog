// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135949307
// LeetCode 452. 用最少数量的箭引爆气球 — Rust 版（方案1）
fn find_min_arrow_shots(mut points: Vec<Vec<i32>>) -> i32 {
    // 定义函数/方法 find_min_arrow_shots
    if points.is_empty() {
        return 0;
    } // 若 points 是否为空 { return 0; }
    points.sort_by_key(|x| x[1]); // points.sort_by_key( 按位或 x 按位或 x[1]);
    let mut arrows = 1; // 把 1; 写入 let mut arrows
    let mut end = points[0][1]; // 把 points[0][1]; 写入 let mut end
    for p in points.iter().skip(1) {
        // 逐个取出 points 的元素（节点）
        if p[0] > end {
            arrows += 1;
            end = p[1];
        } // 若 节点[0] 超过 终点 { arrows 累加 1; 终点 赋值为 节点[1]; }
    }
    arrows // arrows
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        find_min_arrow_shots(vec![vec![10, 16], vec![2, 8], vec![1, 6], vec![7, 12]]),
        2
    ); // 断言校验
    assert_eq!(find_min_arrow_shots(vec![]), 0); // 断言校验
    assert_eq!(
        find_min_arrow_shots(vec![vec![1, 2], vec![3, 4], vec![5, 6], vec![7, 8]]),
        4
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
