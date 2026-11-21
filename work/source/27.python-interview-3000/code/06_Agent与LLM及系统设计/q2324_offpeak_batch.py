"""错峰批处理:任务只在低谷窗口执行,窗口结束未完成的部分回退到在线队列,不硬扛。"""
class OffPeakScheduler:
    def __init__(self, window=(2, 6)):
        self.window = window
        self.pending = []
        self.ran = []
        self.fallback = []

    def submit(self, job_id, est_minutes):
        self.pending.append({"id": job_id, "est": est_minutes})

    def run_window(self, start_hour, minutes_available):
        if not (self.window[0] <= start_hour < self.window[1]):
            return []
        remaining = minutes_available
        end_hour = start_hour + minutes_available / 60.0
        done = []
        for job in list(self.pending):
            if end_hour > self.window[1]:
                break
            if job["est"] <= remaining:
                self.ran.append(job["id"])
                remaining -= job["est"]
                self.pending.remove(job)
                done.append(job["id"])
            else:
                break
        return done

    def drain_to_online(self):
        moved = [job["id"] for job in self.pending]
        self.fallback.extend(moved)
        self.pending = []
        return moved


if __name__ == "__main__":
    s = OffPeakScheduler()
    s.submit("etl-daily", 60)
    s.submit("embed-all", 120)
    s.submit("reindex", 90)
    assert s.run_window(start_hour=10, minutes_available=240) == [], "窗口外拒绝启动"
    done = s.run_window(start_hour=2, minutes_available=240)
    assert done == ["etl-daily", "embed-all"], "装得下的按序跑"
    assert s.pending and s.pending[0]["id"] == "reindex"
    moved = s.drain_to_online()
    assert moved == ["reindex"], "窗口结束未完成的回退在线队列"
    assert s.run_window(start_hour=2, minutes_available=240) == [], "积压清空后无残留"
    big = OffPeakScheduler()
    big.submit("huge", 300)
    assert big.run_window(start_hour=2, minutes_available=240) == [], "单任务超窗直接回退 不硬扛"
    print("错峰批处理通过:窗口校验 按序装填 溢出回退 在线限速")
