# To-Do List Application (MVC Architecture)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-black?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

![image](https://github.com/user-attachments/assets/52af1a45-9da5-4690-b188-0ce2e77fb670)

## 📖 Project Overview

This repository presents a minimalist web-based To-Do List application built with Flask, meticulously structured around the Model-View-Controller (MVC) architectural pattern. The primary objective of this project is to demonstrate a clear separation of concerns, modular design principles, and effective backend development practices using Python and Flask.

The application allows users to perform standard task management operations: adding new tasks, marking existing tasks as completed (or reverting their status), and deleting tasks. Data persistence is managed via a local `tasks.json` file, serving as a straightforward, file-based mock database for demonstration purposes. This setup underscores fundamental concepts of data handling without the overhead of a full relational database, focusing instead on architectural clarity.

## ✨ Key Features

*   **Task Management:** Comprehensive CRUD (Create, Read, Update, Delete) operations for managing tasks.
    *   **Add Tasks:** Facilitates the creation of new tasks with user-defined descriptions.
    *   **View Tasks:** Displays an organized list of all current tasks.
    *   **Toggle Status:** Allows for marking tasks as `completed` or reverting them to `pending`.
    *   **Delete Tasks:** Provides functionality to permanently remove tasks from the list.
*   **Data Persistence:** Tasks are automatically saved to and loaded from `tasks.json`, ensuring data integrity across application restarts.
*   **MVC Adherence:** Strict separation of application logic into distinct Model, View, and Controller layers for enhanced maintainability and scalability.
*   **Responsive UI:** A clean and functional user interface built with standard HTML5 and CSS3, designed for basic usability.

## Technologies Utilized

*   **Python:** The core programming language for the entire backend logic and application orchestration.
*   **Flask:** A lightweight and flexible micro-web framework used for defining application routes, handling HTTP requests, and rendering templates.
*   **HTML5:** Serves as the standard markup language for structuring the web content and user interface (`index.html`).
*   **CSS3:** Employed for styling the application's visual presentation, ensuring a clean and intuitive user experience.
*   **Jinja2:** Flask's default templating engine, enabling dynamic content generation within HTML files.
*   **JSON:** Utilized as the data interchange format for persisting task data, simulating a backend data store.

## 🏗️ Project Structure & Architectural Design (MVC)

The project adheres to the MVC pattern to ensure a logical and modular organization of code, promoting scalability and ease of maintenance.

```bash
to-do-list-mvc/
├── app.py
├── requirements.txt
├── tasks.json
├── controllers/
│   └── todo_controller.py
├── data/
│   └── task_mock_data.py
├── models/
│   └── todo_list_model.py
└── templates/
    └── index.html
```

## 🚀 Setup and Local Installation

To get this project up and running on your local machine, follow these steps:

1.  **Clone the Repository:**
    Start by cloning the project from GitHub to your local development environment:
    ```bash
    git clone git@github.com:matheusenomoto/to-do-list-mvc.git
    cd to-do-list-mvc
    ```

2.  **Create a Virtual Environment (Recommended):**
    It is highly recommended to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects:
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    Once the virtual environment is active, install all necessary Python packages listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application:**
    Execute the main application file to start the Flask development server:
    ```bash
    python app.py
    ```

6.  **Access the Application:**
    Open your web browser and navigate to the address provided in the terminal (typically `http://127.0.0.1:5000/`).

## 👨‍💻 Usage Instructions

*   **Adding a New Task:** Type the desired task description into the input field at the top of the page and click the "Add Task" button.
*   **Toggling Task Status:** Click the "Complete" button next to a pending task to mark it as completed. The task's text will be struck through, and the button will change to "Undo," allowing you to revert its status.
*   **Deleting a Task:** Click the "Delete" button adjacent to any task to permanently remove it from your list.

## 📈 Future Enhancements & Potential Improvements

This project serves as a robust foundation and can be significantly expanded upon. Here are several potential enhancements that could be implemented:

*   **Database Integration:** Transition from file-based `tasks.json` to a more robust database solution (e.g., SQLite, PostgreSQL, MongoDB) using an ORM like SQLAlchemy for improved data management and scalability.
*   **User Authentication and Authorization:** Implement a user management system, allowing individual users to have their own private To-Do lists.
*   **RESTful API:** Expose the application's functionalities via a RESTful API, enabling integration with other services or front-end frameworks (e.g., React, Vue.js).
*   **Comprehensive Testing:** Develop a suite of unit tests for the Model and Controller layers, and integration tests for the Flask routes, ensuring application reliability and code quality.
*   **Enhanced User Interface (UI):** Integrate a modern CSS framework (e.g., Bootstrap, Tailwind CSS) or a JavaScript framework for a more dynamic and interactive user experience.
*   **Advanced Task Features:** Add functionalities such as task prioritization, due dates, categories, or search capabilities.
*   **Error Handling and Validation:** Implement more comprehensive input validation and error handling mechanisms to improve application robustness.
*   **Deployment:** Set up continuous integration/continuous deployment (CI/CD) pipelines for automated deployment to cloud platforms (e.g., Heroku, AWS, Render).

## 🤝 Contributing

Contributions are welcome! If you find any issues, have suggestions for improvements, or would like to add new features, please feel free to open a pull request or submit an issue.

---

#### **Matheus Enomoto**
- [Blog](https://matheusenomoto.com/)
- [LinkedIn](https://www.linkedin.com/in/matheus-lopes-enomoto/)
