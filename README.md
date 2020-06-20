# PexelsPy
A Python package form API for pexels website. All the variables in the documentation are included.

# INSTALLATION
```python
pip install pexelsPY
```
# Credits
- Photo source [AguilarLagunasArturo](https://github.com/AguilarLagunasArturo)
- Thanks for clearing my doubts [RRRohit7](https://github.com/RRRohit7)

# Sample Program
This is a sample program to run in your terminal.
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

# To use programs under singleSamples folder.

**_NOTE:_** First you must create a environment variable in your respective machine called 'PEXELS_API' with your API VALUE.

- Assuming you are in the same directory as the files are present.

### searchPhotos.py
syntax: ```python searchPhotos.py your_required_search_name page_number Number_of_images_in_that_page```\
Example: ```python searchPhotos.py koala 1 1```

### popularPhotos.py
syntax: ```python popularPhotos.py page_number_you_want_to_search number_of_images_you_need```\
Example: ```python popularPhotos.py 2 2```

### curatedPhotos.py
syntax: ```python curatedPhotos.py page_number_you_want_to_search number_of_images_you_need```\
Example: ```python curatedPhotos.py 2 2```

# References
- Stackoverflow
- [Photo Source](https://github.com/AguilarLagunasArturo/pexels-api)
