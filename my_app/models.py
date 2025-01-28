from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name

class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.name} ({self.league.name})"


class Goal_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='goal_profile')
    favorite_league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True, blank=True)
    favorite_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    favourite_player = models.CharField(max_length=100, default = 'No favourite player yet')
    favourite_squad_number = models.IntegerField(default=0)
    bio = models.TextField()
    profile_pic = CloudinaryField('image ', default = 'goals-profile-pic')
  
   
    

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = CloudinaryField('image ', default = 'goals-post-pic')
  

    def __str__(self):
        return self.title + ' Posted By  ' + self.user.username
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
 

    def __str__(self):
        return self.content
    

    

class Connection(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
       
    ]
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connection_initiated')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connection_received')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
   

    class Meta:
        unique_together = ('user1', 'user2')  # Prevents duplicate friend requests

    def __str__(self):
        return f"{self.user1.username} - {self.user2.username} ({self.status})"
    

class LikesDislike(models.Model):
     LIKE = 'like'
     DISLIKE = 'dislike'

     REACTION_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

     user = models.ForeignKey(User, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
     reaction_type = models.CharField(max_length=7, choices=REACTION_CHOICES)
     

     class Meta:
        unique_together = ('user', 'post', 'comment')  # Prevent duplicate reactions

     def __str__(self):
        if self.post:
            return f"{self.user.username} {self.reaction_type}d post {self.post.id}"
        elif self.comment:
            return f"{self.user.username} {self.reaction_type}d comment {self.comment.id}"



class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('friend_request', 'Friend Request'),
        ('message', 'Message'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    connections = models.ForeignKey('Connection', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.sender} - {self.notification_type} - {self.user}"



