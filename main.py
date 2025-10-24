def hello_world(request):
    name = request.args.get('name', 'Nakshatra')
    return f"Hello, {name}! Welcome to Cloud Functions!"
