# Movie API Service

This is a RESTful API service for managing a list of movies.

## Requirements

- Poetry

## Installation and Running the Server

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Baltsat/restful-api
    cd restful-api
    ```

2. **Install Dependencies:**
    ```bash
    poetry install
    ```

3. **Activate the Virtual Environment:**
    ```bash
    poetry shell
    ```

4. **Run the Server:**
    ```bash
    python3 run.py
    ```

## Project Structure

- **main.py**: Точка входа в приложение, настраивает FastAPI приложение и включает роутеры.
- **models.py**: Определяет Pydantic модели для валидации данных.
- **database.py**: Обрабатывает подключения к базе данных и инициализацию.
- **crud.py**: Содержит CRUD операции.
- **routes/movie.py**: Определяет API маршруты, связанные с фильмами.
- **run.py**: Скрипт для запуска приложения.

## Endpoints

- **GET /api/movies**: Retrieve a list of movies.
- **GET /api/movies/{id}**: Retrieve a movie by ID.
- **POST /api/movies**: Create a new movie.
- **DELETE /api/movies/{id}**: Delete a movie by ID.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

[Your Name](https://github.com/Baltsat)
