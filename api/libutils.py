from datetime import datetime, timezone

def utils_convert_timestamp_to_datetime(ts, format="%Y-%m-%dT%H:%M:%S.%fZ"):
# {
	dt_object = datetime.fromtimestamp(ts, tz=timezone.utc)
	dt_formated = dt_object.strftime(format)
	return dt_formated
# }