import gradio as gr
import os
from brain_of_the_doctor import analyze_image_with_query, encode_image
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import multilingual_tts_response

# Set the model
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# Process user input
def process_input(user_text, image, audio_file, history=None):
    if history is None:
        history = []

    user_display = ""
    translated_text = user_text
    language_code = "en"  # default

    # Handle audio input
    if audio_file:
        try:
            audio_path = audio_file
            original_text, detected_lang, translated = transcribe_with_groq(
                "whisper-large-v3", audio_path, os.environ.get("GROQ_API_KEY")
            )
            user_display = f"🗣️ Transcribed: {original_text} ({detected_lang})"
            translated_text = translated
            language_code = detected_lang
        except Exception as e:
            user_display = f"⚠️ Audio transcription error: {e}"
            translated_text = ""

    elif user_text:
        user_display = f"📝 You said: {user_text}"
        translated_text = user_text

    # Encode image if present
    encoded_img = encode_image(image) if image else None

    # Generate AI response
    try:
        ai_response = analyze_image_with_query(
            translated_text,
            GROQ_MODEL,
            encoded_image=encoded_img,
            history=history
        )
    except Exception as e:
        ai_response = f"⚠️ Error generating AI response: {e}"

    # Update history
    history.append((translated_text, ai_response))

    # Generate voice output
    audio_output_path = multilingual_tts_response(ai_response, language_code)

    return user_display, ai_response, audio_output_path, history, history


# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🧑‍⚕️ MediSage: An Advanced Solution For Health Diagnosis Using AI (Vision and Voice)")

    state = gr.State([])  # ✅ To store persistent chat history

    with gr.Row():
        text_input = gr.Textbox(label="Type your message (optional)", placeholder="Describe your issue or question")
        image_input = gr.Image(type="filepath", label="Upload image (optional)")
        audio_input = gr.Audio(type="filepath", label="Speak instead (optional)")

    submit_btn = gr.Button("Submit")

    with gr.Row():
        user_transcript_display = gr.Textbox(label="Patient's Input", interactive=False)
        response_display = gr.Textbox(label="MediSage's Response", interactive=False)

    with gr.Row():
        audio_output = gr.Audio(label="Voice of the AI Doctor")
        chat_output = gr.Chatbot(label="Full Chat History")  # ✅ Use chatbot instead of textbox

    # Button logic
    submit_btn.click(
        fn=process_input,
        inputs=[text_input, image_input, audio_input, state],  # ✅ send state
        outputs=[
            user_transcript_display,
            response_display,
            audio_output,
            chat_output,  # ✅ update chatbot
            state         # ✅ update state
        ]
    )

demo.launch()
