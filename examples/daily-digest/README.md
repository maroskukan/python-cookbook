# Daily Digest Application

## External Content Retrieval

### Weather data

In order to retrieve data from [Openweathermap](https://openweathermap.org), you need to make sure the following system variable exist and is valid.

```bash
# Example credentials
export OW_API_KEY=3eabc245650b64b87867afc08e5d1bac
```

### Twitter data

In order to retrieve data from [Twitter](https://twitter.com), you need to make sure the following system variable exist and is valid. Finally, the minimum level you need for Twitter API v2 is Elevated.

```bash
# Example credentials
export TWT_API_KEY=pkfeaLKilhfajioH@Qhfwaszw
export TWT_SECRET_KEY=jkfLAISJF5056WOPJFA8400ifal43lljkkljo8nfkjqnioj289
```

## Messaging

### Email Support

In order to send the email digest, you need to make sure the following system variables exists and are valid.

```bash
# Example credentials
export EMAIL_USER=0foap20rsflakf
export EMAIL_PASS=opgkapojsgiwoa
```

These are being used to send outgoing mail to SMTP server hosted at [mailtrap.io](https://mailtrap.io)