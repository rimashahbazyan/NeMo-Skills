from nemo_skills.pipeline.cli import generate, wrap_arguments


input_dir = ""
output_dir = ""
tokens_to_generate = 131072
model = "/hf_models/gpt-oss-120b"
cluster = ""

generate(
    ctx=wrap_arguments(
        f"++inference.tokens_to_generate={tokens_to_generate} "
        f"++skip_filled=True "
        f"++inference.extra_body.reasoning_effort=high "
        f"++inference.temperature=1.0 "
        f"++inference.top_p=1.0 "
    ),
    server_type="vllm",
    model=model,
    cluster=cluster,
    generation_type="stem_error_type",
    input_dir=input_dir,
    output_dir=output_dir,
    expname="stem_error_type",
    server_gpus=4,
    server_nodes=1,
    random_seeds=[0]
)

