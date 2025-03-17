from functools import partial

def doc_to_text(example, including_answer=True):
    prompt = f"""Answer the following multiple choice question. The last line of your response should be of the following format: 'Answer: $LETTER' (without quotes) where LETTER is one of {'ABCDE'[:len(example['options'])]}. Think step by step before answering.\n\n"""

    question = example["question"].strip()
    options = example["options"]
    prompt += question + "\n\n"

    for i, opt in enumerate(options):
        assert opt[0] in ["1", "2", "3", "4", "5"] and opt[1] == ")"

        opt = ["A", "B", "C", "D", "E"][int(opt[0])-1] + ")" + opt[2:]
        prompt += opt.strip() + "\n"

    return prompt.strip()

def doc_to_target(example):
    return ["ABCDE"[int(sol)-1] for sol in example['solution']]