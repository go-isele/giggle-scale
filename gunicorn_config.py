
bind = "0.0.0.0:8000"
module = "skillmate.wsgi:application"

workers = 4  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

certfile = "/etc/letsencrypt/live/ctr.somocloud.org/fullchain.pem"
keyfile = "/etc/letsencrypt/live/ctr.somocloud.org/privkey.pem"