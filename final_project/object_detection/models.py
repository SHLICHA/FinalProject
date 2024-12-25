from django.db import models

from users.models import User, CHOISE_MODEL


class Object(models.Model):
    """Модель загружаемого изображения.
    Поля:
        user - пользователь, загрузивший изображение
        model - модель ИИ, используемая для определения
        pub_date - дата публикации изображения. Заполняется автоматически. А админ-панели не меняется
        source_image - собственно само изображение
        processed_image - изображение с указанными координатами и точностью определения
    """
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )
    model = models.CharField(
        verbose_name='Используемая модель',
        choices=CHOISE_MODEL
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата загрузки',
        auto_now_add=True
    )
    source_image = models.ImageField(
        verbose_name='Исходное изображение',
        upload_to='original_images/',
        blank=False
    )
    processed_image = models.ImageField(
        verbose_name='Распознанное изображение',
        upload_to='processed_images/',
        blank=False
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return f'{self.user.username} {self.source_image.path}'


class DetectedObject(models.Model):
    """
    Модель, хранящая данные о случае определения
    Поля:
        model - используемая модель
        original_image - используемое изображение
        object_type - результат обнаружения. Хранит данные о том, что на изображении
        confidence - уверенность. Степень уверенности ИИ в результате
        location - координаты объекта
    """
    model = models.CharField(
        verbose_name='Используемая модель',
        choices=CHOISE_MODEL
    )
    original_image = models.ForeignKey(
        Object,
        verbose_name='Оригинальное изображение',
        related_name='detected_objects',
        on_delete=models.CASCADE)
    object_type = models.CharField(
        verbose_name='Тип изображения',
        max_length=100)
    confidence = models.FloatField(
        verbose_name='Уверенность'
    )
    location = models.CharField(
        verbose_name='Координаты',
        max_length=255)

    class Meta:
        verbose_name = 'Распознанный объект'
        verbose_name_plural = 'Распознанные объекты'

    def __str__(self):
        return f"{self.object_type} ({self.confidence * 100}%) on {self.original_image.source_image.name}"
