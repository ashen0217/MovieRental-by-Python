# Movie Rental System (Python)

A simple command-line application for managing a movie rental store. This project demonstrates basic object-oriented programming, file handling, and separation of concerns using Python.

## Features

- Add, list, and manage DVDs
- Borrow and return DVDs
- Track rental and borrowing history
- Data persistence using text files

## Folder Structure

```
Movie-rental-in-python-master/
├── borrow.txt                # Borrow records
├── dvd.txt                   # DVD records
├── main.py                   # Entry point
├── controller/               # Business logic controllers
├── domain/                   # Core domain models and validators
├── repository/               # Data access and repositories
└── ui/                       # User interface (CLI)
```

## Getting Started

1. **Clone the repository**
2. **Navigate to the project folder**
3. **Run the application:**
   ```sh
   python Movie-rental-in-python-master/main.py
   ```

The program will create `borrow.txt` and `dvd.txt` automatically if they do not exist.

## Requirements

- Python 3.x

## Usage

Follow the on-screen menu to manage DVDs and rentals.

## License

This project is for educational purposes.
