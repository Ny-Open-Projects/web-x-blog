ROUTING = {
    "report.*": {"queue": "slow"},
    "notify.*": {"queue": "fast"},
}

def route_for(task_name: str) -> str:
    for pattern, cfg in ROUTING.items():
        head = pattern.split("*")[0]
        if task_name.startswith(head):
            return cfg["queue"]
    return "default"

print(route_for("report.daily"), route_for("notify.sms"), route_for("misc.export"))
