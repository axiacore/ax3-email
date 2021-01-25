from django.conf import settings

AX3EMAILBACKEND = getattr(settings, 'AX3EMAILBACKEND', 'django.core.mail.backends.smtp.EmailBackend')
AX3RETRIES = getattr(settings, 'AX3RETRIES', 3)
AX3DELAY = getattr(settings, 'AX3DELAY', 600)
