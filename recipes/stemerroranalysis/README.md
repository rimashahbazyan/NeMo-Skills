# Stem Error Type Generation

This document describes the generation process for the `stem_error_type` generation mechanism. The main purpose of this process is to analyze model responses and generate an additional column indicating the specific error type present in a given response.

## Input File Requirements

The input file must contain the following fields:

- **problem**: The statement or description of the problem.
- **generation**: The model's generated response or solution.
- **reference_solution**: The correct or expected solution provided as a reference.
- **expected_answer**: The answer that should have been provided.

## Generation Process

When processing an input file with the required fields, the generation step will return a new column labeled `error_type`. This column will contain one of the following error types that best describes the observed error in the model's output:

- **Incorrectly stated formula/theorem/rule**
  - The model gives the wrong version of a known formula, theorem, or rule—for example, mixing up the formula for area and perimeter.

- **Correctly stated formula/theorem/rule, but it is not suitable**
  - A formula or method is recalled accurately, but it does not apply to the context or problem being solved.

- **Misinterprets the context of the question**
  - The model misunderstands the setting, requirements, or what is being asked in the problem.

- **Wrong conclusion from otherwise correct results**
  - After a correct solution process, the model draws an incorrect final answer or misinterprets its own results.

- **Missed or ignored a key constraint in the prompt**
  - The model overlooks an explicit requirement or restriction provided in the task.

- **Invented or hallucinated a constraint or detail**
  - The model adds limitations, assumptions, or facts that were not present in the original question.

- **Calculation or arithmetic error**
  - A basic math error occurs during the solution steps, even if the method is otherwise correct.

- **Logical flaw or omitted steps in reasoning**
  - A necessary step in the logical chain is skipped, or a non-sequitur conclusion is made.

- **"Lost in the middle" or context drift**
  - During a long or complex answer, the model loses track of the original problem or its own previous reasoning.

- **Copied data or number incorrectly from prompt**
  - Transcription error: a key figure or fact from the question is misrepresented in the answer.

- **Incomplete answer**
  - The response addresses only part of a multi-part question, leaving the rest unanswered.

- **Formatting or presentation error**
  - The answer does not follow the requested format or structure, making it unclear or less useful.

- **Over-confident or unsupported assertion**
  - The model states something as a certainty without evidence or appropriate warnings, especially in speculative contexts.

## Usage

1. Ensure your files in input_dir include the required fields: `problem`, `generation`, `reference_solution`, and `expected_answer`.
2. Run the `stem_error_type` generation process. The output will be a file with an additional column `error_type` indicating the category of the error detected in each generated response.
 
Example:
```
from nemo_skills.pipeline.cli import generate, run_cmd, wrap_arguments


input_dir = ""
output_dir = ""
tokens_to_generate = 0 # set according to model type
model = ""

generate(
    ctx=wrap_arguments(
        f"++inference.tokens_to_generate={tokens_to_generate} "
        f"++skip_filled=True "
    ),
    server_type="vllm",
    model=model,
    cluster={cluster_name_here},
    generation_type="stem_error_type", # set to stem_error_type to generate and postprocess
    input_dir=input_dir,
    output_dir=output_dir,
    expname="stem_error_type",
    server_gpus=0, # set according to the model 
    server_nodes=0, # set according to the model 
    random_seeds=[0] # set according to the generations in input_dir 
)


```


This setup will help in systematically categorizing and addressing errors in model generations, enhancing both the evaluation process and future model improvements.

