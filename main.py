def hello_world(request):
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}! Welcome to Cloud Functions!"

