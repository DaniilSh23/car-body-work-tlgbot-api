from django.db import models


class WorkCategory(models.Model):
    '''Модель для категорий работ'''
    category_name = models.CharField(max_length=50, verbose_name='Название категории работ')

    class Meta:
        ordering = ['id']
        db_table = 'Категории работ'
        verbose_name = 'Категория работ'
        verbose_name_plural = 'Категории работ'

    def __str__(self):
        return self.category_name


class Applications(models.Model):
    '''Модель для хранения заявок'''
    tlg_user_id = models.CharField(max_length=50, verbose_name='ID пользователя телеграмма')
    tlg_user_name = models.CharField(max_length=50, verbose_name='Имя пользователя телеграмма')
    processing_status = models.BooleanField(verbose_name='Статус обработки', default=False)
    application_text = models.TextField(max_length=1000, verbose_name='Текст заявок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата заявки')

    class Meta:
        ordering = ['id']
        db_table = 'Заявки'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка от {self.tlg_user_name}'


class CompletedWorks(models.Model):
    '''Модель для выполненных работ'''
    work_title = models.CharField(max_length=50, verbose_name='Название работы')
    result_price = models.FloatField(verbose_name='Итоговая цена работы')
    work_description = models.TextField(max_length=1000, verbose_name='Описание работы')
    work_category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE, verbose_name='Категория работ')
    date_of_completion = models.DateField(auto_now_add=True, verbose_name='Дата выполнения работы')

    class Meta:
        ordering = ['id']
        db_table = 'Выполненные работы'
        verbose_name = 'Выполненная работа'
        verbose_name_plural = 'Выполненные работы'

    def __str__(self):
        return self.work_title


class MediaFilesForCompletedWorks(models.Model):
    '''Модель для хранения меди файлов(фото, видео) для выполненных работ'''
    media_file = models.FileField(upload_to=f'files/%Y/%m/%d', max_length=2000, null=True, blank=True)
    for_work = models.ForeignKey(CompletedWorks, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['id']
        db_table = 'Медиа работ'


