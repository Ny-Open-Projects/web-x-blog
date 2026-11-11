-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130778527
-- LeetCode 125. 验证回文串 — Lua 版（方案3）
local function is_palindrome(s) -- local function is_palindrome(字符串)
	local f = {} -- 把 {} 写入 local f
	for c in s:gmatch("[%a%d]") do -- for 字符 in 字符串:gmatch(「[ 对…取模 数组 对…取模 d]」) do
		f[#f + 1] = c:lower() -- 把 字符:lower() 写入 f[#f + 1]
	end -- 终点
	local i, j = 1, #f -- 把 1, #f 写入 local i, j
	while i < j do -- while 下标 i 小于 下标 j do
		if f[i] ~= f[j] then
			return false
		end -- 若 f[下标 i] ~ 赋值为 f[下标 j] then return false 终点
		i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		j = j - 1 -- 把 下标 j 减 1 存入 下标 j
	end -- 终点
	return true -- 返回 true
end -- 终点
assert(is_palindrome("A man, a plan, a canal: Panama") == true) -- 断言校验
assert(is_palindrome("race a car") == false) -- 断言校验
assert(is_palindrome(" ") == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
