# A. 인기 영화 조회 (problem_a)

- 학습한 내용 : requests 라이브러리와 api를 이용해 인기있는 영화의 데이터를 받아와서 그 영화의 갯수를 출력하는 것.

- 어려웠던 부분 : api를 이용해 해당한 주소의 데이터를 뽑아내는 것이 어려웠다.

- 새로 배운 것들 및 느낀 점 : URL을 이용해서 데이터를 뽑아내는 것. api가 없으면 데이터를 뽑아낼 수 없다.

- 구현한 코드 : 

```python
import requests

api='5ef064e7f4721766a54899e612e85f67'
def popular_cont():
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api}&language=ko-KR&page=1'
#f-string을 이용해, URL을 출
    params = {}
    res = requests.get(URL, params=params)
    data = res.json()
    return len(data['results'])# data['results']가 영화의 리스트들이므로 이 데이터의 길이를 반환함.
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.

if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20 
```

# B. 특정 조건에 맞는 인기 영화 조회 1 (problem_b)

- 학습한 내용 : requests 라이브러리와 api를 이용해 인기있는 영화의 데이터를 받아와서 영화의 데이터들을 리스트 형태로 출력하는 것.

- 어려웠던 부분 : f-string을 이용해 api값을 넣는데, api를 def 안에서 선언하면 에러가 발생한다. 

- 새로 배운 것들 및 느낀 점 : 저번 pjt와 비슷했지만 api를 이용한다는 점에서 차이가 있었다.

- 구현한 코드 :

```python
import requests
from pprint import pprint

api='5ef064e7f4721766a54899e612e85f67'
def vote_average_movies():
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api}&language=ko-KR&page=1'
# a와 동일함.
    params = {}
    res = requests.get(URL, params=params)
    data = res.json()
    ans=[] # 조건을 만족하는 요소들을 집어넣을 빈 리스트를 만든다.
    for i in range(len(data['results'])):
        if data['results'][i]['vote_average']>=8:
          ans.append(data['results'][i])
    return ans
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())


'''
[{'adult': False,
  'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
  'genre_ids': [28, 18],
  'id': 361743,
  'original_language': 'en',
  'original_title': 'Top Gun: Maverick',
  'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
              '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
              '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
              '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
  'popularity': 5886.004,
  'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
  'release_date': '2022-05-24',
  'title': '탑건: 매버릭',
  'video': False,
  'vote_average': 8.3,
  'vote_count': 1722}, 생략
'''
```

# C. 특정 조건에 맞는 인기 영화 조회 1 (problem_c)

- 학습한 내용 : requests 라이브러리와 api를 이용해 인기있는 영화의 데이터를 받아와서 가장 인기있는 영화 5개를 인기 있는 순서대로 출력하는 것.

- 어려웠던 부분 : lambda를 이용해 정렬. -x 로 정렬하는 것이 가장 중요했다. (오름차순 정렬)

- 새로 배운 것들 및 느낀 점 : sort() 한 뒤, 함수 가장 끝에 있는 부분을 뽑아와서 reverse=True 하는 방법은 쓰기 번거롭기 때문에, lambda를 이용해 정렬하는 것이 흥미로웠다.  

- 구현한 코드 :

```python
import requests
from pprint import pprint

api='5ef064e7f4721766a54899e612e85f67'
def ranking():
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api}&language=ko-KR&page=1'
    params = {}
    res = requests.get(URL, params=params)
    data = res.json()
    ans=[]
    for i in range(len(data['results'])):
      ans.append(data['results'][i]) #여기까지는 b와 동일함.
    ans.sort(key=lambda x: -x['vote_average']) # 여기서 vote_average가 높은 순서대로 정렬.
    ans2=[] # 조건을 만족하는 요소를 넣을 빈 리스트 생성.
    for i in range(5): # index가 0,1,2,3,4인 수를 ans2에 저장.
      ans2.append(ans[i])
    return ans2
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
```

# D. 특정 추천 영화 조회 (problem_d)

- 학습한 내용 : 두 개의 URL을 이용해 하나의 URL에서는 영화의 id값, 그리고 다른 하나의 URL에서는 영화의 id 값을 이용해 추천영화 리스트를 출력하는 것.

- 어려웠던 부분 : 두개의 URL을 사용해야 하는것. 그리고 문제를 꼼꼼히 읽어야 함을 느꼈다. 오류가 생겼을 때는 try-except를 이용해 오류를 탈출하는 것.

- 새로 배운 것들 및 느낀 점 : except 에러를 제대로 지정해주지 않으면 수많은 이유들로 except 되어버린다. 어떤 오류인지 체크하는 것이 중요.

- 구현한 코드 :

```python
import requests
from pprint import pprint

api='5ef064e7f4721766a54899e612e85f67'
def recommendation(title):
    URL1=f'https://api.themoviedb.org/3/search/movie?api_key={api}&language=ko-KR&page=1&include_adult=false&query={title}'
     # 이 URL을 통해 id를 저장하려고 함.
    params1 = {}
    res1 = requests.get(URL1, params=params1)
    data1 = res1.json()
    m_id=''
    for i in range(len(data1['results'])): # 검색한 후, 첫 번째 영화를 m_id에 저장. 
        m_id=data1['results'][0]['id']
    URL = f'https://api.themoviedb.org/3/movie/{m_id}/credits?api_key={api}&language=ko-KR'
     # 위에 저장한 m_id를 이용해 추천영화 리스트를 알아내려고 함.
    params = {}
    res = requests.get(URL, params=params)
    data = res.json()
    ans=[] # 추천 영화를 담을 빈 리스트 생성.
    try: # try에서 에러가 발생하면 except로 넘어가게 함.
        if data['results']:
            for i in data['results']:
                ans.append(i['title'])
        return ans
    except: # except로 넘어오면 None을 반환.
        return None
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
```

# E. 출연진, 연출진 데이터 조회 (problem_e)

- 학습한 내용 : 두 개의 URL을 이용해 하나의 URL에서는 영화의 id값, 그리고 다른 하나의 URL에서는 영화의 id 값을 이용해 배우와 디렉터의 리스트를 뽑아낸다.

- 어려웠던 부분 : 영화의 정보가 너무 길어서 하나의 리스트에 여러 개의  dict형이 있다는 걸 몰랐다. 그리고 d와 마찬가지로 오류가 생겼을 땐, try-except로 탈출하는 것. dict형에서는 그냥 value를 뽑아내는 것보다, 오류를 줄이기 위해 get을 써야한다는 것을 느꼈다.

- 새로 배운 것들 및 느낀 점 : try-except의 사용이 흥미로웠다. 또 다른 방법은 어떤 방법이 있을까 고민하게 되었다.

- 구현한 코드 :

```python
import requests
from pprint import pprint

api='5ef064e7f4721766a54899e612e85f67'
def credits(title):
    URL1=f'https://api.themoviedb.org/3/search/movie?api_key={api}&language=ko-KR&page=1&include_adult=false&query={title}'
    # 첫 번째로, 영화의 id를 저장하려 함.
    params1 = {}
    res1 = requests.get(URL1, params=params1)
    data1 = res1.json()
    m_id=''
    for i in range(len(data1['results'])):
        m_id=data1['results'][0]['id']
# 검색한 URL에서의 첫 번째 영화의 id를 출력함.
    URL = f'https://api.themoviedb.org/3/movie/{m_id}/credits?api_key={api}&language=ko-KR'
# 두 번째로, 그 영화의 정보를 알아내려고 함.
    params = {}
    res = requests.get(URL, params=params)
    data = res.json()
    ans={'cast':[],'directing':[]}
 # 알아낸 정보를 통해, dict형을 만들고 그 안에 빈 리스트 두개를 만든다.
    try: # try에서 에러가 발생하면 except로 넘어가게 함.
        for i in data['cast']: # 조건에 만족하는 요소들을 리스트에 넣는다.
            if i.get('cast_id')<10:
                ans['cast'].append(i['name'])
        for j in data['crew']:
            if j.get('department')=='Directing':
                ans['directing'].append(j['name'])
        return ans
    except: # except로 넘어오면 None을 반환.
        return None
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
```
