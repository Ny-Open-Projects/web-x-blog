-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753613
-- LeetCode 392. 判断子序列 — Lua 版（方案2）
local function is_subsequence(s, t) -- local function is_subsequence(字符串, 另一字符串)
	local i = 1 -- 把 1 写入 local i
	for j = 1, #t do -- 把 1, #另一字符串 do 写入 for j
		if i <= #s and s:sub(i, i) == t:sub(j, j) then
			i = i + 1
		end
	end -- 终点
	return i > #s -- 返回 下标 i 超过 #字符串
end -- 终点
assert(is_subsequence("abc", "ahbgdc") == true) -- 断言校验
assert(is_subsequence("axc", "ahbgdc") == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
