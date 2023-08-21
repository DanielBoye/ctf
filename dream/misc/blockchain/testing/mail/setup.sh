pip install -r requirements.txt

sudo docker build -t satoshi_from_wish .

# change this port for what you want it to run on
sudo docker run -p 5002:5002 satoshi_from_wish