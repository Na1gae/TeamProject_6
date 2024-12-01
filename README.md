# 팀프로젝트 Ver 1

![스크린샷 2024-12-01 203126](https://github.com/user-attachments/assets/1ee8a191-74f5-4e1a-8727-2d23ab1f4e9e)

## moduleA
전체 과목의 분포 데이터를 가진 상위 클래스를 만들고 한 과목의 분포 데이터를 가진 하위 클래스를 만듦.  
판다스를 사용해 csv 파일을 읽고 이용하기 쉬운 dataframe 객체로 만듦.  
dataframe의 인덱싱을 활용해 원하는 데이터들만 추출 후 인스턴스 속성으로 만듦.  

## moduleB
주어진 데이터를 이용해 인스턴스를 만들고, bar_chart()를 이용해 그래프를 그림.
각 축의 라벨과 타이틀을 올바르게 달고, 한글 대응을 위해 폰트 설정.
차트가 제대로 표시될 수 있도록 rotation 옵션 추가.

## moduleC
파일로 distribution 객체를 만들고 그걸로 다시 graph 객체를 만듦.  
graph 클래스의 bar_chart 메서드로 그래프를 그림.
