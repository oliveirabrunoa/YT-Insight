class Video():

    def __init__(self, video_link, title, description, resume):
        self.video_link = video_link
        self.title = title
        self.description = description
        self.resume = resume    

    def __repr__(self):
        return f"<Video(title={self.title}, video_link={self.video_link})>"
    
    def __str__(self):
        return f"{self.title}"