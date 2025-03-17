export OPENAI_API_KEY="..."


# # aya-expanse-8b korean prompt
# lm_eval --model cohere-compatible-chat \
#     --model_args model="c4ai-aya-expanse-8b" \
#     --tasks kmmlu_pro_poc_simple-evals \
#     --write_out \
#     --log_samples \
#     --gen_kwargs "max_gen_toks=4096,top_p=0.95,temperature=0.6" \
#     --output_path "results" \
#     --num_fewshot 0 \
#     --apply_chat_template


lm_eval --model vllm \
    --model_args pretrained=amphora/r1-7b-v2.0.21,max_model_len=10000 \
    --tasks kmmlu_pro_poc_simple-evals_en_patent_attorney \
    --write_out \
    --log_samples \
    --gen_kwargs "max_gen_toks=8192,top_p=0.95,temperature=0.6" \
    --output_path "results" \
    --num_fewshot 0 \
    --apply_chat_template
