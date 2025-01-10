# CarValueAI

## Overview
**CarValueAI** is a machine learning-powered web application for predicting car prices based on various input features such as brand, year of manufacture, fuel type, and mileage. This project utilizes a pre-trained machine learning model and provides an intuitive user interface built using Streamlit.

---

## Features
- **Accurate Predictions**: Leverages a pre-trained machine learning model for precise car price estimation.
- **Interactive UI**: Users can input details like car brand, year, mileage, engine capacity, and more.
- **Custom Styling**: A modern and user-friendly design with CSS enhancements.
- **Data-Driven Insights**: Processes categorical and numerical data seamlessly for accurate predictions.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Streamlit
- pandas
- pickle

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MLPRJ.git
   cd MLPRJ/CarValueAI
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the following files in the project directory:
   - `model.pkl`: Pre-trained machine learning model.
   - `Cardetails.csv`: Dataset for reference.

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open the application in your web browser at:
   ```
   http://localhost:8501
   ```

---

## Usage
1. Enter the car details in the provided input fields:
   - Select the **Car Brand**.
   - Choose the **Year of Manufacture** using the slider.
   - Specify **KMs Driven**, **Fuel Type**, **Transmission**, etc.
2. Click the **Predict Price** button.
3. View the predicted car price displayed below the form.

---

## File Structure
```
CarValueAI/
├── app.py               # Main application script
├── model.pkl            # Pre-trained ML model (required for predictions)
├── Cardetails.csv       # Dataset containing car details
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Technologies Used
- **Python**: Core programming language
- **Streamlit**: Web application framework
- **pandas**: Data manipulation and preprocessing
- **pickle**: Model serialization

---

## Future Enhancements
- **Enhanced Styling**: Improve UI/UX with advanced CSS and animations.
- **Additional Features**: Integrate graphs and visualizations for user insights.
- **Multi-language Support**: Expand the app's accessibility for global users.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.

---

## Acknowledgements
- The dataset used is from [Kaggle](https://www.kaggle.com/).
- Special thanks to the open-source community for providing tools and resources.
