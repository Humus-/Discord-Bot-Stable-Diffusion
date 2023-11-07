# Flask app for running the models

Just adding a quick app in the same repo.
This can be run on a separate machine. Even the different models can be handled by different servers. All configurable by config.yml

For testing you can use the command
```
flask --app ai_app --debug run
```

But its recommended to use a WSGI server for serving the application. Eg: Gunicorn