-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
-- LeetCode 108673483. 减治策略 — Lua 版（方案1：二分查找）
local function binary_search(arr, target) -- local function binary_search(数组, 目标值)
	local left, right = 1, #arr -- 把 1, #数组 写入 local left, right
	while left <= right do -- 把 右边界 do 写入 while left <
		local mid = math.floor((left + right) / 2) -- 把 math.floor((左边界 加 右边界) 除以 2) 写入 local mid
		if arr[mid] == target then
			return mid - 1
		end -- 若 数组[中点] 等于 目标值 then return 中点 减 1 终点
		if arr[mid] < target then
			left = mid + 1
		else
			right = mid - 1
		end -- 若 数组[中点] 小于 目标值 then 左边界 赋值为 中点 加 1 else 右边界 赋值为 中点 减 1 终点
	end -- 终点
	return -1 -- 返回 减 1
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ { 1, 3, 5, 7, 9 }, 5, 2 },
	{ { 1, 3, 5, 7, 9 }, 4, -1 },
	{ {}, 5, -1 },
	{ { 1, 3, 5, 7, 9 }, 1, 0 },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local got = binary_search(c[1], c[2]) -- 把 binary_search(字符[1], 字符[2]) 写入 local got
	assert(got == c[3], string.format("case %d failed: got %d want %d", idx, got, c[3])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
