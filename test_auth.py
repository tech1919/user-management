import requests
import json

jwt_token = "eyJraWQiOiJOa01wb1ptcXY0VUJFV2tOXC95Q3ZOXC9XMnJTRm5IUnN3RGE2UGppeUFVdWM9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJlYzEwODY2Ni0zNGY3LTQyMjQtOWJhNy04OWFmZTVhYTYyMDIiLCJjb2duaXRvOmdyb3VwcyI6WyJERVZFTE9QRVIiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMi5hbWF6b25hd3MuY29tXC91cy1lYXN0LTJfSkE4S1NoYkltIiwidmVyc2lvbiI6MiwiY2xpZW50X2lkIjoiN2huMXY3azkyYnE5dGh2YTM5bDBmbG9vcm0iLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCBwcm9maWxlIiwiYXV0aF90aW1lIjoxNjcxMjAyNDEwLCJleHAiOjE2NzEyMDYwMTAsImlhdCI6MTY3MTIwMjQxMCwianRpIjoiN2U5N2JkYWYtYjA3NC00YmM0LTkzMWItY2I1MGQ3MjQ4MmVhIiwidXNlcm5hbWUiOiJvZnJ5Lm1ha2Rhc3kifQ.R1Sl0zjtFC1gDv1QUoWhGWGbIkwMDTey_gweev_NTON26u8JQhy4x35s9rRcxE-wZQaiBIUTktnoWDOwpr72ELiWbuY-CEhEMJCruqgxCK0auZXr9TeNYdQkVXmv4yiy8XPDw3HiHgrswgwRFkeH_Ssu5OXfmFu-wA6wtZ7tTeqMlZtCy85ZceTeMHdK8NdqfV-b14U3Koct3Wm5M2nmAjOM5BXr7LSeXdMnIvD4E8uqTG7fbcoccagSd-M2WXxR_p587Ca9DRSwsFgN5nod53qJwLwM_NZ1BsCJ6uXvvSAHdHygQSwOXa1vv090dlRQLPcqZSbjwHUOe6dDgxlZ5w"
url = "http://localhost:8000/auth/not_secure"


header = {
    # "Authorization" : f"Bearer {jwt_token}" , 
    "Content-Type" : "application/json",
}
x = requests.get(url , headers=header)



with open("user_creds.json" , "w") as f:
    print(x.json())
    f.write(json.dumps(x.json()))


