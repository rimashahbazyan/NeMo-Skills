from enum import Enum


class GenerationType(str, Enum):
    generate = "generate"
    math_judge = "math_judge"
    check_contamination = "check_contamination"
    stem_error_type = "stem_error_type"


GENERATION_MODULE_MAP = {
    GenerationType.generate: "nemo_skills.inference.generate",
    GenerationType.math_judge: "nemo_skills.inference.llm_math_judge",
    GenerationType.check_contamination: "nemo_skills.inference.check_contamination",
    GenerationType.stem_error_type: "nemo_skills.inference.stem_error_type",
}
