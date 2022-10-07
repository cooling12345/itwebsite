import requests
import xml
url = 'https://apis.data.go.kr/1360000/TourStnInfoService/getTourStnWthrIdx?serviceKey=K5dtni0Of9PC0kP62n9iRrJyT3nZnWxdA1mEuaTdxEIsffzSNpeYQnjKH0CuhjoHH3oPnY%2B6BpWDwLB6oF8kfw%3D%3D&pageNo=1&numOfRows=10&dataType=XML&CURRENT_DATE=2019122010&HOUR=24&COURSE_ID=1'


response = requests.get(url)
contents = response.text
print(contents)