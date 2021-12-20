# 데이터분석기반의 전자제조 전문인력 양성사업단 2021년 하반기 산학협력 프로젝트

## 참가자

### 서울과학기술대학교 

박영준, 김종백

### 숙명여자대학교 

원다영, 오경은

## 데이터 크롤링

- 사전에 입력받은 키워드를 바탕으로 Google Patent의 데이터를 Selenium을 활용하여 크롤링
    - Google Patent의 데이터를 파일화하는 것은 50,000건이 최대이므로, period를 산정할 때 limit에 걸리지 않게 주의할 것.
- 크롤링한 후 특허 데이터로 활용 가능한 것들의 코드만을 추출하여 list화

```python
search_text = 'electronic battery' #검색 키워드
search_period = [
                    ['20180101','20180331'], ['20180401', '20180630'],['20180701','20180930'], ['20181001', '20181231'],        
                    ['20190101','20190331'], ['20190401', '20190630'],['20190701','20190930'], ['20191001', '20191231'],
                    ['20200101','20200331'], ['20200401', '20200630'],['20200701','20200930'], ['20201001', '20201231'],
                    ['20210101','20210331'], ['20210401', '20210630'],['20210701','20210930'], ['20211001', '20211231'],
                ] #분기별로 구간 분리

for length in search_period:
    begin_date = length[0]
    end_date = length[1]
    driver.get(f'https://patents.google.com/?q={search_text}&country=US&before=priority:{end_date}&after=priority:{begin_date}&language=ENGLISH') 
    time.sleep(30) # 429(Too many Requests Error)를 방지
    driver.find_element_by_xpath('//*[@id="count"]/div[1]/span[2]/a').click() # 페이지 내의 csv 파일 다운로드 링크 클릭
```

