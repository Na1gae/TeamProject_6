import matplotlib.pyplot as plt
import numpy as np

class graph:
    def __init__(self, distribution_instance):
        self.distribution = distribution_instance

    def bar_chart(self, stacked=False):
        """
        표준점수별 막대 그래프를 생성합니다.
        :param stacked: True이면 하나로 합쳐진 막대 그래프를 생성합니다. False이면 두개가 분리됩니다.
        """
        scores = self.distribution.score
        men = self.distribution.man
        women = self.distribution.woman
        subject = self.distribution.subject

        x = np.arange(len(scores))
        width = 0.45

        plt.rc('font', family='NanumGothic')
        fig, ax = plt.subplots(figsize=(15, 6))

        if stacked:
            ax.bar(x, men, width, label='남', color='blue', alpha=0.7)
            ax.bar(x, women, width, bottom=men, label='여', color='pink', alpha=0.7)
        else:
            ax.bar(x - width/2, men, width, label='남', color='blue', alpha=0.7)
            ax.bar(x + width/2, women, width, label='여', color='pink', alpha=0.7)

        ax.set_xlabel('표준 점수', fontsize=12)
        ax.set_ylabel('학생 수', fontsize=12)
        ax.set_title(f'2024학년도 수능 {subject} 표준점수 분포', fontsize=14)
        ax.set_xticks(x)
        ax.set_xticklabels(scores, rotation=90)
        ax.legend()

        plt.tight_layout()
        plt.show()
