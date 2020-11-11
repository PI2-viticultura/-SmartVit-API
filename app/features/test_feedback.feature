Feature: Captar requisicao feita no frontend e enviar ao microsservico feedback atraves do BFF 
  Como Sistema, quero pegar os dados informados no frontend pelo usuario,
  e registra-los no meu servico.

  Context: O usuario registra o feedback 
    Dado que os dados resgistrados utilizem o servico atraves do BFF

    Scenario: Usuario registrar feedback desejado
        Given a pagina de registro do feedback
        When ele registar os campos do feedback
        | title        | message_body                       | 
        | Recomendacao | Poderia adicionar download por pdf | 
        Then os dados devem passar pelo servico atraves do BFF e armazenar no banco
        | title        | message_body                       | 
        | Recomendacao | Poderia adicionar download por pdf | 