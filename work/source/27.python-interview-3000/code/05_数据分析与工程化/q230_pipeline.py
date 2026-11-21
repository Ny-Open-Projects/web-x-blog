from dataclasses import dataclass


@dataclass
class Artifact:
    image: str
    sha: str


def pipeline(commit: str, gates: dict[str, bool]) -> list[str]:
    # 返回流水线实际走过的阶段
    stages = []
    if not all(gates.values()):
        stages.append("ci-failed")
        return stages
    stages += ["build-wheel", "build-image"]
    artifact = Artifact(image=f"reg/app:{commit[:7]}", sha=commit)
    stages.append(f"deploy-staging:{artifact.image}")
    if gates.get("smoke_ok"):
        stages += ["canary-5", "canary-50", "deploy-all"]
    return stages


def test_happy_path():
    gates = {"lint": True, "test": True, "smoke_ok": True}
    stages = pipeline("abcdef1234567890", gates)
    assert stages[-1] == "deploy-all"
    assert stages[0] == "build-wheel"

def test_ci_failure_short_circuits():
    assert pipeline("x" * 40, {"lint": False, "test": True}) == ["ci-failed"]
