## libgen-api

### Setup
`pip install`

Run the Flask server
`python app.py`

<hr>

### Endpoints

```
GET /query
```
> Example: GET /python

**RESULT**
```json
{
    "books": [
        {
            "Author(s)": [
                "Markus Nix"
            ],
            "Book": {
                "link": "link-for-the-book",
                "title": "Exploring Python"
            },
            "Extension": "djvu",
            "Language": "German",
            "Pages": "174",
            "Publisher": "Entwickler",
            "Size": "2 Mb",
            "Year": "2005"
        },
        {
            "Author(s)": [
                "Peter C. Norton",
                "Alex Samuel",
                "Dave Aitel",
                "Eric Foster-Johnson",
                "Leonard Richardson",
                "Jason Diamond",
                "Aleatha Parker",
                "Michael Roberts"
            ],
            "Book": {
                "link": "link-for-the-book",
                "title": "Beginning Python"
            },
            "Extension": "pdf",
            "Language": "English",
            "Pages": "679",
            "Publisher": "Wiley Pub",
            "Size": "4 Mb",
            "Year": "2005"
        },
        ...
    ]

}

```

```
Example: GET /query/book_name
```
> GET /python/Exploring Python

