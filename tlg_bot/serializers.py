from rest_framework import serializers

from tlg_bot.models import WorkCategory, Applications, CompletedWorks, MediaFilesForCompletedWorks


class WorkCategorySerializer(serializers.ModelSerializer):
    '''Сериалайзер для категорий работ'''
    class Meta:
        model = WorkCategory
        fields = ['id', 'category_name']


class ApplicationsSerializer(serializers.ModelSerializer):
    '''Сериалайзер для заявок'''
    class Meta:
        model = Applications
        fields = ['id', 'tlg_user_id', 'tlg_user_name', 'processing_status', 'application_text', 'date']


class CompletedWorksSerializer(serializers.ModelSerializer):
    '''Сериалайзер для выполненных работ'''
    class Meta:
        model = CompletedWorks
        fields = ['id', 'work_title', 'result_price', 'work_description', 'work_category', 'date_of_completion']


class MediaFilesForCompletedWorksSerializer(serializers.ModelSerializer):
    '''Сериалайзер для медиа файлов для выполненных работ'''
    class Meta:
        model = MediaFilesForCompletedWorks
        fields = ['id', 'media_file', 'for_work']