
from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static 
urlpatterns = [
 path('',views.home,name='home') ,
  path('login_page',views.login_page,name="login_page"),
    path('usercreate',views.usercreate,name='usercreate'),  
    path('admin_home',views.admin_home,name='admin_home'),
    path('user_home',views.user_home,name='user_home'),
    path('add_category',views.add_category,name='add_category'),
    path('category',views.category,name='category'),
    path('add_books',views.add_books,name='add_books'),
    path('books',views.books,name='books'),
    path('show_customers',views.show_customers,name='show_customers'),
    path('show_books',views.show_books,name='show_books'),
    path('edit_books/<int:pk>',views.edit_books,name='edit_books'),
    path('search',views.search,name='search'),
     path('profile',views.profile,name='profile'),
     path('delete/<int:pk>',views.delete,name='delete'),
     path('edit_profile',views.edit_profile,name='edit_profile'),
     path('user_issue',views.user_issue,name='user_issue'),
      path('user_issued',views.user_issued,name='user_issued'),
    path('edit_profile_details/<int:pk>',views.edit_profile_details,name='edit_profile_details'),
      path('edit_book_details/<int:pk>',views.edit_book_details,name='edit_book_details'),
     path('delete_books/<int:pk>',views.delete_books,name='delete_books'),
    path('book_details/<int:pk>',views.book_details,name='book_details'),
   path('request_issue/<int:pk>',views.request_issue,name='request_issue'),
   path('admin_issue',views.admin_issue,name='admin_issue'),
    path('admin_issued',views.admin_issued,name='admin_issued'),
   path('issue_book/<int:pk>',views.issue_book,name='issue_book'),
     path('returned_book/<int:pk>',views.returned_book,name='returned_book'),
      path('return_approve/<int:pk>',views.return_approve,name='return_approve'),
   path('return_book',views.return_book,name='return_book'),
   path('cancel_book/<int:pk>',views.cancel_book,name='cancel_book'),
   path('return_books',views.return_books,name='return_books'),
  
   path('penalty/<int:pk>',views.penalty,name='penalty'),
   path('user_penalty',views.user_penalty,name='user_penalty'),
    path('payment/<int:pk>',views.payment,name='payment'),
    path('ok/<int:pk>',views.ok,name='ok'),
    path('admin_penalty',views.admin_penalty,name='admin_penalty'),
    path('cancelled_book',views.cancelled_book,name='cancelled_book'),
   path('logout',views.logout,name='logout')
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 