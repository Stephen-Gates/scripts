# Import Metrics

A Python script that reads an Excel file and adds metrics to existing fact sheets.

The XLS file is called `input.xlsx` and contains:

- measurement
- fact sheet id
- date
- key
- value

You'll need to add your own values to the lines:

```python
api_token = '<API-Token>'
ws_id = '<WS-ID>'
```

 *Warning: Don't do this in a Public Repository like this one.*

Learn more about metrics at:

- <https://docs.leanix.net/docs/metrics>
- <https://dev.leanix.net/docs/api-overview#section-metrics-api-real-time-data>
