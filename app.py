import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="Beans AI Chatbot",
    page_icon="☕",
    layout="centered"
)

st.title("Beans AI Chatbot")

# Sidebar branding
with st.sidebar:
    st.header("☕ Beans AI")
    st.write("Powered by beans and AI!")
    st.write("Love coffee? So do we!")
    st.markdown("---")
    st.write("Built with Streamlit & OpenAI")

# Initialize OpenAI client if API key is available
api_key = os.environ.get("OPENAI_API_KEY")
test_mode = False

with st.sidebar:
    st.subheader("🔑 API Key Setup")
    if not api_key:
        api_key = st.text_input("Enter OpenAI API Key (optional)", type="password", help="Your API key will not be stored. For production, use environment variables.")
        if api_key:
            st.success("API key set for this session!")
    
    # Test mode toggle
    test_mode = st.checkbox("Enable Test Mode", value=True, help="Use simulated AI responses without API calls for testing UI")
    if test_mode:
        st.info("Test Mode: Using simulated responses that acknowledge your questions")

client = None
if api_key and not test_mode:
    client = OpenAI(api_key=api_key)
elif not test_mode:
    st.warning("OpenAI API key not found. Set the OPENAI_API_KEY environment variable or enter it above for AI responses. Currently using echo mode.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What's brewing? ☕"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate AI response
    if test_mode:
        # Simulated test response with streaming effect
        import time
        prompt_lower = prompt.lower()
        
        # Simple Q&A logic for common questions
        if "how are you" in prompt_lower or "how do you do" in prompt_lower:
            response = f"I'm doing great, thanks for asking! As Beans AI, I'm always brewing up good conversations. ☕ How about you?"
        elif "finger" in prompt_lower and ("how many" in prompt_lower or "count" in prompt_lower):
            response = f"A human hand typically has 5 fingers! That's one thumb and four fingers. 🖐️"
        elif "dog" in prompt_lower and ("are you" in prompt_lower or "you a" in prompt_lower):
            response = f"No, I'm not a dog! I'm Beans, an AI assistant powered by coffee beans. 🐶☕ Though I do love a good pup-peroni!"
        elif "best coffee" in prompt_lower or ("what" in prompt_lower and "coffee" in prompt_lower and "best" in prompt_lower):
            response = f"The best coffee is subjective, but I recommend trying Ethiopian Yirgacheffe or Colombian Supremo! ☕ Freshly roasted and brewed properly makes all the difference. What's your favorite type?"
        elif "coffee" in prompt_lower and ("like" in prompt_lower or "know about" in prompt_lower or "tell me" in prompt_lower):
            coffee_facts = [
                f"Coffee comes from the Coffea plant, and there are over 120 species! Did you know the most common are Arabica and Robusta? ☕",
                f"Great question about coffee! The perfect brewing temperature is around 195-205°F (90-96°C). Too hot and it can taste bitter! ☕",
                f"Coffee contains over 1,000 chemical compounds! That's why it has such complex flavors. My favorite is the aroma of freshly ground beans. ☕",
                f"Coffee was discovered in Ethiopia around the 9th century. Legend says a goat herder noticed his goats getting energetic after eating red berries! ☕"
            ]
            import random
            response = random.choice(coffee_facts)
        elif "time" in prompt_lower or "date" in prompt_lower:
            from datetime import datetime
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response = f"Current time is {now}. Time flies when you're having fun conversations! ⏰"
        elif "joke" in prompt_lower:
            coffee_jokes = [
                f"Why did the coffee file a police report? It got mugged! ☕😄",
                f"What do you call a sad cup of coffee? Depresso! ☕😢",
                f"Why don't skeletons drink coffee? Because it goes right through them! ☕💀",
                f"How does a coffee bean greet its friends? 'Hey, brew-can!' ☕👋"
            ]
            import random
            response = random.choice(coffee_jokes)
        else:
            # Fallback to acknowledging responses with variety
            fallback_responses = [
                f"Thanks for asking about '{prompt}'! As Beans AI, I'm here to help with coffee-fueled insights. ☕",
                f"That's an interesting question: '{prompt}'. Let me brew up some thoughts on that...",
                f"Regarding '{prompt}' - I'm Beans, your AI assistant powered by beans! Here's what I think...",
                f"I love questions like '{prompt}'! As an AI who runs on coffee, I'd suggest...",
                f"About '{prompt}' - remember, good conversations are like good coffee: warm and energizing! Here's my take..."
            ]
            import random
            response = random.choice(fallback_responses)
        
        response_placeholder = st.empty()
        current_text = ""
        for char in response:
            current_text += char
            response_placeholder.markdown(current_text + "▌")
            time.sleep(0.03)  # Simulate typing speed
        response_placeholder.markdown(current_text)
    elif client:
        try:
            # Prepare messages for OpenAI API
            messages = [{"role": "system", "content": "You are Beans, a helpful AI assistant powered by beans. You love talking about coffee, productivity, and being awesome!"}] + st.session_state.messages[-10:]  # Last 10 messages for context
            response_obj = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150,
                stream=True  # Enable streaming for real-time responses
            )
            response = ""
            response_placeholder = st.empty()
            for chunk in response_obj:
                if chunk.choices[0].delta.content:
                    response += chunk.choices[0].delta.content
                    response_placeholder.markdown(response + "▌")  # Show typing indicator
            response_placeholder.markdown(response)  # Final response
        except Exception as e:
            response = f"Error: {str(e)}. Falling back to echo mode."
    else:
        response = f"Echo: {prompt}"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})