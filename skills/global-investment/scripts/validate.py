#!/usr/bin/env python3
"""global-investment 技能验证脚本。

断言“产出=合规成立”而非“动作已执行”：
- GOOD 样例：含全部合规要素，且无违规 → exit 0
- BAD 样例：命中任一违规模式 → exit 1

退出码契约：0=通过，1=存在错误，2=文件错误。
"""
import re
import sys
from pathlib import Path

EXIT_OK = 0
EXIT_FAIL = 1
EXIT_FILE_ERROR = 2


def read_sample(path: str) -> str:
    p = Path(path)
    if not p.is_file():
        print(f"文件不存在: {path}", file=sys.stderr)
        sys.exit(EXIT_FILE_ERROR)
    return p.read_text(encoding="utf-8")


GOOD_REQUIREMENTS = [
    ('不构成投资建议|非投资建议|风险自担', '缺少不构成投资建议声明'),
    ('口径|实际利率|数据来源|截止', '缺少数据口径核查'),
    ('周期.{0,8}(边界|局限|嵌套)|情景推演', '缺少周期框架边界/情景标注'),
    ('汇率|对冲', '缺少汇率敞口/对冲成本'),
    ('gotchas|坑位|红线', '缺少 gotchas 坑位引用'),
]

BAD_VIOLATIONS = [
    ('稳赚|保证.{0,4}(收益|盈利|翻倍)|必(涨|跌|赚)', '命中违规：保证收益话术'),
    ('内幕|消息面|跟单|带单', '命中违规：内幕/跟单话术'),
    ('全仓|梭哈|一把梭', '命中违规：全仓赌博话术'),
    ('(忽略|无视|不用管).{0,4}(风险|止损)', '命中违规：忽略风险'),
]


def find_violations(text: str) -> list:
    hits = []
    for pattern, msg in BAD_VIOLATIONS:
        if re.search(pattern, text, re.IGNORECASE):
            hits.append(msg)
    return hits


def find_missing_good(text: str) -> list:
    missing = []
    for pattern, msg in GOOD_REQUIREMENTS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(msg)
    return missing


def main():
    if len(sys.argv) < 2:
        print("用法: validate.py <sample.md>", file=sys.stderr)
        sys.exit(EXIT_FILE_ERROR)

    sample_path = sys.argv[1]
    text = read_sample(sample_path)
    fname = Path(sample_path).name.lower()
    is_bad = "bad" in fname

    errors = []

    violations = find_violations(text)
    if is_bad:
        if not violations:
            errors.append("BAD 样例未命中任何已知违规模式（应至少命中一条）")
        else:
            errors.append(f"BAD 样例命中 {len(violations)} 条违规（预期失败）：{'; '.join(violations)}")
    else:
        if violations:
            errors.append(f"GOOD 样例命中违规（不应有）：{'; '.join(violations)}")
        missing = find_missing_good(text)
        errors.extend(missing)

    if errors:
        print(f"验证失败（{len(errors)} 项）：", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(EXIT_FAIL)

    print("验证通过")
    sys.exit(EXIT_OK)


if __name__ == "__main__":
    main()
