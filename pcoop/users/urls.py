from django.urls import path

from pcoop.users.views import (
    user_list_view,
    user_create_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,

)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("new_parent/", view=user_create_view, name="create_user"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),

]
