# ApiREST_processoSeletivo
Consultor Data Science



O objetivo aqui foi produzir uma API REST usando Flask para dar resposta as  questões descritas abaixo.

Para isso, foi codificada uma classe que em processo atua como um listener, aguardando as solicitações de serviço que são respondidas após conexão com um database mySQL. Para um 
smbiente de teste as informações de usuário e senha estão hardcoded no programa, o que não ocorreria em um ambiente de produção. Para cada questão foi codificada uma classe específica

Questão 1 - Gostaria de listar os órgãos que responderam a pesquisa, passando o ano referência do diagnóstico como parâmetro.
 Eles devem ser apresentados como uma lista de objetos e conter minimante o nome do órgão e o tipo de órgão.
 
 URL usada para solicitar o serviço em teste com o Postman: http://127.0.0.1:5000/quest1/2019
 
 Resposta obtida: (primeiras linhas)
 
 "Administra\ç\ão Indireta\"}, {\"nome\": \"SEHAB\", \"tipo\": \"Secretaria\"},
 {\"nome\": \"SUBMO\", \"tipo\": \"Subprefeitura\"}, {\"nome\": \"SMUL\", \"tipo\": \"Secretaria\"},
 {\"nome\": \"SMADS\", \"tipo\": \"Secretaria\"}, {\"nome\": \"CET\", \"tipo\": \"Administra\ç\ão Indireta\"},
 {\"nome\": \"SG\", \"tipo\": 
 
 Questão 2 - Passando o órgão como parâmetro opcional e ano como parâmetros obrigatório na chamada, gostaria que
 saber quantas pessoas trabalharam de forma dedicada à TI na Prefeitura de São Paulo.
 
 URL de teste: http://127.0.0.1:5000/quest2/2019/SF
  Resposta obtida: (primeiras linhas)
  "[{\"ano\": \"2019\", \"nome\": \"SF\", \"somaEquipe\": 43, \"tipo\": \"Secretaria\"}]"
 
 Questão 3 - Considerando que todas as pessoas que trabalharam de forma dedicada a TI receberam R$ 12.500,00/mês,
			gostaria de saber qual a proporção de custo com pessoal de TI por tipo de órgão.
			URL de teste: http://127.0.0.1:5000/quest3/
			Resposta obtida:
			"[{\"proporcao\": \"15.79%\", \"tipo\": \"Subprefeitura\"}, {\"proporcao\": \"53.77%\", \"tipo\": \"Secretaria\"},
			{\"proporcao\": \"30.43%\", \"tipo\": \"Administra\ç\ão Indireta\"}]"

Questão 4 - Gostaria de listar a quantidade de desktop próprios e desktop locados, por secretaria. 
			URL de teste: http://127.0.0.1:5000/quest4/
			
			Resposta obtida:
			"[{\"DesktopLocado\": 0, \"DesktopProprio\": 17500, \"nome\": \"SMS\", \"tipo\": \"Secretaria\"}, {\"DesktopLocado\": 0,
			\"DesktopProprio\": 1239, \"nome\": \"SMJ\", \"tipo\": \"Secretaria\"}, {\"DesktopLocado\": 0, \"DesktopProprio\": 1236,
			\"nome\": \"SMSUB\", \"tipo\": \"Secretaria\"}, {\"DesktopLocado\": 0,
			\"DesktopProprio\": 5117, \"nome\": \"SMSU\", \"tipo\": \"Secretaria\"},
			{\"DesktopLocado\": 0, 
			
	Questão 5 - Criar uma tabela cópia da tabela respostas_diagnostico apenas com os formulários qu
	e foram devidamente concluídos e aceitos. Incluir uma coluna do
	tipo datetime para gravar a data de última atualização de cada registro.
	
		create table respostas_diagnostico_copia (ultima_atualizacao datetime) select * from respostas_diagnostico where data_submissao is not null;
		
	Questão 6 - Criar um único endpoint para atualização das seguintes informações na tabela criada no item 5: Quantidade de pessoas que trabalham de forma dedicada
	, utilização de metodologia para gerenciamento de projetos, desktops próprios, locados e antigos.
	
	URL para teste: ://127.0.0.1:5000/quest6/10/2017/400/1/150/25/8/
	
	{
    "message": "Alterações efetuadas"
}
	

