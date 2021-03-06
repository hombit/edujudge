from django.contrib import admin
from judge.api.models import Task, Solution, Comment, Test, Example


class CommentAdmin(admin.ModelAdmin):

    list_display = ('id', 'task', 'user', 'task_owner', 'text', 'time')
    ordering = ('-id',)


class SolutionAdmin(admin.ModelAdmin):

    list_display = ('id', 'task', 'user', 'error', 'test', 'time')
    ordering = ('-id',)
    readonly_fields = ('task', 'test', 'user', 'source')
    exclude = ('source_path',)


admin.site.register(Task)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Test)
admin.site.register(Example)
admin.site.register(Solution, SolutionAdmin)
