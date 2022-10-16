import requests
from pprint import pprint

api='5ef064e7f4721766a54899e612e85f67'
def recommendation(title):
    URL1=f'https://api.themoviedb.org/3/search/movie?api_key={api}&language=ko-KR&page=1&include_adult=false&query={title}' # 이 URL을 통해 id를 저장하려고 함.
    params1 = {}
    res1 = requests.get(URL1, params=params1)
    data1 = res1.json()
    m_id=''
    for i in range(len(data1['results'])): # 검색한 후, 첫 번째 영화를 m_id에 저장. 
        m_id=data1['results'][0]['id']
    URL = f'https://api.themoviedb.org/3/movie/{m_id}/recommendations?api_key={api}&language=ko-KR&page=1' # 위에 저장한 m_id를 이용해 추천영화 리스트를 알아내려고 함.
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
