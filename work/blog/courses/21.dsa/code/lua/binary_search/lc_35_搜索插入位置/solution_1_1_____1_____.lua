-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233077
-- LeetCode 35. 搜索插入位置 — Lua 版（方案1：二分查找）
local function search_insert(nums, target) -- local function search_insert(数组, 目标值)
	local left, right = 1, #nums + 1 -- 把 1, #数组 加 1 写入 local left, right
	while left < right do -- while 左边界 小于 右边界 do
		local mid = math.floor((left + right) / 2) -- 把 math.floor((左边界 加 右边界) 除以 2) 写入 local mid
		if nums[mid] < target then
			left = mid + 1
		else
			right = mid
		end -- 若 数组[中点] 小于 目标值 then 左边界 赋值为 中点 加 1 else 右边界 赋值为 中点 终点
	end -- 终点
	return left - 1 -- 返回 左边界 减 1
end -- 终点
local cases = { -- 把 { 写入 local cases
	{ { 1, 2, 3 }, 1, 0 },
	{ { 1, 3, 5, 6 }, 5, 2 },
	{ { 1, 3, 5, 6 }, 2, 1 },
	{ { 1, 3, 5, 6 }, 7, 4 },
	{ { 1, 3, 5, 6 }, 0, 0 },
}
for _, c in ipairs(cases) do -- 遍历取 字符
	assert(search_insert(c[1], c[2]) == c[3], "case failed") -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
