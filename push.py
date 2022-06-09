from requests import post

# ip = "192.168.0.137:5000"
ip = "localhost:5000"

post(f"http://{ip}/api/mode/manual")
while True:
    input()
    post(f"http://{ip}/api/push")
