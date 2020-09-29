from models.feedback import MongoDB

def save_feedback_request(request):
    fields = ['title', 'message_body']

    if not all(field in request.keys() for field in fields):
        return { 
            
            "erro": "Por gentileza, preencha todos os campos para ser enviado o feedback"
            }, 400
    
    if not request["title"]:
        return {
            "erro": "Informe o título da mensagem"
            }, 400

    if not request["message_body"]:
        return {
            "erro": "Informe a descrição do feedback"
            }, 400

    db = MongoDB()

    connection_is_alive = db.test_connection()
    if connection_is_alive:
        if(db.insert_one(request)):
            return {"message": "Sucess"}, 200
    db.close_connection()

    return {'error': 'Something gone wrong'}, 500