// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
package main
import ("fmt";"os";"reflect")
func knapsack(weights, values []int, capacity int) (int, []int) {
    n := len(weights)
    dp := make([][]int, n+1)
    for i := range dp { dp[i] = make([]int, capacity+1) }
    for i := 1; i <= n; i++ {
        w, v := weights[i-1], values[i-1]
        for c := 0; c <= capacity; c++ {
            dp[i][c] = dp[i-1][c]
            if c >= w && dp[i-1][c-w]+v > dp[i][c] { dp[i][c] = dp[i-1][c-w]+v }
        }
    }
    c := capacity
    chosen := []int{}
    for i := n; i > 0; i-- {
        if dp[i][c] != dp[i-1][c] {
            chosen = append([]int{i-1}, chosen...)
            c -= weights[i-1]
        }
    }
    return dp[n][capacity], chosen
}
func main() {
    val, ch := knapsack([]int{1,3,4,5}, []int{1,4,5,7}, 7)
    ok := true
    if val != 9 { ok=false; fmt.Printf("FAIL val=%d\n", val) }
    if !reflect.DeepEqual(ch, []int{1,2}) { ok=false; fmt.Printf("FAIL ch=%v\n", ch) }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}
