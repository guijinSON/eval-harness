
# aya-expanse-8b korean prompt
lm_eval --model cohere-compatible-chat \
    --model_args model="c4ai-aya-expanse-8b" \
    --tasks kmmlu_pro_poc_simple-evals \
    --write_out \
    --log_samples \
    --gen_kwargs "max_gen_toks=4096,top_p=0.95,temperature=0.6,do_sample=True" \
    --output_path "aya_8b_ko" \
    --num_fewshot 0 \
    --apply_chat_template

# aya-expanse-8b english prompt
lm_eval --model cohere-compatible-chat \
    --model_args model="c4ai-aya-expanse-8b" \
    --tasks kmmlu_pro_poc_simple-evals_en \
    --write_out \
    --log_samples \
   --gen_kwargs "max_gen_toks=4096,top_p=0.95,temperature=0.6,do_sample=True" \
    --output_path "aya_8b_en" \
    --num_fewshot 0 \
    --apply_chat_template

# cr7B korean prompt
lm_eval --model cohere-compatible-chat \
    --model_args model="command-r7b-12-2024" \
    --tasks --tasks kmmlu_pro_poc_simple-evals \
    --write_out \
    --log_samples \
    --gen_kwargs "max_gen_toks=4096,top_p=0.95,temperature=0.6,do_sample=True" \
    --output_path "cr_7b_ko" \
    --num_fewshot 0 \
    --apply_chat_template

# cr7B english prompt
lm_eval --model cohere-compatible-chat \
    --model_args model="command-r7b-12-2024"\
    --tasks kmmlu_pro_poc_simple-evals_en \
    --write_out \
    --log_samples \
   --gen_kwargs "max_gen_toks=4096,top_p=0.95,temperature=0.6,do_sample=True" \
    --output_path "cr_7b_en" \
    --num_fewshot 0 \
    --apply_chat_template
