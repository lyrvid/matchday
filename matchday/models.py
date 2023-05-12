from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['author'])
        ]

    def __str__(self):
        return f"\"{self.quote}\" - {self.author}"
