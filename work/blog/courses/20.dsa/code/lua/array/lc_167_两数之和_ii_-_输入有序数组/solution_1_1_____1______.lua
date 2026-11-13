-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133524779
-- LeetCode 167. 两数之和II — Lua 版（方案1）
local function two_sum(numbers, target) -- local function two_sum(numbers, 目标值)
	local l, r = 1, #numbers -- 把 1, #numbers 写入 local l, r
	while l < r do -- while 左指针 小于 右指针 do
		local s = numbers[l] + numbers[r] -- 把 numbers[左指针] 加 numbers[右指针] 写入 local s
		if s == target then
			return { l, r }
		end -- 若 字符串 等于 目标值 then return {左指针, 右指针} 终点
		if s < target then
			l = l + 1
		else
			r = r - 1
		end -- 若 字符串 小于 目标值 then 左指针 赋值为 左指针 加 1 else 右指针 赋值为 右指针 减 1 终点
	end -- 终点
	return {} -- 返回 {}
end -- 终点
assert(table.concat(two_sum({ 2, 7, 11, 15 }, 9), ",") == "1,2") -- 打印输出
assert(table.concat(two_sum({ 2, 3, 4 }, 6), ",") == "1,3") -- 打印输出
assert(table.concat(two_sum({ -1, 0 }, -1), ",") == "1,2") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
