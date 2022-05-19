import os


path_to_pipeline_deployment = "pipeline_deployment/pipeline_deployment.py"
path_to_config = "pipeline_deployment/pipeline_config.json"


if __name__ == '__main__':
    os.system(f"python {path_to_pipeline_deployment} --config_path {path_to_config}")