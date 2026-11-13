-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
-- LeetCode 108673483. 减治策略 — Lua 版（方案3：Boyer-Moore 摩尔投票求多数元素）
local function majority_element(arr) -- local function majority_element(数组)
	local candidate = nil -- 把 nil 写入 local candidate
	local count = 0 -- 把 0 写入 local count
	for _, num in ipairs(arr) do -- 遍历取 num
		if count == 0 then
			candidate = num
		end -- 若 计数 等于 0 then candidate 赋值为 num 终点
		if num == candidate then
			count = count + 1
		else
			count = count - 1
		end -- 若 num 等于 candidate then 计数 赋值为 计数 加 1 else 计数 赋值为 计数 减 1 终点
	end -- 终点
	local cnt = 0 -- 把 0 写入 local cnt
	for _, num in ipairs(arr) do -- 遍历取 num
		if num == candidate then
			cnt = cnt + 1
		end -- 若 num 等于 candidate then 计数 赋值为 计数 加 1 终点
	end -- 终点
	if cnt > math.floor(#arr / 2) then
		return candidate
	end -- 若 计数 超过 math.floor(#数组 除以 2) then return candidate 终点
	return -1 -- 返回 减 1
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ { 2, 2, 1, 1, 1, 1, 1 }, 1 },
	{ { 1, 2, 3 }, -1 },
	{ { 3, 3, 4 }, 3 },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local got = majority_element(c[1]) -- 把 majority_element(字符[1]) 写入 local got
	assert(got == c[2], string.format("case %d failed: got %d want %d", idx, got, c[2])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
