from google.cloud import aiplatform

# Inicializa el entorno
aiplatform.init(
    project="proyecto-1-461620",
    location="us-central1",
)

# Envía el pipeline a Vertex AI Pipelines
job = aiplatform.PipelineJob(
    display_name="xgb-distributed-training",
    template_path="distributed_pipeline.json",
    enable_caching=False,
)

# 👉 El parámetro `service_account` va aquí
job.run(service_account="vertex-ai-pipeline-sa@proyecto-1-461620.iam.gserviceaccount.com", sync = True)


