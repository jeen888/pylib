import pprint

# 테스트를 위한 복잡한 중첩 데이터
data = {
    "users": [
        {"id": 1, "name": "Alice", "hobbies": ["reading", "hiking", "coding"], "active": True},
        {"id": 2, "name": "Bob", "hobbies": ["gaming", "cooking"], "active": False},
        {"id": 3, "name": "Charlie", "hobbies": None, "active": True}
    ],
    "config": {
        "version": "1.2.0",
        "settings": {
            "theme": "dark",
            "notifications": {"email": True, "sms": False}
        }
    },
    "metadata": ("2024-05-20", "server-01")
}

print("--- 일반 print 출력 ---")
print(data)
print("\n")

print("--- 기본 pprint 출력 ---")
pprint.pprint(data)
print("\n")

print("--- 옵션을 활용한 pprint 출력 ---")
# indent: 들여쓰기 공백 수
# width: 한 줄의 최대 너비
# depth: 출력할 중첩 구조의 깊이 제한
# compact: 여러 요소를 한 줄에 모아 출력할지 여부
pp = pprint.PrettyPrinter(indent=4, width=40, depth=2, compact=True)
pp.pprint(data)

print("\n--- 특정 깊이까지만 출력 (depth=2) ---")
pprint.pprint(data, depth=2)

# formatted_string = pprint.pformat(data)
# 이제 formatted_string을 파일에 저장하거나 로그로 남길 수 있습니다.

# 아주 깊은 데이터 예시
# deep_data = {"level1": {"level2": {"level3": {"level4": "Too Deep!"}}}}

# 2단계까지만 출력하기
# pprint.pprint(deep_data, depth=2)
# 결과: {'level1': {'level2': {...}}}