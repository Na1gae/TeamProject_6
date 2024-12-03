import pandas as pd

'''
distribution 클래스 설명
객체 생성시 파라미터에 파일이름을 모두 넣어주세요.
연도, 영역, 유형을 차례로 입력해주세요.
생성된 인스턴스 속성 year(연도), domain(영역), subject(유형), score(표준점수), man(남자), woman(여자)을 자유롭게 사용하세요.
'''

class distributions:
    def __init__(self,*a):
        self.df=pd.DataFrame(columns=['연도','영역','유형','표준점수','남자','여자'])
        for i in a:
            self.data=pd.read_csv(i,encoding='euc_kr')
            self.data['연도']=i[:4]
            self.df=pd.concat([self.df,self.data],ignore_index=True)
            

class distribution(distributions):
    def __init__(self,*a):
        super().__init__(*a)
        self.year=input(f'다음 중 연도를 선택해주세요\n{set(self.df['연도'])}')
        self.domain=input(f'다음 중 영역을 선택해주세요\n{set(self.df[self.df['연도']==self.year]['영역'])}')
        self.subject=input(f'다음 중 유형을 선택해주세요\n{set(self.df[self.df['영역']==self.domain]['유형'])}')
        self.score=list(self.df[self.df['유형']==self.subject]['표준점수'])
        self.man=list(self.df[self.df['유형']==self.subject]['남자'])
        self.woman=list(self.df[self.df['유형']==self.subject]['여자'])