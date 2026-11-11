-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135129920
-- LeetCode 8. 字符串转换整数 (atoi) — Lua 版（方案2）
local function my_atoi(s) -- local function my_atoi(字符串)
	local i = 1 -- 把 1 写入 local i
	local n = #s -- 把 #字符串 写入 local n
	while i <= n and s:sub(i, i) == " " do
		i = i + 1
	end
	local sign = 1 -- 把 1 写入 local sign
	if i <= n and (s:sub(i, i) == "+" or s:sub(i, i) == "-") then
		if s:sub(i, i) == "-" then
			sign = -1
		end -- 若 字符串:sub(下标 i, 下标 i) 等于 「 减 」 then sign 赋值为 减 1 终点
		i = i + 1 -- 把 下标 i 加 1 存入 下标 i
	end -- 终点
	local ans = 0 -- 把 0 写入 local ans
	while i <= n and s:sub(i, i):match("%d") do
		ans = ans * 10 + tonumber(s:sub(i, i)) -- 把 答案 乘 10 加 tonumber(字符串:sub(下标 i, 下标 i)) 存入 答案
		if ans > 2147483648 then
			ans = 2147483648
		end -- 若 答案 超过 2147483648 then 答案 赋值为 2147483648 终点
		i = i + 1 -- 把 下标 i 加 1 存入 下标 i
	end -- 终点
	ans = ans * sign -- 把 答案 乘 sign 存入 答案
	if ans > 2147483647 then
		return 2147483647
	end -- 若 答案 超过 2147483647 then return 2147483647 终点
	if ans < -2147483648 then
		return -2147483648
	end -- 若 答案 小于 减 2147483648 then return 减 2147483648 终点
	return ans -- 返回 答案
end -- 终点
assert(my_atoi("42") == 42) -- 断言校验
assert(my_atoi(" -42") == -42) -- 断言校验
assert(my_atoi("4193 with words") == 4193) -- 断言校验
assert(my_atoi("-91283472332") == -2147483648) -- 断言校验
assert(my_atoi("words and 987") == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
