-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133812752
-- LeetCode 234. 回文链表 — Lua 版（方案3）
local function is_palindrome_list(vals) -- local function is_palindrome_list(vals)
	local i, j = 1, #vals -- 把 1, #vals 写入 local i, j
	while i < j do -- while 下标 i 小于 下标 j do
		if vals[i] ~= vals[j] then
			return false
		end -- 若 vals[下标 i] ~ 赋值为 vals[下标 j] then return false 终点
		i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		j = j - 1 -- 把 下标 j 减 1 存入 下标 j
	end -- 终点
	return true -- 返回 true
end -- 终点
assert(is_palindrome_list({}) == true) -- 断言校验
assert(is_palindrome_list({ 1, 2, 2, 1 }) == true) -- 断言校验
assert(is_palindrome_list({ 1, 2 }) == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
