# 🌿 Health Tips Generator 🌿

Welcome to the Health Tips Generator! This project leverages Flask, OPAL for policy-based access control, and a weather API to provide users with tailored health tips based on current weather conditions. 🚀

## 📝 Project Overview

This application generates health tips based on the current weather of a given location. Access control is enforced using OPAL, ensuring only authorized roles can view or edit health tips. 

### Key Features

- 🌐 **Flask Web Application**: A user-friendly interface for generating health tips.
- 🔒 **Policy-Based Access Control**: Enforced using OPAL.
- ☁️ **Weather-Based Health Tips**: Tips are generated based on real-time weather data.

## 🛠️ Setup and Installation

Follow these steps to set up and run the project locally:

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- OPAL server

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Harshit-shrivastav/Health-Tips.git
    cd Health-Tips
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup environment variables**:
    Create a `.env` file in the project root and add the following:
    ```env
    WEATHER_API_URL=https://api.weatherapi.com/v1/current.json
    WEATHER_API_KEY=your_weather_api_key
    OPAL_SERVER_URL=http://localhost:7002
    ```

5. **Run OPAL server**:
    ```bash
    opal-server
    ```

6. **Synchronize policies and data**:
    ```bash
    python data_config.py
    ```

7. **Run the Flask application**:
    ```bash
    flask run
    ```

## 📜 Usage

- Open your browser and navigate to `http://127.0.0.1:5000`.
- Select a user role and enter a location to generate health tips.


## 🏗️ Project Structure

```plaintext
health_tips_app/
├── app.py
├── policies.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│        └── style.css    
├── opal_config.py
├── data_config.py
└── .env
```

## 🎨 Customization

Feel free to customize the project by adding more features or improving the UI. Contributions are welcome!

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Thanks to [WeatherAPI](https://www.weatherapi.com/) for providing the weather data.
- Inspired by the OPAL policy-based access control framework.
