package com.webfault.dsa;
import java.util.*;
class Main {
    // faithful translation of python solution_1___1.py (LCS length + subsequence)
    static Object[] lcs(String text1, String text2){
        int m=text1.length(), n=text2.length();
        int[][] dp=new int[m+1][n+1];
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(text1.charAt(i-1)==text2.charAt(j-1)) dp[i][j]=dp[i-1][j-1]+1;
                else dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);
            }
        }
        // 回溯构造子序列
        int i=m, j=n;
        StringBuilder sb=new StringBuilder();
        while(i>0&&j>0){
            if(text1.charAt(i-1)==text2.charAt(j-1)){
                sb.append(text1.charAt(i-1));
                i--; j--;
            } else if(dp[i-1][j]>=dp[i][j-1]){
                i--;
            } else {
                j--;
            }
        }
        String seq=sb.reverse().toString();
        return new Object[]{dp[m][n], seq};
    }
    public static void main(String[] args) {
        String[][] cases={
            {"abcde","ace"},
            {"abc","abc"},
            {"abc","def"},
            {"","abc"},
        };
        Object[][] wants={
            {3,"ace"},
            {3,"abc"},
            {0,""},
            {0,""},
        };
        boolean ok=true;
        for(int ci=0;ci<cases.length;ci++){
            Object[] got=lcs(cases[ci][0],cases[ci][1]);
            if(!got[0].equals(wants[ci][0])||!got[1].equals(wants[ci][1])){
                ok=false; System.out.println("FAIL lcs("+cases[ci][0]+","+cases[ci][1]+")="+got[0]+","+got[1]+" want="+wants[ci][0]+","+wants[ci][1]);
            }
        }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
