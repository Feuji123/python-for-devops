# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

# URL to fetch pull requests from the GitHub API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url)  # Add headers=headers inside get() for authentication

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()

    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}

    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

___________________________________________________________________________________

import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
print(response)
print(type(response))

output:
<Response [200]>
<class 'requests.models.Response'>

import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
print(response.json())      ---> to print what you see in web (Convert the JSON response to a dictionary)
print(response.status_code)    ---> to check whether api call is success or not.  200 - success

complete_detail=response.json()
print(complete_detail[0]["id"])      ----> output: <id> of 1st item

print(complete_detail[0]["user"]["login"]) ---> to get the first login username

import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_detail=response.json()
for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])   --? list all users login usernames 
_____________________________________________________________________________________________

