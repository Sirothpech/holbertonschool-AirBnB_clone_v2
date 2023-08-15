# AirBnB clone - Web framework

This repository contains a Flask web application with several routes that display different messages and functionalities.

Run the Flask application:

```bash
python app.py
```

The web application will be accessible at http://0.0.0.0:5000/.

## Tasks: Routes and Functionality

### 0. Hello Flask!

- Route: `/`
- Description: Displays "Hello HBNB!"
- Usage:
  ```bash
  curl 0.0.0.0:5000
  ```

### 1. HBNB

- Route: `/hbnb`
- Description: Displays "HBNB"
- Usage:
  ```bash
  curl 0.0.0.0:5000/hbnb
  ```

### 2. C is fun!

- Route: `/c/<text>`
- Description: Displays "C " followed by the value of the text variable (replace underscore _ symbols with a space)
- Usage:
  ```bash
  curl 0.0.0.0:5000/c/is_fun
  ```

### 3. Python is cool!

- Route: `/python/<text>`
- Description: Displays "Python " followed by the value of the text variable (replace underscore _ symbols with a space). The default value of text is "is cool".
- Usage:
  ```bash
  curl -Ls 0.0.0.0:5000/python/is_magic
  ```

### 4. Is it a number?

- Route: `/number/<n>`
- Description: Displays "n is a number" only if n is an integer.
- Usage:
  ```bash
  curl 0.0.0.0:5000/number/89
  ```

### 5. Number template

- Route: `/number_template/<n>`
- Description: Displays an HTML page only if n is an integer. The page contains an H1 tag with "Number: n".
- Usage:
  ```bash
  curl 0.0.0.0:5000/number_template/89
  ```

### 6. Odd or even?

- Route: `/number_odd_or_even/<n>`
- Description: Displays an HTML page only if n is an integer. The page contains an H1 tag with "Number: n is even|odd".
- Usage:
  ```bash
  curl 0.0.0.0:5000/number_odd_or_even/89
  ```

### 7. Improve engines

- Description: Updates the FileStorage and DBStorage engines to include a `close()` method to handle deserialization and session closure.

### 8. List of states

- Route: `/states_list`
- Description: Displays an HTML page with a list of all State objects sorted by name. Each state is described as `<state.id>: <state.name>`.
- Usage:
  ```bash
  curl 0.0.0.0:5000/states_list
  ```

### 9. Cities by states

- Route: `/cities_by_states`
- Description: Displays an HTML page with a list of all State objects and their associated City objects sorted by name. States are described as `<state.id>: <state.name>`, and cities are described as `<city.id>: <city.name>`.
- Usage:
  ```bash
  curl 0.0.0.0:5000/cities_by_states
  ```

### 10. States and State

- Route: `/states`
- Description: Displays an HTML page with a list of all State objects sorted by name. Each state is described as `<state.id>: <state.name>`. Additionally, the route `/states/<id>` displays details about a specific state and its linked City objects.
- Usage:
  ```bash
  curl 0.0.0.0:5000/states
  curl 0.0.0.0:5000/states/1
  ```

### 11. HBNB filters

- Route: `/hbnb_filters`
- Description: Displays an HTML page with filters for States, Cities, and Amenities. Allows users to select filtering options for each category.
- Usage:
  ```bash
  curl 0.0.0.0:5000/hbnb_filters
  ```

## Author

This project was realized Christophe Ngan (@Sirothpech)
