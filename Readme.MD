# Django Unsplash Image Gallery

This is a Django web application that allows users to view and explore images from the Unsplash API based on different categories.

## Features

- Browse images from various categories on Unsplash.
- Select a category to view corresponding images.
- Uses the Unsplash API to fetch images.

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python (3.6 or higher)
- Django (3.x or higher)
- Git

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/django-unsplash-gallery.git
   ```

2. Navigate to the project directory:

   ```
   cd django-unsplash-gallery
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Acquire API Key from Unsplash:

   - Visit the Unsplash Developer API: [Unsplash Developer](https://unsplash.com/developers)
   - Create a new application to get your access key.

5. Configure the API Key:

   - Open `settings.py` in your project's directory.
   - Replace `'YOUR_ACCESS_KEY'` with your actual Unsplash API access key.

6. Run Migrations:

   ```
   python manage.py migrate
   ```

7. Run the Development Server:

   ```
   python manage.py runserver
   ```

8. Access the Application:

   Open your web browser and navigate to `http://127.0.0.1:8000/` to access the Unsplash Image Gallery.

## Usage

- Browse the categories in the dropdown.
- Select a category to view images from that category.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open a GitHub issue or submit a pull request.

## License
```
This project is licensed under the [MIT License](LICENSE).
```

Please make sure to replace placeholders like `your-username`, `YOUR_ACCESS_KEY`, and update the project directory name as needed. Additionally, ensure that your project structure and settings match the instructions in the README.