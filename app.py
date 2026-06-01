import streamlit as st

st.title("🤖 Student Mental Health Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box at bottom
user_input = st.chat_input("Type your message here...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    text = user_input.lower()

    if "happy" in text:
        response = "😊 I'm glad you're feeling happy."

    elif "stress" in text or "exam" in text:
        response = "📚 Academic stress is common. Try taking breaks and managing your study schedule."

    elif "sad" in text:
        response = "💙 I'm sorry you're feeling sad. Talking to friends or family can help."

    elif "hopeless" in text:
        response = "⚠️ It sounds like you're going through a difficult time. Please consider speaking with a counselor or trusted person."

    else:
        response = "Thank you for sharing your thoughts with me."

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()