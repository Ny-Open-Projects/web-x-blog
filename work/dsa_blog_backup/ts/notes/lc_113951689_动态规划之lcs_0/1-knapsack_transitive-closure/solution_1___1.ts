// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
    export function demo(): void {
        function lcs(text1: string, text2: string): [number, string] {
        const m = text1.length;
        const n = text2.length;
        const dp: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
            for (let i = 1; i <= m; i++) {
                for (let j = 1; j <= n; j++) {
                    if (text1[i - 1] === text2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    let i = m;
    let j = n;
    const seq: string[] = [];
        while (i > 0 && j > 0) {
            if (text1[i - 1] === text2[j - 1]) {
            seq.push(text1[i - 1]);
            i--;
            j--;
        } else if (dp[i - 1][j] >= dp[i][j - 1]) {
        i--;
    } else {
    j--;
}
}
seq.reverse();
return [dp[m][n], seq.join("")];
}
const [len, seq] = lcs("abcde", "ace");
    if (len !== 3 || seq !== "ace") {
    throw new Error("FAILED");
}
console.log("PASS");
}
demo();
