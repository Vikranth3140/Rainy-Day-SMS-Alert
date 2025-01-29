# Rainy-Day-SMS-Alert

A comparative analysis of OpenAI's GPT-4o and DeepSeek's R1 models for weather-based SMS alerts, powered by [OpenWeatherMap](https://openweathermap.org) API.

---

## 📌 Project Overview

This project evaluates code implementations from [OpenAI](https://openai.com) [ChatGPT](https://openai.com/index/chatgpt/) [4o](https://openai.com/index/hello-gpt-4o/) and [DeepSeek](https://www.deepseek.com) [R1](https://github.com/deepseek-ai/DeepSeek-R1) to create an automated SMS alert system for rainy weather. The goal is to compare how each AI model structures, optimizes, and extends a base Python script that fetches weather data and sends SMS notifications.

---

## ✨ Features

- **Real-Time Weather Checks**: Uses OpenWeatherMap API to fetch live weather data.
- **SMS Alerts**: Sends SMS notifications via Twilio (or similar service) when rain is detected.
- **Model Comparison**: Compares code quality, error handling, and extensibility between GPT-4o and DeepSeek R1.
- **Hybrid Implementations**: Includes improved versions where each model iterates on the other's code.

---

## 📂 Repository Structure

| File                               | Description                                                                                   |
|------------------------------------|-----------------------------------------------------------------------------------------------|
| [base-code.py](base-code.py)       | Initial code template for weather checks and SMS alerts.                                      |
| [gpt4o.py](gpt4o.py)               | Implementation by **OpenAI GPT-4o** based on `base-code.py`.                                 |
| [deepseekr1.py](deepseekr1.py)     | Implementation by **DeepSeek R1** based on `base-code.py`.                                   |
| [improved-hybrid-deepseekr1.py](improved-hybrid-deepseekr1.py) | DeepSeek R1's improved version of GPT-4o's code.                                              |
| [improved-hybrid-gpt4o.py](improved-hybrid-gpt4o.py) | GPT-4o's improved version of DeepSeek R1's code.                                              |

---

## 🛠️ Setup & Usage

### Prerequisites
- Python 3.x
- API Keys:
  - [OpenWeatherMap API Key](https://openweathermap.org/api)
  - [Twilio Account SID & Auth Token](https://www.twilio.com/docs/usage/api) (for SMS)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Vikranth3140/Rainy-Day-SMS-Alert.git
   cd Rainy-Day-SMS-Alert
   ```
2. Install dependencies:
   ```bash
   pip install requests python-dotenv
   ```
3. Create a `.env` file:
   ```env
   OPENWEATHER_API_KEY="your_api_key"
   TWILIO_ACCOUNT_SID="your_twilio_sid"
   TWILIO_AUTH_TOKEN="your_twilio_token"
   TWILIO_PHONE_NUMBER="+1234567890"
   USER_PHONE_NUMBER="+0987654321"
   ```

### Run the Script
Execute any version (e.g., GPT-4o's implementation):
```bash
python gpt4o.py
```

---

## 📊 Model Comparison Results

| Metric              | GPT-4o Implementation          | DeepSeek R1 Implementation     |
|---------------------|---------------------------------|---------------------------------|
| **Code Readability**| Clean, modular structure       | Concise, functional approach   |
| **Error Handling**  | Robust try-except blocks       | Basic error checks              |
| **Extensibility**   | Easily customizable            | Minimalist design               |
| **API Integration** | Uses `python-dotenv` for keys  | Direct variable assignments     |

---

## 🤝 Contributing

Contributions are welcome! 
1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-idea`.
3. Commit changes: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-idea`.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙌 Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org).
- SMS functionality powered by [Twilio](https://www.twilio.com).
- AI models: [OpenAI GPT-4o](https://openai.com) and [DeepSeek R1](https://deepseek.com).

---

## 💬 Discussion

- **ChatGPT 4o Conversation**: [View Here](https://chatgpt.com/share/67996afd-30ec-8009-b3e7-2763cddcda4f)
- **DeepSeek R1 Chat**: Not publicly shareable yet.

---

**Let it rain… but only in your app!** 🌧️🚀