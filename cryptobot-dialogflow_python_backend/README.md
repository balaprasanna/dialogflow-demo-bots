## Link to Instructions Doc

https://docs.google.com/document/d/1LhXRXFeqI5DIX6zRIe4RTMPtjMcVYza4sBVQfF5PQlM/edit

## If you are lazy to follow the previous instructions, you can bypass that step by doing the following

1. Find the cryptobot.zip zip file 
2. Create a new bot in your account.
3. Go its settings, find "Import from ZIP file"
4. Just upload `cryptobot.zip` to your bot.
5. This should be able to bypass the instructions list

**WARNING** - Please remember to update the ngrok tunnel url in your bot.


## TO run this backend

```
git clone https://github.com/balaprasanna/dialogflow_python_backend.git
```

## IF downloading zip file
- If you are manually downloading the zip file from github
- Then make sure you extract the zip file to a folder.


## Locate the folder
```
cd dialogflow_python_backend
```

## Install Dependencies
```
pip install -r requirements.txt
```

## Run python app file
```
python app.py
```


## To run this backend with ngrok tunnel

- Download the ngrok tunnel binary from ngrok.com

For mac/linux
```
ngrok http 5000
```

For Windows
```
ngrok.exe http 5000
```
