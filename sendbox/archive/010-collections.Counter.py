from collections import Counter
import re

data = """
산에는 꽃 피네.
꽃이 피네.
갈 봄 여름없이
꽃이 피네.

산에
산에
피는 꽃은
저만치 혼자서 피어있네.

산에서 우는 새여
꽃이 좋아
산에서
사노라네.

산에는 꽃지네
꽃이 지네.
갈 봄 여름 없이
꽃이 지네.
"""

words = re.findall(r'\w+', data)    # r은 정규표현식이 원시문자열(raw string)임을 표시
counter = Counter(words)
print(counter.most_common(1))
print(counter.most_common(3))
print(counter)
