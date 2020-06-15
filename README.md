# PexelsPy
A Python package form API for pexels website. All the variables in the documentation are included.

# Sample Program
This is a sample program to run in your terminal irrespective of your Operating system.
```python
from pexelsPy import API
PEXELS_API = "YOUR-PEXELS-API"
api = API(PEXELS_API)

#For photos
api.search_photos('your search',page=no of pages, results_per_page=number)    
photos = api.get_photos()

#for videos
api.search_videos('your search',page=no of pages, results_per_page=number)
videos = api.get_videos()

#To access the details in the variables photos and videos LOOP through the variable
#for photos
for data in photos:
	print(data.[Your-required-data_structure])

#for videos
for data in videos:
  print(data.[data_structure])
```
