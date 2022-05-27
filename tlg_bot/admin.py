from django.contrib import admin
from .models import MediaFilesForCompletedWorks, WorkCategory, Applications, CompletedWorks


class WorkCategoryAdmin(admin.ModelAdmin):
    '''Регистрация модели категорий работ в админ панели'''
    list_display = ['id', 'category_name']
    list_display_links = ['id', 'category_name']


class ApplicationsAdmin(admin.ModelAdmin):
    '''Регистрация модели заявок в админ панели'''
    list_display = ['id', 'tlg_user_id', 'tlg_user_name', 'processing_status', 'date']
    list_display_links = ['id', 'tlg_user_id', 'tlg_user_name', 'processing_status', 'date']


class MediaFilesForCompletedWorksAdminInlines(admin.StackedInline):
    '''Регистрация модели медиа файлов для выполненных работ в админ панели, в режиме инлайн'''
    model = MediaFilesForCompletedWorks


class CompletedWorksAdmin(admin.ModelAdmin):
    '''Регистрация модели выполненных работ в админ панели'''
    list_display = ['id', 'work_title', 'result_price', 'work_category']
    list_display_links = ['id', 'work_title', 'result_price', 'work_category']
    inlines = [MediaFilesForCompletedWorksAdminInlines]


admin.site.register(WorkCategory, WorkCategoryAdmin)
admin.site.register(Applications, ApplicationsAdmin)
# admin.site.register(MediaFilesForCompletedWorks, MediaFilesForCompletedWorksAdminInlines)
admin.site.register(CompletedWorks, CompletedWorksAdmin)