Gestão Financeira Pessoal
=========================

Sistema antigo criado para controle pessoal de finanças.

Este sistema será reescrito em breve.

# para rodar

* Clone o repositório
* Crie um virtualenv com Python 3.5
* Ative o virtualenv
* Instale as dependências
* Rode as migrações de banco
* Crie um super usuário
* Rode o servidor
* Acesse em [http://localhost:8000](http://localhost:8000)

```shell
git clone git@github.com:fsevero/financial-manager-v0.git financial
cd financial
python -m venv .financial
source .financial/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# Conceitos

Sistema se encontra somente dentro do **admin** (/admin)

**Contas** gerencia diferentes contas bancárias onde serão feitos lançamentos de receitas e despesas.
Exemplo: conta do banco do brasil, poupança, minha carteira.

**Itens** são "classificações para os gastos".
Exemplo: mercado, gasolina, passagem, etc.

**Mensais** são previsões de receitas e despesas que são fixas todos os meses.
Estas informações **não são lançadas automaticamente**.
Exemplos: salário, gasolina, luz, conta do cartão de crédito.

**Despesas** são valores que retiram saldo da sua conta.

**Receitas** são valores que acrescentam saldo na sua conta.