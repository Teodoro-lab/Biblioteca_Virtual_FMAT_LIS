from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

DAILY_FILE_QUOTA = 5
DAILY_COMMENT_QUOTA = 10

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    comment_quota = models.IntegerField(default=DAILY_COMMENT_QUOTA, validators=[MinValueValidator(0)])
    file_quota = models.IntegerField(default=DAILY_FILE_QUOTA, validators=[MinValueValidator(0)])
    last_reset = models.DateTimeField(default=timezone.now)

    def reset_form_quota(self):
        breakpoint()
        self.comment_quota = DAILY_COMMENT_QUOTA
        self.file_quota = DAILY_FILE_QUOTA
        self.last_reset = timezone.now()
        self.save()