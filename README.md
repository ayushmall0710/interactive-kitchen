# Interactive Kitchen API Documentation

Welcome to the Interactive Kitchen API! This documentation provides an overview of the available endpoints and their usage. All endpoints require authentication unless otherwise specified.

## **Base URL**
`http://<your-domain>/api/`

---

## **Authentication**

### **Register**
**POST** `/auth/register/`

#### Request:
```json
{
    "username": "example_user",
    "email": "user@example.com",
    "password": "secure_password",
    "date_of_birth": "2000-01-01"
}
```

#### Response:
```json
{
    "token": "your_auth_token"
}
```

### **Login**
**POST** `/auth/login/`

#### Request:
```json
{
    "username": "example_user",
    "password": "secure_password"
}
```

#### Response:
```json
{
    "token": "your_auth_token"
}
```

### **Logout**
**POST** `/auth/logout/`

#### Response:
```json
{
    "message": "Logged out successfully"
}
```

---

## **Inventory Management**

### **Get All Inventory Items**
**GET** `/inventory/`

#### Response:
```json
[
    {
        "id": 1,
        "name": "Milk",
        "quantity": 2,
        "unit": "liters",
        "expiration_date": "2025-01-15",
        "added_by": 1
    }
]
```

### **Create Inventory Items**
**POST** `/inventory/`

#### Request:
```json
[
    {
        "name": "Milk",
        "quantity": 2,
        "unit": "liters",
        "expiration_date": "2025-01-15"
    },
    {
        "name": "Eggs",
        "quantity": 12,
        "unit": "pieces",
        "expiration_date": "2025-01-20"
    }
]
```

#### Response:
```json
[
    {
        "id": 1,
        "name": "Milk",
        "quantity": 2,
        "unit": "liters",
        "expiration_date": "2025-01-15",
        "added_by": 1
    },
    {
        "id": 2,
        "name": "Eggs",
        "quantity": 12,
        "unit": "pieces",
        "expiration_date": "2025-01-20",
        "added_by": 1
    }
]
```

### **Update Inventory Item**
**PUT** `/inventory/<id>/`

#### Request:
```json
{
    "name": "Milk",
    "quantity": 3,
    "unit": "liters",
    "expiration_date": "2025-01-18"
}
```

#### Response:
```json
{
    "id": 1,
    "name": "Milk",
    "quantity": 3,
    "unit": "liters",
    "expiration_date": "2025-01-18",
    "added_by": 1
}
```

### **Delete Inventory Item**
**DELETE** `/inventory/<id>/`

#### Response:
```json
{
    "message": "Item deleted successfully."
}
```

---

## **Recipe Suggestions**

### **Suggest Recipes**
**POST** `/recipe/suggest/`

#### Request:
```json
{
    "ingredients": [
        {"name": "Tomato", "quantity": 500, "unit": "g", "expiration_date": "2025-01-13"},
        {"name": "Cheese", "quantity": 200, "unit": "g", "expiration_date": "2025-02-02"}
    ], // optional, defaults to full inventory of current user
    "cuisine": "Italian",
    "spicy_level": "Low",
    "cooking_time": "30 minutes"
}
```

#### Response:
```json
{
    "user": {
        "username": "example_user",
        "email": "user@example.com"
    },
    "recipes": [
        {
            "recipe": "Cheesy Tomato Pasta",
            "ingredients": [
                {"name": "Tomato", "quantity": 500, "unit": "g", "expiration_date": "2025-01-13"},
                {"name": "Cheese", "quantity": 200, "unit": "g", "expiration_date": "2025-02-02"}
            ],
            "cuisine": "Italian",
            "spicy_level": "Low",
            "cooking_time": 30,
            "instructions": "1. Cook pasta. 2. Prepare sauce. 3. Combine and serve."
        }
    ]
}
```

---

## **User Management**

### **Get All Users**
**GET** `/users/`

#### Response:
```json
[
    {
        "id": 1,
        "username": "example_user",
        "email": "user@example.com",
        "date_of_birth": "2000-01-01"
    }
]
```

---

## **Notes**
1. **Authentication**: Most endpoints require an authentication token in the `Authorization` header:
   ```
   Authorization: Token <your_auth_token>
   ```

2. **Error Handling**:
   - Missing or invalid data will return a `400 Bad Request`.
   - Authentication issues return a `401 Unauthorized`.
   - Server issues return a `500 Internal Server Error`.

Feel free to reach out for any clarifications or support!

