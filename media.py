import webbrowser

class Movie():
    def __init__(self, title, story, img, yt):
        self.title = title
        self.story = story
        self.poster_image_url = img
        self.trailer_youtube_url = yt

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
        
