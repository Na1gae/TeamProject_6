import pandas as pd

'''
distribution 클래스 설명
객체 생성시 파라미터에 파일이름을 넣어주세요.
영역과 유형을 차례로 입력해주세요.
생성된 인스턴스 속성 domain(영역), subject(유형), score(표준점수), man(남자), woman(여자)을 자유롭게 사용하세요.
'''

class distributions:
    def __init__(self,a):
        self.df=pd.read_csv(a)
        self.domains=self.df['영역']
        self.subjects=self.df['유형']
        self.scores=self.df['표준점수']
        self.men=self.df['남자']
        self.women=self.df['여자']

class distribution(distributions):
    def __init__(self,a):
        super().__init__(a)
        self.domain=input(f'다음 중 영역을 선택해주세요\n{set(self.domains)}')
        self.subject=input(f'다음 중 유형을 선택해주세요\n{set(self.df[self.df['영역']==self.domain]['유형'])}')
        self.score=list(self.df[self.df['유형']==self.subject]['표준점수'])
        self.man=list(self.df[self.df['유형']==self.subject]['남자'])
        self.woman=list(self.df[self.df['유형']==self.subject]['여자'])