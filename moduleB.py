import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self, distribution_instance):
        self.distribution = distribution_instance

    def line_chart(self):
        # 데이터 내림차순 정렬
        sorted_indices = np.argsort(self.distribution.score)[::-1]  # 내림차순 정렬
        scores = np.array(self.distribution.score)[sorted_indices]
        men = np.array(self.distribution.man)[sorted_indices]
        women = np.array(self.distribution.woman)[sorted_indices]

        x = np.arange(len(scores))

        plt.rc('font', family='NanumGothic')
        fig, ax = plt.subplots(figsize=(15, 6))

        # 선 그래프 생성 (선 두께와 점 크기 조정)
        ax.plot(x, men, marker='o', markersize=3, linewidth=1, label='남', color='blue', alpha=0.7)
        ax.plot(x, women, marker='o', markersize=3, linewidth=1, label='여', color='pink', alpha=0.7)

        ax.set_xlabel('표준 점수', fontsize=12)
        ax.set_ylabel('학생 수', fontsize=12)
        ax.set_title(f'{int(self.distribution.year)+1}학년도 수능 {self.distribution.subject} 표준점수 분포', fontsize=14)

        xticks = np.arange(0, len(scores), max(1, len(scores) // 10))
        ax.set_xticks(xticks)
        ax.set_xticklabels([scores[i] for i in xticks], rotation=90)
        ax.legend()

        plt.tight_layout()
        plt.show()
