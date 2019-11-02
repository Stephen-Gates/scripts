# Create Documents

A Python script that reads a CSV file for document links and adds them to existing fact sheets.

The CSV file is called `Book1.csv`, has semi-colon separated values, and contains:

- fact sheet id (required)
- document name (required)
- document url (required)
- document description (optional)

You need to add your API token to the line:

```python
api_token = '<API-Token>'
```

*Warning: Don't do this in a Public Repository like this one.*
