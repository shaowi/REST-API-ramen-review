<h1 align="center" id="top">REST API Ramen Reviews</h1>

---

## Table of Contents

You're sections headers will be used to reference location of destination.

- [Description](#description)
- [REST Endpoint URL](#rest-endpoint-url)
- [How To Use](#how-to-use)
- [Technologies](#technologies)
- [Author Info](#author-info)

---

## Description

> A REST API for users to send request and create new ramen reviews, modify existing ramen reviews data, delete existing ramen reviews and query on ramen reviews based on country or inputted search value.

### REST Endpoint URL

> To create, modify and delete ramen review:

- Only one ramen review is created, modified, deleted at a point of time so it is mapped by it's <i>id</i>
- Endpoint URL: ramen/<i>id</i>
  > where <i>id</i> is the unique identifier for that ramen review.

> To get ramen reviews:

- Based on user inputs', there may be multiple records of ramen reviews. The search result depends on what the data column the user filters out as well.
- Endpoint URL: ramens?country=<i>value</i>&search=<i>value</i>
  > where <i>value</i> is the value associated with the user input.

## Technologies

1. Flask
   - flask_restful
   - flask_sqlalchemy

[Back To The Top](#top)

---

## How To Use

0. Clone this repository/Download as zipped file and extract it.
1. Install Python at https://www.python.org/downloads/
2. Navigate to the this directory and install the dependencies with the command below.

```
pip install -r requirements.txt
```

3. Run the main.py file.

```
python main.py
```

4. Configure the test.py file for CRUD operations.

[Back To The Top](#top)

---

## Author Info

👤 **Lee Shao Wee**

- Website: [URL](https://leeshaowee.netlify.app/)
- Github: [@shaowi](https://github.com/shaowi)

---

## Show your support

Give a ⭐️ if this project helped you!

[Back To The Top](#top)
