// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
package main
import ("fmt";"os")
func lcs(text1, text2 string) (int, string) {
    m, n := len(text1), len(text2)
    dp := make([][]int, m+1)
    for i := range dp { dp[i] = make([]int, n+1) }
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            if text1[i-1] == text2[j-1] { dp[i][j] = dp[i-1][j-1] + 1 } else if dp[i-1][j] > dp[i][j-1] { dp[i][j] = dp[i-1][j] } else { dp[i][j] = dp[i][j-1] }
        }
    }
    i, j := m, n
    seq := []byte{}
    for i > 0 && j > 0 {
        if text1[i-1] == text2[j-1] { seq = append([]byte{text1[i-1]}, seq...); i--; j-- } else if dp[i-1][j] >= dp[i][j-1] { i-- } else { j-- }
    }
    return dp[m][n], string(seq)
}
func main() {
    ok := true
    L, S := lcs("abcde", "ace")
    if L != 3 || S != "ace" { ok=false; fmt.Printf("FAIL1 L=%d S=%s\n", L, S) }
    L2, S2 := lcs("abc", "abc")
    if L2 != 3 || S2 != "abc" { ok=false; fmt.Printf("FAIL2 L=%d S=%s\n", L2, S2) }
    if !ok { os.Exit(1) }
    fmt.Println("PASS")
}
