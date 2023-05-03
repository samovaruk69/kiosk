from django.db import models

class Traffic_gaz(models.Model):
    title = models.CharField('Название', max_length=150)
    price_gaz = models.FileField('Файл', upload_to='price/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тариф на газ';
        verbose_name_plural = 'Тарифы на газ'



class Video_OT(models.Model):
    title = models.CharField('Название', max_length=150)
    video_ot = models.FileField('Файл', upload_to='video//')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео ОТ'
        verbose_name_plural = 'Видео ОТ'


class Procedure_and_time_limits(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Procedure_and_time_limits/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Порядок и сроки обжалования принятых административных решений'
        verbose_name_plural = 'Порядок и сроки обжалования принятых административных решений'


class Rights_and_obligations_of_citizens_in_the_implementation_of_administrative_procedures(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Rights_and_obligations_of_citizens_in_the_implementation_of_administrative_procedures/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Права и обязанности граждан при осуществлении административных процедур'
        verbose_name_plural = 'Права и обязанности граждан при осуществлении административных процедур'



class Lists_of_administrative_procedures(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Lists_of_administrative_procedures/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Перечни административных процедур, осуществляемых ПУ "Полоцкгаз" по заявлениям граждан'
        verbose_name_plural = 'Перечни административных процедур, осуществляемых ПУ "Полоцкгаз" по заявлениям граждан'

class BRSM(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='BRSM/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'БРСМ'
        verbose_name_plural = 'БРСМ'

class leadership_GPO(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='leadership_GPO/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Руководство ГПО'
        verbose_name_plural = 'Руководство ГПО'



class leadership_Minenergo(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='leadership_Minenergo/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Руководство Минэнерго'
        verbose_name_plural = 'Руководство Минэнерго'


class leadership_Oblgas(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='leadership_Oblgas/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Руководство Облгаз'
        verbose_name_plural = 'Руководство Облгаз'

class leadership_Polotsk(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='leadership_Polotsk/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Руководство Полоцкгаз'
        verbose_name_plural = 'Руководство Полоцкгаз'


class Mode_of_operation_and_schedule_of_reception_of_citizens(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Mode_of_operation_and_schedule_of_reception_of_citizens/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Режим работы и график приема граждан'
        verbose_name_plural = 'Режим работы и график приема граждан'



class Document_forms(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Document_forms/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Формы(бланки) документов'
        verbose_name_plural = 'Формы(бланки) документов'

class Decrees(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Decrees/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Декреты'
        verbose_name_plural = 'Декреты'

class Directives(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Directives/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Директивы'
        verbose_name_plural = 'Директивы'

class Laws(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Laws/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Законы'
        verbose_name_plural = 'Законы'

class Ordinances(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Ordinances/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Указы'
        verbose_name_plural = 'Указы'

class Others(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Others/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Другое'
        verbose_name_plural = 'Другое'

class Resolutions(models.Model):
    title = models.CharField('Название', max_length=150)
    file = models.FileField('Файл', upload_to='Resolutions/')
    times = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Постановления'
        verbose_name_plural = 'Постановления'

# Create your models here.

