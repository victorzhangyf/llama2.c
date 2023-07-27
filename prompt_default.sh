#! /bin/bash

make runomp
TEMP_PROMPT_FILE=tmp_prompt_ids
python prompt_to_token.py "$1" "$TEMP_PROMPT_FILE"
./run llama2_7b.bin 0.5 4096 "$TEMP_PROMPT_FILE"
rm "$TEMP_PROMPT_FILE"
