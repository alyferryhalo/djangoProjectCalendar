from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    complete = models.BooleanField(default=False)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('calendarapp:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('calendarapp:event-detail', args=(self.id,))
        #DATE_INPUT_FORMATS = ['%d-%m-%Y']
        if self.complete == False:
            return f'<p><b>{self.start_time.strftime("%H:%M")}</b><a href="{url}"> {self.title} </a></p>'
        else:
            return f'<strike><b>{self.start_time.strftime("%H:%M")}</b><a href="{url}"> {self.title} </a></strike>'


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)

    