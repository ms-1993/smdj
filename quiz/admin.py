from django.contrib import admin


from quiz.models import Quiz, Question, Choice
# Register your models here.


class choiceAdmin(admin.ModelAdmin):
    model = Choice
    list_display = ('correct', 'choice_text')


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice, choiceAdmin)
