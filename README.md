This project demonstrates a simple serverless function deployed using Google Cloud Functions.
The function is written in Python and triggered via an HTTP request.
When accessed through the browser or API call, it executes instantly and returns a greeting message.
The function runs in a serverless environment, meaning no manual setup or maintenance of servers is needed.
This approach provides scalability, cost efficiency, and automatic resource management.


Task 4: Deploy a Serverless Function to Google Cloud
🎯 Objective

Learn serverless computing by creating and deploying a cloud function (FaaS) that runs automatically in response to an HTTP trigger — without managing servers.

🛠 Tools

Google Cloud Platform (Free Tier)

Python 3.10 runtime

Browser (for testing)

📦 Function Details

Function Name	- helloWorld
Runtime	- Python 3.10
Trigger	- HTTP (Allow unauthenticated)
Entry Point	- hello_world

Source code
def hello_world(request):
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}! Welcome to Cloud Functions!"

🚀 Deployment Steps

1.Go to Google Cloud Console → Cloud Functions
2.Click + Create Function
3.Fill in:
   Name: helloWorld
   Region: nearest to you (e.g., asia-south1)
   Trigger: HTTP
   Authentication: Allow unauthenticated
4.Runtime: Python 3.10
5.Entry point: hello_world
6.Paste the code in inline editor
7.Click Deploy and wait until status shows Active

🧪 Testing the Function

1️⃣ Test in Browser
Open the Trigger URL
Output:
Hello, Guest! Welcome to Cloud Functions!

🧹 Cleanup

To avoid using free-tier resources:
Go to Cloud Functions → Select function → Delete

📌 Outcome

Learned serverless architecture and Function-as-a-Service (FaaS)
Deployed a function that executes on HTTP trigger
Tested functions in browser and Postman
Learned to handle query parameters

💬 Interview Questions

1.What is serverless computing and how is it different from traditional hosting?
2.What are triggers in serverless functions?
3.What happens behind the scenes when you deploy a cloud function?
4.Advantages of serverless architecture?
5.How does FaaS reduce operational overhead?
6.What are cold starts in serverless computing?
7.How can you secure an HTTP endpoint?
8.Give a real-world use case of serverless computing.
