# Helper function for Habit Tracker Model

This function purposes is to receive the forecasted position and current user position and compare them to receive a boolean which will be piped to another endpoint.

## Summary

A function for determining if the predicted vs current user position is more than 1 km, this is determining if user follow their regular routine that is already trained from the model. The main purpose of this function is to act as a helper for the model itself, as currently the model has a quite minimal capabilities

## Reference

By following Google's recommendation of building cloud functions development environment [here](https://cloud.google.com/functions/docs/running/overview), and by following the code examples [here](https://cloud.google.com/functions/docs/calling/http#functions-calling-http-nodejs), to act as a basis for the code development environment.

The development environment of this function is initiated by using project wide python's [virtual environment](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a,part%20of%20your%20operating%20system.), and usage of [pip](https://pypi.org/project/pip/).

## Structure

No definite structure for this repository, you can put anything on the root of the repository.

## Usage

Make sure you have made the virtual environemnt for this project with `python3 -m venv <venv_name>` if you want to run the function locally, if not invoke straight with the function endpoint.

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