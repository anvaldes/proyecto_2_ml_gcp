FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY requirements.txt .
COPY train.py .
COPY evaluate.py .
COPY modelo_base/ ./modelo_base/
COPY config_accelerate.yaml .
RUN mkdir -p /root/.cache/huggingface/accelerate && \
    cp config_accelerate.yaml /root/.cache/huggingface/accelerate/default_config.yaml

# Instalar dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Comando por defecto para entrenamiento distribuido
# CMD ["accelerate", "launch", "train.py", \
#     "--gcs_path=gs://proyecto_2_ml_central/2025_06", \
#     "--output_dir=./results"]