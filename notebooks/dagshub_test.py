import dagshub
import mlflow
mlflow.set_tracking_uri("https://dagshub.com/dwt012/water-safety-prediction-mlops-.mlflow")
dagshub.init(repo_owner='dwt012', repo_name='water-safety-prediction-mlops-', mlflow=True)

# import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
