import requests
from pprint import pprint

api='5ef064e7f4721766a54899e612e85f67'
def credits(title):
    URL1=f'https://api.themoviedb.org/3/search/movie?api_key={api}&language=ko-KR&page=1&include_adult=false&query={title}' # 첫 번째로, 영화의 id를 저장하려 함.
    params1 = {}
    res1 = requests.get(URL1, params=params1)
    data1 = res1.json()
    m_id=''
    for i in range(len(data1['results'])): # 검색한 URL에서의 첫 번째 영화의 id를 출력함.
        m_id=data1['results'][0]['id']
    URL = f'https://api.themoviedb.org/3/movie/{m_id}/credits?api_key={api}&language=ko-KR' # 두 번째로, 그 영화의 정보를 알아내려고 함.
    params = {}
    res = requests.get(URL, params=params)
    data = res.json()
    ans={'cast':[],'directing':[]} # 알아낸 정보를 통해, dict형을 만들고 그 안에 빈 리스트 두개를 만든다.
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
