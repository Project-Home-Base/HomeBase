# HomeBase API Contracts

This document defines the REST API contracts between the frontend and the Python backend for the HomeBase local cloud application. 

**Base URL**: `/api`

---

## Identity Domain (`/api/identity`)

### `POST /login`
Authenticates a user and starts a session.
- **Request Body**: `{"username": "str", "password": "str"}`
- **Response**: `200 OK` with `{"token": "str", "user_id": "str"}`

### `GET /me`
Retrieves the current authenticated user's profile.
- **Response**: `200 OK` with `{"user_id": "str", "username": "str", "email": "str"}`

---

## Metadata Domain (`/api/metadata`)

### `GET /directories`
Lists virtual directories for the user.
- **Query Params**: `parent_id` (optional, string)
- **Response**: `200 OK` with `{"directories": [{"id": "str", "name": "str", "parent_id": "str", "created_at": "datetime"}]}`

### `POST /directories`
Creates a new virtual directory.
- **Request Body**: `{"name": "str", "parent_id": "str"}`
- **Response**: `201 Created` with `{"id": "str", "name": "str"}`

### `GET /files`
Lists metadata for files in a specific directory.
- **Query Params**: `directory_id` (string)
- **Response**: `200 OK` with `{"files": [{"id": "str", "name": "str", "size_bytes": integer, "sha256": "str", "created_at": "datetime"}]}`

---

## Storage Domain (`/api/storage`)

### `POST /upload`
Uploads a new file chunk or completes an upload.
- **Content-Type**: `multipart/form-data`
- **Form Data**:
  - `file`: The binary file chunk
  - `file_id`: String (optional, required if appending chunk)
  - `directory_id`: String
  - `sha256`: String (checksum of the full file or chunk)
- **Response**: `200 OK` with `{"file_id": "str", "status": "processing|completed"}`

### `GET /download/{file_id}`
Retrieves the binary content of a file.
- **Response**: `200 OK` (binary file stream or chunk stream)
