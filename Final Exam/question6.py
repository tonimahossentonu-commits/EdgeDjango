def add_book(request):
    # Django receives an HTTP request object.
    # If request.method == "POST", it means user submitted the form.
    if request.method == "POST":
        form = BookForm(request.POST)  # Django parses POST data and binds it to the form.
        if form.is_valid():            # Form validation occurs (checks field types, required fields, etc.).
            form.save()                # If valid, Django saves data to the database via the ORM.
            return redirect('list_books')  # Django prepares an HTTP redirect response to send back.
    else:
        form = BookForm()  # For GET request, Django sends empty form to the template.

    return render(request, 'library/add_book.html', {'form': form})
    # render() combines the template with context data and returns an HttpResponse to the browser.
