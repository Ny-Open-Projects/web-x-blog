-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133968437
-- LeetCode 268. 丢失的数字 — Lua 版（方案1）
local function missing_number(nums) -- local function missing_number(数组)
	local n = #nums -- 把 #数组 写入 local n
	local sum = 0 -- 把 0 写入 local sum
	for _, v in ipairs(nums) do
		sum = sum + v
	end -- 遍历取 值
	return n * (n + 1) // 2 - sum -- 返回 元素个数 乘 (元素个数 加 1)
end -- 终点
assert(missing_number({ 3, 0, 1 }) == 2) -- 断言校验
assert(missing_number({ 0, 1 }) == 2) -- 断言校验
assert(missing_number({ 9, 6, 4, 2, 3, 5, 7, 0, 1 }) == 8) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
