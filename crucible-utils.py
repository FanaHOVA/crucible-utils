import requests
import os
import dotenv

dotenv.load_dotenv()

CHALLENGE = "test"
CRUCIBLE_URL = "https://crucible.dreadnode.io"
CHALLENGE_URL = "https://test.crucible.dreadnode.io"

def query(input_data, challenge_url=CHALLENGE_URL):
    response = requests.post(
        f"{challenge_url}/score",
        headers={"Authorization": os.getenv("CRUCIBLE_API_KEY")},
        json={"data": input_data}
    )
    return response.json()

def submit_flag(flag, challenge=CHALLENGE, crucible_url=CRUCIBLE_URL):
    url = f"{crucible_url}/api/submit-flag"
    headers = {"Authorization": os.getenv("CRUCIBLE_API_KEY")}
    payload = {"challenge": challenge, "flag": flag}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        if response.json().get("correct") is True:
            print("The flag was correct. Congrats!")
        else:
            print("The flag was incorrect. Keep trying!")
    else:
        print("There was an error submitting your flag")
        print(response.text)