import random

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from tlg_bot.models import WorkCategory, Applications, CompletedWorks, MediaFilesForCompletedWorks
from tlg_bot.serializers import ApplicationsSerializer, CompletedWorksSerializer, \
    MediaFilesForCompletedWorksSerializer


class WorkCategoryView(APIView):
    def get(self, request, format=None):
        works_categories_tpl = WorkCategory.objects.values_list('id', 'category_name')
        return Response(works_categories_tpl, status.HTTP_200_OK)


class CompletedWorksList(APIView):
    '''
    Класс-представление для списка выполненных работ.
    Обеспечивает получение списка выполненных работ.
    '''

    def get(self, request, format=None):
        req_work_category_id = request.query_params.get('id')
        if req_work_category_id:
            # запрос, в котором получаем выполненные работы, по названию категории
            completed_works_lst_tpl = CompletedWorks.objects.select_related('work_category').filter(
                work_category__id=req_work_category_id
            ).values_list('id', 'work_title')
        else:
            completed_works_lst_tpl = CompletedWorks.objects.values_list('id', 'work_title')
        return Response(completed_works_lst_tpl, status.HTTP_200_OK)


class DetailDescriptionCompletedWorks(APIView):
    '''
    Класс-представление для детального представления выполненной работы.
    Обеспечивает получение описания и медиа файлов выполненной работы.
    '''

    def get(self, request, pk, format=None):
        '''Возвращаем детальную инфу о выполненной работе и медиа файлы к ней'''
        # берём работу
        detail_work = CompletedWorks.objects.get(pk=pk)
        # сериализуем работу
        work_serializer = CompletedWorksSerializer(detail_work, many=False)
        # берём медиа файлы для работы, через выборку связанной модели
        media_list = MediaFilesForCompletedWorks.objects.select_related('for_work').filter(for_work__pk=pk)
        # сериализуем медиа файлы
        media_serializer = MediaFilesForCompletedWorksSerializer(media_list, many=True)
        # даём ответ, в котором передаём как работу, так и медиа файлы, но компануем в виде списка
        return Response([work_serializer.data, media_serializer.data], status.HTTP_200_OK)


class ApplicationsViewMixin(ListModelMixin, CreateModelMixin, GenericAPIView):
    '''
    Класс-представление на основании миксинов для заявок.
    Обеспечивает получение списка заявок и создание в БД данных новой заявки
    '''

    # можно будет переопределить queryset, чтобы получать заявки с определённым статусом
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer

    def get(self, request):
        '''GET - запрос возвращает список всех заявок'''
        return self.list(request)

    def post(self, request, format=None):
        '''POST - запрос создаёт в БД инфу о новой заявки'''
        return self.create(request)