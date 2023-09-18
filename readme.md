# Billz-api

This is a REST API supporting the billz app. 

Supported functionality:
- Register a User
- Login
- CRUD Bills
- Crud Upcoming Bills

## Usage
### Register a user
`POST /users/register`

EXAMPLE:
```
http://13.37.106.218/users/register

{
    "first_name":"Abadan",
    "last_name": "Kano",
    "email": "kano87@gmail.com",
    "password": "kano87",
    "phone_number": "0700123458"
}
```

Response:
```
{
    "message": "registration, successful",
    "user": {
        "phone_number": "0700123458",
        "first_name": "Abadan",
        "user_id": "02ccb40e-79dd-4d9a-9df0-0bcc2de4b5f2",
        "last_name": "Kano",
        "email": "kano87@gmail.com"
    }
}
```

### Login a User
`POST /users/login`

EXAMPLE:
```
http://13.37.106.218/users/login

{
    "email": "kano87@gmail.com",
    "password": "kano87"
}
```
Response:
```
{
    "message": "login successful",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MTE3NjA3MywianRpIjoiZjhjMTZjYWUtMmI2Mi00YTUzLThmMGQtZTQ3Nzg5NmVmYjFlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjAyY2NiNDBlLTc5ZGQtNGQ5YS05ZGYwLTBiY2MyZGU0YjVmMiIsIm5iZiI6MTY2MTE3NjA3MywiZXhwIjoxNjYxMjYyNDczfQ.VrikfaSv_IJY1Z69cZf6NPKDOxFuC04vWCS9mCKn98M",
    "user_id": "02ccb40e-79dd-4d9a-9df0-0bcc2de4b5f2"
}
```

### Post a Bill
`POST /bills`

EXAMPLE:
```
http://13.37.106.218/bills

{
    "bill_id": "edf3d7f9-28b1-4696-a747-c453c210ad79",
    "name": "Garbage",
    "amount": 150,
    "frequency": "Weekly",
    "due_date": "4",
    "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5"
}
```
Response:
```
{
    "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5",
    "due_date": "4",
    "name": "Garbage",
    "amount": 150.0,
    "frequency": "Weekly",
    "bill_id": "edf3d7f9-28b1-4696-a747-c453c210ad79"
}
```

### Update a Bill
`PUT /bills/<UUID:bill_id>`

EXAMPLE:
```
http://13.37.106.218/bills/edf3d7f9-28b1-4696-a747-c453c210ad79

{
    "amount": 120
}
```
Response:
```
{
    "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5",
    "due_date": "4",
    "name": "Garbage",
    "amount": 120.0,
    "frequency": "Weekly",
    "bill_id": "edf3d7f9-28b1-4696-a747-c453c210ad79"
}
```

### Get your bills
`GET /bills`

EXAMPLE:
```
http://13.37.106.218/bills/
```
Response:
```
[
    {
        "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5",
        "due_date": "5",
        "name": "Rent",
        "amount": 20000.0,
        "frequency": "Monthly",
        "bill_id": "e6e5ce9e-a8f6-4b9d-a971-308baf67acd1"
    },
    {
        "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5",
        "due_date": "2023-09-05",
        "name": "Water",
        "amount": 2000.0,
        "frequency": "Monthly",
        "bill_id": "e6e5ce9e-a8f6-4b9d-a971-308baf67acd2"
    },
    {
        "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5",
        "due_date": "4",
        "name": "Garbage",
        "amount": 120.0,
        "frequency": "Weekly",
        "bill_id": "edf3d7f9-28b1-4696-a747-c453c210ad79"
    }
]
```

### Post an Upcoming Bill
`POST /upcoming-bills`

EXAMPLE:
```
http://13.37.106.218/upcoming-bills

{
    "upcoming_bill_id": "ba8ac872-360d-4af6-b8ce-80784d44d372",
    "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5",
    "due_date": "2023-09-20",
    "name": "Garbage",
    "amount": 120.0,
    "frequency": "Weekly",
    "bill_id": "edf3d7f9-28b1-4696-a747-c453c210ad79",
    "paid": false
}
```
Response:
```
{
    "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5",
    "due_date": "2023-09-20",
    "name": "Garbage",
    "paid": false,
    "amount": 120.0,
    "frequency": "Weekly",
    "bill_id": "edf3d7f9-28b1-4696-a747-c453c210ad79",
    "upcoming_bill_id": "ba8ac872-360d-4af6-b8ce-80784d44d372"
}
```

### Update an Upcoming Bill
`PUT /upcoming-bills/<UUID:bill_id>`

EXAMPLE:
```
http://13.37.106.218/upcoming-bills/edf3d7f9-28b1-4696-a747-c453c210ad79

{
    "paid": true
}
```
Response:
```
{
    "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5",
    "due_date": "2023-09-20",
    "name": "Garbage",
    "paid": true,
    "amount": 120.0,
    "frequency": "Weekly",
    "bill_id": "edf3d7f9-28b1-4696-a747-c453c210ad79",
    "upcoming_bill_id": "ba8ac872-360d-4af6-b8ce-80784d44d372"
}
```

### Get your upcoming bills
`GET /upcoming-bills`

EXAMPLE:
```
http://13.37.106.218/upcoming-bills
```
Response:
```
[
    {
        "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5",
        "due_date": "2023-09-05",
        "name": "Rent",
        "paid": true,
        "amount": 20000.0,
        "frequency": "Monthly",
        "bill_id": "e6e5ce9e-a8f6-4b9d-a971-308baf67acd1",
        "upcoming_bill_id": "b46a83a9-4369-4fe9-8924-c2af7346721c"
    },
    {
        "user_id": "41e03543-93a4-4b03-863e-8c34c70a44c5",
        "due_date": "2023-09-20",
        "name": "Garbage",
        "paid": true,
        "amount": 120.0,
        "frequency": "Weekly",
        "bill_id": "edf3d7f9-28b1-4696-a747-c453c210ad79",
        "upcoming_bill_id": "ba8ac872-360d-4af6-b8ce-80784d44d372"
    }
]
```


