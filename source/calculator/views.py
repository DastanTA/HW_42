from django.shortcuts import render

def main_page(request):
    to_response = {}
    first_number = 0
    second_number = 0
    operation = ''
    if request.GET:
        try:
            first_number = int(request.GET.get("first_number"))
            second_number = int(request.GET.get("second_number"))
        except:
            warning = "Please enter digits!"
            to_response = {'warning': warning}
        operation = request.GET.get("operation")

    if operation == "add":
        result = first_number + second_number
        to_response = {'first_number': first_number, 'second_number': second_number, 'operation': '+', 'result': result, 'equals': '='}
    elif operation == "subtract":
        result = first_number - second_number
        to_response = {'first_number': first_number, 'second_number': second_number, 'operation': '-', 'result': result, 'equals': '='}
    elif operation == "multiply":
        result = first_number * second_number
        to_response = {'first_number': first_number, 'second_number': second_number, 'operation': '*', 'result': result, 'equals': '='}
    elif operation == "divide":
        if second_number == 0:
            warning = "A number cannot be divided by 0! Don't you know?!"
            result = 'error'
            to_response = {'first_number': first_number, 'second_number': second_number, 'operation': '/', 'result': result, 'equals': '=', 'warning': warning}
        else:
            result = round(first_number / second_number, 2)
            to_response = {'first_number': first_number, 'second_number': second_number, 'operation': '/', 'result': result, 'equals': '='}
    elif first_number or second_number and not operation:
        warning = "Please, select an operation"
        to_response = {'warning': warning}

    return render(request, 'index.html', to_response)
