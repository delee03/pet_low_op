# Pet Manager

A comprehensive pet management system built with FastAPI that allows users to manage pets, owners, and related information.

## Project Overview

Pet Manager is a RESTful API service designed to help veterinary clinics, pet shelters, or pet owners manage information about pets and their owners. The application provides endpoints for creating, reading, updating, and deleting pet and owner records.

## Features

- Owner management (create, read, update, delete)
- Pet management (create, read, update, delete)
- Relationship management between pets and owners
- Data validation and error handling
- RESTful API design

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLAlchemy ORM
- **API Documentation**: Swagger UI (provided by FastAPI)
- **Project Structure**: Modular design with repositories, services, and routers

## Project Structure

```
pet_manager/
├── app/
│   ├── models/          # Database models
│   ├── repositories/    # Data access layer
│   ├── routers/         # API endpoints
│   ├── schemas/         # Pydantic models for request/response
│   ├── services/        # Business logic
│   ├── db.py            # Database configuration
│   └── main.py          # Application entry point
└── README.md            # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pet_manager.git
   cd pet_manager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python -m app.db
   ```

### Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the API documentation:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## API Endpoints

- `GET /owners` - List all owners
- `POST /owners` - Create a new owner
- `GET /owners/{owner_id}` - Get owner details
- `PUT /owners/{owner_id}` - Update owner information
- `DELETE /owners/{owner_id}` - Delete an owner
- `GET /owners/{owner_id}/pets` - List all pets for an owner
- `POST /owners/{owner_id}/pets` - Add a pet to an owner

Similar endpoints exist for pets and other resources.

## Contributing

We welcome contributions to the Pet Manager project! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request

### Contribution Guidelines

- Follow the existing code style and conventions
- Write tests for new features
- Update documentation as needed
- Make sure all tests pass before submitting a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FastAPI for the excellent web framework
- SQLAlchemy for the ORM functionality
- All contributors who have helped improve this project
