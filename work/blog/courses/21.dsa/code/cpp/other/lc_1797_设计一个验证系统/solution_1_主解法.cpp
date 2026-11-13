// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145634738
// LeetCode 1797. 设计一个验证系统 — C++ 版（方案1）
#include <cassert>             // 引入头文件
#include <iostream>            // 引入头文件
#include <string>              // 引入头文件
#include <unordered_map>       // 引入头文件
struct AuthenticationManager { // 定义类型
    long long ttl;             // long long ttl;
    std::unordered_map<std::string, long long>
        expiresAt; // std::unordered_map 小于 std::string, long long 超过 expiresAt;
    explicit AuthenticationManager(long long timeToLive) : ttl(timeToLive) {}
    void generate(const std::string &tokenId, long long currentTime) {
        expiresAt[tokenId] = currentTime + ttl;
    }
    int renew(const std::string &tokenId, long long currentTime) { // 定义函数/方法 renew
        auto it = expiresAt.find(tokenId);                         // 把 expiresAt 查找 tokenId) 存入 it
        if (it != expiresAt.end() && it->second > currentTime)
            it->second = currentTime + ttl;
        return countValidTokens(currentTime); // 返回 countValidTokens(currentTime)
    }
    int countValidTokens(long long currentTime) const { // int countValidTokens(long long currentTime) const {
        int cnt = 0;                                    // 把 0 存入 计数
        for (auto &[_, e] : expiresAt)
            if (e > currentTime)
                ++cnt;
        return cnt; // 返回 计数
    }
};
int main() {                               // 程序入口：跑内嵌自测用例
    AuthenticationManager auth(5);         // AuthenticationManager auth(5);
    auth.generate("aaa", 1);               // auth.generate(「aaa」, 1);
    assert(auth.countValidTokens(3) == 1); // 断言校验
    assert(auth.renew("aaa", 4) == 1);     // 断言校验
    assert(auth.countValidTokens(6) == 1); // 断言校验
    std::cout << "PASS" << std::endl;      // 全部用例通过，输出 PASS
    return 0;                              // 返回 0
}
