# SlackBoxLive
Using the unofficial [Xbox Live API](xboxapi.com), this service is meant to be integrated into Slack such that friend status changes will be reported to a Slack Channel.

```bash
$ docker run sbl
Usage: main [OPTIONS]

Options:
  --api-key TEXT  API Key provided by xboxapi.com
  --user-id TEXT  User ID of the account to use for notification
  --help          Show this message and exit.
  ```