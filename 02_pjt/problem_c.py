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
