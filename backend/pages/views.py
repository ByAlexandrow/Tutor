from django.shortcuts import render


def page_not_found(request, exception='Страницы не найдена'):
    """Отображение шаблона ошибки 404 (ошибка пользователя)."""

    template_name = 'pages/404.html'
    return render(request, template_name, status=404)


def csrf_failure(request, reason='Отказано в праве доступа'):
    """Отображение шаблона ошибки 403 (отказ в праве доступа)."""

    template_name = 'pages/403csrf.html'
    return render(request, template_name, status=403)


def server_error(request, error='Сервер не отвечает'):
    """Отображение шаблона ошибки 500 (ошибка работы сервера)."""

    template_name = 'pages/500.html'
    return render(request, template_name, status=500)
