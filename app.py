import streamlit as st
import joblib

# Carregar o modelo e o vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    vectorizer = joblib.load("vectorizer_sem_ajuste_sem_kfold-c1-gSC.pkl")
    model = joblib.load("modelo_sem_ajuste_sem_kfold-c1-gSC.pkl")
    return vectorizer, model

vectorizer, model = load_model_and_vectorizer()

# Configuração da página
st.title("Classificador de Emails - Spam ou Ham")
st.subheader("Insira um email abaixo para verificar se é Spam ou Ham")

# Entrada do usuário
email_input = st.text_area("Digite o conteúdo do email:")

# Botão de previsão
if st.button("Classificar"):
    if email_input.strip():
        # Pré-processar e prever
        email_vectorized = vectorizer.transform([email_input])
        prediction = model.predict(email_vectorized)[0]

        # Exibir resultado
        if prediction == 1:
            st.error("O email foi classificado como **SPAM**.")
        else:
            st.success("O email foi classificado como **HAM** (não é spam).")
    else:
        st.warning("Por favor, insira um conteúdo de email válido.")
