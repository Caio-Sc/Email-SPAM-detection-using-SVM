# Classificador de Emails - Spam ou Ham

Este é um aplicativo web simples desenvolvido com **Streamlit** para demonstrar um modelo de classificação de emails treinado em Python usando o **Scikit-learn**. O modelo classifica emails como **Spam** (1) ou **Ham** (0, ou seja, não é spam).

## Funcionalidades
- Interface amigável para testar o modelo.
- Insira o conteúdo de um email e obtenha a classificação imediatamente.
- Feedback visual (mensagens de sucesso para Ham e erro para Spam).

## Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.7 ou superior) e as seguintes bibliotecas Python:

- `streamlit`
- `joblib`
- `scikit-learn`

Instale as dependências usando o comando:

```bash
pip install -r requirements.txt
```

## Como Configurar

1. Clone este repositório ou baixe os arquivos.
2. Certifique-se de que os seguintes arquivos estão no mesmo diretório:

    - app.py (o código do aplicativo)
    - vectorizer.joblib (o vectorizer salvo durante o treinamento do modelo)
    - model.joblib (o modelo salvo durante o treinamento)

3. Execute o aplicativo com o seguinte comando:
```bash
streamlit run app.py
```

## Como Usar

1. Abra o navegador. O Streamlit geralmente abre automaticamente no endereço http://localhost:8501.
2. Insira o texto do email no campo de entrada.
3. Clique no botão Classificar.
4. Veja o resultado:

   - HAM: O email foi classificado como não sendo spam.
   - SPAM: O email foi identificado como spam.

## Personalização
- Caso precise treinar um novo modelo, salve-o novamente usando o joblib:

```bash
from joblib import dump
dump(model, 'model.joblib')
dump(vectorizer, 'vectorizer.joblib')
```

- Substitua os arquivos existentes no diretório para atualizar o modelo ou o vectorizer.
