# S1 : List users
get : http://localhost:8000/users/

# S2 : Create user
POST : http://localhost:8000/users/
params:
    username: "John"
    password: "123"
    first_name: "John"
    last_name: "Doe"
    email: "johnDoe@gmail.com"

# S3 : Login user
POST : http://localhost:8000/auth
params:
    username: "John"
    password: "123"
returns :
    Login Token


# S4 : Remove User
POST : http://localhost:8000/users/removeUser/
params:
    username: "John"
returns :
    True

# S5 : Update user
POST : http://localhost:8000/users/updateUser/
params:
    username: "John"
    password: "123"
    first_name: "John"
    last_name: "Doe"
    email: "

# S6 : get specific user
GET : http://localhost:8000/users/{id}

# S7 : addExchange
POST : http://localhost:8000/exchange/addExchange/
params:
    username: "John"
    booksell : "ISN NUMBER"
    bookBuy1 : "ISBN NUMBER"
    bookBuy2 : "ISBN NUMBER"
    bookBuy3 : "ISBN NUMBER"
    [HIDDEN] : username

What I need to do
- take username and fetch user
- take booksell and fetch booksell
- take bookBuy1 and fetch bookBuy1
- take bookBuy2 and fetch bookBuy2
- take bookBuy3 and fetch bookBuy3
- create exchangeName as username-booksell and set it in username