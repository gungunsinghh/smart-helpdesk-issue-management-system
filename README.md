# Smart Helpdesk & Issue Management System

A backend-based helpdesk system developed using Python Flask and MongoDB for managing support tickets through RESTful APIs.

## Features

- Create support tickets
- View all tickets
- Update ticket status and priority
- Delete support tickets
- REST API-based architecture
- MongoDB Atlas database integration
- Environment-based configuration
- CRUD operations

## Tech Stack

- Python
- Flask
- MongoDB Atlas
- PyMongo
- REST API
- Git & GitHub

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/tickets` | Create a new ticket |
| GET | `/api/tickets` | Retrieve all tickets |
| PUT | `/api/tickets/<ticket_id>` | Update ticket status/priority |
| DELETE | `/api/tickets/<ticket_id>` | Delete a ticket |

## Ticket Information

Each ticket can contain:

- Title
- Description
- Priority
- Category
- Status

## Project Structure

```text
Smart Helpdesk & Issue Management System/
│
├── app.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
