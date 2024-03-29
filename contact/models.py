from django.db import models


class Contact(models.Model):
    UNREAD = 'unread'
    READ = 'read'
    HANDLED = 'handled'
    STATUS_CHOICES = [
        (UNREAD, 'Unread'),
        (READ, 'Read'),
        (HANDLED, 'Handled'),
    ]

    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=UNREAD,
    )

    def __str__(self):
        return self.name
