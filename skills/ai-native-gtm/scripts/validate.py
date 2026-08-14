#!/usr/bin/env python3
"""ai-native-gtm 技能验证脚本。

断言"产出=合规成立"而非"动作已执行"：
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
    ('opt-?in|opt-?out|退订|同意', '缺少邮件 opt-in/opt-out 机制'),
    ('披露|#ad|disclose|赞助', '缺少 KOL 披露要求'),
    ('GDPR|CASL|CAN-SPAM|隐私', '缺少目标国营销法规核查'),
    ('(平台|ToS|规则).{0,8}(核查|合规|遵守)', '缺少平台规则核查'),
    ('gotchas|坑位|红线', '缺少 gotchas 坑位引用'),
]

BAD_VIOLATIONS = [
    ('(买|购|采购).{0,6}(名单|列表|leads|leads)', '命中违规：购买邮件名单'),
    ('(不提供|没有|去掉|删除).{0,4}(退订|opt-?out)', '命中违规：无退订机制'),
    ('(不标|隐藏|不提).{0,6}(赞助|#ad|合作|披露)', '命中违规：隐藏赞助披露'),
    ('(抓取|爬|scrape).{0,10}(LinkedIn|社交|平台)', '命中违规：抓取平台数据'),
    ('(群发|批量).{0,6}(未经|未获).{0,4}(同意|订阅)', '命中违规：未经同意群发'),
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
