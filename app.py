<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 30px;
        }
        h1 {
            margin-bottom: 30px;
        }
        .botao {
            display: inline-block;
            padding: 15px 25px;
            margin: 10px;
            background-color: #0077cc;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
        }
        .botao:hover {
            background-color: #005fa3;
        }
    </style>
</head>
<body>
    <h1>Bem-vindo, {{ perfil }}!</h1>

    {% if perfil == 'ADM' %}
        <a class="botao" href="https://app.powerbi.com/view?r=LINK_PBI_ADMIN" target="_blank">Relatório Geral (ADM)</a>
        <a class="botao" href="https://app.powerbi.com/view?r=LINK_PBI_NIVEL1" target="_blank">Relatório Nível 1</a>
        <a class="botao" href="https://app.powerbi.com/view?r=LINK_PBI_NIVEL2" target="_blank">Relatório Nível 2</a>
        <a class="botao" href="https://app.powerbi.com/view?r=LINK_PBI_NIVEL3" target="_blank">Relatório Nível 3</a>
    {% elif perfil == 'NIVEL1' %}
        <a class="botao" href="https://app.powerbi.com/view?r=LINK_PBI_NIVEL1" target="_blank">Relatório Nível 1</a>
    {% elif perfil == 'NIVEL2' %}
        <a class="botao" href="https://app.powerbi.com/view?r=LINK_PBI_NIVEL2" target="_blank">Relatório Nível 2</a>
    {% elif perfil == 'NIVEL3' %}
        <a class="botao" href="https://app.powerbi.com/view?r=LINK_PBI_NIVEL3" target="_blank">Relatório Nível 3</a>
    {% else %}
        <p>Seu perfil não tem acesso a relatórios.</p>
    {% endif %}

    <p style="margin-top: 40px;">
        <a href="{{ url_for('logout') }}">Sair</a>
    </p>
</body>
</html>
