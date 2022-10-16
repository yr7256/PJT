import requests

api='5ef064e7f4721766a54899e612e85f67'
def popular_count():
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api}&language=ko-KR&page=1' #f-string을 이용해, URL을 출
    params = {}
    res = requests.get(URL, params=params)
    data = res.json()
    return len(data['results']) # data['results']가 영화의 리스트들이므로 이 데이터의 길이를 반환함.
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
