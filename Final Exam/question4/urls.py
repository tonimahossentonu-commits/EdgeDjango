path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
