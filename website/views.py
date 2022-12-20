import json

from django.shortcuts import render
from website.qiwi_engine import Qiwi
from website.models import Payments, Settings
from pydonsys.settings import AUTH_TOKEN_ENDPOINTS
from django.http import HttpResponseRedirect, HttpResponse


def load_settings():
    settings = Settings.objects.all()
    if settings.count() > 0:
        return settings.last()
    else:
        return Settings.objects.create()


def index(request):
    settings = load_settings()

    data = {
        'notif_text': settings.notif_text
    }

    return render(request, "default/index.html", context=data)


def pay(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        cost = request.POST.get('cost')

        if first_name is not None and cost is not None:
            if cost.isdigit():
                cost = int(cost)
                if cost >= 15 and cost <= 15000:
                    new_payment = Payments.objects.create(first_name=first_name, cost=cost)

                    q = Qiwi()
                    invoce = q.new_invoice(payment=new_payment)
                    if invoce['status']:
                        pay_url = invoce['data'].get('payUrl')
                        if pay_url is not None:
                            return HttpResponseRedirect(pay_url)
                        else:
                            return other_error(request=request, data={
                                'title': '500-06: Ошибка генерации ссылки на оплату',
                                'text': 'При создании ссылки на оплату пошло что-то не так!'
                            })
                    else:
                        return other_error(request=request, data={
                            'title': '500-05: Ошибка генерации ссылки на оплату',
                            'text': 'При создании ссылки на оплату пошло что-то не так!'
                        })
                else:
                    return other_error(request=request, data={
                        'title': '500-04: Ошибка формы',
                        'text': 'Сумма должна быть больше или равна 15 и меньше или равна 15 000!'
                    })
            else:
                return other_error(request=request, data={
                    'title': '500-02: Ошибка формы',
                    'text': 'Сумма в форме должна быть числом!'
                })
        else:
            return other_error(request=request, data={
                'title': '500-01: Ошибка формы',
                'text': 'Не правильно заполнены поля имени и суммы в форме!'
            })
    else:
        return other_error(request=request, data={
            'title': '500-03: Ошибка формы',
            'text': 'Адрес /pay принмиает только - POST запросы!'
        }, code=403)


def terms_of_use(request):
    settings = load_settings()

    data = {
        'title': 'Пользовательское соглашение',
        'text': settings.terms_of_use_text,
    }

    return render(request, "default/info_page.html", context=data)


def privacy_policy(request):
    settings = load_settings()

    data = {
        'title': 'Политика конфиденциальности',
        'text': settings.privacy_policy_text,
    }

    return render(request, "default/info_page.html", context=data)


def description_of_goods(request):
    settings = load_settings()

    data = {
        'title': 'Описание товаров',
        'text': settings.description_of_goods_text,
    }

    return render(request, "default/info_page.html", context=data)


def contacts(request):
    settings = load_settings()

    data = {
        'title': 'Контакты',
        'text': settings.contacts_text,
    }

    return render(request, "default/info_page.html", context=data)


def payments_list(request):
    if request.method == 'GET':
        token = request.GET.get('token')

        if token is not None and token == AUTH_TOKEN_ENDPOINTS:

            payments_data = Payments.objects.filter(complete=True, processed=False)

            p_list = [{
                'fn': p.first_name,
                'cost': p.cost
            } for p in payments_data]

            payments_data.update(processed=True)

            data = {
                'ststus': True,
                'result': p_list
            }
        else:
            data = {
                'status': False,
                'text': 'Авторизация не удалась!'
            }
    else:
        data = {
            'status': False,
            'text': 'Метод роута должен быть POST!'
        }

    return HttpResponse(json.dumps(data))


def other_error(request, data, code=500):
    load_settings()

    response = render(request, 'default/info_page.html', context=data)
    response.status_code = code

    return response


def handler403(request, *args, **argv):
    load_settings()

    data = {
        'title': '403: Ошибка доступа!',
        'text': 'Доступ к этому адресу запрещен!'
    }

    return other_error(request=request, data=data)


def handler404(request, *args, **argv):
    load_settings()

    data = {
        'title': '404: Страница не найдена!',
        'text': 'Такой страницы нет!'
    }

    return other_error(request=request, data=data)


def handler500(request, *args, **argv):
    load_settings()

    data = {
        'title': '500: Ошибка сервера!',
        'text': 'Что-то пошло не так!'
    }

    return other_error(request=request, data=data)