from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None, user=None):
        self.text = text
        self.timestamp = timestamp
        self.user = user

    def set_user(self, user):
        self.user = user 


class TextPost(Post):
    def __init__(self,text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp=None)
        self.timestamp = timestamp
	
    def __str__(self):
        first = self.user.first_name
        last = self.user.last_name
        text = self.text
        date = self.timestamp.strftime('%A, %b %d, %Y')
        return ('@{first} {last}: "{text}"\n\t{date}'.format(first=first,last=last,text=text,date=date))

class PicturePost(Post):
    def __init__(self,text, image_url, timestamp=None):
        self.image_url = image_url
        super(PicturePost, self).__init__(text, timestamp)
        self.timestamp = timestamp
		
    def __str__(self):
        first = self.user.first_name
        last = self.user.last_name
        text = self.text
        image = self.image_url
        date = self.timestamp.strftime('%A, %b %d, %Y')
        return ('@{first} {last}: "{text}"\n\t{image}\n\t{date}'.format(first=first,last=last,text=text,image=image,date=date))
    
class CheckInPost(Post):
    def __init__(self,text, latitude, longitude, timestamp=None):
        self.latitude = latitude
        self.longitude = longitude
        super(CheckInPost, self).__init__(text, timestamp=None) 
        self.timestamp = timestamp
		
    def __str__(self):
        first = self.user.first_name
        text = self.text
        lat = self.latitude
        lon = self.longitude
        date = self.timestamp.strftime('%A, %b %d, %Y')
        return ('@{first} Checked In: "{text}"\n\t{lat}, {lon}\n\t{date}'.format(first=first,text=text,lat=lat,lon=lon,date=date))
		