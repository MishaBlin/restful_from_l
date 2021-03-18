from pprint import pprint

from requests import get, post, delete

# pprint(get('http://localhost:8080/api/v2/news/1').json())
#
# pprint(get('http://localhost:8080/api/v2/news').json())

pprint(get('http://localhost:8080/api/v2/users/1').json())

# print(post('http://localhost:8080/api/news',
#            json={'title': 'Заголовок'}).json())

# print(post('http://localhost:8080/api/news',
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости',
#                  'user_id': 1,
#                  'is_private': False}).json())

# print(delete('http://localhost:8080/api/news/3').json())
