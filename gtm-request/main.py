import os
import requests
import random
import time
import json

src_ip_list = [
    "192.168.110.10",
    "192.168.120.11",
    "192.168.130.12",
    "192.168.140.13",
    "192.168.150.14",
    "192.168.160.15",
    "192.168.170.16",
    "192.168.180.17",
    "192.168.190.18",
    "192.168.200.19",
    "192.168.210.20",
    "192.168.220.21",
    "192.168.230.22",
    "192.168.240.23",
    "192.168.250.24",
]
user_list = [
    "user1",
    "user2",
    "user3",
    "user4",
    "user5",
    "user6",
    "user7",
    "user8",
    "user9",
    "user10",
]


# def send
def send(url):
    headers = {
        "Content-Type": "application/json",
    }
    random_ip = random.choice(src_ip_list)
    random_user = random.choice(user_list)
    payload = json.dumps(
        {
            "name": random_user,
            "src_ip": random_ip,
            "src_port": random.randint(1000, 9999),
            "protocol": "http",
            "package": random.randint(100, 999),
            "code": random.randint(100, 500),
        }
    )
    print(payload)
    resp = requests.post(f"http://{url}/api/v1/gtm", data=payload, headers=headers)
    print(resp.text)


url = os.getenv("GTM_URL", "192.168.97.103:8080")


def main():
    while True:
        send(url)
        time.sleep(30)


if __name__ == "__main__":
    main()
