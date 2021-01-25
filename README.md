# AX3 EmailBackend

AX3 EmailBackend A Django app to send emails using Huey tasks

## Installation
AX3 EmailBackend is easy to install from the PyPI package:

```
$ pip install ax3-email-backend
```

After installing the package, the project settings need to be configured.
add `ax3_email_backend` to your `INSTALLED_APPS`

`INSTALLED_APPS += [ax3_email_backend]`
## Configuration
Add email backend settings
``` 
# app/settings.py
EMAILBACKEND = 'AX3EmailBackend'
AX3_EMAIL_BACKEND = # Django EmailBackend that does the actual sending // Optional - Default smtp (django)
AX3_RETRIES =  # Maximun number of times to retry // Optional - Default 3
AX3_DELAY = # Time in seconds between attemps // Optional - Default = 600
```
