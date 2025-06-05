from kfp import dsl

@dsl.container_component
def training_step():
    return dsl.ContainerSpec(
        image='us-central1-docker.pkg.dev/proyecto-1-461620/my-kfp-repo/train-distributed:latest',
        command=[
            'accelerate', 'launch', 'train.py'
        ],
        args=[
            '--gcs_path=2025_06',
            '--output_dir=./results'
        ]
    )

@dsl.container_component
def evaluation_step():
    return dsl.ContainerSpec(
        image='us-central1-docker.pkg.dev/proyecto-1-461620/my-kfp-repo/train-distributed:latest',
        command=[
            'python3', 'evaluate.py'
        ],
        args=[
            '--gcs_path=2025_06',
            '--model_path=2025_06/outputs'
        ]
    )

@dsl.pipeline(name="xgb-distributed-training-and-eval")
def distributed_pipeline():
    train = training_step()
    evaluate = evaluation_step()
    evaluate.after(train)