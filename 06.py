import requests
from pprint import pprint

BASE_URL = "https://api.themoviedb.org/3"
path1 = "/search/movie" 

params = {
    "api_key": "e89f1ac075fe652da53b26e8466adbac",
    "language": "ko-KR",
    "region": "KR",
}

def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    params["query"] = title
    response = requests.get(BASE_URL+path1, params=params).json()
    responseLi = response.get("results")
    if len(responseLi) > 0:
        movie_id = responseLi[0].get("id")
        path2 = f"/movie/{movie_id}/credits"
        params["movie_id"] = movie_id
        credit = requests.get(BASE_URL+path2, params=params).json()
        cast = credit.get("cast")
        castReturn = []
        for i in cast:
            if i.get("cast_id") < 10.0:
                castReturn.append(i.get("name"))
        crew = credit.get("crew")
        directingReturn = []
        for i in crew:
            if i.get("department") == "Directing":
                directingReturn.append(i.get("name"))
        def movieInfo():
            mvif = {}
            mvif["cast"] = castReturn
            mvif["crew"] = directingReturn
            return mvif
        return movieInfo()
    else:
        return("None")


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
