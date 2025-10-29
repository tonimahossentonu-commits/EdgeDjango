from django.shortcuts import render

def hello_user(request, username):
    # The 'render()' function is a shortcut provided by Django.
    # Internally, it performs THREE main steps:

    # 1️⃣ It loads the HTML template file ('hello.html') from the templates directory.
    # 2️⃣ It fills the template with the context data (here: {'username': username}),
    #     replacing template variables like {{ username }} with actual values.
    # 3️⃣ It returns an HttpResponse object containing the rendered HTML page,
    #     which is then sent back to the user's web browser.

    # In short: render() = loader.get_template() + template.render(context) + HttpResponse()
    
    return render(request, 'hello.html', {'username': username})
