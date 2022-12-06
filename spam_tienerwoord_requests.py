from time import sleep
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import threading
import requests

keep_sending = True
count = 0
threadcount = int(input("Hoeveel threads? "))
threads = []
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
user_agents = user_agent_rotator.get_user_agents()

def send_requests():
    global keep_sending
    global count
    
    while keep_sending:
        
        try:
            user_agent = user_agent_rotator.get_random_user_agent()
            headers = { 'User-Agent': user_agent }
            response = requests.post("https://vrtnws-api.vrt.be/nwsnwsnws/teenager-word-election/_vote", json={"word": "slay"}, headers=headers)
        except:
            sleep(10)
                
        if response.status_code == 200:
            count += 1
            print(response.json(), "|", f"Request {count}")
        else:
            print(response.json(), "|", f"Request {count}")
            print("-------------------------")
            print(f"{count} requests gestuurd!")
            keep_sending = False
    sleep(10)
    return send_requests()
    
for i in range(threadcount):
    thread = threading.Thread(target=send_requests, daemon=True)
    threads.append(thread)

for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()()