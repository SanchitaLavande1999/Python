import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_details = response.json()
# Print the id of first element in list
print(complete_details[0]["id"])
# The whole web page is list
# Create for loop to iterate through loop and get all user names
for i in range(len(complete_details)):
    print(complete_details[i]["user"]["login"])
