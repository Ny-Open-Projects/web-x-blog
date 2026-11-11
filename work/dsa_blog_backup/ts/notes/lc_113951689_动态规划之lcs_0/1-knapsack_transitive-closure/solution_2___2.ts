// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
    export function demo(): void {
        function knapsack(weights: number[], values: number[], capacity: number): [number, number[]] {
        const n = weights.length;
        const dp: number[][] = Array.from({ length: n + 1 }, () => new Array(capacity + 1).fill(0));
            for (let i = 1; i <= n; i++) {
            const w = weights[i - 1];
            const v = values[i - 1];
                for (let c = 0; c <= capacity; c++) {
                dp[i][c] = dp[i - 1][c];
                    if (c >= w) {
                    dp[i][c] = Math.max(dp[i][c], dp[i - 1][c - w] + v);
                }
            }
        }
        let c = capacity;
        const chosen: number[] = [];
            for (let i = n; i > 0; i--) {
                if (dp[i][c] !== dp[i - 1][c]) {
                chosen.push(i - 1);
                c -= weights[i - 1];
            }
        }
        chosen.reverse();
        return [dp[n][capacity], chosen];
    }
    const [mv, chosen] = knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7);
        if (mv !== 9 || chosen.length !== 2 || chosen[0] !== 1 || chosen[1] !== 2) {
        throw new Error("FAILED");
    }
    console.log("PASS");
}
demo();
