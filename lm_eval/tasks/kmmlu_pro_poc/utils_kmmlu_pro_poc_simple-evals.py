from functools import partial

def doc_to_text(example, including_answer=True):
    prompt = f"""다음 문제에 대해 정답을 고르세요. 당신의 최종 정답은 {'ABCDE'[:len(example['options'])]} 중 하나이고, \"정답:\" 뒤에 와야 합니다. 정답을 고르기 전에 차근차근 생각하고 추론하세요.\n\n"""

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