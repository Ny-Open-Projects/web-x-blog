-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
-- LeetCode 621. 任务调度器 — Lua 版

-- 方案3（贪心模拟，每轮取剩余次数最多的 n+1 个，最后一轮只计实际执行数）
local function least_interval(tasks, n) -- local function least_interval(tasks, 元素个数)
	local count = {} -- 把 {} 写入 local count
	for _, t in ipairs(tasks) do -- 遍历取 另一字符串
		count[t] = (count[t] or 0) + 1 -- 把 (计数[另一字符串] or 0) 加 1 写入 count[t]
	end -- 终点
	local cnt = {} -- 把 {} 写入 local cnt
	for _, v in pairs(count) do
		cnt[#cnt + 1] = v
	end -- 遍历取 值
	local time = 0 -- 把 0 写入 local time
	while #cnt > 0 do -- while #计数 超过 0 do
		table.sort(cnt, function(a, b)
			return a > b
		end) -- 排序
		local used = 0 -- 把 0 写入 local used
		for i = 1, math.min(n + 1, #cnt) do -- 让 下标 i 从 1 走到 math（Lua 1 基）
			if cnt[i] > 0 then -- 若 计数[下标 i] 超过 0 then
				cnt[i] = cnt[i] - 1 -- 把 计数[下标 i] 减 1 写入 cnt[i]
				used = used + 1 -- 把 已用标记 加 1 存入 已用标记
			end -- 终点
		end -- 终点
		local kept = {} -- 把 {} 写入 local kept
		for _, c in ipairs(cnt) do -- 遍历取 字符
			if c > 0 then
				kept[#kept + 1] = c
			end -- 若 字符 超过 0 then kept[#kept 加 1] 赋值为 字符 终点
		end -- 终点
		cnt = kept -- 把 kept 存入 计数
		time = time + (#cnt > 0 and (n + 1) or used) -- 把 time 加 (#计数 超过 0 and (元素个数 加 1) or 已用标记) 存入 time
	end -- 终点
	return time -- 返回 time
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
