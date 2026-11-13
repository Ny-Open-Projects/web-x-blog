-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
-- LeetCode 621. 任务调度器 — Lua 版

-- 方案2（Counter 公式法）
local function least_interval(tasks, n) -- local function least_interval(tasks, 元素个数)
	local count = {} -- 把 {} 写入 local count
	for _, t in ipairs(tasks) do -- 遍历取 另一字符串
		count[t] = (count[t] or 0) + 1 -- 把 (计数[另一字符串] or 0) 加 1 写入 count[t]
	end -- 终点
	local max_count = 0 -- 把 0 写入 local max_count
	for _, v in pairs(count) do -- 遍历取 值
		if v > max_count then
			max_count = v
		end -- 若 值 超过 max_count then max_count 赋值为 值 终点
	end -- 终点
	local max_count_tasks = 0 -- 把 0 写入 local max_count_tasks
	for _, v in pairs(count) do -- 遍历取 值
		if v == max_count then
			max_count_tasks = max_count_tasks + 1
		end
	end -- 终点
	return math.max(#tasks, (max_count - 1) * (n + 1) + max_count_tasks)
end -- 终点

-- 自测：与 TS 事实源内嵌用例一致
local cases = { -- 把 { 写入 local cases
	{ { "A", "A", "A", "B", "B", "B" }, 2, 8 },
	{ { "A", "A", "A", "A" }, 2, 10 },
	{ { "A", "B", "C", "D" }, 0, 4 },
}
for i, c in ipairs(cases) do -- 遍历取 字符
	local got = least_interval(c[1], c[2]) -- 把 least_interval(字符[1], 字符[2]) 写入 local got
	assert(got == c[3], string.format("FAIL case %d got %d want %d", i, got, c[3])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
