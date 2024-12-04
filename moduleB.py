import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self, distribution_instance):
        self.distribution = distribution_instance

    def line_chart(self):
        scores = self.distribution.score
        men = self.distribution.man
        women = self.distribution.woman
        subject = self.distribution.subject

        x = np.arange(len(scores))

        plt.rc('font', family='NanumGothic')
        fig, ax = plt.subplots(figsize=(15, 6))

        # 선 그래프 생성
        ax.plot(x, men, marker='o', markersize=4, label='남', color='blue', alpha=0.7)
        ax.plot(x, women, marker='o', markersize=4, label='여', color='pink', alpha=0.7)

        ax.set_xlabel('표준 점수', fontsize=12)
        ax.set_ylabel('학생 수', fontsize=12)
        ax.set_title(f'2024학년도 수능 {subject} 표준점수 분포', fontsize=14)
        ax.set_xticks(x)
        ax.set_xticklabels(scores, rotation=90)
        ax.legend()

        plt.tight_layout()
        plt.show()
