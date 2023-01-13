import requests

BASE_URL = "https://api.themoviedb.org/3"
path = "/movie/popular" 
params = {
    "api_key": "e89f1ac075fe652da53b26e8466adbac",
    "language": "ko-KR",
    "region": "KR"
}

response = requests.get(BASE_URL+path, params=params).json()
# print(response)

def popular_count():
    pass 
    return(len(response.get("results")))


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20