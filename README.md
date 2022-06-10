# Helper function for Habit Tracker Model

This function purposes is to receive the forecasted position and current user position and compare them to receive a boolean which will be piped to another endpoint.

## Usage

If running locally install dependencies specified at `requirements.txt` and then do the following to have a simple http server:

```bash
functions-framework --target hello --debug
 * Serving Flask app "hello" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 ```

 then do a curl to localhost

 ```bash
 curl --request POST \
  --url http://localhost:8080/ \
  --header 'Content-Type: application/json' \
  --data '{
	"prediction":[0.0, 0.0],
	"cur_position":[0.0101, 0.1001]
}'
```

to get a response with either

```bash
{
	"too_far?": "True"
}
```

or

```bash
{
    "too_far?": "False"
}
```