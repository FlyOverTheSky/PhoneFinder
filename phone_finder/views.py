from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from phone_finder.finder import search_phone_details
from phone_finder.forms import CheckPhoneForm


@api_view(['GET'])
def get_phone_data(request):
    number = str(request.data.get('phone_number'))
    print(request.data)
    phone_form = CheckPhoneForm(request.data)
    if not phone_form.is_valid():
        raise ValidationError(phone_form.errors)
    find_results = list(*search_phone_details(number))
    output = {
        'Номер телефона': number,
        'Оператор': find_results[4],
        'Регион': find_results[5]
    }
    return Response(data=output, status=status.HTTP_200_OK)


def find_phone(request):
    if request.method == "POST":
        phone_form = CheckPhoneForm(request.POST)
        print(request.POST)
        if phone_form.is_valid():
            phone_number = str(phone_form.cleaned_data["phone_number"])
            find_results = list(*search_phone_details(phone_number))
            output = {
                'Номер телефона': phone_number,
                'Оператор': find_results[4],
                'Регион': find_results[5]
            }
            return render(request, "phone_results.html", {"results": output})
        else:
            return HttpResponse(f"Invalid data {phone_form.errors} try again")
    else:
        phone_form = CheckPhoneForm()
        return render(request, "find_phone.html", {"form": phone_form})
