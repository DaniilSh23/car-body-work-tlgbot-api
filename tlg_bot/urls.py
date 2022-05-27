from django.urls import path
from tlg_bot.views import WorkCategoryView, ApplicationsViewMixin, CompletedWorksList, \
    DetailDescriptionCompletedWorks
urlpatterns = [
    path('category/', WorkCategoryView.as_view(), name='category'),
    path('applications/', ApplicationsViewMixin.as_view(), name='applications'),
    path('completed_works_list/', CompletedWorksList.as_view(), name='completed_works_list'),
    path(
        'completed_works_detail_description/<int:pk>',
        DetailDescriptionCompletedWorks.as_view(),
        name='completed_works_detail_description'
    ),
]
