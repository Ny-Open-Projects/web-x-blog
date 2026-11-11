-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
-- LeetCode 933. 最近的请求次数 — Lua 版

-- 方案2：front 指针懒删除（不真正移除元素，仅移动队头下标）
local RecentCounter = {} -- 把 {} 写入 local RecentCounter
RecentCounter.__index = RecentCounter -- 把 RecentCounter 写入 RecentCounter.__index

function RecentCounter.new() -- function RecentCounter.new()
	return setmetatable({ queue = {}, front = 0 }, RecentCounter) -- 返回 setmetatable({ 队列 赋值为 {}, front 赋值为 0 }, RecentCounter)
end -- 终点

function RecentCounter:ping(t) -- function RecentCounter:ping(另一字符串)
	self.queue[#self.queue + 1] = t -- 把 另一字符串 写入 self.queue[#self.queue + 1]
	while self.queue[self.front + 1] < t - 3000 do -- while self.队列[self.front 加 1] 小于 另一字符串 减 3000 do
		self.front = self.front + 1 -- 把 self.front 加 1 写入 self.front
	end -- 终点
	return #self.queue - self.front -- 返回 #self.队列 减 self.front
end -- 终点

-- 自测：与 TS 事实源内嵌用例一致
local c = RecentCounter.new() -- 把 RecentCounter.new() 写入 local c
local got = { c:ping(1), c:ping(100), c:ping(3001), c:ping(3002) }
local want = { 1, 2, 3, 3 } -- 把 { 1, 2, 3, 3 } 写入 local want
for i = 1, #want do -- 把 1, #want do 写入 for i
	assert(got[i] == want[i], string.format("FAIL case %d got %d want %d", i, got[i], want[i])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
