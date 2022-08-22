# Melody-Share

## Video demo (turn on volume)

https://user-images.githubusercontent.com/53788322/185797897-b72c6323-2e58-4082-af6e-31bb296a9ca2.mp4

## Description
Melody-Share is a website to create and share your music (made using the Python Django Framework). 
- Users can record music using an interactive piano, drums, and by singing. 
- Registered users have an option to save their music to their profile, publish it to view music webpage containing all users published music, and upvote other users’ music. 
- There is also feature where users can externally share (tweet) their recorded music via the Twitter API.


## Screenshots

| Home Page  | Create Account Page | Make Music Page |
| ------------- | ------------- | ------------- |
| <img src="https://user-images.githubusercontent.com/53788322/185816766-71dc8a69-997a-4e81-bb0a-7fc7c35d58f7.png" width="330" height="156" /> | <img src="https://user-images.githubusercontent.com/53788322/185816874-9b0748ee-a408-475e-b13c-b504a24f5b8b.png" width="330" height="156" />| <img src="https://user-images.githubusercontent.com/53788322/185815704-c99b35c6-f196-4820-99eb-851b0dae8638.png" width="330" height="156" />|



| Profile Page  | View Music Page | Share Page |
| ------------- | ------------- | ------------- |
| <img src="https://user-images.githubusercontent.com/53788322/185817121-d5053114-6b50-42fa-9ac6-c439e23454b7.png" width="330" height="156" /> | <img src="https://user-images.githubusercontent.com/53788322/185816965-c34c074e-af0c-403c-81dc-d336ce226fe1.png" width="330" height="156" />| <img src="https://user-images.githubusercontent.com/53788322/185816813-a3f6257a-e29e-46e8-8115-a538701998f7.png" width="330" height="156" />|


## Installation
- Go to the projects directory on command prompt and type: 
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
### To make tweet feature work
- Go to https://developer.twitter.com, sign into your twitter, apply for elevated access, create your project/app and copy the keys and tokens it provides, then paste them into the respective variables in settings.py.
### To run the website:
- `python manage.py runserver`
