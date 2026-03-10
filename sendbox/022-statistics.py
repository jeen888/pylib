# 평균값 중앙값

import statistics

marks = [90, 80, 70, 60, 50, 43, 77, 88, 92, 85, 95, 100, 55, 65, 75, 82, 78, 91, 89, 94]
result=statistics.mean(marks) # 평균값
print(result)
result=statistics.median(marks) # 중앙값
print(result)