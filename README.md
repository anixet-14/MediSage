# 🧠 MediSage

**MediSage** is a **Multimodal Health Diagnosis Assistant** powered by advanced **LLMs**, **speech processing**, and **language translation**. It simulates a real-time voice-driven doctor-patient interaction—accepting symptoms via voice in any language, translating them, diagnosing with a Groq-hosted LLM (like LLaMA3), and responding back with synthesized speech.

---

## 📌 Features

- 🎙️ **Voice-to-Text** – Patient speaks symptoms through microphone.
- 🌍 **Language Translation** – Auto-detects language and converts to English.
- 🧠 **AI Doctor Brain** – Uses **Groq** (LLama3/Mixtral) for smart medical responses.
- 🔊 **Text-to-Speech** – Doctor’s response is spoken back via voice.
- 🔁 **Interactive Loop** – Complete conversational cycle via CLI.
- ✅ Modular Python scripts for each function (I/O, LLM, STT, TTS, translation).

---

## 🧩 Project Structure

```
📦 MediSage/
 ┣ 📄 app.py                  # Main execution loop
 ┣ 📄 brain_of_the_doctor.py  # Groq API call for diagnosis
 ┣ 📄 voice_of_the_patient.py # Speech recognition + translation
 ┣ 📄 voice_of_the_doctor.py  # TTS (Google TTS or ElevenLabs)
 ┣ 📄 requirements.txt        # Python dependencies
```

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/medisage.git
cd medisage
```

### 2. Install Python Requirements

```bash
pip install -r requirements.txt
```

### 3. Add Your API Key

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

(Optional: If using ElevenLabs TTS, include `ELEVEN_API_KEY` too)

### 4. Run the App

```bash
python app.py
```

---

## 🧪 Workflow

1. **Patient Speaks**: Audio is recorded.
2. **STT & Translation**: Whisper transcribes audio; translated to English if needed.
3. **LLM Inference**: Groq API generates diagnosis from symptoms.
4. **Doctor Speaks**: AI response is converted back to audio using TTS.

---

## 🛠️ Tech Stack

| Component        | Tool / Library         |
|------------------|------------------------|
| Voice Input      | `speechrecognition`, `pydub` |
| Transcription     | Whisper (via `Groq`)   |
| Translation      | `langdetect`, `deep-translator` |
| LLM Response     | `groq` (LLaMA3 / Mixtral) |
| TTS              | `gTTS`, optionally `elevenlabs` |
| CLI Interface    | Python (Modular Scripts) |

---

## 🧠 Sample Dialogue

> **Patient (Hindi)**: "मुझे बुखार और गले में खराश है।"  
> ➤ Translated: "I have fever and sore throat."  
> ➤ Diagnosis: "These may be symptoms of viral infection. Stay hydrated and consider paracetamol."  
> ➤ Played via TTS.


## 🚀 Demo
![MediSage](./examples/example1.png)

---

## 🔒 Security Note

- Never expose API keys in code.
- Always use `.env` and `python-dotenv` (already integrated).

---

## 🧭 Future Roadmap

- [ ] Gradio/Streamlit UI
- [ ] Visual symptom input (images)
- [ ] Persistent memory across turns
- [ ] Medical record logging

---

## 🙌 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Groq Console](https://console.groq.com/)
- [Deep Translator](https://pypi.org/project/deep-translator/)
- [gTTS / ElevenLabs](https://gtts.readthedocs.io/)

---

## 📄 License

This project is under the **MIT License**. See `LICENSE` for details.
