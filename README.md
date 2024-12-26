# Django Client Management Project

A REST API project for managing clients, projects, and user assignments using Django and SQLite.

## Features
- Manage clients (create, retrieve, update, delete).
- Assign projects to clients and users.
- Retrieve projects assigned to logged-in users.

## Setup

1. **Clone the Repository**  
   ```bash
   git clone <repository-url>
   cd client_project1
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a Superuser**  
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Server**  
   ```bash
   python manage.py runserver
   ```

# Database Design

### 1. **User** (Django Default)
- **id**, **username**, **email**, **password**, etc.

### 2. **Client**
- **id**: Primary Key  
- **client_name**: String  
- **created_at**, **updated_at**: Timestamps  
- **created_by**: FK → User  

### 3. **Project**
- **id**: Primary Key  
- **project_name**: String  
- **client**: FK → Client  
- **created_at**: Timestamp  
- **created_by**: FK → User  
- **users**: M2M → User  

### Relationships
- **User ↔ Client**: One-to-Many  
- **Client ↔ Project**: One-to-Many  
- **Project ↔ User**: Many-to-Many  

## Endpoints
- Admin Panel: `/admin/`
- API Root: `/api/`




