from functools import partial

def doc_to_text(example, including_answer=True):
    prompt = "다음 시험 문제에 대해서, 충분히 생각하고 추론하여, 보기 중 정답을 고르세요.\n문제: "
    question = example["full_question"].strip()
    options = example["options"]
    prompt += question + "\n"

    for i, opt in enumerate(options):
        #prompt += "{}. {}\n".format(choices[i], opt)
        prompt += opt.strip() + "\n"

    prompt += "당신의 대답은 \"정답은 [정답 보기]입니다.\"로 끝나야하고, [정답 보기]는 주어진 보기 중 하나여야 합니다.\n\n정답: 문제를 풀기 위해, 한 번 천천히 생각해봅시다."

    return prompt

"""def doc_to_target(example):
    return example['cot_content'].replace(
        "A: Let's think step by step.", ""
    ).strip().split(
        " The answer is ("
    )[0] + f" The best answer is {example['answer']}."

#doc_to_text = partial(format_cot_example, including_answer=False)
#fewshot_to_text = partial(format_cot_example, including_answer=True)


def process_docs(dataset, subject):
    return dataset.filter(lambda x: x["category"] == subject)


process_biology = partial(process_docs, subject="biology")
process_business = partial(process_docs, subject="business")
process_chemistry = partial(process_docs, subject="chemistry")
process_computer_science = partial(process_docs, subject="computer science")
process_economics = partial(process_docs, subject="economics")
process_engineering = partial(process_docs, subject="engineering")
process_health = partial(process_docs, subject="health")
process_history = partial(process_docs, subject="history")
process_law = partial(process_docs, subject="law")
process_math = partial(process_docs, subject="math")
process_other = partial(process_docs, subject="other")
process_philosophy = partial(process_docs, subject="philosophy")
process_physics = partial(process_docs, subject="physics")
process_psychology = partial(process_docs, subject="psychology")
"""