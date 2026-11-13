-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134221939
-- LeetCode 704. 二分查找 — Lua 版

-- 0 基下标语义与 TS 参考一致（Lua 数组本身 1 基，读取时 +1）
local function search(nums, target) -- local function search(数组, 目标值)
	local left = 0 -- 把 0 写入 local left
	local right = #nums - 1 -- 把 #数组 减 1 写入 local right
	while left <= right do -- 把 右边界 do 写入 while left <
		local mid = left + math.floor((right - left) / 2) -- 把 左边界 加 math.floor((右边界 减 左边界) 除以 2) 写入 local mid
		local v = nums[mid + 1] -- 把 数组[中点 加 1] 写入 local v
		if v == target then -- 若 值 等于 目标值 then
			return mid -- 返回 中点
		elseif v < target then -- elseif 值 小于 目标值 then
			left = mid + 1 -- 把 中点 加 1 存入 左边界
		else -- 否则
			right = mid - 1 -- 把 中点 减 1 存入 右边界
		end -- 终点
	end -- 终点
	return -1 -- 返回 减 1
end -- 终点

-- 自测：与 LeetCode 官方用例一致
assert(search({ 1, 2, 3 }, 1) == 0, "case 1 failed") -- 断言校验
assert(search({ -1, 0, 3, 5, 9, 12 }, 9) == 4, "case 2 failed") -- 断言校验
assert(search({ -1, 0, 3, 5, 9, 12 }, 2) == -1, "case 3 failed") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
