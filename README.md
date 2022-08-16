# Domo Slack Relay

A simple Google Cloud Function for sending alerts from Domo to slack webhook URLs.

## Deployment

Clone the repository then deploy the cloud function normally with the python 3.10 runtime with an http trigger and allow unauthenticated requests.

```bash
gcloud functions deploy <function name> \
    --runtime python310 \
    --trigger-http \
    --allowunauthenticated
```

## Usage
Create the alert as specified in [this documentation in domo](https://domohelp.domo.com/hc/en-us/articles/360042925994-Creating-an-Alert-for-a-DataSet).

Follow the instructions to attach a webhook action in [this section of the documentation](https://domohelp.domo.com/hc/en-us/articles/360042925994-Creating-an-Alert-for-a-DataSet#2.3.1.):

- For the URL, input the url for your cloud function.
- For the request method, choose POST.
- Customize the alert message for the webhook action, the first line should be the webhook URL you would like to send the message to. The actual alert message should start on the second line.