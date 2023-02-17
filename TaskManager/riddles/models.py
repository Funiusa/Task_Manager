from django.db import models


class Riddle(models.Model):
    riddle_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name = "Riddle"
        verbose_name_plural = "Riddles"

    def __str__(self):
        return self.riddle_text


class Option(models.Model):
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
