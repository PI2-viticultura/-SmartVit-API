from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
api_url = None


@given('a pagina de registro do feedback')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-feedback-dev.herokuapp.com/feedback'
    print('url :'+api_url)


@when('ele registar os campos do feedback')
def step_impl_when(context):
    request_bodies['POST'] = {"title": "Recomendacao",
                              "message_body": "Poderia adicionar download por pdf"}
    response = requests.post(
                            'https://smartvit-feedback-dev.herokuapp.com/feedback',
                            json=request_bodies['POST']
                            )


@then('os dados devem passar pelo servico atraves do BFF e armazenar no banco')
def step_impl_then(context):
    api_bff_url = 'https://smartvit-user-bff-dev.herokuapp.com/feedback/'
    response = requests.post(
                            api_bff_url,
                            json=request_bodies['POST']
                            )
    assert response.status_code != 200