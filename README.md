
# django-dropbox-example

> An example of how to setup `django-dropbox-storage` and use it.

## Requirements
Create a virtual environment and activate it:

```
python -m venv myenv
cd myenv/Scripts
activate
```

Install the requirements:

`pip install -r requirements.txt`

And install django-dropbox-storage

`pip install git+https://github.com/zahidtokur/django-dropbox-storage.git`


## Next Steps

- Make sure to follow the instructions on setting up `django-dropbox-storage`. Refer to [this repository](https://github.com/zahidtokur/django-dropbox-storage).

- Go to [Dropbox App Console](https://www.dropbox.com/developers/apps) and click your app.

- Go to **Permissions** tab and grant the following permissions to your app:
	- files.metadata.write
	- files.metadata.read
	- files.content.write
	- files.content.read

## Finally

Clone this repository:

```
git clone https://github.com/zahidtokur/django-dropbox-example.git
cd django-dropbox-example
```

Before running the project make sure to set the following in `settings.py`:

```
DROPBOX_CONSUMER_KEY = 'YOUR DROPBOX CONSUMER KEY HERE'
DROPBOX_CONSUMER_SECRET = 'YOUR DROPBOX CONSUMER SECRET HERE'
DROPBOX_ACCESS_TOKEN = 'ACCESS TOKEN GENERATED FROM get_dropbox_token'
```

Migrate and create a superuser to test it:

```
python manage.py migrate
python manage.py createsuper
```

After logging in to django admin site, go to http://127.0.0.1:8000/admin/core/dropboxfile/ page and create a DropboxFile to test it.

If all goes well, you will see the uploaded file on your Dropbox.

Good luck!
